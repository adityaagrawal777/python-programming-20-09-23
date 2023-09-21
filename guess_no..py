import random
computer_num = random.randrange(1,100)
score = 10
while True:
    user_num = int(input("guess the no. between 1 to 100"))
    if user_num == computer_num:
        print("you win with score",score)
    elif user_num<computer_num:
        print("too small")
    else:
        print("too large")
    score-=1