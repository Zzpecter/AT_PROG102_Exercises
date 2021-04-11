from note import Note
from diagramRow import DiagramRow

if __name__ == '__main__':

     #input handling
    invalidInput = True
    while invalidInput:

        print('Enter the Length of the song:')
        n = input()
        try:
            n=int(n)
        except ValueError:
            print('Must enter integer numbers!')
            pass

        print('Enter the Notes:')
        noteInput = input().split(' ')

        if len(noteInput) == n:
            invalidInput = False
        else:
            print('the length must coincide with the number of notes! Try again..')

    pos = 0
    notes = []
    #classify each input and create an associated Note object
    for n in noteInput:
        if len(n) == 1:
            notes.append(Note(pitch=n, duration=1, pos=pos))
            pos += 2
        elif len(n) == 2:
            duration = int(n[1])
            notes.append(Note(pitch=n[0], duration=duration, pos=pos))
            pos += (duration + 1)


    #Create the objects that will store the info.
    diagramRows = []
    diagramRows.append(DiagramRow(pitch='G', length=pos+1, fillChar=' '))
    diagramRows.append(DiagramRow(pitch='F', length=pos+1))
    diagramRows.append(DiagramRow(pitch='E', length=pos+1, fillChar=' '))
    diagramRows.append(DiagramRow(pitch='D', length=pos+1))
    diagramRows.append(DiagramRow(pitch='C', length=pos+1, fillChar=' '))
    diagramRows.append(DiagramRow(pitch='B', length=pos+1))
    diagramRows.append(DiagramRow(pitch='A', length=pos+1, fillChar=' '))
    diagramRows.append(DiagramRow(pitch='g', length=pos+1))
    diagramRows.append(DiagramRow(pitch='f', length=pos+1, fillChar=' '))
    diagramRows.append(DiagramRow(pitch='e', length=pos+1))
    diagramRows.append(DiagramRow(pitch='d', length=pos+1, fillChar=' '))
    diagramRows.append(DiagramRow(pitch='c', length=pos+1, fillChar=' '))
    diagramRows.append(DiagramRow(pitch='b', length=pos+1, fillChar=' '))
    diagramRows.append(DiagramRow(pitch='a', length=pos+1))

    #add the notes
    for r in diagramRows:
        actualPitch = r.pitch
        #look for notes with the same pitch
        for note in notes:
            if note.pitch == actualPitch:
                r.addNote(note.pos, note.duration)

    #output
    for r in diagramRows:
        print(r.getString() + '\n')
