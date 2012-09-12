#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2012
# Glenn P. Downing
# Edited by Lauren Yew
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_odd_eval, eval_num, cache_eval

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

    	def test_read_start0 (self) :
		r = StringIO.StringIO("05 02\n")
		a = [0, 0]
		b = collatz_read(r,a)
		self.assert_(b    == True)
		self.assert_(a[0] == 5)
		self.assert_(a[1] == 2)
	
    	def test_read_empty (self) :
		r = StringIO.StringIO("")
		a = [0,0]
		b = collatz_read(r, a)
		self.assert_(b    == False)

    	def test_read_backwards (self) :
		r = StringIO.StringIO("10 1\n")
		a = [0,0]
		b = collatz_read(r,a)
		self.assert_(b    == True)
		self.assert_(a[0] == 10)
		self.assert_(a[1] == 1)



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
		v = collatz_eval(2, 2)
		self.assert_(v == 2)

    	def test_eval_backwards (self) :
		v = collatz_eval(10, 1)
		self.assert_(v == 20)
    
    	def test_eval_small (self) :
		v = collatz_eval(1, 2)
		self.assert_(v == 2)




    	# -----
    	# print
    	# -----

    	def test_print (self) :
        	w = StringIO.StringIO()
        	collatz_print(w, 1, 10, 20)
        	self.assert_(w.getvalue() == "1 10 20\n")

    	def test_print_1 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 10, 20, 30)
		self.assert_(w.getvalue() == "10 20 30\n")

    	def test_print_2 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 1, 2, 3)
		self.assert_(w.getvalue() == "1 2 3\n")

    	def test_print_3 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 3, 2, 1)
		self.assert_(w.getvalue() == "3 2 1\n")


    	# -----
    	# solve
    	# -----

    	def test_solve (self) :
        	r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        	w = StringIO.StringIO()
        	collatz_solve(r, w)
        	self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    	def test_solve_backwards (self) :
		r = StringIO.StringIO("10 1\n200 100\n210 201\n900 1000\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n900 1000 174\n")

    	def test_solve_same (self) :
		r = StringIO.StringIO("2 2\n1 1\n")
		w = StringIO.StringIO()
		collatz_solve(r,w)
		self.assert_(w.getvalue() == "2 2 2\n1 1 1\n")

    	def test_solve_small (self) :
		r = StringIO.StringIO("2 1\n")
		w = StringIO.StringIO()
		collatz_solve(r,w)
		self.assert_(w.getvalue() == "2 1 2\n")





    	# ----
    	# collatz_odd_eval
    	# ---- 

    	def test_collatz_odd_eval_basic (self) :
		v = 1
		v2 = collatz_odd_eval(v)
		w = StringIO.StringIO(str(v) + " " + str(v2) + "\n")
		self.assert_(w.getvalue() == "1 2\n")

    	def test_collatz_odd_eval_2 (self) :
		v = 3
		v2 = collatz_odd_eval(v)
		w = StringIO.StringIO(str(v) + " " + str(v2) + "\n")
		self.assert_(w.getvalue() == "3 5\n")

    	def test_collatz_odd_eval_3 (self) :
		v = 5
		v2 = collatz_odd_eval(v)
		w = StringIO.StringIO(str(v) + " " + str(v2) + "\n")
		self.assert_(w.getvalue() == "5 8\n")



    	# ---
    	# eval_num
    	# ---


    	def test_eval_num_odd (self) :
		v = 3
		val = eval_num(v)
		self.assert_(val == [5,2])

    	def test_eval_num_even (self) :
		v = 2
		val = eval_num(v)
		self.assert_(val == [1,1])

    	def test_eval_num_one (self) :
		v = 1
		val = eval_num(v)
		self.assert_(val == [2,2])



    	# ---
    	# cache_eval
    	# ---


    	def test_cache_eval_odd (self) :
		temp = 3
		val = cache_eval(temp,0)
		self.assert_(val == 8)

    	def test_cache_eval_even (self) :
		temp = 2
		val = cache_eval(temp,0)
		self.assert_(val == 2)

    	def test_cache_eval_one (self) :
		temp = 1
		val = cache_eval(temp,0)
		self.assert_(val == 1)


	
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."

