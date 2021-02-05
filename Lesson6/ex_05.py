str = 'X-DSPAM-Confidence:0.8475'

startpos = str.find(':')

extractvalue = float(str[startpos + 1:])

print(extractvalue)