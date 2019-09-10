import random

def generate(str_len,array_of_match_indexes=0):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    res =''
    for i in range(str_len):
        res = res + alphabet[random.randrange(27)]
    return res

#print(generate(15))

def calculate_score(goal,test):
    num_of_correct_characters = 0
    correct_places=[]
    for i in range(len(test)):
        if goal[i] == test[i]:
            num_of_correct_characters+=1
            correct_places.append(i)
    return correct_places

#print(calculate_score('me thinks it looks like a weasel','i am an idiot and dont know it'))

def monkeyTypist():
    target = list('methinks it is like a weasel')
    alphabet = list(' abcdefghijklmnopqrstuvwxyz')
    best_string = generate(28)
    best_score = len(calculate_score(target,best_string))/len(best_string)
    attempt_counter = 0
    print('String\t\t\t\t\t\tScore')
    while best_score<100:
        if best_score==100:
            break
        next_str = generate(28,calculate_score(target,best_string))
        next_score = calculate_score(target,next_str)
        if next_score>best_score:
            best_score=next_score
            best_string=next_str
        if attempt_counter==100:
            print("%s   %d" %   ("".join(best_string),best_score))
            break
        attempt_counter+=1

monkeyTypist()