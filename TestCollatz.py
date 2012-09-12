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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_find_cycle_length

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
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
    
    def test_read_1 (self) :
        r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 200)
    
    def test_read_2 (self) :
        r = StringIO.StringIO("201 210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 201)
        self.assert_(a[1] == 210)
    
    def test_read_3 (self) :
        r = StringIO.StringIO("900 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  900)
        self.assert_(a[1] == 1000)

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
        v = collatz_eval(569698, 513737)
        self.assert_(v == 452)
    
    def test_eval_6 (self) :
        v = collatz_eval(999999, 1)
        self.assert_(v == 525)
    
    def test_eval_7 (self) :
        v = collatz_eval(2, 2)
        self.assert_(v == 2)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    
    def test_print_1 (self) :
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

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    
    def test_solve_1 (self) :
        r = StringIO.StringIO("569698 513737\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "569698 513737 452\n")
    
    def test_solve_2 (self) :
        r = StringIO.StringIO("999999 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "999999 1 525\n")
    
    def test_solve_3 (self) :
        r = StringIO.StringIO("2 2\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "2 2 2\n")
    
    # -----
    # find_cycle_length
    # -----
    
    def test_find_cycle_length_1 (self) :
        result = collatz_find_cycle_length(5, {1: 1})
        self.assert_(result == 6)
    
    def test_find_cycle_length_2 (self) :
        result = collatz_find_cycle_length(22, {1: 1})
        self.assert_(result == 16)
    
    def test_find_cycle_length_3 (self) :
        result = collatz_find_cycle_length(2, {1: 1})
        self.assert_(result == 2)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
