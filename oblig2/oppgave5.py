
def char_in_String(string, char):
    for x in range(len(string)):
        if string[x] == char:
            print("found match at position  " + str(x))
            return

    print("Did not find a char")

char_in_String("hei","i")
