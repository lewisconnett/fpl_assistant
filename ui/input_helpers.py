def get_user_choice() -> str:
    while True:
        choice = input('Choose an option (1-5): ').strip()
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        
        print('\nInvalid choice. Please enter 1-5')
    