from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def puissance(x,y):
    res = 1
    if y == 0:
        return 1
    else:
        for i in range(y):
            res*=x
        return res
#DECIMAL VERS X
def DecToBin(x):
    res = ""
    while x!=0:
        res = str(x%2) + res
        x = x//2
    return res

def DecToOct(x):
    res = ""
    while x!=0:
        res = str(x%8) + res
        x = x//8
    return res

def DecToHex(x):
    res = ""
    while x!=0:
        rest = x % 16
        if 10<= rest <=15:
            res = chr( 65 +(rest-10)) + res
        else:
            res = str(rest) + res
        x = x // 16
    return res

#x vers Decimal
def BinToDec(x):
    res = 0
    strx = str(x)
    i = len(strx)
    j = 0
    while i>0:
        i-=1
        res = res + int(strx[i])*puissance(2,j)
        j +=1
    return res
def HexToDec(x):
    res = 0
    i = len(x)
    j = 0
    while i>0:
        i-=1
        if "A"<=x[i]<="F":
            res = res + (ord(x[i])-55)*puissance(16,j)
        else:
            res = res + int(x[i])*puissance(16,j)
        j +=1
    return res
def OctToDec(x):
    res = 0
    i = len(x)
    j = 0
    while i>0:
        i-=1
        res = res + int(x[i])*puissance(8,j)
        j +=1
    return res
#radio valeurs
def radio1():
    binary = windows.binary.isChecked()
    hexadecimal = windows.hexa.isChecked()
    dec = windows.dec.isChecked()
    octa = windows.oct.isChecked()
    if binary == True:
        return "binary"
    elif hexadecimal == True:
        return "hex"
    elif dec == True:
        return "dec"
    elif octa == True :
        return "oct"
def radio2():
    binary = windows.binaryRES.isChecked()
    hexadecimal = windows.hexRES.isChecked()
    dec = windows.decRES.isChecked()
    octa = windows.octRES.isChecked()
    if binary == True:
        return "binary"
    elif hexadecimal == True:
        return "hex"
    elif dec == True:
        return "dec"
    elif octa == True :
        return "oct"
    
def Verifier():
    global x
    global validite
    global choice
    choice = radio1()
    validite = False
    x = windows.input1.text()
    if choice== "binary":
        if len(x)!=0:
            for i in range(len(x)):
                if x[i]!="0" and x[i]!="1":
                    windows.msg.setText("erreur")
                    break
                else:
                    validite = True
                    windows.msg.setText("valide")
        else:
            windows.msg.setText("champ vide")
    elif choice== "hex":
        if len(x)!=0:
            test = 0
            for i in range(len(x)):
                if (65<=ord(x[i])<=70) or (x[i].isdecimal()):
                    test+=1
            if test == len(x):
                windows.msg.setText("valide")
                validite = True
            else:
                windows.msg.setText("erreur")
            
        else:
            windows.msg.setText("champ vide")
            
    elif choice == "dec":
        if len(x)!=0:
            if x.isdecimal():
                validite = True
                windows.msg.setText("valide")
            else:
                windows.msg.setText("erreur")
    elif choice == "oct":
        if len(x)!=0:
            test = 0
            for i in range(len(x)):
                if "0"<=x[i]<="8":
                    test+=1
            if test == len(x):
                    windows.msg.setText("valide")
                    validite = True
            else:
                windows.msg.setText("erreur")
        else:
            windows.msg.setText("champ vide")
                        
    
def Convertir():
    global x
    global validite
    if validite == True:
        if choice == "binary":
            if radio2() == "binary":
                windows.resultat.setText(x)
            elif radio2() == "hex":
                DecX = BinToDec(int(x))
                HexX = DecToHex(DecX)
                windows.resultat.setText(str(HexX))
            elif radio2() == "dec":
                BinX = BinToDec(int(x))
                windows.resultat.setText(str(BinX))
            elif radio2() == "oct":
                DecX = BinToDec(int(x))
                OctX = DecToOct(DecX)
                windows.resultat.setText(str(OctX))
        elif choice == "hex":
            if radio2() == "binary":
                DecX = HexToDec(x)
                BinX = DecToBin(DecX)
                windows.resultat.setText(BinX)
            elif radio2() == "hex":
                windows.resultat.setText(x)
            elif radio2() == "dec":
                DecX = HexToDec(x)
                windows.resultat.setText(str(DecX))
            elif radio2() == "oct":
                DecX = HexToDec(x)
                OctX = DecToOct(DecX)
                windows.resultat.setText(str(OctX))
        elif choice == "dec":
            if radio2() == "binary":
                BinX = DecToBin(int(x))
                windows.resultat.setText(BinX)
            elif radio2() == "hex":
                HexX = DecToHex(int(x))
                windows.resultat.setText(HexX)
            elif radio2() == "dec":
                windows.resultat.setText(str(x))
            elif radio2() == "oct":
                OctX = DecToOct(int(x))
                windows.resultat.setText(str(OctX))
        elif choice == "oct":
            if radio2() == "binary":
                DecX = OctToDec(x)
                BinX = DecToBin(DecX)
                windows.resultat.setText(BinX)
            elif radio2() == "hex":
                DecX = OctToDec(x)
                HexX = DecToHex(DecX)
                windows.resultat.setText(HexX)
            elif radio2() == "dec":
                DecX = OctToDec(x)
                windows.resultat.setText(str(DecX))
            elif radio2() == "oct":
                
                windows.resultat.setText(x)
            

app = QApplication([])
windows = loadUi ("C:/Users/yungm/OneDrive/Desktop/Projet python/FG.ui")
windows.show()
windows.Convertir_2.clicked.connect ( Convertir )
windows.Verifier_2.clicked.connect ( Verifier )

app.exec_()