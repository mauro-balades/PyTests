from pytests import PyTest

tests = PyTest()

class CustomException(Exception):
  pass

def my_test():
  return True

def my_test2():
  return 23

def my_test3():
  return "hello"

def my_test4():
  raise CustomException

tests.new(
  my_test, # Function with out calling
  name="My test with description",
  description="This is a description used to give more context from the test",
  result=True,
  #....
)

tests.new(
  my_test2, # Function with out calling
  name="This is a second test",
  description="The test below will have a default name",
  result=24,
  #....
)

tests.new(
  my_test3, # Function with out calling
  result="hello",
  #....
)

tests.new(
  my_test4, # Function with out calling
  name="Error test",
  description="This test is being used with an error",
  error=CustomException,
  #....
)


tests.run_all()

