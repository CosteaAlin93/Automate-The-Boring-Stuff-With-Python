from codecs import BOM_BE


name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hello Alice')
elif age > 100 and age < 105:
    print('Kind of old granny')
elif age < 2000 or (age > 2500 and age < 2700):
    print('You are a nice quite zombie')
elif age == 3000:
    print('Finally, I found you stranger!')
elif age == 1:
    print('You have a lot time from now on...')