from pytests import PyTest

tests = PyTest()

def my_test():
  return True

tests.new(
  my_test, # Function with out calling
  name="My test with description",
  description="This is a description used to give more context from the test",
  result=True,
  #....
)

tests.run_all()

