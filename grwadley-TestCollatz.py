#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
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

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)
	#blank line test
	def test_read_2 (self):
		r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)

	#newline test
	def test_read_3 (self):
		r = StringIO.StringIO("\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)
	#reversed order test
    def test_read_4 (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 10)
        self.assert_(a[1] == 1)
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

	#test reverse order
    def test_eval_5 (self) :
        v = collatz_eval(863, 82)
        self.assert_(v == 171)

    def test_eval_6 (self) :
        v = collatz_eval(27, 14)
        self.assert_(v == 112)
	#large numbers
    def test_eval_7 (self) :
        v = collatz_eval(5013, 5245)
        self.assert_(v == 179)

    def test_eval_8 (self) :
        v = collatz_eval(301608, 466857)
        self.assert_(v == 449)
    # -----
    # print
    # -----
	#empty test
    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, "", "", "")
        self.assert_(w.getvalue() == "  \n")

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
	#large values
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10000, 983761, 535)
        self.assert_(w.getvalue() == "10000 983761 535\n")
	#non ints
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, "test", "test", "test")
        self.assert_(w.getvalue() == "test test test\n")
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
	#another test of multiple lines
    def test_solve_2 (self) :
        r = StringIO.StringIO("863 82\n 5013 5245\n301608 466857\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "863 82 171\n5013 5245 179\n301608 466857 449\n")
	#large values
    def test_solve_3 (self) :
        r = StringIO.StringIO("900000 930000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "900000 930000 476\n")
	#reverse values
    def test_solve_4 (self) :
        r = StringIO.StringIO("9000 354\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "9000 354 262\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
