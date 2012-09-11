#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    cycle_length_cache = {1: 1}   # dictionary containing mapping from an integer to its cycle length
    current_cycle_length = 0
    v = 0
    for num in xrange(i, j + 1) :
        current_cycle_length = collatz_find_cycle_length(num, cycle_length_cache)
        if (current_cycle_length > v) :
            v = current_cycle_length
    assert v > 0
    return v

# -------------------------
# collatz_find_cycle_length
# -------------------------

def collatz_find_cycle_length (num, cycle_length_cache) :
    """
    num is the integer input whose cycle length is to be calculated
    return the cycle length of num as an integer
    """
    assert num > 0 and num < 1000000
    assert cycle_length_cache != None
    result = 0
    if (num in cycle_length_cache) :
        result = cycle_length_cache[num]
    else :
        if (num % 2 == 0) :
            result = collatz_find_cycle_length(num / 2, cycle_length_cache) + 1
        else :
            result = collatz_find_cycle_length(3 * num + 1, cycle_length_cache) + 1
        cycle_length_cache[num] = result
    return result

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
