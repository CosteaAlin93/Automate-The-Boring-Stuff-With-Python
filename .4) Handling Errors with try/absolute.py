print('How many cats do I have?')
numCats = int(input())
try:
    pozitive = abs(numCats)
    if pozitive >= 4:
        print('That is a lot of cats.')
    else:
        print('Thas is not that many cats')
except ValueError:
    print('Please insert a number')   