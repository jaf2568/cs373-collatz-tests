#!/usr/bin/env python

# -------------------------------
# Copyright (C) 2012
# Glenn P. Downing
# -------------------------------

"""
To test the program:
% python TestCollatz.py >& TestCollatz.py.out
% chmod ugo+x TestCollatz.py
% TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read_1 (self) :
        r = StringIO.StringIO("5 25\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 5)
        self.assert_(a[1] == 25)

    def test_read_2 (self) :
        r = StringIO.StringIO("3 52\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 3)
        self.assert_(a[1] == 52)

    def test_read_3 (self) :
        r = StringIO.StringIO("4000 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 4000)
        self.assert_(a[1] == 1000000)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    def test_eval_5 (self) :
        v = collatz_eval(353336, 353343)
        self.assert_(v == 167)

    def test_eval_6 (self) :
        v = collatz_eval(129315, 129287)
        self.assert_(v == 194)

    def test_eval_7 (self) :
        v = collatz_eval(37518, 37153)
        self.assert_(v == 306)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 2, 3, 8)
        self.assert_(w.getvalue() == "2 3 8\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 219194, 219522, 337)
        self.assert_(w.getvalue() == "219194 219522 337\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 37518, 37153, 306)
        self.assert_(w.getvalue() == "37518 37153 306\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO.StringIO("59754 60242\n353336 353343\n665661 665863\n795320 795389\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "59754 60242 317\n353336 353343 167\n665661 665863 248\n795320 795389 225\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("2 2\n3 3\n4 4\n5 5\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "2 2 2\n3 3 8\n4 4 3\n5 5 6\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("17216 17568\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "17216 17568 235\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
