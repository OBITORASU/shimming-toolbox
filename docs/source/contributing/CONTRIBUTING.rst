Contributing to shimming-toolbox
================================



.. contents:: Table of Contents
   :depth: 2
..


Introduction
------------

First off, thanks for taking the time to contribute to our project! 🎉

When contributing to this repository, please first discuss the change you wish
to make by opening a new `GitHub issue <https://github.com/shimming-toolbox/shimming-toolbox/issues>`_ with one of the templates.

Contributions relating to content of the Github repository can be
submitted through `GitHub pull requests <https://github.com/shimming-toolbox/shimming-toolbox/pulls>`_ (PR).

PR for bug fixes or new features should be based on the `master <https://github.com/shimming-toolbox/shimming-toolbox/tree/master>`_ branch.

The following GitHub documentation may be useful:

-   See `Using Pull Requests <https://help.github.com/articles/using-pull-requests>`_ for more information about Pull Requests.
-   See `Forking a repository <http://help.github.com/forking/>`_ for an introduction to forking a repository.
-   See `Creating branches <https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/>`_
    for an introduction on branching within GitHub.

**For external contributors:** Please fork this repository, make the desired
changes, and then open a Pull request to have your code reviewed and merged.

**For internal contributor:** You can open a
branch (see `Opening a branch`) directly in this repository. If you don't
have the rights, contact the team leader.


Opening an issue
----------------

Issues (bugs, enhancement requests, or feature requests) can be submitted `on our project's issue page <https://github.com/shimming-toolbox/shimming-toolbox/issues>`_. Please select the appropriate template when creating a new issue.


Before Submitting a New Issue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please take a few seconds to search the issue database in case the issue has already been raised.

When reporting an issue, make sure your installation has not been tampered with (and if you can, update to the latest release in case the problem has already been fixed).


Submitting an Issue
~~~~~~~~~~~~~~~~~~~

Go through the checklist of the issue template to ensure you've met all our issue formatting requirements. This will help us to quickly address the issue ticket.


Issue Examples
^^^^^^^^^^^^^^

Some good real-life examples:

- https://github.com/neuropoly/spinalcordtoolbox/issues/2240
- https://github.com/neuropoly/spinalcordtoolbox/issues/2236
- https://github.com/neuropoly/spinalcordtoolbox/issues/2245


Opening a Branch
----------------

If you are part of the core developer team, you can open a branch directly in this repository. Prefix the branch name with a personal
identifier (e.g. your initials) and a forward slash; If the branch you are working on is in response to an issue, provide the issue number;
Add some text that make the branch name meaningful.

Examples:

-  ``ol/100-fixup-lr-scheduler``
-  ``ab/loader-pep8``


Developing
----------

Pre-commit checks
~~~~~~~~~~~~~~~~~

We use ``pre-commit`` to enforce conventions like file sizes, correct Python syntax, and no merge conflict strings in the changeset. After you've installed ``shimming-toolbox``, install the hooks by running ``pre-commit install`` at the root of the repo clone.

Conflicts
~~~~~~~~~

Make sure the PR changes are not in conflict with the master branch.

Code style
~~~~~~~~~~

Please review your changes for styling issues, clarity, according to the `PEP8 convention <https://www.python.org/dev/peps/pep-0008/>`__. Correct
any code style suggested by an analyzer on your changes. `PyCharm <https://www.jetbrains.com/help/pycharm/2016.1/code-inspection.html>`__
has a code analyser integrated or you can use `pyflakes <https://github.com/PyCQA/pyflakes>`__.

Do not address your functional changes in the same commits as any styling clean-up you may be doing on existing code.

Documentation and docstrings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are implementing a new feature, update the documentation to describe the feature, and comment the code (things that are not
trivially understandable from the code) to improve its maintainability.

Make sure to cite any papers, algorithms or articles that can help understand the implementation of the feature. If you are implementing an
algorithm described in a paper, add pointers to the section / steps.

Please use the `Google style docstrings <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`__.

Testing
~~~~~~~

Please add tests, especially with new code. As of now, we have unit tests (in ``/test``). They are straightforward to augment, but we understand
it's the extra mile; it would still be appreciated if you provide something lighter (eg. in the commit messages or in the PR or issue text)
that demonstrates that an issue was fixed, or a feature is functional.

Consider that if you add test cases, they will ensure that your feature still works in the future.

Licensing
~~~~~~~~~

Ensure that you are the original author of your changes, and if that is not the case, ensure that the borrowed/adapted code is compatible with
the `project's license <https://github.com/shimming-toolbox/shimming-toolbox/blob/master/LICENSE>`_.


Committing
----------

Commit Titles
~~~~~~~~~~~~~

Provide a concise and self-descriptive title (avoid > 80 characters).
You may "scope" the title using the applicable command name(s), folder
or other "module" as a prefix. If a commit is responsible for fixing
an issue, post-fix the description with ``(fixes #ISSUE_NUMBER)``.

Examples:

::

    testing: add testing function for validation metrics
    loader: add timer
    documentation: add slice_axis to the config files

Commit Sequences
~~~~~~~~~~~~~~~~

Update your branch to be baseline on the latest master if new
developments were merged while you were developing. Please prefer
**rebasing** to merging, as explained in `this
tutorial <https://coderwall.com/p/7aymfa/please-oh-please-use-git-pull-rebase>`__.
Note that if you do rebases after review have started, they will be
cancelled, so at this point it may be more appropriate to do a pull.

Clean-up your commit sequence. If your are not familiar with git, `this
good tutorial <https://www.atlassian.com/git/tutorials/rewriting-history>`__
on the subject may help you.

Focus on committing 1 logical change at a time. See `this article
<https://github.com/erlang/otp/wiki/writing-good-commit-messages>`__
on the subject.


Submitting a Pull Request
-------------------------

Please go through the checklist in the PR template to ensure you've met all our PR formatting requirements. This will help us to easily review your PR so it can be quickly merged when ready.

PR Labels
~~~~~~~~~

You **must** add labels to your PRs, as these are used to automatically generate Changelog:

- **Category:** Choose **one** label that describes the `category <https://github.com/shimming-toolbox/shimming-toolbox/labels?q=bug+documentation+feature+enhancement+testing+installation>`_.


- **Cross-compatibility:** If your PR breaks cross-compatibility with a previous stable release of SCT, you should add the label ``compatibility`` (orange label).



Work in progress
~~~~~~~~~~~~~~~~

If your PR is not ready for review yet, you can convert it to a "Draft", so the team is informed.

A draft pull request is styled differently to clearly indicate that it’s in a draft state.
Merging is blocked in draft pull requests. Change the status to "Ready for review" near the
bottom of your pull request to remove the draft state and allow merging according to your
project’s settings.

Continuous Integration
~~~~~~~~~~~~~~~~~~~~~~

The PR can't be merged if `GitHub Actions "Run
tests" <https://travis-ci.com/github/shimming-toolbox/shimming-toolbox>`__
hasn't succeeded. If you are familiar with it, consult the test results
to fix the problem.

Reviewers
~~~~~~~~~

Any changes submitted for inclusion to the master branch will have to go
through a
`review <https://help.github.com/articles/about-pull-request-reviews/>`__.

Only request a review when you deem the PR as "good to go". If the PR is
not ready for review, convert it to a "Draft".

GitHub may suggest you to add particular reviewers to your PR. If that's
the case and you don't know better, add all of these suggestions. The
reviewers will be notified when you add them.

Merging your PR
~~~~~~~~~~~~~~~

When your PR has been approved by the reviewers you requested, you can merge it yourself using the rebase method.

Versioning
----------
Versioning uses the following convention: MAJOR.MINOR.PATCH, where:

PATCH version when there are backwards-compatible bug fixes or enhancements, without alteration to Python's modules or data/binaries. MINOR version when there are minor API changes or new functionality in a backwards-compatible manner, or when there are alteration to Python's modules or data/binaries (which requires to re-run installer for people working on the dev version), MAJOR version when there are major incompatible API changes, Beta releases follow the following convention:

MAJOR.MINOR.PATCH-beta.x (with x = 0, 1, 2, etc.) Stable version is indicated in the file version.txt. For development version (on master), the version is "dev".
