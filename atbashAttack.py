ciphertxt = list(map(str, input().split()))
ciphertxt = [list(i) for i in ciphertxt]
ciphertxt = [[chr(ord('Z') - (ord(j)-ord('A'))) for j in i] for i in ciphertxt]
ciphertxt = [''.join(i) for i in ciphertxt]
ciphertxt = ' '.join(ciphertxt)
print(ciphertxt)