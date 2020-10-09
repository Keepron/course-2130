"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""


def t1(number):
    if number%20!=0: a = (number // 20 + 1) * 20
    else: a=number
    return a
    pass


def t2(string):
    b = string.split()
    for i in range(len(b)): b[i]=b[i][::-1]
    c=' '.join(b)
    return c
    pass


def t3(dictionary):
    a=list(f'{value}: {key}' for value, key in dictionary.items())
    b='; '.join(a)
    return b
    pass


def t4(string, sub_string):
    a=sub_string[::-1] 
    b=string.find(a)
    return -1!=b
    pass


def t5(strings):
    a=strings
    c=[]
    for i in range(len(a)): 
        if a[i].replace(' ','').isdigit()==1 and len(a[i].split())==4 and int(a[i].split()[3])==int(a[i].split()[0])*int(a[i].split()[1])*int(a[i].split()[2]):
            c.append(a[i])
    return c
    pass


def t6(string):
    for i in range(string.count("#")): 
        a=string.find("#") 
        if a==0: string=string[1::]
        elif a==-1: return string
        else: string=string[0:a-1:]+string[a+1::]
    return string
    pass


def t7(lst):
    new=[]
    for i in range(len(lst)): 
        for j in range(len(lst)): 
            if i!=j and lst[i]==lst[j]: break
        else: new.append(lst[i])
    return sum(new)
    pass


def t8(string):
    new=[]
    num=''
    for i in range(len(string)): 
        if string[i].isdigit()==1: num=num+string[i]
        else:
            if num!='':
                new.append(int(num))
                num=''
    if num!='': 
        new.append(int(num))
    return max(new)
    pass


def t9(number):
    a=list(str(number))
    if len(a)>4:
        return ''.join(a)
    else:
        for i in range(5-len(a)):
            a=['0']+a
    return ''.join(a)
    pass


def t10(string):
    b = list(string)
    c=len(b)
    if c==1:
        return ''.join(b)
    for i in range(c):
        d=len(b)
        for j in range(d-1):
            if (b[j]=='B' and b[j+1]=='R') or (b[j+1]=='B' and b[j]=='R'):
                b[j]='G'
            elif (b[j]=='R' and b[j+1]=='G') or (b[j+1]=='R' and b[j]=='G'):
                b[j]='B'
            elif (b[j]=='G' and b[j+1]=='B') or (b[j+1]=='G' and b[j]=='B'):
                b[j]='R'
        if len(b)>1: b=b[0:-1:]
        else: return ''.join(b)
    return ''.join(b)
    pass


def t11(lst):
    a=0
    b=sum(lst)
    for i in range(len(lst)):
        a=a+lst[i]
        if a-lst[i]==(b-lst[i])/2:
            return i
    return -1
    pass

import re
def t12(lst):
    b=[]
    for i in range(len(lst)):
        a=''.join(re.findall(r'\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}',lst[i]))
        a=a.replace(' ','')
        a=a.replace("-","")
        a=a.replace("+","")
        a=a.replace(")","")
        a=a.replace("(","")
        if len(a)==11:
            a='8'+a[1::]
        else: a='8'+a
        b.append(a)
    return b
    pass


def t13(number_1, number_2):
    a=list(str(number_1))
    b=list(str(number_2))
    c=''
    for i in range(max(len(a),len(b))-min(len(a),len(b))):
        if len(a)>len(b): b=['0']+b
        else: a=['0']+a
    for i in range(len(a)):
        c=c+str(int(a[i])+int(b[i]))
    return int(c)
    pass


def t14(string):
    a={ '+':   'Plus ', '-':   'Minus ', '*':   'Times ', '/':   'Divided By ', '**':  'To The Power Of ', '=':   'Equals ', '!=':  'Does Not Equal ' }
    b={'10': 'Ten ', '9': 'Nine ','8': 'Eight ','7': 'Seven ','6': 'Six ','5': 'Five ','4': 'Four ','3': 'Three ','2': 'Two ','1': 'One ', '0': 'Zero '}
    a.update(b)
    c=string.split()
    for i in range(len(c)):
        c[i]=a[c[i]]
    return ''.join(c).strip()
    pass


def t15(lst):
    a=0
    if len(lst)==len(lst[0]):
        for i in range(len(lst)): 
            a=a+lst[i][i]+lst[i][-i-1]
    else:
        for i in range(min(len(lst),len(lst[0]))):
            a=a+lst[i][i]+lst[len(lst)-1-i][i]
    return a
    pass

"""усе"""