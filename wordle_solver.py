from audioop import error
import json
import os
from os.path import exists


class WordleSolver:

    WORD_SIZE = 5
    GENERIC_ERROR = "Expected puzzle encoding: {} tokens, separated by commas, e.g. WG,?,?,?,SY using 'G' for greens and 'Y' for yellows and ?'s for unknowns".format(WORD_SIZE)

    def __init__(self):
        self._positional_list = []
        self._containment_map = {}

        for i in range(WordleSolver.WORD_SIZE):
            self._positional_list.append({})

        self._slurp_csw()

        
    def _slurp_csw(self):
        """
        Crude to just assume file, but honestly this dictionary isn't all that big, so no real point in optimizing/trimming it
        Assumes a file in CWD called csw.txt
        """
        file = os.getcwd() + "/csw.txt"
        if exists(file):
            lines = open(file, 'r').readlines()
            for line in lines:
                word = line.strip()
                if len(word) == WordleSolver.WORD_SIZE:

                    # Setup positional list used for "green" positional matching
                    i = 0
                    for c in word:
                        if c not in self._positional_list[i]:
                            self._positional_list[i][c] = set()
                        self._positional_list[i][c].add(word)
                        i = i + 1

                    # Setup containment used for "yellow" partial matches
                    for c in word:
                        if c not in self._containment_map:
                            self._containment_map[c] = set()
                        self._containment_map[c].add(word)
        else:
            raise error("CSW does not exist at " + file)


    def solve(self, encoding:str, exclusion:str):
        """
        Solve based on the following encoding:
        encoding:
            Provide a comma-sep-string of size WORD_SIZE (e.g. 5). Each token should be 1-2 chars in length. Valid tokens:
            1) ?   -> An unknown position
            2) JG  -> J was guessed and it's in the right position (green)
            3) JY  -> J was guessed and it's in the word, but wrong position (yellow)

        exclusion:
            Provide a comma-sep-sring of letters used that were marked as NOT in the word
        """
        tokens = encoding.split(",")
        if len(tokens) != WordleSolver.WORD_SIZE:
            raise error(WordleSolver.GENERIC_ERROR)

        non_letters = exclusion.split(",")


        possible_words = None
        i = 0
        for token in tokens:
            if len(token) > 2:
                raise error(WordleSolver.GENERIC_ERROR)

            is_positional = False
            is_contained = False
            if len(token) == 2:
                if token[1] == 'G':
                    is_positional = True
                elif token[1] == 'Y':
                    is_contained = True
                else:
                    raise error(WordleSolver.GENERIC_ERROR)
            
            char = token[0]

            if is_positional:
                words = self._positional_list[i][char]
                if possible_words is None:
                    possible_words = words
                else:
                    possible_words = possible_words.intersection(words)

            if is_contained:
                words = self._containment_map[char]
                if possible_words is None:
                    possible_words = words
                else:
                    possible_words = possible_words.intersection(words)
            i = i + 1

        trimmed = set()
        for word in possible_words:
            for letter in non_letters:
                if letter not in word:
                    trimmed.add(word)

        for word in trimmed:
            print(word)