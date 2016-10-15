print ('Enter your name:')
x = input ()

def welcome ():
    print ('Hello ' + x + '!')

if x:
    welcome ()
else:
    x = 'World'
    welcome ()