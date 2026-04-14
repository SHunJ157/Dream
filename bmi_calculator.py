# --- BMI Calculator Professional Version ---
# Goals: Loop until quit, handle input errors, and clean output.

while True:
    print("\n" + "="*30)
    print("  BMI CALCULATOR SYSTEM  ")
    print("="*30)
    print("Type 'q' to quit at any time.")
    
    # 1. 取得身高輸入，並提供退出機制
    user_input = input("Enter height in cm (or 'q' to exit): ")
    if user_input.lower() == 'q':
        print("System shutdown. Goodbye!")
        break
        
    try:
        # 2. 轉換資料型態
        height_cm = float(user_input)
        weight = float(input("Enter weight in kg: "))

        # 3. 核心運算
        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)

        print("-" * 30)
        print(f"RESULT: Your BMI is {bmi}")

        # 4. 條件判斷邏輯
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 24:
            status = "Normal weight"
        elif 24 <= bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"
            
        print(f"STATUS: {status}")
        print("-" * 30)

    except ValueError:
        # 如果使用者輸入的不是數字，會執行這裡
        print("\n[Error] Invalid input! Please enter numbers only.")

