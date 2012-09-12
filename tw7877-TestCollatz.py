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

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_fail (self) :
        r = StringIO.StringIO("")
        a = [0,0]
        b = collatz_read(r,a)
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

    def test_read_2 (self) :
        r = StringIO.StringIO("500 500\n")
        a = [0,0]
        b = collatz_read(r,a)
        self.assert_(b == True)
        self.assert_(a[0] == 500)
        self.assert_(a[1] == 500)

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

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_strings (self) :
        w = StringIO.StringIO()
        collatz_print(w, "Hi", "there", "person")
        self.assert_(w.getvalue() == "Hi there person\n")

    def test_print_anything (self) :
        w = StringIO.StringIO()
        collatz_print(w, 7, "ate", 9)
        self.assert_(w.getvalue() == "7 ate 9\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("5 15\n16 20\n21 25\n26 30\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "5 15 20\n16 20 21\n21 25 24\n26 30 112\n")    
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("500 600\n700 800\n900 1000\n1200 1300\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "500 600 137\n700 800 171\n900 1000 174\n1200 1300 177\n")

    def test_get_cycle_1 (self) :
        num = 1
        self.assert_(get_cycle_length(num) == 1)

    def test_get_cycle_5 (self) :
        num = 5
        self.assert_(get_cycle_length(num) == 6)

    def test_get_cycle_big (self) :
        num = 200000
        self.assert_(get_cycle_length(num) == 130)
        
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
