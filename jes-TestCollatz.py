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

    def test_read_1 (self) : # given
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) : # tests 2-4 for read are new
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

    def test_read_3 (self) :
        r = StringIO.StringIO("105 202\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 105)
        self.assert_(a[1] == 202)

    def test_read_4 (self) :
        r = StringIO.StringIO("1 1000000\n") # that's 1 million, testing the limits
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 1000000)

    # ----
    # eval
    # ----

    def test_eval_1 (self) : #tests 1-4 for eval are given
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

    def test_eval_5 (self) : #tests 5-7 for eval are new
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    def test_eval_6 (self) :
        v = collatz_eval(100, 100)
        self.assert_(v == 26)

    def test_eval_7 (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    # -----
    # print
    # -----

    def test_print (self) : #given 
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) : #tests 1-3 for print are based on eval's tests 2-4 of eval()
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_2 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    def test_print_3 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

    def test_print_4 (self) : #tests 4-6 are new, corresponding to eval's tests 5-7
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_print_5 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 100, 100, 26)
        self.assert_(w.getvalue() == "100 100 26\n")

    def test_print_6 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) : #given
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) : #tests 1-3 for solve are new
        r = StringIO.StringIO("1 1\n100 100\n10 1\n5 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n100 100 26\n10 1 20\n5 1000 179\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("2 7\n150 200\n2010 2009\n1000 19000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "2 7 17\n150 200 125\n2010 2009 69\n1000 19000 279\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("20000 50000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "20000 50000 324\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
