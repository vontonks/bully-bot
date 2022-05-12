import random
import word_list

name = 'me'

def gen_insult():
    roll = random.randrange(1,7)
    print(roll)
    if roll == 1:
        return('is ' + word_list.random_noun + '.')

    if roll == 2:
        return('has ' + word_list.random_feature + '.')
    
    if roll == 3:
        return('is ' + word_list.random_noun + ' and has ' + random.choice(word_list.feature) + '.')
    
    if roll == 4:
        return('has ' + word_list.random_feature + ' and is ' + random.choice(word_list.noun) + '.')
    
    if roll == 5:
        return('is ' + word_list.random_noun + ' and ' + random.choice(word_list.noun) + '.')
    
    if roll == 6:
        return('has ' + word_list.random_feature + ' and ' + random.choice(word_list.feature))