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
        print("|   4. Show buffer     |")
        print("|   5. Load from File. |")
        print("|   6. Save to File.   |")
        print("|   7. Exit            |")
        print("-" * 24)


