Changes
=======


v0.7.1
------

* Fix pipeline, doc8 linting ignores D001, line too long


v0.7
----

* Add ``customize`` function, part of #1
* Change _filter to filter_packages and make it public
* Improve filter_package explanation
* Improve docs
* Add check_qt() function
* Add check_numbers() function
* Enhance help from command line parser
* Enhance command line order
* Correct mispelling errors
* Remove importlib_metadata for Pytho 3.8+, incoporated into std lib, MR#2
* Add MANIFEST.in, part of #9
* Improve internal code and linting
* Remove support for Python 2.7 and 3.4, closes #8


v0.6.10
--------

* Fix gitlab-ci, again
* Whole pipeline working on gitlab, even upload to pypi


v0.6.9
------

* Fix gitlab-ci


v0.6.8
------

* Change stage names
* Split test in more envs
* Improve tutorial


v0.6.7
------

* Lint code and docs
* Add more docs
* Add pylint configuration
* Improve tests and linters
* Add docs generate with sphinx
* Add tutorial for personalization - Spyder example
* Add build, test and release on gitlab-ci
* Add release requirements
* Fix tox commands to build, test and release

v0.6.6
------

* Fix Python 2 compatibility of FileNotFoundError
* Lint code
* Add tox and gitlab CI - working, passing


v0.6.5
------

* Make it compatible with Python 2.7, no errors are issued
* Remove shell=True to improve security
* Improve command calls
* Test url to check starts with http
* Add tests using tox for py27, py34, py36, py37
* Add requirement files for develop, doc, stable, test and update envs
* Fix packages-conda adding --no-pip option (seems not working, conda issue)


v0.6.4
------

* Remove print from code


v0.6.3
------

* Fix problems when none binding is installed for abstractions, fixes #5


v0.6.2
------

* Add function to print output


v0.6.1
------

* Fix readme links

v0.6
----

* Add filter to target packages
* Fix conda list not to not list packages installed with pip


v0.5
----

* Enhance internal docs
* Add ``--distributions`` to list Python and Conda distributions
* Remove ``--network`` from minimalist output
* Enhance README including examples from files


v0.4.2
------

* Enhance readme and update changes


v0.4.1
------

* Fix network command


v0.4
----

* Add commands for bindings and abstractions
* Add binding variable and import name


v0.3
----

* Fix readme format


v0.2
----

* Fix ``conda`` command not found error
* Fix memory info and add swap info
* Add thread information
* Add more options and change some options names
* Improve docs
* Classifiers and year update


v0.1
----

* First working version
