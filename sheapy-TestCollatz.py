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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, calc_cycle

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
        r = StringIO.StringIO("999999 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  999999)
        self.assert_(a[1] == 1000000)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("34646 56725\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  34646)
        self.assert_(a[1] == 56725)

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
        v = collatz_eval(1, 1)
        self.assert_(v == 1)
        
    def test_eval_6 (self) :
        v = collatz_eval(1, 2)
        self.assert_(v == 2)  
        
    def test_eval_7 (self) :
        v = collatz_eval(999998, 999999)
        self.assert_(v == 259)
        
    def test_eval_8 (self) :
        v = collatz_eval(999999, 999998)
        self.assert_(v == 259)   
        
    def test_eval_9 (self) :
        v = collatz_eval(100, 100)
        self.assert_(v == 26)  
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 999998, 999999, 259)
        self.assert_(w.getvalue() == "999998 999999 259\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 2, 2)
        self.assert_(w.getvalue() == "1 2 2\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    # ----
    # calc_cycle
    # ----
    
    def test_calc_cycle_1 (self) :
        bad = [0] * 100
        r = 10
        v = calc_cycle(r,bad)
        self.assert_(v == 7)
    
    def test_calc_cycle_2 (self) :
        bad = [0] * 16
        r = 5
        v = calc_cycle(r,bad)
        self.assert_(v == 6)
    
    def test_calc_cycle_3 (self) :
        bad = [0] * 100
        r = 100
        v = calc_cycle(r,bad)
        self.assert_(v == 26)
    
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."