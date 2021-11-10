# PyTests
Write small or big tests with PyTests a testing framework

## Usage

NOTE: Things might change

```py

from PyTests import PyTest

tests = PyTests()

def my_test():
  return true

tests.new(
  my_test # Function with out calling
  name="My test"
  description=""
  #....
)

tests.run_all()
```