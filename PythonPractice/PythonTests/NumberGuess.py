max_retry = 10
current_try = 0
correct_guess = False

while current_try < max_retry:

    user_input_number = int(input("Please enter a number : "))

    if user_input_number != 19:
        print(f"Not correct in attempt {current_try}")
    else:
        print("Correct Guess")
        correct_guess = True
        break

    current_try += 1
else:
    print("Max limit reached")

