'''26 long array - a to z
5 of them
count
go through and add up number of letters per slot and number of words in general

make guess

update list to only still-valid words'''

def main():
    slot1, slot2, slot3, slot4, slot5 = "", "", "", "", ""
    slots = [slot1, slot2, slot3, slot4, slot5]

    output = ""
    words = open(r"5lwords.txt", "r")
    words = words.readlines()

    count = 0
    for i in range(5757):
        if green(words[i], 'c', 1) and yellow(words[i], 'i', 3) and yellow(words[i], 'n', 4):
            output = words[i]
            count += 1
        else:
            output = "       "

        for j in range(5):
            slots[j] += output[j]

    fullPrint(slots, count)
    return

def green(text, c, slot):
    slot = slot - 1
    if text[slot] == c:
        return True
    return False

def yellow(text, c, slot):
    slot = slot - 1
    contains = False
    for i in range(5):
        if text[i] == c:
            contains = True
    return (contains and text[slot] != c)

def fullPrint(slots, count):
    for i in range(5):
        printFrequencies(slots[i], i, count)

def printFrequencies(text, slot, length):
    for i in range(97, 123):
        count = 0
        for j in range(len(text)):
            if (text[j] == (chr(i))):
                count += 1
        percent = (100*count/length)
        if percent > 10:
            print("Frequency of " + chr(i) + " in slot " + str(slot + 1) + " is " + str(percent) + "%")

    return


main()
