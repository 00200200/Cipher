class MainMenu:
    NUMBER_OF_OPTIONS = 7
    """
    Represents the menu interface for User interaction
    """
    @staticmethod
    def show_menu():
        """
        Displays the main menu for Cipher Application.
        """
        print("-" * 24)
        print("|", f"CIPHER MENU".center(20), "|")
        print("-" * 24)
        print("|   1. Encrypt Text.   |")
        print("|   2. Decrypt Text.   |")
        print("|   3. Show buffer     |")
        print("|   4. Clear buffer     |")
        print("|   5. Load from File. |")
        print("|   6. Save to File.   |")
        print("|   7. Exit            |")
        print("-" * 24)

    @staticmethod
    def get_choice() -> int:
        """
        Prompts the user for a menu choice
        returns:
            str : choice from the menu options.
        """
        while True:
            try:
                choice = int(input("Choose an option:"))
                if choice in range(1, MainMenu.NUMBER_OF_OPTIONS + 1):
                    return choice
                print("-" * 24)
                print(f"Invalid choice. Choice should be between 1 and {MainMenu.NUMBER_OF_OPTIONS}. ")
                print("-" * 24)
            except ValueError:
                print("-" * 24)
                print("Invalid choice. Option should be an Integer.")
                print("-" * 24)
                print("Try again...")
                print("-" * 24)
