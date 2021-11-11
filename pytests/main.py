"""
MIT License

Copyright (c) 2021 Mauro Baladés

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Callable
from pytests.test import Test
from pytests.print import *

class PyTest:

  default_color = True

  def __init__(self, *args, **kwargs):

    # TODO: More settings
    self.colors = kwargs.get("color", self.default_color)
    self._tests = []

  def new(self, test: Callable, result: any = None, name: str = None, description: str = None, error: Exception = None):
    _test = Test(
        test=test,
        result=result,
        name=(name if name is not None else self._create_name()),
        description=description,
        error=error,
      )

    self._tests.append(_test)
    return _test

  # TODO: make a single run() function

  def run_all(self):
    
    for test in self._tests:
      success = False
      test.start_clock()

      # Check if an error was expected
      if test.error:
        success = self._run_error_test(test)
        self._print_result(success, test, result)
        continue

      # Run test and get result
      result = test.test()
      if result == test.result:
        # If test result equals to the expected result
        success = True

      self._print_result(success, test, result)

  def _print_result(self, result: bool, test: Test, res: any):

    if result:
      print_success(test)
    else:
      print_error(test, res)
      
  def _run_error_test(self, test: Test):
    suc = False

    try: test.test()
    except test.error: suc = True
    except: pass
    finally: pass

    return suc

  def _create_name(self):
    _len = len(self._tests)
    return f"Test #{_len + 1}"
