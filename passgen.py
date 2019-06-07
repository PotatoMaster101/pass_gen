#!/usr/bin/env python3
#==============================================================================
# passgen.py
# Script to generate passwords. Run with python 3. 
#
# Author: PotatoMaster101
# Date:   15/02/2019
#==============================================================================

import sys
import argparse
import secrets
import string

def get_args():
    """
    Returns the arguments provided by the user. 
    """
    p = argparse.ArgumentParser(description="Password generator.")
    p.add_argument("length", type=int, default=14, nargs="?", 
            help="length of the password")
    p.add_argument("-p", "--pool", type=str, default="", dest="pool", 
            help="pool of characters to use")
    p.add_argument("-pA", "--pool-alpha", action="store_true", dest="palph", 
            help="include all alphabetical characters in pool")
    p.add_argument("-pU", "--pool-upper", action="store_true", dest="pup", 
            help="include all upper case characters in pool")
    p.add_argument("-pL", "--pool-lower", action="store_true", dest="plow", 
            help="include all lower case characters in pool")
    p.add_argument("-pN", "--pool-num", action="store_true", dest="pnum", 
            help="include all numerical characters in pool")
    p.add_argument("-pP", "--pool-punc", action="store_true", dest="ppunc", 
            help="include all punctuation characters in pool")
    p.add_argument("-e", "--pool-except", type=str, default="", dest="ign", 
            help="list of characters to remove from the pool")
    p.add_argument("-b", "--brute-speed", type=int, default=1000000000, 
            dest="brute", help="brute force speed (tries per second)")
    p.add_argument("-v", "--verbose", action="store_true", dest="verb", 
            help="produce verbose output")
    return p


def get_pool(argp):
    """
    Returns the character pool specified by the user. 
    """
    pool = argp.pool
    if argp.palph:
        pool += string.ascii_letters
    if argp.pup:
        pool += string.ascii_uppercase
    if argp.plow:
        pool += string.ascii_lowercase
    if argp.pnum:
        pool += string.digits
    if argp.ppunc:
        pool += string.punctuation
    if not pool:
        pool += string.ascii_letters + string.digits + string.punctuation
    if argp.ign:
        pool = pool.translate(str.maketrans("", "", argp.ign))
    return "".join(set(pool))


def get_total_combo(pool, size):
    """
    Computes the total number of possible passwords using the character pool 
    and password length. 
    """
    return len(pool) ** argp.length


def get_bruteforce_time(combo, speed=1000000000):
    """
    Returns the average day it takes to bruteforce the specified number of 
    combinations. 
    """
    return (combo // speed) // (24 * 3600)


if __name__ == "__main__":
    """
    Entry point. 
    """
    argp = get_args().parse_args()
    pool = get_pool(argp)
    if argp.length <= 0:
        print("[-] Length is 0 or negative.", file=sys.stderr)
        exit(1)
    if argp.brute <= 0:
        print("[-] Password bruteforce time is 0 or negative", file=sys.stderr)
        exit(1)

    if argp.verb:
        combo = get_total_combo(pool, argp.length)
        time = get_bruteforce_time(combo, argp.brute)
        print("[+] Password length:         %s" %argp.length)
        print("[+] Character pool size:     %s" %len(pool))
        print("[+] Character pool:          %s" %pool)
        print("[+] Total posibilities:      %s" %combo)
        print("[+] Bruteforce speed (p/s):  %s" %argp.brute)
        print("[+] Average bruteforce time: %s days" %time)
        print("[+] Password:")
    print("".join(secrets.choice(pool) for _ in range(argp.length)))
    exit(0)

