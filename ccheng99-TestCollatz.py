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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, get_cycle_length

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
	
    def test_read_multiline (self) :
        r = StringIO.StringIO("1 10\n100 200\n101 120")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
		
	b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 200)
	
	b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 101)
        self.assert_(a[1] == 120)
		
    def test_read_empty (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)

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
		
    def test_print_multiline (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
	collatz_print(w, 100, 200, 125)
	collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n")
	
	# Make sure that it prints regardless of input
    def test_print_multiline_badinput (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
	collatz_print(w, 100, 200, 2)
	collatz_print(w, 201, 210, 5)
        self.assert_(w.getvalue() == "1 10 20\n100 200 2\n201 210 5\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
	
    def test_solve_oneline (self) :
        r = StringIO.StringIO("1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n")
	
    def test_solve_empty (self) :
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")
        
        
    # ----
    # get_cycle_length
    # ----
    
    def test_get_cycle_length (self) :
        result = get_cycle_length(10)
        self.assert_(result == 7)
        
    def test_get_cycle_length_large_number (self) :
        result = get_cycle_length(113383)
        self.assert_(result == 248)
        
    def test_get_cycle_length_large_number2 (self) :
        result = get_cycle_length(982037)
        self.assert_(result == 140)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
