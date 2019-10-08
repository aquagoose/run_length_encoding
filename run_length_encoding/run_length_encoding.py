def compress(text):  # RLE compressor
    try:
        global count
        textsplit = []  # what the text is split into so it can be counted
        count = 1  # the variable that actually does the counting
        finstr = ""  # the final string to return
        for character in text:  # this splits the string into each character in the list
            textsplit.append(character)

        textsplit.append("")  # this is needed to prevent integer overflows

        for i in range(len(textsplit)-1):  # with the space, it allows the list to count 1 more than the text is in length without an overflow
            if textsplit[i] == textsplit[i+1]:  # <-- without a space it would break here!
                count += 1  # if the current character is equal to the next character, increase count by 1
            else:  # once it isn't it does the following:
                finstr += "{0:02}".format(count) + textsplit[i]  # this appends the number (formated to 2 characters) of characters + the actual character
                count = 1  # resets the counter

        return finstr
    except:
        print("Error while compressing.")


def decompress(text, mode):  # RLE Decompressor
    # MODE:
    # mode allows the decompressor to operate in 2 different ways.
    # mode 1 is the default. it only allows 99 chars (e.g. 99a) to be entered, so (100a) won't work. this allows it to be compatible with numbers (e.g. 068 will print 6 8's)
    # mode 2 can be selected, it allows infinite chars (e.g. 9423a) to be entered, however it won't work with numbers (e.g. 068 will print nothing)
    try:
        if mode == 1:
            charlist = []  # the character list
            count = 1  # counts to 3 then resets
            finstr = ""  # the final string...
            numbertoapp = ""  # the number of letters it should print
            for char in text:  # same as usual, splits each character into a list
                charlist.append(char)

            for i in range(len(charlist)):
                if count == 3:  # when count is 3, stop appending the number, and set this variable to the string to output
                    strtoapp = charlist[i]
                    count = 1  # resets counter
                    for a in range(0, int(numbertoapp)):  # this appends the string the number of time that numbertoapp says
                        finstr += strtoapp
                    numbertoapp = ""  # resets the numbertoapp, it IS a string
                else:
                    numbertoapp += charlist[i]  # otherwise append the number to the numbertoapp
                    count += 1  # increase the counter
            return finstr
        elif mode == 2:
            charlist = []  # the list it splits the text into
            for char in text:  # the same as the compressor, splits each character
                charlist.append(char)

            finlist = []  # i could use 1 list but i didn't. this list is a 2d list which contains the count and the letter
            numbertoapp = ""  # a string to make it easy to append to, this gets converted to a string and then gets put at point 0 of the 2d list
            finstr = ""  # the string value that gets appended to point 1 of the 2d list
            for i in range(len(charlist)):
                try:  # this try and except is key to this whole thing working
                    int(charlist[i])  # this attempts to convert each item of charlist into an integer
                    numbertoapp += charlist[i]  # if its successful it changes numbertoapp to the number
                except:  # if it fails,
                    strtoapp = charlist[i]  # the string to append is set to the string
                    finlist.append([int(numbertoapp),strtoapp])  # both values then get appended, number first (converted to int)
                    numbertoapp = ""  # because strtoapp is reset anyway, numbertoapp has to be reset

            for i in range(len(finlist)):
                for b in range(0, finlist[i][0]):  # this repeats the number of times the number is on the list
                    finstr += finlist[i][1]  # appends to the the final string which is then returned.

            return finstr
    except:
        print("Error while decompressing")


def help():
    option = int(input("What would you like help with?\n\t1. Compressing\n\t2. Decompressing"))
    print(option)
