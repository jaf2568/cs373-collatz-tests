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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_max, collatz_cycle

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
        
    def test_read2 (self) :
        r = StringIO.StringIO("30 20\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 30)
        self.assert_(a[1] == 20)
        
    def test_read3 (self) :
        r = StringIO.StringIO("2000 3000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 2000)
        self.assert_(a[1] == 3000)

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
        v = collatz_eval(972699, 998031)
        self.assert_(v == 440)
        

    # -----
    # cycle
    # -----
    
    def test_cycle_1 (self) :
        v = collatz_cycle(5)
        self.assert_(v == 6)

    def test_cycle_2 (self) :
        v = collatz_cycle(9)
        self.assert_(v == 20)
        
    def test_cycle_3 (self) :
        v = collatz_cycle(1)
        self.assert_(v == 1)
        
    def test_cycle_4 (self) :
        v = collatz_cycle(6)
        self.assert_(v == 9)
        
    def test_cycle_5 (self) :
        v = collatz_cycle(15)
        self.assert_(v == 18)
    
    
    # -----
    # max
    # -----

    def test_max_1 (self) :
        v = collatz_max(1, 0)
        self.assert_(v == 1)
        
    def test_max_2 (self) :
        v = collatz_max(12, 3)
        self.assert_(v == 12)
        
    def test_max_3 (self) :
        v = collatz_max(14, 21)
        self.assert_(v == 21)
        
    def test_max_4 (self) :
        v = collatz_max(133, 144)
        self.assert_(v == 144)
        
    def test_max_5 (self) :
        v = collatz_max(12, 12)
        self.assert_(v == 12)

    # -----
    # print
    # -----

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")
        
    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")
        
    def test_print4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve2 (self) :
        r = StringIO.StringIO("201 210\n200 100\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "201 210 89\n200 100 125\n")
        

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."