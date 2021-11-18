import keyboard
import random as rand
import time
import mouse

numlist = ['0','1','2','3','4','5','6','7','8','9']
run = 0
#Put loop here for to run code 10 times
loop = int(input('How many times do you want to loop? '))
loop += 1
print(loop)
while(run<loop):
    time.sleep(2)
    input1 = rand.choice(numlist)
    input2 = rand.choice(numlist)
    input3 = rand.choice(numlist)
    input4 = rand.choice(numlist)
    input5 = rand.choice(numlist)
    input6 = rand.choice(numlist)
    input7 = rand.choice(numlist)
    print(input1)
    print(input2)
    print(input3)
    print(input4)
    print(input5)
    print(input6)
    print(input7)
    keyboard.press_and_release(input1)
    keyboard.press_and_release(input2)
    keyboard.press_and_release(input3)
    keyboard.press_and_release(input4)
    keyboard.press_and_release(input5)
    keyboard.press_and_release(input6)
    keyboard.press_and_release(input7)
    keyboard.press_and_release('enter')

    time.sleep(1.5)
    #keyboard.press_and_release('control')
    #keyboard.press_and_release('t')
    mouse.click('left')
    run +=1
