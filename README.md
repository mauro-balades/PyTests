# PyTests
Write small or big tests with PyTests a testing framework

## Usage

NOTE: Things might change

```py

from pytests import PyTest

tests = PyTest()

def my_test():
  return True

tests.new(
  my_test, # Function with out calling
  name="My test",
  description="",
  result=True,
  #....
)

tests.run_all()

```