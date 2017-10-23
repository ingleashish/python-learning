myname = "Ashish"

try:
    f = open('simple.tx', 'r')
    f.write('Hello World')
except IOError:
    print('IOError: caused!')
except NameError:
    print('NameError: caused!')
else:
    print('Sucess writing')
    f.close()
finally:
    print('this always execute')
