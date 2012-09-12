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
    
    
    ##My own tests for read 
    
    def test_reverse (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 10)
        self.assert_(a[1] ==  1)
    
    def test_read_nothing (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)
        
    def test_read_large_nums (self) :
        r = StringIO.StringIO("5555555555 88374629\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 5555555555)
        self.assert_(a[1] == 88374629)
                    
    
    
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
        
        
    #my own tests for eval
    
    def test_eval_out_of_order (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)
    
    def test_eval_same_num (self) :
        v = collatz_eval(3, 3)
        self.assert_(v == 8) 
    
    def test_eval_large_num (self):
        v = collatz_eval(1, 999999) 
        self.assert_(v == 525)
        
        
     
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    
    
    ##my own print tests
    
    def test_print_large_num (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 999999, 525)
        self.assert_(w.getvalue() == "1 999999 525\n")
            
    def test_print_same_num (self) :
        w = StringIO.StringIO()
        collatz_print(w, 3, 3, 8)
        self.assert_(w.getvalue() == "3 3 8\n")
            
    def test_print_another_test (self) :
        w = StringIO.StringIO()
        collatz_print(w, 777, 77, 171)
        self.assert_(w.getvalue() == "777 77 171\n")
        
        
        
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


    ##my own solve tests
    
    def test_solve_rev (self) :
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")
    
    def test_solve_large (self) :
        r = StringIO.StringIO("5000 10000\n470000 500000\n777777 888888\n1 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "5000 10000 262\n470000 500000 426\n777777 888888 525\n1 999999 525\n")
        
    def test_solve_other (self) :
        r = StringIO.StringIO("9 4050\n115 135\n220 5000\n68 854\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "9 4050 238\n115 135 122\n220 5000 238\n68 854 171\n")
        
    
    # ----
    # cycle length
    # ----
    
    def test_cycle_length_max_num_for_cache (self):
        v = collatz_cycle_length(999999)
        self.assert_(v == 259)
        
    def test_cycle_length1 (self):
        v = collatz_cycle_length(548763)
        self.assert_(v == 178)
        
    def test_cycle_length2 (self):
        v = collatz_cycle_length(97)
        self.assert_(v == 119)
        
    def test_cycle_length4 (self):
        v = collatz_cycle_length(59)
        self.assert_(v == 33)
        
    def test_cycle_length5 (self):
        v = collatz_cycle_length(175)
        self.assert_(v == 81) 
    
        
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."