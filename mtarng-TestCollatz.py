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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length, cycle_recursion, populate_memory, access_cache

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

    def test_read2 (self) :
        r = StringIO.StringIO("6 15\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  6)
        self.assert_(a[1] == 15)
		
    def test_read3 (self) :
        r = StringIO.StringIO("19 300\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  19)
        self.assert_(a[1] == 300)
		
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
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 50\n50 1000\n1000 9001\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 50 112\n50 1000 179\n1000 9001 262\n")
	
    def test_solve3 (self) :
        r = StringIO.StringIO("4 6\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "4 6 9\n")
		
	# ----
	# cycle_length
	# ----
	
    def test_cycle_length_1 (self) :
        self.assert_(3 == cycle_length(4))
		
    def test_cycle_length_2 (self) :
	self.assert_(6 == cycle_length(5))
		
    def test_cycle_length_3 (self) :
	self.assert_(9 == cycle_length(6))
	
    def test_cycle_length_4 (self) :
	self.assert_(25 == cycle_length(50))	
		
    
    # ----
    # cycle_recursion
    # ----	

    def test_cycle_recursion_1 (self) :
        self.assert_(1 == cycle_recursion(1))

    def test_cycle_recursion_2 (self) :
        self.assert_(8 == cycle_recursion(3))

    def test_cycle_recursion_3 (self) :
        self.assert_(9 == cycle_recursion(6))

    def test_cycle_recursion_4 (self) :
        self.assert_(17 == cycle_recursion(7))

    # ----
    # populate_memory
    # access_cache
    # ----

    def test_populate_memory_1 (self) :
        populate_memory (10)
        self.assert_(access_cache(1) == 1)

    def test_populate_memory_2 (self) :
        populate_memory (3)
        self.assert_(access_cache(2) == 2)
        self.assert_(access_cache(3) == 8)

    def test_populate_memory_3 (self) :
        populate_memory (100)
        self.assert_(access_cache(100) == 26)
        self.assert_(access_cache(99) == 26)
        self.assert_(access_cache(73) == 116)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
