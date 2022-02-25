# Usage
```
> wordle_solver (main) $ python3 wordle.py
        First argument:
           A comma-sep-string of size WORD_SIZE (e.g. 5). Each token should be 1-2 chars in length. Valid tokens:
              1) ?   -> An unknown position
              2) JG  -> J was guessed and it's in the right position (green)
              3) JY  -> J was guessed and it's in the word, but wrong position (yellow)
        Second argument:
          A comma-sep-sring of letters used that were marked as NOT in the word
          
        This script assumes "csw.txt" is in your CWD which you can download from here (for example): 
        https://drive.google.com/open?id=1oGDf1wjWp5RF_X9C7HoedhIWMh5uJs8s
```

## Example, you've found V in two positional locations and {A, Y, T} are not in the word:
```
> $ python3 wordle.py VG,?,VG,?,? A,Y,T
VIVID
VIVES
VIVAT
VIVAS
VIVDA
VIVER
```

## Example, you've locked in V, but U and A are in incorrect positions and {Y, M, N} are not in the word:
```
> python3 wordle.py VG,?,?,UY,AY  Y,M,N
VAUCH
VAULT
VAUNT
VAUTE
VAUTS
```