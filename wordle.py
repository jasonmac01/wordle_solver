import sys
from tkinter import N
from wordle_solver import *

solver = WordleSolver()

if len(sys.argv) < 3:
    msg = "\
        First argument:\n\
           A comma-sep-string of size WORD_SIZE (e.g. 5). Each token should be 1-2 chars in length. Valid tokens:\n\
              1) ?   -> An unknown position\n\
              2) JG  -> J was guessed and it's in the right position (green)\n\
              3) JY  -> J was guessed and it's in the word, but wrong position (yellow)\n\
        Second argument:\n\
          A comma-sep-sring of letters used that were marked as NOT in the word\n\
          \n\
        This script assumes \"csw.txt\" is in your CWD which you can download from here (for example): \n\
        https://drive.google.com/open?id=1oGDf1wjWp5RF_X9C7HoedhIWMh5uJs8s"
    print(msg)
    sys.exit(1)

solver.solve(sys.argv[1], sys.argv[2])