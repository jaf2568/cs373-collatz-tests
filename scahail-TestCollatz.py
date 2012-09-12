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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_len

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
        r = StringIO.StringIO("1 10 20\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)

    def test_read_3 (self) : 
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)

    def test_read_4 (self) :
        r = StringIO.StringIO("20 30 50\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 20)
        self.assert_(a[1] == 30)

    def test_read_5 (self) :
        r = StringIO.StringIO("03 040")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 3)
        self.assert_(a[1] == 40)

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
        v = collatz_eval(999998, 999999)
        self.assert_(v == 259)

    def test_eval_7 (self) :
        v = collatz_eval(1, 999999)
        self.assert_(v == 525)

    def test_eval_8 (self) :
        v = collatz_eval(50, 100)
        self.assert_(v == 119)

    def test_eval_9 (self) :
        v = collatz_eval(1, 100)
        self.assert_(v == 119)

    def test_eval_10 (self) :
        v = collatz_eval(50000, 100000)
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
        collatz_print(w, 2, 20, 40)
        self.assert_(w.getvalue() == "2 20 40\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 3, 30, 70)
        self.assert_(w.getvalue() == "3 30 70\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 0, 0, 0)
        self.assert_(w.getvalue() == "0 0 0\n")

    def test_print_5 (self) :
        w = StringIO.StringIO()
        collatz_print(w, -1, -1, -1)
        self.assert_(w.getvalue() == "-1 -1 -1\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 3\n3 5\n4 5\n5 6\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 3 8\n3 5 8\n4 5 6\n5 6 9\n")
    
    def test_solve_3 (self) :
        r = StringIO.StringIO("10 20\n20 30\n30 40\n40 50\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 20 21\n20 30 112\n30 40 107\n40 50 110\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("20 10\n30 20\n40 30\n50 40\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "20 10 21\n30 20 112\n40 30 107\n50 40 110\n")

    def test_solve_5 (self) :
        r = StringIO.StringIO("100 200\n200 300\n300 400\n400 500\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "100 200 125\n200 300 128\n300 400 144\n400 500 142\n")

    def test_solve_6 (self) :
        r = StringIO.StringIO("200 100\n300 200\n400 300\n500 400\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "200 100 125\n300 200 128\n400 300 144\n500 400 142\n")

    def test_solve_7 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_8 (self) :
        r = StringIO.StringIO("50 60\n60 70\n70 80\n80 90\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "50 60 113\n60 70 108\n70 80 116\n80 90 111\n")

    def test_solve_9 (self) :
        r = StringIO.StringIO("1 100000\n2 20000\n3 3000\n4 400\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 100000 351\n2 20000 279\n3 3000 217\n4 400 144\n")

    def test_solve_10 (self) :
        r = StringIO.StringIO("200 400\n400 800\n800 1600\n1600 3200\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "200 400 144\n400 800 171\n800 1600 182\n1600 3200 217\n")    

    # -----------------
    # collatz_cycle_len
    # -----------------

    def test_collatz_cycle_len_1 (self) :
        v = collatz_cycle_len(1)
        self.assert_(v == 1)

    def test_collatz_cycle_len_2 (self) :
        v = collatz_cycle_len(5)
        self.assert_(v == 6)

    def test_collatz_cycle_len_3 (self) :
        v = collatz_cycle_len(3)
        self.assert_(v == 8)

    def test_collatz_cycle_len_4 (self) :
        v = collatz_cycle_len(22)
        self.assert_(v == 16)

    def test_collatz_cycle_len_5 (self) :
        v = collatz_cycle_len(365)
        self.assert_(v == 95)

    def test_collatz_cycle_len_6 (self) :
        v = collatz_cycle_len(999999)
        self.assert_(v == 259)

    def test_collatz_cycle_len_7 (self) :
        v = collatz_cycle_len(4073)
        self.assert_(v == 96)

    def test_collatz_cycle_len_8 (self) :
        v = collatz_cycle_len(2016)
        self.assert_(v == 113)

    def test_collatz_cycle_len_9 (self) :
        v = collatz_cycle_len(700000)
        self.assert_(v == 168)

    def test_collatz_cycle_len_10 (self) :
        v = collatz_cycle_len(111111)
        self.assert_(v == 116)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
