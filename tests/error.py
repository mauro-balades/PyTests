
from pytests import PyTest

tests = PyTest()

class CustomException(Exception):
  pass

def my_test():
  raise CustomException

tests.new(
  my_test, # Function with out calling
  name="My test",
  description="",
  error=CustomException,
  #....
)

tests.run_all()
