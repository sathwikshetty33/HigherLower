import random
from data import data
from art import  *
print(logo)
def form(acc):
    name=acc['name']
    country=acc['country']
    des=acc['description']
    return f"{name} is a {des} from {country}"
score=int(0)
acc_a=random.choice(data)
acc_b=random.choice(data)
while acc_a==acc_b:
    acc_b = random.choice(data)
while True:

    print("Who has more followers:")
    print(f"A:{form(acc_a)}")
    print(vs)
    print(f"B:{form(acc_b)}")
    ans=input("Choose A or B:  ").lower()
    while ans != 'a' or ans != 'b':
        ans=input("Choose a proper option: ")
    def check(ans, acc_a ,acc_b):
        if ans == 'a':
            if acc_a['follower_count']>acc_b['follower_count']:
                return True
            else:
                return False
        if ans == 'b':
            if acc_a['follower_count']<acc_b['follower_count']:
                return True
            else:
                return False

    c=check(ans,acc_a,acc_b)
    if c:
        score+=1
        print(f"You are correct. Your score is {score}")
        if acc_a['follower_count'] < acc_b['follower_count']:
            acc_a=acc_b
        acc_b = random.choice(data)
        while acc_a == acc_b:
            acc_b = random.choice(data)
    else:
        print(f"You lose. Your Score is {score}")
        break