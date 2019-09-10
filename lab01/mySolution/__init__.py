import random
from collections import OrderedDict
import matplotlib.pyplot as plt

def generate(str_len,dictionary_of_matches=0):
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

def calculate_score(goal,test):
    num_of_correct_characters = 0
    correct_places= OrderedDict()
    for i in range(len(test)):
        if goal[i] == test[i]:
            num_of_correct_characters+=1
            correct_places[i]=test[i]
    return correct_places

def monkeyTypist():
    target = list('methinks it is like a weasel')
    alphabet = list(' abcdefghijklmnopqrstuvwxyz')
    best_string = generate(28)
    best_score = float(len(calculate_score(target,best_string))/len(best_string))*100
    attempt_counter = 0
    indexes=[0]
    scores=[best_score]
    print('String\t\t\t\t\t\tScore')
    while best_score<100:
        if best_score==100:
            break
        next_str = change_one(best_string,target)
        next_score = float(len(calculate_score(target,next_str))/len(best_string))*100
        if next_score>best_score:
            best_score=next_score
            best_string=next_str
            indexes.append(attempt_counter)
            scores.append(best_score)
        if attempt_counter==100000:
            break
        if attempt_counter%100==0:
            print("%s  \t\t\t %d" %   ("".join(best_string),best_score))
        attempt_counter+=1
    ax1=plt.plot(indexes,scores,'r+')
    plt.xlabel('Iteration')
    plt.ylabel('Score of Best String')
    plt.ylim(0,100)
    plt.xscale
    plt.show()

monkeyTypist()