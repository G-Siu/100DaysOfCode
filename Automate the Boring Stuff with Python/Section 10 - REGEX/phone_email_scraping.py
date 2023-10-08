import re
import pyperclip

# Create a regex for phone numbers
phone_regex = re.compile(r"""
# 123-123-1234, 555-0000, (123) 123-1234, 123-1234 ext 12345, ext.12345, x12345

(
((\d\d\d\d) | (\(\d\d\d\d\)))  # area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
(\s|-)                      # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|x)           # extension word-part(optional)
 (\d{2,5}))?                  # extension number-part (optional)
)
""", re.VERBOSE)

# Create a regex for email addresses
email_regex = re.compile(r"""
# some.+_thing@(\d{2,5})?.com

[a-zA-Z0-9_.+]+      # name part
@                    # @ symbol
[a-zA-Z0-9_.+]+      # domain name part
""", re.VERBOSE)
# Get the text off the clipboard
text = pyperclip.paste()
# Extract the email/phone from this text
extracted_phone = phone_regex.findall(text)
# print(extracted_phone)
extracted_email = email_regex.findall(text)
# print(extracted_email)

all_phone = []
for number in extracted_phone:
    all_phone.append(number[0])
print(all_phone)
# Copy the extracted email/phone to the clipboard
results = "\n".join(all_phone) + "\n" + "\n".join(extracted_email)
pyperclip.copy(results)  # Copy the phone numbers and emails to clipboard
