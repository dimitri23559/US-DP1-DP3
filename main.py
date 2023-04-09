from tkinter import *
from convert import *

window = Tk()
wWidth = round(window.winfo_screenwidth()/2)
wHeight = window.winfo_screenheight()

window.title('Covert')
window['bg'] = 'green'
window.geometry(f"{wWidth}x{wHeight- 50}+{wWidth-10}+0")

clickedFrom = StringVar()
clickedTo = StringVar()


def changeInput(event):
    inp = inputtxt.get(1.0, "end-1c")
    result = inp + event.char if event.char != '\x08' else inp[:-1]
    optionsFrom = []

    if result.find(' ') == -1:
        optionsFrom = filterFrom(result)
    else:
        result = result.split(' ')
        optionsFrom = filterFroms(result)

    list = Control.pack_slaves()
    for l in list:
        l.destroy()

    if result:

        fromValue = OptionMenu(Control, clickedFrom, *optionsFrom)
        fromValue.pack(side=LEFT, padx=30)

        Convert = Label(Control, text='di ubah ke')
        Convert.pack(side=LEFT)

        toValue = OptionMenu(Control, clickedTo, *options)
        toValue.pack(side=LEFT, padx=30)

    if fail:
        failtext = Label(window, text='Sorry, there was an error')
        failtext.pack()


def convertfun():
    inp = inputtxt.get(1.0, "end-1c")
    # options = ['Text', 'Number', 'Binary', 'Octal', 'Hexadecimal']
    From = clickedFrom.get()
    To = clickedTo.get()
    decimal = []
    output = ''

    if inp.find(' ') == -1:
        if From == 'Text':
            for Tinp in [*inp]:
                decimal.append(fromText(Tinp))
                # print(fromText(Tinp))
        elif From == 'desimal':
            decimal.append(int(inp))
            # print(inp)
        elif From == 'Binary':
            decimal.append(fromBin([*inp]))
            # print(fromBin([*inp]))
        elif From == 'Octal':
            decimal.append(fromOct([*inp]))
            # print(fromOct([*inp]))
        elif From == 'Hexadecimal':
            decimal.append(fromHex([*inp]))
            # print(fromHex([*inp]))
        else:
            fail = True
    else:
        inps = inp.split(' ')

        if From == 'Text':
            for Tinp in [*inp]:
                decimal.append(fromText(Tinp))
                # print(fromText(Tinp))
        else:
            for inp in inps:
                if From == 'desimal':
                    decimal.append(int(inp))
                    # print(inp)
                elif From == 'Binary':
                    decimal.append(fromBin([*inp]))
                    # print(fromBin([*inp]))
                elif From == 'Octal':
                    decimal.append(fromOct([*inp]))
                    # print(fromOct([*inp]))
                elif From == 'Hexadecimal':
                    decimal.append(fromHex([*inp]))
                    # print(fromHex([*inp]))
                else:
                    fail = True

    for char in decimal:
        if To == 'Text':
            output += toText(char)
        elif To == 'desimal':
            output += (' ' + str(char))
        elif To == 'Binary':
            output += (' ' + toBin(char))
        elif To == 'Octal':
            output += (' ' + toOct(char))
        elif To == 'Hexadecimal':
            output += (' ' + toHex(char))
        else:
            fail = True

    # output = 'Maaf ada kesalahan' if (fail) else output

    outputtxt.config(text=output)


inputtxt = Text(window,
                height=5,
                width=30)
inputtxt.pack(pady=30, side=TOP)
inputtxt.bind('<Key>', changeInput)

Control = Frame(window)
Control['bg'] = 'green'
Control.pack(fill=Y)

clickedFrom.set("")
clickedTo.set("")

convertButton = Button(window, text='Convert', command=convertfun)
convertButton.pack(pady=30)

outputFrame = Frame(window, height=10,
                    width=(wHeight - 100))
outputFrame.pack(fill=Y)

outputtxt = Message(outputFrame,
                    text='', justify='center')
outputtxt.pack(pady=20, side=BOTTOM)


window.mainloop()