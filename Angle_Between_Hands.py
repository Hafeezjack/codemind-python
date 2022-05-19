a,b=map(int,input().split(':'))
if abs(30*a-5.5*b)>180:
    print((360-abs(30*a-5.5*b)))
else:
    print(abs(30*a-5.5*b))
    