# testver

*Programmatically edit python package versions for testing.*

When publishing a python package from a continuous integration system, it can
be useful to publish it to a test package repository such as test.pypi.org.

However, package repositories only accept a certain version of a package once.
To get around this, this package edits the python version in your python code
(defined as the `<package>.__version__` variable).

This works well with systems such as flit.
