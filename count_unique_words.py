import os

brian = os.getcwd() + "/life_of_brian.txt"
news = os.getcwd() + "/swe_news.txt"
alphabet = "abcdefghijklmnopqrstuvwxyz'-"
special = "\n"


def cleanword(word):
    newword = ""
    for i in word:
        if i in alphabet:        # rewrites the word without special characters
            newword = newword + i
    return newword


def read_file(input_file):
    lst = []
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")
            line = line.lower().split(" ")
            for i in line:
                lst.append(cleanword(i))
    return lst


def count_unique(lst):
    return len(set(lst))


def count_occurences(lst):
    dct = {}
    for i in lst:
        if len(i) > 4:
            if i not in dct:
                dct[i] = 0
            dct[i] += 1
    sortdct = sorted(dct.items(), key=lambda tpl: tpl[1], reverse=True)

    # Slice at 10 words
    for i in sortdct[:10]:
        print(f"The word  '{i[0]}' \t  occured {i[1]} times")
    return sortdct


file = read_file(brian)
file2 = read_file(news)


print("\nLife of Brian has", count_unique(file), "unique words\n")
count_occurences(file)

print("\n\nSwedish news has", count_unique(file2), "unique words\n")
count_occurences(file2)
