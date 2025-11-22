import random
def simple_hangman():
    words = ["apple", "banana", "orange", "grape", "melon"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 5
    
    print("简单版 Hangman 游戏")
    print(f"单词: {' '.join(guessed)}")
    
    while attempts > 0 and "_" in guessed:
        letter = input("猜一个字母: ").lower()
        
        if letter in word:
            for i, char in enumerate(word):
                if char == letter:
                    guessed[i] = letter
            print(f"✅ 正确! {' '.join(guessed)}")
        else:
            attempts -= 1
            print(f"❌ 错误! 剩余尝试: {attempts}")
    
    if "_" not in guessed:
        print(f"🎉 你赢了! 单词是: {word}")
    else:
        print(f"💔 你输了! 单词是: {word}")

# 运行简单版本
simple_hangman()