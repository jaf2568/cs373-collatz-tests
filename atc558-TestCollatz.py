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

from Collatz import *

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
        
    def test_read_2(self):
        r = StringIO.StringIO("")
        a = [0,0]
        b = collatz_read(r,a)
        self.assert_(b == False)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("1 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 1000000)

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
        
    # ---------------
    # find_num_cycles
    # ---------------
    """ MY PERSONAL FUNCTION
    def test_find_num_cycles_1(self):
        v = find_num_cycles(1)
        self.assert_(v == 1)

    def test_find_num_cycles_2(self):
        v = find_num_cycles(837799)
        self.assert_(v == 525)
        
    def test_find_num_cycles_3(self):
        v = find_num_cycles(999999)
        self.assert_(v == 259)
    """
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 210, 201, 89)
        self.assert_(w.getvalue() == "210 201 89\n")
    
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900000, 1000000, 507)
        self.assert_(w.getvalue() == "900000 1000000 507\n")
    

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n100 200\n201 210\n900000 1000000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n100 200 125\n201 210 89\n900000 1000000 507\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("210 201\n201 210\n1000 900\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "210 201 89\n201 210 89\n1000 900 174\n900 1000 174\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."