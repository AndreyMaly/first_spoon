import numpy as np


def game_core_v3(number: int=1) -> int:
    '''
    Guess random number from 1 to 100. 
    Getting the number with 7 trials maximum.

    
    Args:
        number (int, optional): A number to guess. Default to 1.
        
    Returns:
        int: The number of trials.
    '''

    count = 0
    predict_number = 50 # a number to try

    while True:
        count += 1

        if  number == predict_number:
            break
        else:
            corrector = 50 // 2**count + 1 # step for next number to try 

            if number > predict_number:
                predict_number += corrector
            else:
                predict_number -= corrector

    return count

sum = 0
trials_list = []
for i in range(1,101):
    sum += game_core_v3(i)
    trials_list.append(game_core_v3(i))



print (sum)
print((trials_list))


    

#print(f'Количество попыток: {game_core_v3(17)}')