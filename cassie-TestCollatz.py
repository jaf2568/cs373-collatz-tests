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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length, collatz_lazy_cacher, lazy

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        # Test basic input
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        # Test a line with whitespace - used to cause a runtime error
        r = StringIO.StringIO(" \n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)

    def test_read_3 (self) :
        # Test EOF
        r = StringIO.StringIO("\n")
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
        # Test num which causes overflow
        v = collatz_eval(997823, 997823)
        self.assert_(v == 1)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        # Test working example
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        # Test incorrect example
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 200)
        self.assert_(w.getvalue() == "1 10 200\n")

    def test_print_3 (self) :
        # Test random input
        w = StringIO.StringIO()
        collatz_print(w, "how", "are", "you?")
        self.assert_(w.getvalue() == "how are you?\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        # Test given input
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        # Test whitespace input
        r = StringIO.StringIO("1 10\n \n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_solve_3 (self) :
        # Test inputs with overflows
        r = StringIO.StringIO("995001 996000\n996001 997000\n997001 998000\n998001 999000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "995001 996000 365\n996001 997000 365\n997001 998000 352\n998001 999000 396\n")

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1 (self) :
        # Test basic input
        self.assert_(collatz_cycle_length(9) == 20)

    def test_cycle_length_2 (self) :
        # Test basic input (again to test cache)
        self.assert_(collatz_cycle_length(28) == 19)

    def test_cycle_length_3 (self) :
        # Test overflow
        self.assert_(collatz_cycle_length(997823) == 1)

    # -----------
    # lazy_cacher
    # -----------
    def test_lazy_cacher_1 (self) :
        collatz_lazy_cacher([8, 4, 2], 4)
        self.assert_(lazy.get(8) == 3)
        self.assert_(lazy.get(4) == 2)
        self.assert_(lazy.get(2) == 1)

    def test_lazy_cacher_2 (self) :
        collatz_lazy_cacher([2, 4, 8], 4)
        self.assert_(lazy.get(2) == 3)
        self.assert_(lazy.get(4) == 2)
        self.assert_(lazy.get(8) == 1)

    def test_lazy_cacher_3 (self) :
        collatz_lazy_cacher([997823], 1)
        self.assert_(lazy.get(997823) == 0)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
