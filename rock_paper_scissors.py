import random

def play_game():
    options = ["rock", "paper", "scissors"] # 列表：存放選項
    
    print("\n" + "="*30)
    print("Welcome to Rock, Paper, Scissors!")
    print("="*30)

    while True:
        # 1. 取得玩家輸入
        user_choice = input("\nEnter Rock, Paper, or Scissors (or 'q' to quit): ").lower()
        
        if user_choice == 'q':
            print("Thanks for playing! Bye!")
            break
            
        if user_choice not in options:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue

        # 2. 電腦隨機選一個
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # 3. 判斷勝負
        if user_choice == computer_choice:
            print("It's a TIE!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("YOU WIN! 🎉")
        else:
            print("YOU LOSE! 💀")

# 執行遊戲
play_game()
