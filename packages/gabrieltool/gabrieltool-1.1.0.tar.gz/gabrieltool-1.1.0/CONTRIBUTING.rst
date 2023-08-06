.. highlight:: shell

Contributing
**********************

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/cmusatyalab/OpenWorkflow/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

OpenWorkflow could always use more documentation, whether as part of the
official OpenWorkflow docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/cmusatyalab/OpenWorkflow/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `OpenWorkflow` for local development.

1. Fork the `OpenWorkflow` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/gabrieltool.git

3. Install your local copy into a virtualenv::

    $ python3 -m venv env
    $ . env/bin/activate
    $ cd gabrieltool/
    $ pip install -r requirements/dev.txt
    $ python setup.py install

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass linter (autopep8) and the
   tests::

    $ python -m pytest <directory>

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring.
3. The pull request should work for Python 3.5, 3.6, and 3.7. Check
   https://github.com/cmusatyalab/OpenWorkflow/actions
   and make sure that the tests pass for all supported Python versions.


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed.

gabrieltool Python Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::bash

    $ bump2version patch # possible: major / minor / patch
    $ git push origin master --follow-tags

[This Github
workflow](https://github.com/cmusatyalab/OpenWorkflow/blob/master/.github/workflows/pythonpackage.yml.yml)
will then deploy to PyPI if tests pass.

FSM Web Editor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::bash

    $ cd gabrieltool/statemachine-editor-react
    $ npm i # install npm if not available
    $ npm build # build react jsx to HTML and Javascript to a dir called build
    $ npm deploy # push the generated HTML and Javascript to remote gh-pages branch

Generate Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::bash

    $ SPHINX_APIDOC_OPTIONS='members,undoc-members,show-inheritance,inherited-members' sphinx-apidoc -H 'gabrieltool API' -f -o docs/source gabrieltool
    $ cd docs
    $ make html

After pushing to remove, `The documentation page
<https://readthedocs.org/projects/openworkflow/>`_ will automatically build the
docs directory through a webhook integration.
