from random import randint

def password(l):

    num = '1234567890'
    salpha = 'abcdefghijklmnopqrstuvwxyz'
    calpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cp = '@#$&%(|);'
    lt = salpha + num + cp +  calpha

    pwd = ''
    if l < 8:
        pwd = "YOUR PASSWORD UNDER 8"
    else:
        for i in range(l):
            pwd = lt[randint(0,len(lt))] + pwd
    return pwd

       
def main():
    length = int(input("Enter the lenght of password: "))
    t = password(length)
    print(t)


if __name__ == '__main__':
    main()    


