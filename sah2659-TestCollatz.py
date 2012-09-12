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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cyclen

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read(self):
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2(self):
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 10)
        self.assert_(a[1] == 1)

    def test_read_3(self):
        r = StringIO.StringIO("22 33\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 22)
        self.assert_(a[1] ==33)

    def test_read_4 (self) :
        r = StringIO.StringIO("1111 1111\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1111)
        self.assert_(a[1] == 1111)

    def test_read_5 (self) :
        r = StringIO.StringIO("12 342\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  12)
        self.assert_(a[1] == 342)

    def test_read_eof(self):
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_1_rev(self):
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_2_rev(self):
        v = collatz_eval(200, 100)
        self.assert_(v == 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_3_rev(self):
        v = collatz_eval(210, 201)
        self.assert_(v == 89)

    def test_eval_4 (self):
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    def test_eval_4_rev(self):
        v = collatz_eval(1000, 900)
        self.assert_(v == 174)


    def test_eval_50_to_20(self):
        v = collatz_eval(50, 20)
        self.assert_(v == 112)

    def test_eval_100_to_80(self):
        v = collatz_eval(100, 80)
        self.assert_(v == 119)

    def test_eval_80_to_100(self):
        v = collatz_eval(80, 100)
        self.assert_(v == 119)

    def test_eval_1_to_100000(self):
        v = collatz_eval(1, 100000)
        self.assert_(v == 351)

    def test_eval_20_to_50(self):
        v = collatz_eval(20, 50)
        self.assert_(v == 112)


    # -----
    # cyclen
    # -----

    def test_cyclen_of_1(self):
        v = collatz_cyclen(1)
        self.assert_(v == 1)

    def test_cyclen_of_22(self):
        v = collatz_cyclen(22)
        self.assert_(v == 16)

    def test_cyclen_10(self):
        v = collatz_cyclen(10)
        self.assert_(v == 7)

    def test_cyclen_2(self):
        v = collatz_cyclen(2)
        self.assert_(v == 2)

    def test_cycle_27 (self) :
        v = collatz_cyclen(27)
        self.assert_(v == 112)

    # -----
    # print
    # -----

    def test_print_1_10_20(self):
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_3_30_112(self):
        w = StringIO.StringIO()
        collatz_print(w, 3, 30, 112)
        self.assert_(w.getvalue() == "3 30 112\n")

    def test_print_4_90_116(self):
        w = StringIO.StringIO()
        collatz_print(w, 4, 90, 116)
        self.assert_(w.getvalue() == "4 90 116\n")

    def test_print_100_10_119(self):
        w = StringIO.StringIO()
        collatz_print(w, 100, 10, 119)
        self.assert_(w.getvalue() == "100 10 119\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO.StringIO("10 20\n30 40\n20 2000\n8888 3333\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 20 21\n30 40 107\n20 2000 182\n8888 3333 262\n")

    def test_solve_3(self):
        r = StringIO.StringIO("838 23\n12 40\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "838 23 171\n12 40 112\n")
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
