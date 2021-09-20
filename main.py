last_1 = 0
last_2 = 0
current = 0
import numpy as np

inputs = np.zeros(shape=(2, 2, 2), dtype=int)



def prediction():
    if inputs[last_2][last_1][1] == 1:
        predict = inputs[last_2][last_1][0]
    else:
        predict = random.randint(0, 1)
    return predict


scores = [0, 0]


def update_scores(predicted, player_input):
    if predicted == player_input:
        scores[1] += scores[1]
        print("The player score is ", scores[0])
        print("The computer score is ", scores[1])
    else:
        scores[0] += 1
        print("The player score is ", scores[0])
        print("The computer score is ", scores[1])


def reset():
    for x in range(len(scores)):
        scores[x] = 0
    for i in range(2):

        for j in range(2):
            for k in range(2):
                inputs[i][j][k] = 0


import random

inputs = np.zeros((2, 2, 2), dtype=int)
last_1 = 0
last_2 = 0
scores = [0, 0]


def update_inputs(current):
    global last_2, last_1
    if inputs[last_2][last_1][0] == current:
        inputs[last_2][last_1][1] = 1
        inputs[last_2][last_1][0] = current
    else:
        inputs[last_2][last_1][1] = 0
        inputs[last_2][last_1][0] = current

    last_2 = last_1
    last_1 = current


def prediction():
    if inputs[last_2][last_1][1] == 1:
        predict = inputs[last_2][last_1][0]
    else:
        predict = random.randint(0, 1)
    return predict


def update_scores(predicted, player_input):
    if predicted == player_input:
        scores[1] += 1
        print("The player score is ", scores[0])
        print("The computer score is ", scores[1])
    else:
        scores[0] += 1
        print("The player score is ", scores[0])
        print("The computer score is ", scores[1])


def reset():
    for x in range(len(scores)):
        scores[x] = 0
    for i in range(2):

        for j in range(2):
            for k in range(2):
                inputs[i][j][k] = 0


def gameplay():
    reset()
    print('Sup? If you wish to defeat me then you must train for another 200 years. I will ask you to enter a number between 0 or 1 and I will try to guess what your nexy input maybe. First to 20 points wins')
    #print(inputs)
    #print(scores)
    valid_entries = ['0', '1']
    while True:
        predicted = prediction()
        player_input = input("Enter either 0 or 1 ")
        while player_input not in valid_entries:
            print("invalid input. Please try again ")
            player_input = input("Enter either 0 or 1 ")
        player_input = int(player_input)
        update_inputs(player_input)
        update_scores(predicted, player_input)
        if scores[1] == 20:
            print("You lost loser! HAHA ")
            break
        elif scores[0] == 20:
            print("How did you beat me? you must be really smart!")
            break


gameplay()