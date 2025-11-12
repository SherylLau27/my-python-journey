import random

def upgraded_number_guessing_game():
    print("猜数字游戏升级版")
    level = input("请选择难度级别（1-简单、2-中等、3-困难）：")
    if level == '1':
        max_num = 50
        max_attempts = 10
    elif level == '2':
        max_num = 100
        max_attempts = 7
    elif level == '3':
        max_num = 200
        max_attempts = 5
    else:
        print("无效选择，默认选择简单难度。")
        max_num = 50
        max_attempts = 10

    number = random.randint(1, max_num)
    attempts = 0
    print(f"游戏开始！我已经选择了一个1到{max_num}之间的数字。你有{max_attempts}次机会猜测它。")
    while attempts < max_attempts:
        try:
            guess = int(input("请输入你猜的数字: "))
        except ValueError:
            print("⚠️ 请输入有效的数字!")
            continue

        attempts += 1

        # 判断结果
        if guess == number:
            print(f"🎉 恭喜! 你在第{attempts}次猜对了!")
            break
        elif guess > number:
            print("太大了!", end=" ")
        else:
            print("太小了!", end=" ")

        # 显示剩余次数
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"还剩{remaining}次机会。")

        # 接近提示
        if abs(guess - number) <= 5:
            print("💡 提示: 很接近了!")

    # 游戏结束处理
    if attempts >= max_attempts and (guess != number):
        print(f"💔 游戏结束! 正确答案是{number}。")

if __name__ == "__main__":
    upgraded_number_guessing_game()

