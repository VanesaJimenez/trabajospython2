def toRoman(num):
    numero=''
    while num!=0:
        while num>=1000 and num<4000:
            if (num//1000)!=0:
                numero+='M'
                num-=1000
        if num>=900:
            numero+='CM'
            num-=900
        if num>=500:
            numero+='D'
            num-=500
            while (num//100)!=0:
                numero+='C'
                num-=100
        if num>=400:
            numero+='CD'
            num-=400
        while num>=100:
            numero+='C'
            num-=100
        if num>=90:
            numero+='XC'
            num-=90
        if num>=50:
            numero+='L'
            num-=50
            while (num//10)!=0:
                numero+='X'
                num-=10
        if num>=40:
            numero+='XL'
            num-=40
        while num>=10:
            numero+='X'
            num-=10
        if num>=9:
            numero+='IX'
            num-=9
        if num>=5:
            numero+='V'
            num-=5
            while (num//1)!=0:
                numero+='I'
                num-=1
        if num>=4:
            numero+='IV'
            num-=4
        while num>=1:
            numero+='I'
            num-=1
        
            
    return numero
