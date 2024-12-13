class Menu:
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
        print("|   4. Load from File. |")
        print("|   5. Save to File.   |")
        print("|   6. Exit            |")
        print("-" * 24)

    @staticmethod
    def get_choice() -> str:
        """
            Prompts the user for a menu choice

            returns:
                str : choice from the menu options.

            """
        while True:
            choice = input("Choose an option:")
            if choice in {"1", "2", "3", "4", "5", "6"}:
                return choice
            print("-" * 24)
            print("Invalid choice. Try again")
            print("-" * 24)
