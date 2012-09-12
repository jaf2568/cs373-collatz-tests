#!/usr/bin/env python

# -------------------------------
# Graham Benevelli
# EID: grambo
# CSID: grahambo
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_eval_single

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

    def test_read1 (self) :
        r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100)
        self.assert_(a[1] == 200)
        
    def test_read2 (self) :
        r = StringIO.StringIO("201 210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  201)
        self.assert_(a[1] == 210)

    def test_read3 (self) :
        r = StringIO.StringIO("900 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  900)
        self.assert_(a[1] == 1000)

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
        v = collatz_eval(2000, 3000)
        self.assert_(v == 217)

    def test_eval_7 (self) :
        v = collatz_eval(205, 391)
        self.assert_(v == 144)

    def test_eval_8 (self) :
        v = collatz_eval(999999, 1000000)
        self.assert_(v == 259)

    # -----------------
    # eval single value
    # -----------------

    def test_eval_single_1 (self) :
        v = collatz_eval_single(1)
        self.assert_(v == 1)

    def test_eval_single_2 (self) :
        v = collatz_eval_single(100)
        self.assert_(v == 26)

    def test_eval_single_3 (self) :
        v = collatz_eval_single(1000)
        self.assert_(v == 112)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO.StringIO("10 100\n1 2\n99 100\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 100 119\n1 2 2\n99 100 26\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n2 2\n999 999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n2 2 2\n999 999 50\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("1 1000000\n2 1000000\n3 1000000\n");
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1000000 525\n2 1000000 525\n3 1000000 525\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
