
def searchFirstOcurrenceIndex(codeChar, message, start):
    idx = None
    charIdx = start

    for i in range(start, len(message)):
        if codeChar == message[i]:
            idx = charIdx
            break
        charIdx += 1

    return idx

if __name__ == '__main__':

    #input handling
    invalidInput = True
    while invalidInput:

        print('Enter the Code and the Message separated by a space:')
        try:
            code, message = input().split(' ')
        except ValueError:
            print('Invalid input, try again!')
            pass

        if len(code)>= 3 and len(code)<= 8 and len(message)>= 10 and len(code)<= 40:
            invalidInput = False
        else:
            print('Invalid input, try again!')
    code = code.upper()
    message = message.upper()

    #solving the problem
    output=""
    firstIdxs = []
    lastIdx =0
    for c in code:
        lastIdx = searchFirstOcurrenceIndex(c, message, lastIdx)
        firstIdxs.append(lastIdx)

    if None not in firstIdxs and firstIdxs == sorted(firstIdxs):
        output='PASS'
    else:
        output='FAIL'

    print(output)
