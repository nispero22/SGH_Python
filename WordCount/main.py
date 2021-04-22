# Word Count
# program that reads a text file containing some text and for each word in the file counts how many times it appears.
# Please note you can use a dictionary structure.
# Before starting to count words it might be necessary to delete all punctuation and special symbols (new line, tab etc.) and put all words in lower case.

# open the text and delete new line
with open('text.txt', 'r') as file:
    lines = file.readlines()

words = []
for i in range(len(lines)):
    lines[i]=lines[i].replace('\n',"")
    lines[i]=lines[i].replace('\t',"")
    lines[i] = lines[i].lower()
    lines[i] = lines[i].replace('.', "")
    lines[i] = lines[i].replace(',', "")
    lines[i] = lines[i].replace('"', "")
    lines[i]=lines[i].split(" ")
    words = words + lines[i]
for i in range(words.count('')):
    words.remove('')

count_word_dict={}

for word in words:
    if word not in count_word_dict.keys():
        count_word_dict[word] = 0
    count_word_dict[word] = count_word_dict[word] + 1

print(count_word_dict)
