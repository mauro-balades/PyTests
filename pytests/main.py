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

import time
from typing import Callable
from pytests.test import Test
from pytests.print import *
from pytests.__version__ import VERSION as PYTEST_VERSION

import platform


class PyTest:

    default_color = True

    def __init__(self, *args, **kwargs):

        # TODO: More settings
        self.colors = kwargs.get("color", self.default_color)
        self._tests = []

        self.start = 0
        self.failures = 0
        self.sucesses = 0

    def new(
        self,
        test: Callable,
        result: any = None,
        name: str = None,
        description: str = None,
        error: Exception = None,
    ):
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

        self._print_start_info()

        for test in self._tests:
            success = False
            test.start_clock()

            # Check if an error was expected
            if test.error:
                success, err = self._run_error_test(test)
                self._print_result(success, test, err)

                if success:
                    self.sucesses += 1
                else:
                    self.failures += 1

                continue
            # Run test and get result
            result = test.test()
            if result == test.result:
                # If test result equals to the expected result
                self.sucesses += 1
                success = True
            else:
                self.failures += 1

            self._print_result(success, test, result)

        self._print_end_info()

    def _print_end_info(self):

        end = "{:.2f}".format((time.time() * 1000) - self.start)

        print("PyTests testing section (end):")
        print(f"  {GRN}➔{reset} Tests failure: {CYN}{self.failures}{reset}")
        print(f"  {GRN}➔{reset} Tests successful: {CYN}{self.sucesses}{reset}")
        print(f"  {GRN}➔{reset} Testing time: {CYN}{end}ms{reset}")
        print("")

    def _print_start_info(self):

        self.start = time.time() * 1000

        print("PyTests testing section:")
        print(f"  {GRN}➔{reset} PyTests version: {CYN}{PYTEST_VERSION}{reset}")
        print(
            f"  {GRN}➔{reset} Python version: {CYN}{platform.python_version()}{reset}"
        )
        print(f"  {GRN}➔{reset} Testing start: {CYN}{self.start}{reset}")
        print("")

    def _print_result(self, result: bool, test: Test, res: any):

        if result:
            print_success(test)
        else:
            print_error(test, res)

    def _run_error_test(self, test: Test):
        suc = False

        try:
            test.test()
        except test.error:
            suc, err = True, test.error
        except Exception as e:
            err = e.__class__.__name__
        finally:
            pass

        return suc, err

    def _create_name(self):
        _len = len(self._tests)
        return f"Test #{_len + 1}"
