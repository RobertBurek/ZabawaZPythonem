import subprocess

stanGry=[[' ',' ',' ',],[' ',' ',' ',],[' ',' ',' ',]]

def wypiszPlansze(t):
    print("    1   2   3 ")
    print(" A  "+str(t[0][0])+" | "+str(t[0][1])+" | "+str(t[0][2])+" ")
    print("   -----------")
    print(" B  "+str(t[1][0])+" | "+str(t[1][1])+" | "+str(t[1][2])+" ")
    print("   -----------")
    print(" C  "+str(t[2][0])+" | "+str(t[2][1])+" | "+str(t[2][2])+" ")

XO='X'

def zapiszRuch(XO):
    ok=False
    while ok==False:
        ruch = input('Postaw '+XO+' podając (A1,B2..3C): ')
        if ruch=='1A' or ruch=='A1':
            if stanGry[0][0]==" ": 
                stanGry[0][0]=XO 
                ok=True
        if ruch=='2A' or ruch=='A2':
            if stanGry[0][1]==" ": 
                stanGry[0][1]=XO 
                ok=True
        if ruch=='3A' or ruch=='A3':
            if stanGry[0][2]==" ": 
                stanGry[0][2]=XO 
                ok=True   
        if ruch=='1B' or ruch=='B1':
            if stanGry[1][0]==" ": 
                stanGry[1][0]=XO 
                ok=True
        if ruch=='2B' or ruch=='B2':
            if stanGry[1][1]==" ": 
                stanGry[1][1]=XO 
                ok=True
        if ruch=='3B' or ruch=='B3':
            if stanGry[1][2]==" ": 
                stanGry[1][2]=XO 
                ok=True   
        if ruch=='1C' or ruch=='C1':
            if stanGry[2][0]==" ": 
                stanGry[2][0]=XO 
                ok=True   
        if ruch=='2C' or ruch=='C2':
            if stanGry[2][1]==" ": 
                stanGry[2][1]=XO 
                ok=True
        if ruch=='3C' or ruch=='C3':
            if stanGry[2][2]==" ": 
                stanGry[2][2]=XO 
                ok=True
        print('Ruch niemożliwy!!!')

wypiszPlansze(stanGry)
i=1
while i<10:
    print('Ruch numer '+str(i)+'.')
    zapiszRuch(XO)
    if XO=='O': 
        XO='X'
    else:
        XO='O' 
    subprocess.call("cls", shell = True)
    wypiszPlansze(stanGry)
    i+=1
