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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

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
        r = StringIO.StringIO("500 101\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 500)
        self.assert_(a[1] == 101)

    def test_read_3 (self) :
        r = StringIO.StringIO("1000000 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 1000000)
        self.assert_(a[1] == 1000000)

    def test_read_4 (self) :
        r = StringIO.StringIO("36843 972436\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 36843)
        self.assert_(a[1] == 972436)		

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
        v = collatz_eval(408, 408)
        self.assert_(v == 28)

    def test_eval_6 (self) :
        v = collatz_eval(1000000, 999999)
        self.assert_(v == 259)

    def test_eval_7 (self) :
        v = collatz_eval(105549, 85547)
        self.assert_(v == 341)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 1000, 174)
        self.assert_(w.getvalue() == "100 1000 174\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 145912, 992630, 525)
        self.assert_(w.getvalue() == "145912 992630 525\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 67313, 67101, 268)
        self.assert_(w.getvalue() == "67313 67101 268\n")

    # -----
    # cycle_length
    # -----
    def test_cyclelength (self) :
	cache = [0] * 1000000
	v = cycle_length(0,cache)
        self.assert_(v == 0)

    def test_cyclelength (self) :
	cache = [0] * 1000000
	v = cycle_length(1,cache)
        self.assert_(v == 1)

    def test_cyclelength (self) :
	cache = [0] * 1000000
	v = cycle_length(25,cache)
        self.assert_(v == 24)

    def test_cyclelength (self) :
	cache = [0] * 1000000
	v = cycle_length(427013,cache)
        self.assert_(v == 74)

    def test_cyclelength (self) :
	cache = [0] * 1000000
	v = cycle_length(1000000,cache)
        self.assert_(v == 153)

    def test_cyclelength (self) :
	cache = [0] * 1000000
	v = cycle_length(985604,cache)
        self.assert_(v == 145)


    # -----
    # solve
    # -----
  
    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
  
    def test_solve (self) :
        r = StringIO.StringIO("848164 848292\n178805 179251\n833861 833921\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "848164 848292 251\n178805 179251 272\n833861 833921 238\n")
 
    def test_solve (self) :
        r = StringIO.StringIO("1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")
  
    def test_solve (self) :
        r = StringIO.StringIO("255734 125906\n521527 590812\n970018 473352\n253387 737843\n904767 536685\n221798 881857\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "255734 125906 443\n521527 590812 452\n970018 473352 525\n253387 737843 509\n904767 536685 525\n221798 881857 525\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
