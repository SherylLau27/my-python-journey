import random
number = random.randint(1,100)
guess=None
attempts=0
max_attempts =10
print("猜数字游戏开始。你有10次机会。")
while  guess != number:
    guess =int(input ("请输入你猜的数字1-100"))
    attempts += 1
    if guess >  number:
        print("你猜的数字太大了！")     
    elif guess < number:
        print("你猜的数字太小了！") 
else:
    print("恭喜你，猜对了！你用了", attempts,"次机会。")
