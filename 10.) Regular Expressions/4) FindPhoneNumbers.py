import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.search('my number is 555-444-1234.')


print(phoneNumRegex.search())