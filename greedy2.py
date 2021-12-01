def coinchange(totalnumber,clist):
    n=totalnumber
    clist.sort()
    index=len(clist)-1
    while True:
        coinvalue=clist[index]
        if n>=coinvalue:
            print(coinvalue)
            n=n-coinvalue
        if n<coinvalue:
            index-=1
        if n==0:
            break

coins=[1,2,5,20,50,100]
coinchange(201,coins)