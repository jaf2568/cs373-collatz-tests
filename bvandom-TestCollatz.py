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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_computeCycle, collatz_eager

# -----------
# TestCollatz
# -----------

# Note: The number in front of a function indicates where it is in the test file.
#     e.g. "1. read" --> test1...() tests collatz_read().
#
# Collatz              (42)
# 1.      read         (7)
# 2.      eval         (12)
# 3.      print        (4)
# 4.      solve        (5)
# 5.      computeCycle (10)
# 6.      eager        (4)

class TestCollatz (unittest.TestCase) :

    # ------------
    # test1 - read
    # ------------

    def test1_basic (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test1_backwards (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 10)
    	self.assert_(a[1] == 1)

    def test1_largeValues (self) :
        r = StringIO.StringIO("100 11234\n")
        a = [0, 0]
        b = collatz_read(r, a)
    	self.assert_(b == True)
    	self.assert_(a[0] == 100)
    	self.assert_(a[1] == 11234)

    def test1_failNewLine (self) :
        r = StringIO.StringIO("\n")
        a = [0, 0]
        b = collatz_read(r, a)
    	self.assert_(b != True)

    def test1_failOneValue (self) :
        r = StringIO.StringIO("110")
        a = [0, 0]
        b = collatz_read(r, a)
    	self.assert_(b != True)

    def test1_failEmptyString (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
    	self.assert_(b != True)

    def test1_whiteSpace (self) :
        r = StringIO.StringIO("22 \t 48 \r\n")
        a = [0, 0]
        b = collatz_read(r, a)
    	self.assert_(b == True)
    	self.assert_(a[0] == 22)
    	self.assert_(a[1] == 48)

    # ------------
    # test2 - eval
    # ------------

    def test2_smallRange (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test2_maxInRange (self) :
        v = collatz_eval(1, 10)
        i = collatz_eval(9, 9)
        self.assert_(v == 20)
        self.assert_(v == i)

    def test2_backwards (self) :
        v = collatz_eval(1, 10)
        j = collatz_eval(10, 1)
        self.assert_(v == 20)
        self.assert_(v == j)

    def test2_mediumRange (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test2_smallRange1 (self) :
        v = collatz_eval(201, 210)
    	self.assert_(v == 89)

    def test2_mediumRange2 (self) :
        v = collatz_eval(900, 1000)
    	self.assert_(v == 174)

    def test2_overflow (self) :
    	v = collatz_eval(1, 200000)
        self.assert_(v == 383)

    def test2_rangesComparison (self) :
    	v1 = collatz_eval(576, 1538)
        v2 = collatz_eval(570, 1550)
        self.assert_(v2 == 182)
    	self.assert_(v2 >= v1)
    
    def test2_rangesTrick (self) :
    	v1 = collatz_eval(50, 100)
    	v2 = collatz_eval(1, 100)
        self.assert_(v1 == 119)
        self.assert_(v1 == v2)

    def test2_rangesTrick2 (self) :
    	v1 = collatz_eval(1, 2000)
    	v2 = collatz_eval(1000, 2000)
        self.assert_(v1 == 182)
        self.assert_(v1 == v2)
    
    def test2_handleOverMil (self) :
    	v = collatz_eval(1000000, 1010000)
        self.assert_(v == 489)
    
    def test2_overflow2 (self) :
        v1 = collatz_eval(232545, 681701)
        v2 = collatz_eval(773104, 675975)
        self.assert_(v1 == 509)
        self.assert_(v2 == 504)

    # -------------
    # test3 - print
    # -------------

    def test3_basic (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test3_wrongAns (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 12)
        self.assert_(w.getvalue() != "100 200 125\n")

    def test3_reverseRange (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1000, 900, 174)
        self.assert_(w.getvalue() == "1000 900 174\n")
    
    def test3_overMil (self) :
    	w = StringIO.StringIO()
        collatz_print(w, 1450000, 2000000, 557)
        self.assert_(w.getvalue() == "1450000 2000000 557\n")

    # -----
    # solve
    # -----

    def test4_basic (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test4_200k (self) :
        r = StringIO.StringIO("1 200000\n200001 400000\n400001 600000\n600001 800000\n800001 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 200000 383\n200001 400000 443\n400001 600000 470\n600001 800000 509\n800001 999999 525\n")
    
    def test4_small (self) :
        r = StringIO.StringIO("1 1\n2 2\n3 3\n4 4\n5 5\n6 6\n7 7\n8 8\n9 9\n10 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n2 2 2\n3 3 8\n4 4 3\n5 5 6\n6 6 9\n7 7 17\n8 8 4\n9 9 20\n10 10 7\n")

    def test4_overflow1 (self) :
        r = StringIO.StringIO("2154 40254\n75594 81000\n82450 130131\n146877 132000\n160475 195590\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "2154 40254 324\n75594 81000 351\n82450 130131 354\n146877 132000 375\n160475 195590 365\n")

    def test4_overflow2 (self) :
        r = StringIO.StringIO("200145 230000\n245067 266287\n274340 302660\n294422 357583\n367489 395554\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "200145 230000 386\n245067 266287 407\n274340 302660 389\n294422 357583 441\n367489 395554 436\n")

    ## --------------------
    ## test5 - computeCycle
    ## --------------------

    def test5_baseCase (self) :
    	v = collatz_computeCycle(1, 1)
        self.assert_(v == 1)
    
    def test5_maxInTen (self) :
    	v = collatz_computeCycle(9, 1)
        self.assert_(v == 20)

    def test5_classExample (self) :
        v = collatz_computeCycle(3, 1)
        self.assert_(v == 8)

    def test5_basicRange (self) :
    	sum_i = 0
        for i in range(1, 11) :
	        sum_i += collatz_computeCycle(i, 1)
    	self.assert_(sum_i == 77)

    def test5_overflow1 (self) :
    	v = collatz_computeCycle(159487, 1)
    	self.assert_(v == 184)

    def test5_overflow2 (self) :
    	v = collatz_computeCycle(113383, 1)
    	self.assert_(v == 248)

    def test5_overflow3 (self) :
        v = collatz_computeCycle(997823, 1)
        self.assert_(v == 440)

    def test5_recursionOutsideCache (self) :
        v = collatz_computeCycle(1819, 1)
        self.assert_(v == 162)

    def test5_million (self) :
    	v = collatz_computeCycle(1000000, 1)
        self.assert_(v == 153)

    def test5_huge (self) :
        v = collatz_computeCycle(1200000000, 1)
        self.assert_(v == 109)

    ## -------------
    ## test6 - eager
    ## -------------

    def test6_range1 (self) :
        collatz_eager()
        n = 1
        i = 1
        while i < 100000 :
            c = collatz_computeCycle(i, 1)
            self.assert_(c == n)
            n += 1
            i *= 2

    def test6_range3 (self) :
        collatz_eager()
        n = 8
        i = 3
        while i < 100000 :
            c = collatz_computeCycle(i, 1)
            self.assert_(c == n)
            n += 1
            i *= 2

    def test6_range5 (self) :
        collatz_eager()
        n = 6
        i = 5
        while i < 100000 :
            c = collatz_computeCycle(i, 1)
            self.assert_(c == n)
            n += 1
            i *= 2

    def test6_range7 (self) :
        collatz_eager()
        n = 17
        i = 7
        while i < 100000 :
            c = collatz_computeCycle(i, 1)
            self.assert_(c == n)
            n += 1
            i *= 2

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
