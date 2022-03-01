def isPhoneNumber(text):    # 415-555-1234
    if len(text) != 12:
        return False        # We need a length of 12 to be sure that it's a phone number
    for i in range(0,3):
        if not text[i].isdecimal():
            return False    # Area Code: First 3 digits need to be numbers
    if text[3] != '-':
        return False        # Missing the dash between area code and the first 3 digits
    for i in range(4,7):
        if not text[i].isdecimal():
            return False    # First 3 digits need to be numerical
    if text[7] != '-':
        return False        # Missing the second digit between the first 3 digits and the last 4 numerical characters
    for i in range(8,12):
        if not text[i].isdecimal():
            return False    # Misiing the last 4 digits
    return True

message = 'Call me at 444-555-6666 today, as from tomorrow I`ll only be available at 444-555-7777'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('We found a number: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Next time, please insert a proper phone number in the message')        
