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

from Collatz import collatz_read, collatz_eval, collatz_loop, collatz_print, collatz_solve

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
		self.assert_(b	  == True)
		self.assert_(a[0] ==  1)
		self.assert_(a[1] == 10)

	def test_read_2 (self) :
		r = StringIO.StringIO("12 50\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b	  == True)
		self.assert_(a[0] == 12)
		self.assert_(a[1] == 50)

	def test_read_3 (self) :
		r = StringIO.StringIO("1 1000\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b	 == True)
		self.assert_(a[0] ==    1)
		self.assert_(a[1] == 1000)

	def test_read_4 (self) :
		r = StringIO.StringIO("55 55\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b	  == True)
		self.assert_(a[0] == 55)
		self.assert_(a[1] == 55)

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
		v = collatz_eval(1000, 1000)
		self.assert_(v == 112)
		
	def test_eval_6 (self) :
		v = collatz_eval(1000, 1001)
		self.assert_(v == 143)
		
	def test_eval_7 (self) :
		v = collatz_eval(210, 201)
		self.assert_(v == 89)
		
	# -----
	# loop
	# -----	
	def test_loop_1 (self) :
		v = collatz_loop(766311)
		self.assert_(v == 225)
		
	def test_loop_2 (self) :
		v = collatz_loop(766345)
		self.assert_(v == 194)
		
	def test_loop_3 (self) :
		v = collatz_loop(9414)
		self.assert_(v == 35)
		
	def test_loop_4 (self) :
		v = collatz_loop(9454)
		self.assert_(v == 61)

	# -----
	# print
	# -----

	def test_print_1 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 1, 10, 20)
		self.assert_(w.getvalue() == "1 10 20\n")
		
	def test_print_2 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 1, 1000, 179)
		self.assert_(w.getvalue() == "1 1000 179\n")
		
	def test_print_3 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 10, 1, 20)
		self.assert_(w.getvalue() == "10 1 20\n")
		
	def test_print_4 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 10, 10, 7)
		self.assert_(w.getvalue() == "10 10 7\n")

	# -----
	# solve
	# -----

	def test_solve_1 (self) :
		r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
		
	def test_solve_2 (self) :
		r = StringIO.StringIO("1 1000\n10 1\n10 10\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 1000 179\n10 1 20\n10 10 7\n")
		
	def test_solve_3 (self) :
		r = StringIO.StringIO("139163 552953\n776468 628994\n378628 766439\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "139163 552953 470\n776468 628994 504\n378628 766439 509\n")
		
	def test_solve_4 (self) :
		r = StringIO.StringIO("9043 9820\n3546 2708\n2234 2573\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "9043 9820 260\n3546 2708 217\n2234 2573 209\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."