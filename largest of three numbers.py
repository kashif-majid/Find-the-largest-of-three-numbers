i=1
while i==1:
    n1=float(input("ENTER THE FIRST NUMBER: "))
    n2=float(input("ENTER THE SECOND NUMBER: "))
    n3=float(input("ENTER THE THIRD NUMBER: "))
    if n1 > n2 and n1 > n3:
        print("{} NUMBER IS GREATEST".format(n1))
    elif n2 > n1 and n2 > n3:
        print("{} NUMBER IS GREATEST".format(n2))
    else:
        print("{} is greatest".format(n3))

    i = int(input("IF U WANT TO CONTINUE PRESS 1 ELSE PRESS ANY KEY: "))
