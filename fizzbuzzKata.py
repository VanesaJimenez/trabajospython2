def fizzbuzz(num):
    if num%15==0:
        n=("fizzbuzz")
    elif num%5==0:
        n=("buzz")
    elif num%3==0:
        n=("fizz")
    else:
        n=("{}".format(num))
    return n
