from user_interface.ExpenseTrackerApp import ExpenseTrackerApp
import tkinter as tk

def main():
    """
    Main function to run the expense tracker application.
    """
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
