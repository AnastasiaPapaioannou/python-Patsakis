"""edw ginete elegxos se pia thesi vriskete px o arithmos zero, an einai stn
0h thesi h sthn 2h gt den ginete na vriskete kapou alou, anamesa tous vriskete
i praksi(minus1,plus1,times), ara elegxoume pou einai keni thesi kai kanoume
to sting arithmo, kai an pleon vriskounte tn thesi 2h simeni telos ts praksis
ara kanoun to string arithmous k ginonte oi praksis"""
def zero(x):
    if( x[0]=='x'):
        x=x.replace("x","0")
    else:
        x=x.replace("z","0")
        if(x[1]=='+'):
            num1=int(x[0])
            num2=int(x[2])
            print num1+num2
        if(x[1]=='-'):
            num1=int(x[0])
            num2=int(x[2])
            print num2-num1
        if(x[1]=='*'):
            num1=int(x[0])
            num2=int(x[2])
            print num1*num2
    return x

def one(x):
    if(x[0]=='x'):
        x=x.replace("x","1")
    else:
        x=x.replace("z","1")
        if(x[1]=='+'):
            num1=int(x[0])
            num2=int(x[2])
            print num1+num2
        if(x[1]=='-'):
             num1=int(x[0])
             num2=int(x[2])
             print num2-num1
        if(x[1]=='*'):
            num1=int(x[0])
            num2=int(x[2])
            print num1*num2
    return x

def two(x):
    if(x[0]=='x'):
         x=x.replace("x","2")
    else:
        x=x.replace("z","2")
        if(x[1]=='+'):
             num1=int(x[0])
             num2=int(x[2])
             print num1+num2
        if(x[1]=='-'):
            num1=int(x[0])
            num2=int(x[2])
            print num2-num1
        if(x[1]=='*'):
            num1=int(x[0])
            num2=int(x[2])
            print num1*num2
    return x
def three(x):
    if(x[0]=='x'):
        x=x.replace("x","3")
    else:
         x=x.replace("z","3")
         if(x[1]=='+'):
              num1=int(x[0])
              num2=int(x[2])
              print num1+num2
         if(x[1]=='-'):
             num1=int(x[0])
             num2=int(x[2])
             print num2-num1
         if(x[1]=='*'):
             num1=int(x[0])
             num2=int(x[2])
             print num1*num2
    return x

def four(x):
    if(x[0]=='x'):
        x=x.replace("x","4")
    else:
        x=x.replace("z","4")
        if(x[1]=='+'):
            num1=int(x[0])
            num2=int(x[2])
            print num1+num2
        if(x[1]=='-'):
            num1=int(x[0])
            num2=int(x[2])
            print num2-num1
        if(x[1]=='*'):
            num1=int(x[0])
            num2=int(x[2])
            print num1*num2
    return x
def five(x):
    if(x[0]=='x'):
        x=x.replace("x","5")
    else:
        x=x.replace("z","5")
        if(x[1]=='+'):
            num1=int(x[0])
            num2=int(x[2])
            print num1+num2
        if(x[1]=='-'):
            num1=int(x[0])
            num2=int(x[2])
            print num2-num1
        if(x[1]=='*'):
            num1=int(x[0])
            num2=int(x[2])
            print num1*num2
    return x
def six(x):
    if(x[0]=='x'):
        x=x.replace("x","6")
    else:
        x=x.replace("z","6")
        if(x[1]=='+'):
            num1=int(x[0])
            num2=int(x[2])
            print num1+num2
        if(x[1]=='-'):
            num1=int(x[0])
            num2=int(x[2])
            print num2-num1
        if(x[1]=='*'):
            num1=int(x[0])
            num2=int(x[2])
            print num1*num2
    return x
def seven(x):
    if(x[0]=='x'):
        x=x.replace("x","7")
    else:
        x=x.replace("z","7")
        if(x[1]=='+'):
            num1=int(x[0])
            num2=int(x[2])
            print num1+num2
        if(x[1]=='-'):
            num1=int(x[0])
            num2=int(x[2])
            print num2-num1
        if(x[1]=='*'):
            num1=int(x[0])
            num2=int(x[2])
            print num1*num2
    return x
def eight(x):
    if(x[0]=='x'):
        x=x.replace("x","8")
    else:
        x=x.replace("z","8")
        if(x[1]=='+'):
            num1=int(x[0])
            num2=int(x[2])
            print num1+num2
        if(x[1]=='-'):
            num1=int(x[0])
            num2=int(x[2])
            print num2-num1
        if(x[1]=='*'):
            num1=int(x[0])
            num2=int(x[2])
            print num1*num2
    return x
def nine(x):
    if(x[0]=='x'):
        x=x.replace("x","9")
    else:
        x=x.replace("z","9")
        if(x[1]=='+'):
            num1=int(x[0])
            num2=int(x[2])
            print num1+num2
        if(x[1]=='-'):
            num1=int(x[0])
            num2=int(x[2])
            print num2-num1
        if(x[1]=='*'):
            num1=int(x[0])
            num2=int(x[2])
            print num1*num2
    return x
"""sinartisis opou ekteloun minus plus, times kai sto kentro dld stn 1h thesi
to antikathistoun to y me +, - h *, analoga tn praksi k epistrefoun to psifio ts
"""
def plus1(x):
    x=x.replace("y","+")
    return x

def times(x):
    x=x.replace("y","*")
    return x

def minus1(x):
    x=x.replace("y","-")
    return x

""" arxikopiooume ena string x ="xyz" , kai kaloume tn sinartisis, apo deksia
sta aristera, etsi panw stn sinartisi pai to x"""
x='xyz'
k=eight(minus1(three(x)))
