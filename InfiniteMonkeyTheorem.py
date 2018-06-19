# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 08:09:29 2018

@author: Neetu
Infinte Monkey Theorem: The theorem states that a monkey hitting keys at 
random on a typewriter keyboard for an infinite amount of time will almost 
surely type a given text, such as the complete works of William Shakespeare.

The sentence we’ll shoot for is: “methinks it is like a weasel”

"""

import string
import random
from difflib import SequenceMatcher
import profile

#global character set
#string.ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
char_set = string.ascii_lowercase + " " 

def str_generator(target,teststr):
    result_list = list(teststr)
    for index in range(len(result_list)):
        if result_list[index] != target[index]:
            result_list[index] = char_set[random.randrange(27)]
    return ''.join(result_list)
    

def cal_score(target,teststr):
    score = (SequenceMatcher(None,teststr,target).ratio())*100
    return score

def main():
    target = "methinks it is like a weasel"
    initial_str = " "*len(target)
    teststr = str_generator(target,initial_str)
    score = cal_score(target,teststr)
    
    tries = 0
    while score < 100.00:
        teststr = str_generator(target,teststr)
        score = cal_score(target,teststr)
        tries += 1
    print("{0} score matched: {1} after trying for {2} number of times".format(score,teststr,tries))
    

profile.run('main()')
