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
from Collatz import collatz_eval_cache, collatz_precalc_cache, collatz_solve_cache

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

    def test_read_negative (self) :
        r = StringIO.StringIO("-1 50\n")
        a = [0, 0]
        b = False
        try:
            b = collatz_read(r, a)
        except AssertionError, e:
            self.assert_(b    == False)
            self.assert_(a[0] == -1)
            self.assert_(a[1] == 50)
            return
        # We should never get here, so fail
        self.assert_(b == True)

    def test_read_alpha (self) :
        r = StringIO.StringIO("abc $%^\n")
        a = [0, 0]
        b = False
        try:
            b = collatz_read(r, a)
        except ValueError, e:
            self.assert_(b    == False)
            self.assert_(a[0] == 0)
            self.assert_(a[1] == 0)
            return
        # We should never get here, so fail
        self.assert_(b == True)

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

    def test_eval_same (self) :
        v = collatz_eval(5, 5)
        self.assert_(v == 6)

    # ----------
    # eval_cache
    # ----------

    def test_eval_cache_1 (self) :
        cache = {1:1, 2:2, 3:8, 4:3, 5:6}
        v = collatz_eval_cache(1, 10, cache)
        self.assert_(v == 20)

    def test_eval_cache_2 (self) :
        cache = {1:1, 2:2, 3:8, 4:3, 5:6, 7:17, 15:18, 19:21, 24:11, 34:14}
        v = collatz_eval_cache(20, 40, cache)
        self.assert_(v == 112)

    def test_eval_cache_3 (self) :
        cache = {16:5, 21:8, 24:11, 40:9, 160:11, 52:12, 22:16, 30:19, 18:21, 25:24}
        v = collatz_eval_cache(100, 200, cache)
        self.assert_(v == 125)

    # -------------
    # precalc_cache
    # -------------

    def test_precalc_cache_1 (self) :
        cache = {}
        collatz_precalc_cache(1, 10, cache)
        self.assert_(cache[1] ==  1)
        self.assert_(cache[3] ==  8)
        self.assert_(cache[9] == 20)

    def test_precalc_cache_2 (self) :
        cache = {}
        collatz_precalc_cache(10, 1, cache)
        self.assert_(cache[1] ==  1)
        self.assert_(cache[5] ==  6)
        self.assert_(cache[7] == 17)

    def test_precalc_cache_3 (self) :
        cache = {}
        collatz_precalc_cache(100, 200, cache)
        self.assert_(cache[106] ==  13)
        self.assert_(cache[134] ==  29)
        self.assert_(cache[159] ==  55)
        self.assert_(cache[189] == 107)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_alpha (self) :
        w = StringIO.StringIO()
        collatz_print(w, 'abc', 123, "^^^")
        self.assert_(w.getvalue() == "abc 123 ^^^\n")

    def test_print_object (self) :
        w = StringIO.StringIO()
        collatz_print(w, w, -1, self)
        ws = str(w)
        ss = str(self)
        self.assert_(w.getvalue() == (ws + " -1 " + ss + "\n"))

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("20 40\n1200 1500\n5000 5100\n10000 11000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "20 40 112\n1200 1500 177\n5000 5100 179\n10000 11000 268\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("149805 468357\n111816 181804\n747961 968449\n312738 923696\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "149805 468357 449\n111816 181804 383\n747961 968449 525\n312738 923696 525\n") 

    # -----------
    # solve_cache
    # -----------

    def test_solve_cache_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve_cache(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_cache_2 (self) :
        r = StringIO.StringIO("20 40\n1200 1500\n5000 5100\n10000 11000\n")
        w = StringIO.StringIO()
        collatz_solve_cache(r, w)
        self.assert_(w.getvalue() == "20 40 112\n1200 1500 177\n5000 5100 179\n10000 11000 268\n")

    def test_solve_cache_3 (self) :
        r = StringIO.StringIO("149805 468357\n111816 181804\n747961 968449\n312738 923696\n")
        w = StringIO.StringIO()
        collatz_solve_cache(r, w)
        self.assert_(w.getvalue() == "149805 468357 449\n111816 181804 383\n747961 968449 525\n312738 923696 525\n") 

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
