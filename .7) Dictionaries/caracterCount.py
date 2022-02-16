import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} # 'r': 12    as example

for character in message.lower():
    count.setdefault(character,0)
    count[character] = count[character] +1

pprint.pprint(count)

