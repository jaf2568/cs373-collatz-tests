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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle

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
        r = StringIO.StringIO("221 2210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  221)
        self.assert_(a[1] == 2210)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("32 330\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  32)
        self.assert_(a[1] == 330)
        
    def test_read_4 (self) :
        r = StringIO.StringIO("12313 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  12313)
        self.assert_(a[1] == 999999)

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
        v = collatz_eval(1, 999999)
        self.assert_(v == 525)
        
    def test_eval_6 (self) :
        v = collatz_eval(2132, 21344)
        self.assert_(v == 279)
        
    def test_eval_7 (self) :
        v = collatz_eval(3149, 91273)
        self.assert_(v == 351)
        
    def test_eval_8 (self) :
        v = collatz_eval(97141, 34892)
        self.assert_(v == 351)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 323, 1341, 1411)
        self.assert_(w.getvalue() == "323 1341 1411\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 131, 65645, 113)
        self.assert_(w.getvalue() == "131 65645 113\n")
        
    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 2348, 13634, 245452)
        self.assert_(w.getvalue() == "2348 13634 245452\n")
        
    def test_print_5 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 999999 525\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("2132 21344\n52352 43242\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "2132 21344 279\n52352 43242 314\n")
        
    def test_solve_4 (self) :
        r = StringIO.StringIO("456456 45123\n6318 31868\n16543 546321\n3564 244651\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "456456 45123 449\n6318 31868 308\n16543 546321 470\n3564 244651 443\n")
        
    def test_solve_5 (self) :
        r = StringIO.StringIO("64645 45066\n456045 654000\n54315 346822\n3125 24186\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "64645 45066 340\n456045 654000 509\n54315 346822 443\n3125 24186 282\n")
        
    # -----
    # cycle
    # -----
    
    def test_cycle_1 (self) :
        i = collatz_cycle(1)
        self.assert_(i == 1)
        
    def test_cycle_2 (self) :
        i = collatz_cycle(5)
        self.assert_(i == 6)
        
    def test_cycle_3 (self) :
        i = collatz_cycle(423423)
        self.assert_(i == 175)
        
    def test_cycle_4 (self) :
        i = collatz_cycle(213443)
        self.assert_(i == 125)
        
    def test_cycle_5 (self) :
        i = collatz_cycle(9843)
        self.assert_(i == 74)
        
    

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
