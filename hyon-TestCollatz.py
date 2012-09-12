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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length

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
        
    def test_read_2 (self) :
	r = StringIO.StringIO("5 9\n")
	a = [0, 0]
	b = collatz_read(r, a)
	self.assert_(b == True)
	self.assert_(a[0] == 5)
	self.assert_(a[1] == 9)
	
    def test_read_3 (self) :
	r = StringIO.StringIO("3 3\n")
	a = [0, 0]
	b = collatz_read(r, a)
	self.assert_(b == True)
	self.assert_(a[0] == 3)
	self.assert_(a[1] == 3)
	
    def test_read_4 (self) :
	r = StringIO.StringIO("100 80\n")
	a = [0, 0]
	b = collatz_read(r, a)
	self.assert_(b == True)
	self.assert_(a[0] == 100)
	self.assert_(a[1] == 80)
	
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
        v = collatz_eval(10, 1)
        self.assert_(v == 20)
        
    def test_eval_7 (self) :
        v = collatz_eval(6, 4)
        self.assert_(v == 9)        
        
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 5, 9, 20)
        self.assert_(w.getvalue() == "5 9 20\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 3, 3, 8)
        self.assert_(w.getvalue() == "3 3 8\n")        
        
    def test_print_4 (self) :
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
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 10\n5 9\n3 3\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n5 9 20\n3 3 8\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("59 61\n10 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "59 61 33\n10 10 7\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("9 10\n2 34\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "9 10 20\n2 34 112\n")
        
    # --------------------
    # collatz_cycle_length
    # --------------------
    
    def test_cycle_length (self) :
	cache = [0] * 1000000
	cache[0] = 1
	n = collatz_cycle_length(7, cache)
	self.assert_(n == 17)
	
    def test_cycle_length_2 (self) :
      	cache = [0] * 1000000
	cache[0] = 1
	n = collatz_cycle_length(10, cache)
	self.assert_(n == 7)
	
    def test_cycle_length_3 (self) :
      	cache = [0] * 1000000
	cache[0] = 1
	n = collatz_cycle_length(999999, cache)
	self.assert_(n == 259)
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
