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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, get_length

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_normal (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read2_backwards_numbers (self) :
        r = StringIO.StringIO("1000000 2\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 1000000)
        self.assert_(a[1] == 2)

    def test_read_large_numbers (self) :
        r = StringIO.StringIO("100 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 1000000)



    # ----
    # eval
    # ----

    def test_eval_small_range (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_100_200 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_201_210 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_900_1000 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    def test_eval_large_range (self) :
        v = collatz_eval(400001, 500000)
        self.assert_(v == 449)
	
    def test_eval_larger_range (self) :
        v = collatz_eval(800001, 900000)
        self.assert_(v == 525)
	
    # ----------
    # get_length
    # ----------
	
    def test_get_length_10 (self) :
        v = get_length (10)
        self.assert_(v == 7)

    def test_get_length_5 (self) :
        v = get_length (5)
        self.assert_(v == 6)

    def test_get_length_50 (self) :
        v = get_length (50)
        self.assert_(v == 25)


    # -----
    # print
    # -----

    def test_print_normal (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_random_numbers (self) :
        w = StringIO.StringIO()
        collatz_print(w, 234, 123, 67)
        self.assert_(w.getvalue() == "234 123 67\n")

    def test_print_big_numbers (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1000000, 374, 1)
        self.assert_(w.getvalue() == "1000000 374 1\n")

    def test_print_simple_numbers (self) :
        w = StringIO.StringIO()
        collatz_print(w, 5, 5, 6)
        self.assert_(w.getvalue() == "5 5 6\n")


    # -----
    # solve
    # -----

    def test_solve_simple (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_big_ranges (self) :
        r = StringIO.StringIO("481354 485994\n934511 808512\n257972 114931\n935653 271837\n941784 299817\n665839 754049\n36170 412962\n850817 184452\n975033 975933\n691108 152452")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "481354 485994 382\n934511 808512 525\n257972 114931 443\n935653 271837 525\n941784 299817 525\n665839 754049 504\n36170 412962 449\n850817 184452 525\n975033 975933 339\n691108 152452 509\n")

    def test_solve_backwards_ranges (self) :
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")



# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."



