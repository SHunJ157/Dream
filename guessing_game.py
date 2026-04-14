import random  # 匯入隨機套件

def start_game():
    # 1. 電腦隨機選一個 1 到 100 之間的數字
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("\n" + "★" * 30)
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("★" * 30)

    while True:
        try:
            # 2. 取得玩家輸入
            guess = input("\nTake a guess (or 'q' to quit): ")
            
            if guess.lower() == 'q':
                print(f"Game Over. The number was {secret_number}. Bye!")
                break
            
            guess = int(guess)
            attempts += 1  # 猜一次，次數就加 1

            # 3. 判斷邏輯
            if guess < secret_number:
                print("Too LOW! Try again.")
            elif guess > secret_number:
                print("Too HIGH! Try again.")
            else:
                print(f"★ CONGRATS! You found it in {attempts} attempts!")
                break  # 猜中了，跳出迴圈
                
        except ValueError:
            print("Invalid input! Please enter a whole number.")

# 執行遊戲
start_game()
