import random
import time

easylist = ["clay", "my", "tent", "mask", "give", "sale", "fuss", "pest", "put", "wind", "bow", "past", "more", "easy",
            "above", "bag", "area", "down", "dance", "far", "cook", "saw", "apple", "tree", "how", "one", "dark", "vim",
            "equal", "tribe", "fit", "death", "ban", "slide", "crack", "tray", "lease", "count", "hall", "pound", "vat",
            "virus", "sheet", "fix", "beg", "go", "desk", "heavy", "ice", "lily", "oh", "ranch", "amuse"]

mediumlist = ["imperial","identity","composer","econobox","theorist","profound","register","material","grateful"]

hardlist = ["correspondence", "identification", "extraterrestrial","characteristic","superintendent","responsibility",
            "disappointment","discrimination","infrastructure","administration"]

name = str(input("Welcome keyboard warrior, what is your name? "))
print("Very good, " + name + " you are about to be faced with a serious of typing challenges that will "
                            "grow in difficulty, to test your abilities.")



def levelone():
    usedtime = 0.0
    remtime = 0.0
    totalwords = 0
    correctwords = 0
    while (usedtime <= 60):
        word = random.choice(easylist)
        easylist.remove(word)
        remtime = 60.0 - usedtime
        print(remtime)
        print(word)
        start = time.time()
        inp = input("Enter a word:")
        end = time.time()
        if (inp == word):
            correctwords += 1
        usedtime += (end - start)
        totalwords += 1
    print("Times up!")
    print("Total no. of words:", totalwords)
    incwords = totalwords - correctwords
    print("No. of incorrect words", incwords)
    raw = (totalwords / usedtime) * 60.0
    print("RAW words per minute %.2f" % raw)
    actual = (correctwords / usedtime) * 60.0
    print("Actual words per minute: %.2f" % actual)

levelone()