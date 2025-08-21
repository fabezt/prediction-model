#This is a simple python script that shows how a chain of events can influence Predictions
import time
from pathlib import Path

def main():
    print(f"We will start a chain with a letter x.") 
    time.sleep(2)
    print("Now we want to guess what you will add to the chain.")
    time.sleep(2)
    print("Acording to the Markov chain, only present states matter, not the future.")
    time.sleep(2)
    print("So we know that your last addition to the chain was x.")
    time.sleep(2)
    print("This will influence the next state of the chain.")
    time.sleep(2)
    print("Now the odds of us gueesing the right letter is P=1/26 = 0.03846153846 (assuming 26 letters in the alphabet).")
    
    p1= 0.03846153846 
    time.sleep(2)
    print("Now we will add events to the chain that will influence the next state.")
    time.sleep(3)
    z= input("Let me ask you a question. Do you prefer A: Harry Potter or B: Lord of the Rings? or C: Hunger Games?")
    print(z)
    if z == "A":
        try:
            txt = Path("harrypotter.txt").read_text(encoding="utf-8")
            total_chars = len(txt)
            vowels ="aeiou"
            consonants = "bcdfghjklmnpqrstvwxyz"
            all = "abcdefghijklmnopqrstuvwxyz"
            a ="a"
            b ="b"
            c ="c"
            d ="d"
            e ="e"
            f ="f"
            g ="g"
            h ="h"
            inew ="i"
            j ="j"
            k ="k"
            l ="l"
            m ="m"
            n ="n"
            o ="o"
            p ="p"
            q ="q"
            r ="r"
            s ="s"
            t ="t"
            u ="u"
            v ="v"
            w ="w"
            x ="x"
            y ="y"
            z ="z"
            print("So i took the last 200 lines of Harry Potter and calculated the probability of the next letter being a x.")
            time.sleep(2)
            print(f"The text has {total_chars} characters")
            time.sleep(2)
            print("Now we want to know what character is most likly to come after an other.")
            time.sleep(2)
            print("First we will count how often each letter appears. In our case x appears 15 times")
            time.sleep(2)
            print("Now we will check what the next letter is after an x.")
            p2 = 5/15
            print(f"The letter t appears {p2*100}% of the time after an x.")
            time.sleep(2)
            print("So if you add an x to the chain, the next letter will most likely be a t. If you want to build an english word.")
            time.sleep(2)
            print("Let's now say that x stands for a universale undefined variable.")
            time.sleep(2)
            print("We would need a matrix of all letters and their probabilities to come after each other.")
            total_chars = len(txt)
            Pa = txt.count("a") 
            Pb = txt.count("b") 
            Pc = txt.count("c") 
            Pd = txt.count("d") 
            Pe = txt.count("e") 
            Pf = txt.count("f") 
            Pg = txt.count("g") 
            Ph = txt.count("h") 
            Pi = txt.count("i") 
            Pj = txt.count("j") 
            Pk = txt.count("k") 
            Pl = txt.count("l") 
            Pm = txt.count("m") 
            Pn = txt.count("n") 
            Po = txt.count("o") 
            Pp = txt.count("p") 
            Pq = txt.count("q") 
            Pr = txt.count("r") 
            Ps = txt.count("s") 
            Pt = txt.count("t") 
            Pu = txt.count("u") 
            Pv = txt.count("v") 
            Pw = txt.count("w") 
            Px = txt.count("x") 
            Py = txt.count("y") 
            Pz = txt.count("z") 
            time.sleep(2)
            print("We will use the text as a fixed point to calculate the probabilities of the next letter.")
            time.sleep(1)

            vowels_count = sum(txt.count(v) for v in vowels)
            consonants_count = sum(txt.count(c) for c in consonants)
            VV = VC = CV = CC = 0
            for i in range(len(txt) - 1):
                first, second = txt[i], txt[i+1]
                if first in vowels and second in vowels:
                    VV += 1
                elif first in vowels and second in consonants:
                    VC += 1
                elif first in consonants and second in vowels:
                    CV += 1
                elif first in consonants and second in consonants:
                    CC += 1

            print(f"Total vowels: {vowels_count}, Total consonants: {consonants_count}")
            time.sleep(2)
            print("We have 4 options: Vowels-Vowels, Vowels-Consonants, Consonants-Vowels, Consonants-Consonants.")
            time.sleep(2)
            print(f"Vowels-Vowels: {VV}, Consonants-Consonants: {CC}, Vowels-Consonants: {VC}, Consonants-Vowels: {CV}")
            time.sleep(2)
            print("Depending on what the letter before the x is, we can calculate the probabilities of the next letter.")
            time.sleep(2)
            letter = input("What letter do you want x to represent? (a-z): ")
            print(letter)
            if letter not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter a valid letter from a to z.")
                return
            elif letter not in vowels:
                print("The letter you chose is a consonant.")
                time.sleep(2)
                print("The chance of Consonant-Consonant is: ", CC / (CC + CV) *100," %")
                time.sleep(2)
                print("The chance of Consonant-Vowel is: ", CV / (CC + CV) *100," %")
                time.sleep(2)
                print("So most likely the next letter will be a vowel.")
                
                LA = LB = LC = LD = LE = LF = LG = LH =LI =LJ=LK=LL=LN=LM=LO=LP=LQ=LR=LS=LT=LU=LV=LW=LX=LY=LZ= 0
                for i in range(len(txt) - 1):
                    first,second = txt[i], txt[i+1]
                    if first in letter and second in a:
                        LA += 1
                    elif first in letter and second in b:
                        LB += 1
                    elif first in letter and second in c:
                        LC += 1
                    elif first in letter and second in d:
                        LD += 1
                    elif first in letter and second in e:
                        LE += 1
                    elif first in letter and second in f:
                        LF += 1
                    elif first in letter and second in g:
                        LG += 1
                    elif first in letter and second in h:
                        LH += 1
                    elif first in letter and second in inew:
                        LI += 1
                    elif first in letter and second in j:
                        LJ += 1
                    elif first in letter and second in k:
                        LK += 1
                    elif first in letter and second in l:
                        LL += 1
                    elif first in letter and second in m:
                        LM += 1
                    elif first in letter and second in n:
                        LN += 1
                    elif first in letter and second in o:
                        LO += 1
                    elif first in letter and second in p:
                        LP += 1
                    elif first in letter and second in q:
                        LQ += 1
                    elif first in letter and second in r:
                        LR += 1
                    elif first in letter and second in s:
                        LS += 1
                    elif first in letter and second in t:
                        LT += 1
                    elif first in letter and second in u:
                        LU += 1
                    elif first in letter and second in v:
                        LV += 1
                    elif first in letter and second in w:
                        LW += 1
                    elif first in letter and second in x:
                        LX += 1
                    elif first in letter and second in y:
                        LY += 1
                    elif first in letter and second in z:
                        LZ += 1
                options = [LA, LB, LC, LD, LE, LF, LG, LH, LI, LJ, LK, LL, LM, LN, LO, LP, LQ, LR, LS, LT, LU, LV, LW, LX, LY, LZ]
                highest = max(options)
                highest_index = options.index(highest)
                highest_option = all[highest_index]
                print("The letters most likely to come after your letter is: ",highest_option,"with", highest,"%")
                time.sleep(2)
                print("We just predicted the next letter now we could rerun this process and eventully build a word.")
                
            elif letter in vowels:
                print("The letter you chose is a vowel.")
                print("The chance of Vowel-Vowel is: ", VV / (VV + VC) *100," %")
                print("The chance of Vowel-Consonant is: ", VC / (VV + VC) *100," %")
                print("So most likely the next letter will be a consonant.")
                LA = LB = LC = LD = LE = LF = LG = LH =LI =LJ=LK=LL=LN=LM=LO=LP=LQ=LR=LS=LT=LU=LV=LW=LX=LY=LZ= 0
                for i in range(len(txt) - 1):
                    first,second = txt[i], txt[i+1]
                    if first in letter and second in a:
                        LA += 1
                    elif first in letter and second in b:
                        LB += 1
                    elif first in letter and second in c:
                        LC += 1
                    elif first in letter and second in d:
                        LD += 1
                    elif first in letter and second in e:
                        LE += 1
                    elif first in letter and second in f:
                        LF += 1
                    elif first in letter and second in g:
                        LG += 1
                    elif first in letter and second in h:
                        LH += 1
                    elif first in letter and second in inew:
                        LI += 1
                    elif first in letter and second in j:
                        LJ += 1
                    elif first in letter and second in k:
                        LK += 1
                    elif first in letter and second in l:
                        LL += 1
                    elif first in letter and second in m:
                        LM += 1
                    elif first in letter and second in n:
                        LN += 1
                    elif first in letter and second in o:
                        LO += 1
                    elif first in letter and second in p:
                        LP += 1
                    elif first in letter and second in q:
                        LQ += 1
                    elif first in letter and second in r:
                        LR += 1
                    elif first in letter and second in s:
                        LS += 1
                    elif first in letter and second in t:
                        LT += 1
                    elif first in letter and second in u:
                        LU += 1
                    elif first in letter and second in v:
                        LV += 1
                    elif first in letter and second in w:
                        LW += 1
                    elif first in letter and second in x:
                        LX += 1
                    elif first in letter and second in y:
                        LY += 1
                    elif first in letter and second in z:
                        LZ += 1
                options = [LA, LB, LC, LD, LE, LF, LG, LH, LI, LJ, LK, LL, LM, LN, LO, LP, LQ, LR, LS, LT, LU, LV, LW, LX, LY, LZ]
                highest = max(options)
                highest_index = options.index(highest)
                highest_option = all[highest_index]
                print("The letters most likely to come after your letter is: ",highest_option,"with", highest,"%")
                time.sleep(2)
                print("We just predicted the next letter now we could rerun this process and eventully build a word.")
                        
        except FileNotFoundError:
            print("Option not found. Please ensure the Option exists.")
            return
    elif z == "B":
        print("You chose Lord of the Rings. This option is not implemented yet.")
    elif z == "C":
        print("You chose Hunger Games. This option is not implemented yet.")
    else:
        print("Choose a valid option.")
    
main()

