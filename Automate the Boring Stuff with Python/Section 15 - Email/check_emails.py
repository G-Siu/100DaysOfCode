import imapclient
import pyzmail

conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)
conn.login("garysiu.dev@gmail.com", "wqtn ccmy tdsz trjy")

conn.select_folder("INBOX", readonly=True)

UIDs = conn.search(["SINCE", "08-Oct-2023"])  # Gives UIDs of emails
# print(UIDs)

raw_message = conn.fetch([108], ["BODY[]", "FLAGS"])
# print(message)
message = pyzmail.PyzMessage.factory(raw_message[108][b"BODY[]"])
# print(message.get_subject())
# print(message.get_addresses("from"))

# print(message.text_part)  # If None, then html, otherwise it is text email
print(message.text_part.get_payload().decode("UTF-8"))

