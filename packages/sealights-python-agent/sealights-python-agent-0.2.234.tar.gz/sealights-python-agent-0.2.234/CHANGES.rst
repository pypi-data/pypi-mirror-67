Changes
=======


0.2.334 (2020-05-06)
--------------------
* bugfix - wrong xml coverage report when using pytest-xdist

0.2.330 (2020-03-11)
--------------------
* Handling not ready test recommendations

0.2.229 (2020-03-11)
--------------------
* Added better test recommendations error handling

0.2.228 (2020-02-22)
--------------------
* Fixed bug when running the agent after dependency update - gitdb2 - ModuleNotFoundError

0.2.219 (2019-10-30)
--------------------
* Pytest test selection support

0.2.213 (2019-10-16)
--------------------
* Python 3.7 support

0.2.201 (2019-07-14)
--------------------
* Use pytest + nose exit code

0.2.199 (2019-02-24)
--------------------
* Performance optimization
    * Added --per-test flag for pytest, nose, unittest, unit2 and run commands. default is on.

0.2.198 (2019-01-21)
--------------------
* changed default scm provider from github to null

0.2.197 (2019-01-14)
--------------------
* added --cov-report option to run command
