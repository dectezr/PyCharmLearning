# put your python code here
latins = ord('a')
double_alphabet = {}
for i in range(26):
    double_alphabet.update({chr(latins + i): chr(latins + i) * 2})

