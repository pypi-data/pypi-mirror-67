"""Utilities for using Tensorflow models.
"""
import numpy as np
import tensorflow as tf
import grpc
from tensorflow_serving.apis import predict_pb2, prediction_service_pb2_grpc


class TFServingPredictor(object):
    """An agent that makes request to a TF serving server to get object detection results.

    This agent communicates with the TF serving server (often a container at
    localhost) through gRPC.
    """

    def __init__(self, host, port):
        """Constructor.

        Args:
            host (string): TF serving server hostname or IP address.
            port (int): TF serving server port number.
        """
        options = [
            ('grpc.max_message_length', 500 * 1024 * 1024),
            ('grpc.max_send_message_length', 500 * 1024 * 1024),
            ('grpc.max_receive_message_length', 500 * 1024 * 1024),
        ]
        self.channel = grpc.insecure_channel('{}:{}'.format(host, int(port)), options=options)
        self.stub = prediction_service_pb2_grpc.PredictionServiceStub(self.channel)

    def infer_one(self, model_name, rgb_image, conf_threshold=0.5):
        """Infer one image by sending a request to TF serving server.

        Args:
            model_name (string): Name of the Model
            rgb_image (numpy array): Image in RGB format
            conf_threshold (float, optional): Cut-off threshold for detection. Defaults to 0.5.

        Returns:
            Dictionary: keys are class ids, values are list of [x1, y1, x2,
            y2, confidence, label_idx]. e.g {'cat': [[0, 0, 100, 100, 0.6, 'cat']],
            1: [[0, 0, 100, 100, 0.7, 1]]}
        """
        parsed_results = self._infer(model_name, np.stack([rgb_image.astype(dtype=np.uint8)], axis=0))
        results = {}
        # parsed_results has
        # num_detections: number of detections
        # detection_scores: 2d array of confidence, [image_idx, bbx_idx]
        # detection_classes: 2d array, [image_idx, bbx_idx]
        # detection_boxes: 3d array, [image_idx, bbx_idx, (ymin,xmin,ymax,xmax)]
        # for each image, should only be 1 image here.
        # num_detections = parsed_results['num_detections']
        detection_scores = parsed_results['detection_scores']
        detection_classes = parsed_results['detection_classes']
        detection_boxes = parsed_results['detection_boxes']
        h, w, _ = rgb_image.shape
        image_idx = 0
        for detection_idx in range(len(detection_classes[image_idx])):
            label = str(detection_classes[image_idx][detection_idx])
            confidence = detection_scores[image_idx][detection_idx]
            if confidence < conf_threshold:
                continue
            norm_bbox = detection_boxes[image_idx][detection_idx]
            bbox = [int(norm_bbox[1]*w), int(norm_bbox[0]*h),
                    int(norm_bbox[3]*w), int(norm_bbox[2]*h)]
            objs = results.setdefault(label, [])
            objs.append([*bbox, confidence, label])
        return results

    def _infer(self, model_name, images):
        # Create prediction request object
        request = predict_pb2.PredictRequest()
        # Specify model name (must be the same as when the TensorFlow serving serving was started)
        request.model_spec.name = model_name
        # Initalize prediction
        request.inputs['inputs'].CopyFrom(
            tf.make_tensor_proto(images))
        # Call the prediction server
        result = self.stub.Predict(request, 10.0)  # 10 secs timeout
        # convert tensorProto to numpy array
        parsed_results = {}
        for k, v in result.outputs.items():
            parsed_results[k] = tf.make_ndarray(v)
        # fix output result types
        if 'detection_classes' in parsed_results:
            parsed_results['detection_classes'] = parsed_results['detection_classes'].astype(np.int64)
        return parsed_results
