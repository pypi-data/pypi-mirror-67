#this library can change text

if True:
    name = 'textchange'
    version = '0.0.5'
    developer = 'Yanwentao'
    update_date = '2020/4/28'
    __before__()

def __before__():
    print('==========textchange==========')
    print('full name : text change')
    print('version : '+version)
    print('developer : '+developer)
    print('update date : '+update_date)
    print('You can type "help()" for more information.')

def help():
    print('''This library has two functions, namely, reading and writing documents.
You only need to enter "write ()" to write to the document, and you need to enter "read ()" to read the document.''')

def read():
    global text
    asktextname = input('Please enter the text location(Type v to view):')
    ion = True
    if asktextname == 'v':
        print('This feature requires the installation of the tkinter library.')
        import time
        time.sleep(1)
        del time
        from tkinter.filedialog import askopenfilename
        asktextname=askopenfilename(filetypes=[('text','*.txt')])
    elif asktextname == '':
        print('This is not a location!')
        text = ''
        ion = 'False'
    if ion:
        try:
            with open(asktextname,'r',encoding='UTF-8') as t:
                text = t.read()
            print()
            print(text)
            print()
            print('The literal variable name is "text".')
        except:
            print('This is not a location!')
            text = ''

def write():
    asktextname = input('Please enter the text location(Type v to view):')
    ion = True
    if asktextname == 'v':
        print('This feature requires the installation of the tkinter library.')
        import time
        time.sleep(1)
        del time
        from tkinter.filedialog import askopenfilename
        asktextname=askopenfilename(filetypes=[('text','*.txt')])
    elif asktextname == '':
        print('This is not a location!')
        text = ''
        ion = 'False'
    if ion:
        try:
            with open(asktextname,'w+',encoding='UTF-8') as t:
                text = t.read()
                text.seek(0)
                text.truncate()
            print()
            print(text)
            print()
            wt = input('Please enter the changed text:')
            text.write(wt)
        except:
            print('This is not a location!')
            text = ''
