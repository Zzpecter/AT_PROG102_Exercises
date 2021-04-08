from piece import Piece
import argparse

if __name__ == '__main__':
    #parse args
    parser = argparse.ArgumentParser(prog='p5.py')
    parser.add_argument('--inputFile', type=str, default='input/sample1.txt',  help='select a txt file with the input')
    opt = parser.parse_args()

    
    #input handling
    try:
        data = open(opt.inputFile, "r")
    except IOError:
        print ("Error: input file does not exist.")

    #reading the input
    BOARD_LINES = 17
    usefulIndexes = [2, 6, 10, 14, 18, 22, 26, 30]
    pieces = []
    posX, posY = 0, 0
    lineList = data.readlines()
    for line in range(BOARD_LINES):
        if line % 2 != 0 and line > 0:
            currentLine = lineList[line]

            for idx in usefulIndexes:
                if currentLine[idx] != '.' and  currentLine[idx] != ':':
                    print(currentLine[idx])
                    color = 'WHITE' if currentLine[idx].isupper() else 'BLACK'
                    kind = currentLine[idx].upper()
                    pieces.append(Piece(kind, color, posX, posY))
                posX += 1
            posY += 1
            posX = 0
    for p in pieces:
        print(p.kind)

