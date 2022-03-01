#! /usr/bin/python3
import re, pyperclip

# To Do Scheleton: 

# Create Regex for Phone Numbers
phoneRegex = re.compile(r'''
# Types: 413-555-1234, 555-0000, (415) 555-0000, 555,0000 ext 12345, ext., x12345
(
((\d\d\d) | (\(\d\d\d\)))?    # Area code (optional)
(\s|-)     # First separator
\d\d\d    # First 3 digits
-    # Second separator
\d\d\d\d     # Last 4 digits
((ext(\.)?\s|x)    # Extension word part(optional)
(\d{2,5}))?    # Extension number part(optional)
)
'''
, re.VERBOSE)

# Create Regex for Email Addresses

emailRegex = re.compile(r'''
# Types: something@something.com, some.extra@domain.com,   
[a-zA-Z0-9_.+]+    # Name part
@                   # @ symbol
[a-zA-Z0-9_.+]+    # Domain Name Part

'''
, re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])



print('Phone Numbers:\n---------------\n')
print(allPhoneNumbers)
print('Email Addresses:\n---------------\n')
print(extractedEmail)
print('-------------------------------------------------------------------')
# Copy the emails to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n-------------------------------------------------------------------\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

print('The results have been copied to the clipboard.' + '\n' + 'However for testing purposes, we will show them here too.')
print(results)