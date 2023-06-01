from click_shell import shell
import os, signal, psutil, platform

@shell(prompt='Saf-Shell >', intro='Wecome to Saf-shell')
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
    return print('3.9.0')