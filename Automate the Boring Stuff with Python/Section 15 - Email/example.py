import smtplib

conn = smtplib.SMTP("smtp.gmail.com")
# print(type(conn))
# print(conn.ehlo())  # Checks if SMTP server is valid
conn.starttls()  # Encrypts password

conn.login("", "")
conn.sendmail(
    "",
    "",
    "Subject: So long...\n\nDear Gary, \nSo long, "
    "and thanks for all the fish.\n\n-G")
