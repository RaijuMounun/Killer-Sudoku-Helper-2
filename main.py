""" Main file to run the Killer Sudoku helper. """
import customtkinter as ctk
from ui import KillerSudokuUI

if __name__ == "__main__":
    root = ctk.CTk()
    app = KillerSudokuUI(root)
    root.mainloop()
