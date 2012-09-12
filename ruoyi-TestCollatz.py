#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2012
# Ruoyi Pu
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

#from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length
from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    #-------------
    # cycle_length
    #-------------

#    def test_cycle_length_1 (self) :
#        self.assert_(cycle_length(1) == 1)

#    def test_cycle_length_2 (self) :
#        self.assert_(cycle_length(1000000) == 153)

#    def test_cycle_length_3 (self) :
#        self.assert_(cycle_length(135664) == 88)

    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 1)

    def test_read_3 (self) :
        r = StringIO.StringIO("1 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
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

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1000000, 153)
        self.assert_(w.getvalue() == "1 1000000 153\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n1 9\n1 1000000\n1000000 1000000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n1 9 20\n1 1000000 525\n1000000 1000000 153\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("9 15\n10 1\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "9 15 20\n10 1 20\n210 201 89\n1000 900 174\n")
        
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
