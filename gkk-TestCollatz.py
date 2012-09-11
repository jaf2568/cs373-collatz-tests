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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

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
        r = StringIO.StringIO("1 2\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 2)

    def test_read_3 (self) :
        r = StringIO.StringIO("2 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 2)
        self.assert_(a[1] == 1)

    def test_read_4 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)


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
        v = collatz_eval(2, 2)
        self.assert_(v == 2)

    def test_eval_7 (self) :
        v = collatz_eval(12, 14)
        self.assert_(v == 18)

    def test_eval_8 (self) :
        v = collatz_eval(14, 12)
        self.assert_(v == 18)

    # -----
    # print
    # -----

    def test_print_1 (self) :
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

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

    def test_print_5 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_print_6 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 2, 2, 2)
        self.assert_(w.getvalue() == "2 2 2\n")

    def test_print_7 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 12, 14, 18)
        self.assert_(w.getvalue() == "12 14 18\n")

    def test_print_8 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 14, 12, 18)
        self.assert_(w.getvalue() == "14 12 18\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("1 1\n2 2\n12 14\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n2 2 2\n12 14 18\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("1 2\n1 2\n1 2\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 2 2\n1 2 2\n1 2 2\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."

