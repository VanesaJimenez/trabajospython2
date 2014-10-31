def primeFactors(number):
    a=[]
    for m in range (2,number+1):
        while number%m==0:
            a.append(m)
            number=number/m
    return a
