

cipher = 'TEBKFKQEBZLROPBLCERJXKBSBKQP';
all_freq = {}
  
for i in cipher:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

#print ("Count of all characters in TEBKFKQEBZLROPBLCERJXKBSBKQP is :\n " +  str(all_freq))
K=4

for key in all_freq:
    all_freq[key] = round((all_freq[key] / 28), K)
print ("Ratio per letter is :\n " + str(all_freq))



h = {1: 0.080}

EngRates = {
'A':8.34,
'B':1.54,
'C':2.73,
'D':4.14,
'E':12.60,
'F':2.03,
'G':1.92,
'H':6.11,
'I':6.71,
'J':0.23,
'K':0.87,
'L':4.24,
'M':2.53,
'N':6.80,
'O':7.70,
'P':1.66,
'Q':0.09,
'R':5.68,
'S':6.11,
'T':9.37,
'U':2.85,
'V':1.06,
'W':2.34,
'X':0.20,
'Y':2.04,
'Z':0.06,
}

for key in EngRates:
    EngRates[key] = round((EngRates[key] / 100), K)

print(EngRates)

AnalyzedRates = {
'A':8.34,
'B':1.54,
'C':2.73,
'D':4.14,
'E':12.60,
'F':2.03,
'G':1.92,
'H':6.11,
'I':6.71,
'J':0.23,
'K':0.87,
'L':4.24,
'M':2.53,
'N':6.80,
'O':7.70,
'P':1.66,
'Q':0.09,
'R':5.68,
'S':6.11,
'T':9.37,
'U':2.85,
'V':1.06,
'W':2.34,
'X':0.20,
'Y':2.04,
'Z':0.06,
}

letters =[]
letters = list(all_freq.keys())


for key in AnalyzedRates:
    if key in letters:
        AnalyzedRates[key] = all_freq[key]
    else:
        AnalyzedRates[key] = 0.00


Analyzed = list(AnalyzedRates.values())
Eng = list(EngRates.values())

Correlation = []
count = 0

for i in range(0,26):
    sum = 0
    for idx in range(0,26):
        sum = sum + (Analyzed[idx]*Eng[(26 + idx - i)%26])
        idx = idx + 1  
    Correlation.append(round(sum, K))
    count = count + 1

TopRated = [0,0,0]
idx = 0 
for i in Correlation:
    print (str(i))
    idx = idx + 1

key = 3
print(key, " ", end='')
for letter in cipher:
    if (ord(letter) + key) > 90:
        encrpted = ord(letter) + key - 25
    else:
        encrpted = ord(letter) + key
    print(chr(encrpted), end='')

print("\n")