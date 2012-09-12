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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_eval_helper

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_0 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_1 (self) :
        r = StringIO.StringIO("5 5\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  5)
        self.assert_(a[1] == 5)
    
    def test_read_2 (self) :
        r = StringIO.StringIO("999999 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  999999)
        self.assert_(a[1] == 999999)
    
    def test_read_3 (self) :
        r = StringIO.StringIO(" 5\n")
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

    def test_eval_5 (self) :
        v = collatz_eval(500, 600)
        self.assert_(v == 137)

    def test_eval_6 (self) :
        v = collatz_eval(1025, 6026)
        self.assert_(v == 238)

    def test_eval_7 (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    def test_eval_8 (self) :
        v = collatz_eval(200, 100)
        self.assert_(v == 125)
    
    def test_eval_9 (self) :
        v = collatz_eval(210, 201)
        self.assert_(v == 89)

    def test_eval_10 (self) :
        v = collatz_eval(1000, 900)
        self.assert_(v == 174)

    def test_eval_11 (self) :
        v = collatz_eval(600, 500)
        self.assert_(v == 137)

    def test_eval_12 (self) :
        v = collatz_eval(6025, 1025)
        self.assert_(v == 238)

    # -----------
    # eval_helper
    # -----------
    def testEvalHelper1 (self) :
        v = collatz_eval_helper(999999)
        self.assert_(v == 259)
    

    def testEvalHelper2 (self) :
        v = collatz_eval_helper(1)
        self.assert_(v == 1)
    

    def testEvalHelper3 (self) :
        v = collatz_eval_helper(500000)
        self.assert_(v == 152)
    

    def testEvalHelper4 (self) :
        v = collatz_eval_helper(42)
        self.assert_(v == 9)
    
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def testPrint2 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 10, 100, 200)
        self.assert_(w.getvalue() == "10 100 200\n")

    def testPrint3 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 1, 2, 3)
        self.assert_(w.getvalue() == "1 2 3\n")

    def testPrint4 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 123456789, 123456789, 123456789)
        self.assert_(w.getvalue() == "123456789 123456789 123456789\n")

    def testPrint5 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 5000, 1000, 1000)
        self.assert_(w.getvalue() == "5000 1000 1000\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def testSolve2 (self) :
        r = StringIO.StringIO("1 1\n5 2\n2 5\n6 7\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n5 2 8\n2 5 8\n6 7 17\n")

    def testSolve3 (self) :
        r = StringIO.StringIO("8 9\n10 100\n25 26\n1 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "8 9 20\n10 100 119\n25 26 24\n1 1000 179\n")

    def testSolve4 (self) :
        r = StringIO.StringIO("2000 4000\n3000 5000\n4000 6000\n5000 7000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "2000 4000 238\n3000 5000 238\n4000 6000 236\n5000 7000 262\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
