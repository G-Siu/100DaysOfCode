text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(".")
number = text[pos:pos+5]
value = float(number)
print(value)