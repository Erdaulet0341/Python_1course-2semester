s = input().split('+')
dic = {'ONE':'1', 'TWO':'2', 'THR':'3', 'FOU':'4' , 'FIV':'5',
       'SIX':'6', 'SEV':'7', 'EIG':'8', 'NIN':'9','ZER':'0'}
def f(s):
    san=''
    arip=''
    for i in range(len(s)): #ONETWO
        if i == len(s)-1:
            arip+=s[i]
        if len(arip)==3:
            for j in dic:
                if arip == j:
                    san+=dic[j]
                    arip=s[i] 
        else:
            arip+=s[i]
    return san
res = int(int(f(s[0])) + int(f(s[1])))
st = str(res)
answer = ''
for i in range(len(st)): #579
    for j in dic:
        if st[i]==dic[j]:
            answer+=j
print(answer)

"""def become(s):
    san=''
    arip=''
    k=len(s)
    for i in range(k): #ONETWO
        if i == k-1:
            san+=s[k-1]
        if len(san)==3:
            if san=="ONE":
                arip+='1'
            elif san=="TWO":
                arip+='2'
            elif san=="THR":
                arip+='3'
            elif san=="FOU":
                arip+='4'
            elif san=="FIV":
                arip+='5'
            elif san=="SIX":
                arip+='6'
            elif san=="SEV":
                arip+='7'
            elif san=="EIG":
                arip+='8'
            elif san=="NIN":
                arip+='9'
            elif san=="ZER":
                arip+='0'
            san = s[i]
        else:
            san+=s[i]
    return arip

text = input()
n = text.find("+")
san1=text[0:n]
san2=text[n+1:len(text)]
res = int(become(san1))+int(become(san2))
san=''
st = str(res)
for i in st:
    if i == '1':
        san+="ONE"
    elif i == "2":
        san+="TWO"
    elif i == "3":
        san+="THR"
    elif i == "4":
        san+="FOU"
    elif i == "5":
        san+="FIV"
    elif i == "6":
        san+="SIX"
    elif i == "7":
        san+="SEV"
    elif i == "8":
        san+="EIG"  
    elif i == "9":
        san+="NIN"
    elif i=="0":
        san+="ZER"
print(san)"""