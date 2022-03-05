T = input()
S = input()
mini = 0
paste = 1
c_m = 1
if (1 <= len(T) <= 10**4) and 1 <= len(S) <= 16:
    for letter in list(T):
        backspace = 0
        if letter in S:
            position = S.find(letter)
            if ((len(S)-1)>position) and position > 0:
                backspace = (len(S)-1)-position
                mini += (paste + backspace)
                backspace = position
                mini += (paste + c_m + backspace + c_m)
            else:
                if position > 0:
                    backspace = position
                    mini += (paste + c_m + backspace + c_m)
                elif (len(S)-1)>position:
                    backspace = (len(S)-1)-position
                    mini += (paste + backspace) 
    print(mini)
                    