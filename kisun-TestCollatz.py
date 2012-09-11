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
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
        
    def test_read_2 (self) :
        r = StringIO.StringIO("9 30\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  9)
        self.assert_(a[1] == 30)
    
    def test_read_3 (self) :
        r = StringIO.StringIO("100000 400000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100000)
        self.assert_(a[1] ==  400000)
    
    def test_read_4 (self) :
        r = StringIO.StringIO("9999 10000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  9999)
        self.assert_(a[1] == 10000)

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
    
    def test_eval_5 (self):
        v = collatz_eval(1, 1)
        self.assert_(v == 1)
    
    def test_eval_6 (self):
        v = collatz_eval(2, 2)
        self.assert_(v == 2)
        
    def test_eval_7 (self):
        v = collatz_eval(1, 2)
        self.assert_(v == 2)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self):
        w = StringIO.StringIO()
        collatz_print(w, 50, 60, 70)
        self.assert_(w.getvalue() == "50 60 70\n")
        
    def test_print_3 (self):
        w = StringIO.StringIO()
        collatz_print(w, 1, 2, 2)
        self.assert_(w.getvalue() == "1 2 2\n")
        
    def test_print_4 (self):
        w = StringIO.StringIO()
        collatz_print(w, 9, 9, 9)
        self.assert_(w.getvalue() == "9 9 9\n")
        
    def test_print_5 (self):
        w = StringIO.StringIO()
        collatz_print(w, 7, 6, 5)
        self.assert_(w.getvalue() == "7 6 5\n")
        
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("142013 151511\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "142013 151511 375\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("1 50\n50 1000\n1000 9001\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 50 112\n50 1000 179\n1000 9001 262\n")
        
    def test_solve_4 (self) :
        r = StringIO.StringIO("847424 860776\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "847424 860776 419\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
