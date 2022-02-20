import os
import random

PATH = os.path.dirname(__file__)

def gen_band_name():
    words = open(PATH + "/names/bands/wordlist.10000").read().splitlines()
    name = "%s %s"%(random.choice(words), random.choice(words))
    
    return name

def gen_member_name():
    first = random.choice( open(PATH + "/names/members/first.txt").read().splitlines())
    last = random.choice( open(PATH + "/names/members/last.txt").read().splitlines())
    
    return first, last

def gen_release_name():
    name = random.choice(open(PATH + "/names/bands/wordlist.10000").read().splitlines())
    
    return name