.. :changelog:

History
-------

0.3.17 (2016-7-28)
-------------------
* Fixed bug with windows dependent line breaks Fixes #34
* Fixed bug while parsing unicode Fixes #32

0.3.16 (2016-5-6)
-------------------
* Fixed bug with non-unicode characters Fixes #32
* Fixed bug with spaces in a file spec for Client and Stream Fixes #29
* Fixed bug if any of the P4 variables were set to an empty string in a config file

0.3.15 (2016-3-9)
-------------------
* Python 3 support

0.3.14 (2016-2-24)
--------------------
* Fixed bug when trying to add an empty file

0.3.13 (2016-2-17)
--------------------
* Changed the parameter in __getVariables to a list Fixes #27

0.3.12 (2016-2-16)
--------------------
* Added an optional connection paramter to all api functions

0.3.11 (2016-2-16)
--------------------
* Added a base class for perforce objects to wrap dict getter
* Added Stream object Fixes #25
* Added tests for new classes Fixes #26
* Added tests for Revision objects as it was lacking
* __getVariables will no longer show a console on windows Fixes #24
* Client and Stream are now exposed at the package level Fixes #23


0.3.10 (2016-1-30)
--------------------
* Added Client object
* Added better support for finding p4 env variables
* Added PendingDeprecationWarnings to Changelist and Revision to accept an optional Connection object.  If not provided, it will use whatever settings it can find to create one
* For Changelist, Revision, and Client, added __getattr__ to use the underlying dict to allow use of all fields if not directly supported by this lib
* Connection.run() now requires a list instead of a string for the command.  A PendingDeprecationWarning will be thrown if a string is used.  Strings will not be supported in 0.4.0

0.3.9 (2016-1-29)
--------------------
* Changelist objects are lazy and will only query files as needed

0.3.7 (2015-1-7)
--------------------
* Fixed bugs regarding spaces in file names or specs
* Fixed bug that may have left too many file handles open
* Added comparison operator to Changelist

0.3.6 (2015-12-3)
--------------------
* Added __iadd_ operator to Changelist
* Added unchanged_only flag to Changelist.revert()
* Added exclude_deleted flag to Connection.ls()
* Fixed a bug on windows that would occur if the command line was too long (>8190)
* Added setter to Connection.client
* Changelist.append will now raise a RevisionError if the file to append is not under the clients root

0.3.5 (2015-11-18)
--------------------

* Changed the argument order for Revisions to be consistent with everything else.  Supports backwards compatible argument orders
* Fixed bug that would attempt to checkout files when querying a changelist

0.3.4 (2015-11-17)
--------------------

* Changed enums to be namedtuples
* Fixed bug when detecting login state

0.3.3 (2015-11-16)
---------------------

* Corrected the way the error levels were being handled
* Added more documentation
* Connection will no longer fail if any of the paramter were incorrect, use Connection.status() to check the status of the connection

0.1.0 (2014-10-16)
---------------------

* First release on PyPI.
