print('How many cats do I have?')
numCats = input()
try:
    if int(numCats)  >= 4:
        print('That is a lot of cats.')
    elif int(numCats) == 0:
        print('You have no cats...')    
    elif int(numCats) >1 and int(numCats) <4:
        print('Not that many actually')
    elif int(numCats) <0:
        print('You can`t have a negative number of cats')    
except ValueError:
    print('Please insert a number')   
