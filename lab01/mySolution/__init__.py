import random
from collections import OrderedDict
import matplotlib.pyplot as plt




def generate(str_len,dictionary_of_matches=0,change_one=0,string=0):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    res =''
    if dictionary_of_matches:
        for i in range(str_len):
            try:
                res=res+dictionary_of_matches[i]
            except:
                ValueError
                res=res+ alphabet[random.randrange(27)]
    else:
        for i in range(str_len):
           res=res+ alphabet[random.randrange(27)]
    return res

def change_one(string,target):
    res=''
    alphabet= ' abcdefghijklmnopqrstuvwxyz'
    changed_one=False
    for i in range(len(string)):
        if string[i]==target[i] or changed_one==True:
            res=res+string[i]
        else:
            res=res+alphabet[random.randrange(27)]
            changed_one=True
    return res


#print(generate(15))

def calculate_score(goal,test):
    num_of_correct_characters = 0
    correct_places= OrderedDict()
    for i in range(len(test)):
        if goal[i] == test[i]:
            num_of_correct_characters+=1
            correct_places[i]=test[i]
    return correct_places

#print(calculate_score('me thinks it looks like a weasel','i am an idiot and dont know it'))

def monkeyTypist():
    target = list('methinks it is like a weasel')
    alphabet = list(' abcdefghijklmnopqrstuvwxyz')
    best_string = generate(28)
    best_score = float(len(calculate_score(target,best_string))/len(best_string))*100
    attempt_counter = 0
    print('String\t\t\t\t\t\tScore')
    while best_score<100:
        if best_score==100:
            break
        next_str = change_one(best_string,target)
        next_score = float(len(calculate_score(target,next_str))/len(best_string))*100
        if next_score>best_score:
            best_score=next_score
            best_string=next_str
        if attempt_counter==100000:
            break
        if attempt_counter%100==0:
            print("%s  \t\t\t %d" %   ("".join(best_string),best_score))
        attempt_counter+=1

#print(calculate_score('test','tee'))
monkeyTypist()

#print(change_one('test','teeee'))