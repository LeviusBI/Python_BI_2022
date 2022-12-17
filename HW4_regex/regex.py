import re
# 1St task
pattern = re.compile(r"ftp[/\w#.]*[\.\w*]\b")
with open('references', "r") as links:
    with open('ftps.txt', "a") as helpme:
        for i in links:
            match = re.findall(pattern, i)
            helpme.write('\n'.join(match)+'\n')
            


# 2Nd task
pattern = re.compile(r"\d+.?\d+")
numbers = []
with open('2430AD', "r") as ouf:
    for i in ouf:
        if re.findall(pattern, i) != []:
            match = re.findall(pattern, i)
            numbers.append(match)
for i in numbers:
    print("\n".join(i))



# 3Rd Task
pattern = re.compile(r"\b\w*[aA]\w*\b")
words = []
with open('2430AD', "r") as ouf:
    for i in ouf:
        if re.findall(pattern, i) != []:
            match = re.findall(pattern, i)
            words.append(match)
for i in words:
    print("\n".join(i))

# 4th task
pattern = re.compile("\\b[\\w ,]+[!]")
stressed = []
with open('2430AD', "r") as ouf:
    for i in ouf:
        if re.findall(pattern, i) != []:
            match = re.findall(pattern, i)
            stressed.append(match)
for i in stressed:
    print("\n".join(i))


#5th task
import seaborn as sns
import numpy as np

unique_words = set()
with open ('2430AD', "r") as cringe:
    for bruh in cringe:
        string = re.findall(r'(\b[\w\'-]+?)[ \.?!,"]', bruh)
        for w in string:
            unique_words.add(str(w).lower())            

only = {i:len(i) for i in unique_words}

counter = {} 

for key, value in only.items():
    counter.setdefault(value, set()).add(key)
frequencies = { i : (len(j) / len(only))  for (i, j) in counter.items()} 



fig = sns.barplot(x=list(frequencies.keys()), y=list(frequencies.values()))
fig.set(xlabel='Длина слова', ylabel='Доля слов данной длины')



# 6th task ёуеыаоэяию
def translator(string, consonant = 'к'):
    return re.sub(r'([ёуеыаоэяию])', f"\\1{consonant}\\1", string, flags=re.IGNORECASE)
smth = 'Поздравляю, вы умерли за донбасс'
translator(smth)