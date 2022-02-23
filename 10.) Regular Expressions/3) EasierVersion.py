import re

message = 'Call me at 444-555-6666 today, as from tomorrow I`ll only be available at 444-555-7777'
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumberRegex.findall(message))