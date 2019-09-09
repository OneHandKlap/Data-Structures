import random

def generate(str_len):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res =''
    for i in range(str_len):
        res = res + alphabet[random.randrange(27)]
    return res

print(generate(15))

def calculate_score(goal,test):
    num_of_correct_characters = 0
    for i in range(len(test)):
        if goal[i] == test[i]:
            num_of_correct_characters+=1
    result = num_of_correct_characters/len(test)
    return result

print(calculate_score('me thinks it looks like a weasel','i am an idiot and dont know it'))