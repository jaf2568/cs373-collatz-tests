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

    current_cycle_length = collatz_find_cycle_length(i)
    v = current_cycle_length
    for num in xrange(i + 1, j + 1) :
        current_cycle_length = collatz_find_cycle_length(num)
        if (current_cycle_length > v) :
            v = current_cycle_length
    assert v > 0
    return v

# -------------------------
# collatz_find_cycle_length
# -------------------------

def collatz_find_cycle_length (num) :
    """
    num is the integer input whose cycle length is to be calculated
    return the cycle length of num as an integer
    """
    assert num > 0
    result = 1
    while (num != 1) :
        result += 1
        if (num % 2 == 0) :
            num /= 2
        else :
            num = 3 * num + 1
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
