from click_shell import shell
import os, signal, psutil, platform, hashlib, pyfiglet, termcolor, qrcode, tkinter, colorthief, pyttsx3, datetime
import colorthief
import matplotlib.pyplot as plt
@shell(prompt='Saf-Shell >>>', intro='Wecome to Saf-shell')
def saf_shell():
    pass

@saf_shell.command()
def help():
    print('1.help')
    print('2.ls - list current file or folder')
    print('4.mkdir - create folder')
    print('5.rmdir - remove folder')
    print('6.cwd - return currend dir')
    print('7.pid - Processing id')
    print('8.kill - Kill pid')
    print('9.add')
    print('10.sub')
    print('11.mult')
    print('12.div')
    print('13.mkfile')
    print('14.cpuusage - return cpu usage')
    print('15.getos')
    print('16.charge')
    print('17.version')
    print('18.hash')
    print('19.figlet')
    print('20.systeminfo')
    print('21.qrcode')
    print('22.clickmegame')
    print('23.time')
    print('24.colorfinder')
@saf_shell.command()
def ls():
    return print(os.listdir())

@saf_shell.command()
def cwd():
    return print(os.getcwd())

@saf_shell.command()
def mkdir():

    inp1 = input('folder name:')
    os.mkdir(inp1)

@saf_shell.command()
def rmdir():
    inp1 = input('folder name:')
    os.rmdir(inp1)

@saf_shell.command()
def pid():
    return print(os.getpid())

@saf_shell.command()
def kill():
    inp = int(input('Enter PID:'))
    os.kill(inp, signal.SIGILL)

@saf_shell.command()
def add():
    inp = int(input('Enter first number:'))
    inp2 = int(input('Enter second number:'))
    return print(inp + inp2)

@saf_shell.command()
def sub():
    inp = int(input('Enter first number:'))
    inp2 = int(input('Enter second number:'))
    return print(inp - inp2)  

@saf_shell.command()
def mult():
    inp = int(input('Enter first number:'))
    inp2 = int(input('Enter second number:'))
    return print(inp * inp2)



@saf_shell.command()
def div():
    inp = int(input('Enter first number:'))
    inp2 = int(input('Enter second number:'))
    return print(inp / inp2)

@saf_shell.command()
def mkfile():
    inp = input('file name:')
    f = open(inp, 'x')

@saf_shell.command()
def cpuusage():
    return print(psutil.cpu_percent())

@saf_shell.command()
def getos():
    return print(platform.platform())

@saf_shell.command()
def charge():
    return print(f'Charge:{psutil.sensors_battery().percent}%')

@saf_shell.command()
def version():
    return print('3.9.1')

@saf_shell.command()
def hash():

    input1 = input('ENTER ANY PASSWORD:')

    #md5
    h = hashlib.md5()
    h.update(input1.encode())
    print('md5:',h.hexdigest())

    #sha256
    h = hashlib.sha256()
    h.update(input1.encode())
    print('sha256:',h.hexdigest())

    #sha224
    h = hashlib.sha224()
    h.update(input1.encode())
    print('sha224:',h.hexdigest())

    #sha384
    h = hashlib.sha384()
    h.update(input1.encode())
    print('sha384:',h.hexdigest())

    #sha512
    h = hashlib.sha512()
    h.update(input1.encode())
    print('sha512:',h.hexdigest())

    #sha1
    h = hashlib.sha1()
    h.update(input1.encode())
    print('sha1:',h.hexdigest())

@saf_shell.command()
def figlet():

    inp = str(input('ENTER TEXT:'))
    inp1 = str(input('ENTER COLOR:'))

    l = inp1.lower()
    fl = pyfiglet.figlet_format(inp)

    cf = termcolor.colored(fl, l)

    return print(cf)

@saf_shell.command()
def systeminfo():
    os1 = platform.platform()
    vm = psutil.virtual_memory()
    tvm = vm.total
    ac = platform.architecture()

    print('Batter power:',psutil.sensors_battery().percent,'%')
    print('OS:',os1)
    print('Machine:',platform.machine())
    print('Processor:',platform.processor())
    print('Design:', ac)
    print('Network name:',platform.node())
    print('CPU percentage:',psutil.cpu_percent())
    print('Total RAM:',tvm/1024/1024/1024,'GB')

@saf_shell.command()
def Qrcode():

    input1 = input('ENTER TEXT:')
    input2 = input('ENTER NAME OF FILE:')

    qrc = qrcode.make(input1)
    qrc.save(input2)

@saf_shell.command()
def clickmegame():
    n = 0
    def click():
        global n
        n+=1
        print(n)
        if n==10:
           print('good')
        if n==50:
           print('very good')
        if n==100:
           print('super')
        if n==500:
           print('topg')
        if n==1000:
           print('hacker')

        w = tkinter.Tk()
        w.title('clickme')
        l = tkinter.Label(w, text='CLICK ME', font=('bold',50))
        l.pack()
        b = tkinter.Button(w, text='Click me')
        b.config(command=click)
        b.pack()


        w.mainloop()

@saf_shell.command()
def time():
    return print(datetime.datetime.now())

@saf_shell.command()
def colorfinder():
    import colorthief
    import matplotlib.pyplot as plt

    inp = input('Enter image name:')
    c = colorthief.ColorThief(inp)
    gc = c.get_palette(quality=1)

    plt.imshow([gc])
    plt.show()


saf_shell()


