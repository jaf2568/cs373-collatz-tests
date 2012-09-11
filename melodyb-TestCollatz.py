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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_recursiveCycle

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
        
    def test_read_2 (self) :
        r = StringIO.StringIO("200 300\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 200)
        self.assert_(a[1] == 300)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("4000 150\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 4000)
        self.assert_(a[1] == 150)
        
    def test_read_4 (self) :
        r = StringIO.StringIO("3 1600\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 3)
        self.assert_(a[1] == 1600)
        
    def test_read_5 (self) :
        r = StringIO.StringIO("1600 3\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1600)
        self.assert_(a[1] == 3)
        
    def test_read_6 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)


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
        v = collatz_eval(22, 22)
        self.assert_(v == 16)
        
    def test_eval_6 (self) :
        v = collatz_eval(1000, 900)
        self.assert_(v == 174)
        
    def test_eval_7 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 3, 3, 8)
        self.assert_(w.getvalue() == "3 3 8\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1000, 900, 174)
        self.assert_(w.getvalue() == "1000 900 174\n")
        
    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 560, 899, 179)
        self.assert_(w.getvalue() == "560 899 179\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("63500 798004\n3209 689943\n293 38\n888888 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "63500 798004 509\n3209 689943 509\n293 38 128\n888888 999999 507\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("45 500\n3900 76666\n12 3\n444 9999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "45 500 144\n3900 76666 340\n12 3 20\n444 9999 262\n")
        
    def test_solve_4 (self) :
        r = StringIO.StringIO("4000 40000\n3900 70000\n100000 1000\n39 78\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "4000 40000 324\n3900 70000 340\n100000 1000 351\n39 78 116\n")
        
    # -----
    # solve
    # -----

    def test_recursiveCycle_1 (self) :
        v = collatz_recursiveCycle(22, 1)
        self.assert_(v == 16)
        
    def test_recursiveCycle_2 (self) :
        v = collatz_recursiveCycle(77, 1)
        self.assert_(v == 23)
        
    def test_recursiveCycle_3 (self) :
        v = collatz_recursiveCycle(900, 1)
        self.assert_(v == 55)
        
    def test_recursiveCycle_4 (self) :
        v = collatz_recursiveCycle(3678, 1)
        self.assert_(v == 163)
        
    def test_recursiveCycle_5 (self) :
        v = collatz_recursiveCycle(21, 1)
        self.assert_(v == 8)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."