import re
from collections import Counter

words_list = []

def words_counter(text):
    words = re.findall(r'\w+', text)
    for word in words:
        words_list.append(word.lower())

    c = Counter(words_list)
    most_common_words = (dict(c.most_common(3))).keys()
    
    if len(c) >= 3:
        print("Most common words:",most_common_words)
    else:
        words_list.clear()
        print("less than 3", words_list)

text = input("Enter text: ")
words_counter(text)