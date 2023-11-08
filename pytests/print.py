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

from pytests.test import Test

BLK = "\033[0;30m"
RED = "\033[0;31m"
GRN = "\033[0;32m"
YEL = "\033[0;33m"
BLU = "\033[0;34m"
MAG = "\033[0;35m"
CYN = "\033[0;36m"
WHT = "\033[0;37m"

# Regular bold text
BBLK = "\033[1;30m"
BRED = "\033[1;31m"
BGRN = "\033[1;32m"
BYEL = "\033[1;33m"
BBLU = "\033[1;34m"
BMAG = "\033[1;35m"
BCYN = "\033[1;36m"
BWHT = "\033[1;37m"

# Regular underline text
UBLK = "\033[4;30m"
URED = "\033[4;31m"
UGRN = "\033[4;32m"
UYEL = "\033[4;33m"
UBLU = "\033[4;34m"
UMAG = "\033[4;35m"
UCYN = "\033[4;36m"
UWHT = "\033[4;37m"

# Regular background
BLKB = "\033[40m"
REDB = "\033[41m"
GRNB = "\033[42m"
YELB = "\033[43m"
BLUB = "\033[44m"
MAGB = "\033[45m"
CYNB = "\033[46m"
WHTB = "\033[47m"

# High intensty background
BLKHB = "\033[0;100m"
REDHB = "\033[0;101m"
GRNHB = "\033[0;102m"
YELHB = "\033[0;103m"
BLUHB = "\033[0;104m"
MAGHB = "\033[0;105m"
CYNHB = "\033[0;106m"
WHTHB = "\033[0;107m"

# High intensty text
HBLK = "\033[0;90m"
HRED = "\033[0;91m"
HGRN = "\033[0;92m"
HYEL = "\033[0;93m"
HBLU = "\033[0;94m"
HMAG = "\033[0;95m"
HCYN = "\033[0;96m"
HWHT = "\033[0;97m"

# Bold high intensity text
BHBLK = "\033[1;90m"
BHRED = "\033[1;91m"
BHGRN = "\033[1;92m"
BHYEL = "\033[1;93m"
BHBLU = "\033[1;94m"
BHMAG = "\033[1;95m"
BHCYN = "\033[1;96m"
BHWHT = "\033[1;97m"

# Reset
reset = "\033[0m"


def print_success(test: Test):
    print(f"{BLK}{GRNB} PASS {reset}", end=" ")
    print(f"{test.test.__name__}, ", end="")

    if test.result:
        print(f"result is {YEL}{test.result}{reset}")
    elif test.error:
        print(f"error is {YEL}{test.error.__name__}{reset}")

    print(f"  {GRN}✓{reset} {test.name} {CYN}({test.stop_clock()}ms){reset}")

    if test.description and test.description != "":
        print(f"    {BLK}└── {test.description}{reset}")

    print("")


def print_error(test: Test, result: any):
    print(f"{BLK}{REDB} FAIL {reset}", end=" ")
    print(f"{test.test.__name__}")
    if test.description and test.description != "":
        print(f"  {BLK}└── {test.description}{reset}\n")

    if test.result:
        print(f"  Expected result: {GRN}{test.result}{reset}")
    elif test.error:
        print(f"  Expected error: {GRN}{test.error.__name__}{reset}")

    print(f"  Received: {RED}{result}{reset}")
    print(f"\n  {RED}X{reset} {test.name} {CYN}({test.stop_clock()}ms){reset}\n")
