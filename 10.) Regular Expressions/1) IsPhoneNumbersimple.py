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

print(isPhoneNumber('123-123-1234'))
