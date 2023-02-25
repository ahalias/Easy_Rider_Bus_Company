import re

string = 'a Sample sentencE 123'
cap = re.findall(r'([A-Z][\w]+)', string)
dig = re.findall(r'([\d]+)', string)
print('Capitalized words:', ', '.join(cap))
print('Digits:', ', '.join(dig))
