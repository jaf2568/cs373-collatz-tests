#!/usr/bin/env python

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_function, collatz_max_cycle

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
        r = StringIO.StringIO("1000 134\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1000)
        self.assert_(a[1] == 134)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 1)
        
    def test_read_4 (self) :
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
        
    def test_eval_5 (self) :
        v = collatz_eval(1000, 900)
        self.assert_(v == 174)
        
    def test_eval_6 (self) :
        v = collatz_eval(210, 201)
        self.assert_(v == 89)
        
    def test_eval_7 (self) :
        v = collatz_eval(5, 5)
        self.assert_(v == 6)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 123, 456, 789)
        self.assert_(w.getvalue() == "123 456 789\n")
    
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 999, 111, 0)
        self.assert_(w.getvalue() == "999 111 0\n")
        
    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 42, 42, 42)
        self.assert_(w.getvalue() == "42 42 42\n")
    
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("456 123\n123 456\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "456 123 144\n123 456 144\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("999 10000\n10000 20011\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "999 10000 262\n10000 20011 279\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("24356 121536\n45454 21315\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "24356 121536 354\n45454 21315 324\n")


    # -----
    # function
    # -----
    def test_function_1 (self) :
        r = collatz_function(1)
        self.assert_(r == 1)
        
    def test_function_2 (self) :
        r = collatz_function(5)
        self.assert_(r == 6)
        
    def test_function_3 (self) :
        r = collatz_function(3)
        self.assert_(r == 8)
        
    def test_function_4 (self) :
        r = collatz_function(555)
        self.assert_(r == 31)
        
    # -----
    # max_cycles
    # -----
    def test_max_cycles_1 (self) :
        r = collatz_max_cycle(1, 10)
        self.assert_(r == 20)
        
    def test_max_cycles_2 (self) :
        r = collatz_max_cycle(800000, 1000000)
        self.assert_(r == 525)
        
    def test_max_cycles_3 (self) :
        r = collatz_max_cycle(1, 200000)
        self.assert_(r == 383)
        
    def test_max_cycles_4 (self) :
        r = collatz_max_cycle(123, 456)
        self.assert_(r == 144)
        
    def test_max_cycles_6 (self) :
        l = collatz_max_cycle(3367, 159873)
        r = collatz_max_cycle(159873, 3367)
        self.assert_(l == r)
    
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
