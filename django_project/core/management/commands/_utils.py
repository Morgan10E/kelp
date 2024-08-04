def get_user_agrees(default: str = "n") -> bool:
    for i in range(5):
        user_input = input().strip().lower()
        if user_input == "":
            user_input = default
        if user_input == "n" or user_input == "y":
            return user_input == "y"
        print("Please enter 'y' or 'n' (without the quotes)")
    print(f"You goofed the entry so many times we're just going to use the default ({default})")
    return default == "y"
