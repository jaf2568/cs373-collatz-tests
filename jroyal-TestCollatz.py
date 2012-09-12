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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_test_setup, collatz_eval_helper

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    collatz_test_setup();
            
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
        r = StringIO.StringIO("100 20\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100)
        self.assert_(a[1] == 20)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("50 50000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  50)
        self.assert_(a[1] == 50000)

    def test_eval_helper_1 (self):
        v = collatz_eval_helper(5)
        self.assert_(v == 6);
    def test_eval_helper_2 (self):
        v = collatz_eval_helper(11)
        self.assert_(v == 15);
    def test_eval_helper_3 (self):
        v = collatz_eval_helper(40)
        self.assert_(v == 9);
    def test_eval_helper_4 (self):
        v = collatz_eval_helper(1000)
        self.assert_(v == 112);
    def test_eval_helper_5 (self):
        v = collatz_eval_helper(1)
        self.assert_(v == 1);
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
        v = collatz_eval(1, 50000)
        self.assert_(v == 324)
        
    def test_eval_6 (self) :
        v = collatz_eval(1, 999999)
        self.assert_(v == 525)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 50000, 324)
        self.assert_(w.getvalue() == "1 50000 324\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("20 100\n1000 20000\n500000 999999\n11 12\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "20 100 119\n1000 20000 279\n500000 999999 525\n11 12 15\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("1 1\n60 100\n218 240\n3000 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n60 100 119\n218 240 128\n3000 1000 217\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
