a = 1
try:
    a = 2
    print(a)
    raise Exception()
except:
    a = 3
    print(a)
    raise
else:
    a = 4
    print(a)
finally:
    a = 5
    print(a)