from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from nltk.util import trigrams
from collections import Counter
import random
import re

def get_head(head, ini_word):
    result = ""
    while not result:
        head = random.choice(list(dict_trig.keys()))
        first_word = head.split()
        result = re.match(ini_word, first_word[0])

    return head

def get_final(tail, final_word):
    return re.match(final_word, tail)


f = open(input(), "r", encoding="utf-8")


wtk = WhitespaceTokenizer().tokenize(f.read())


trig = list(trigrams(wtk))
dict_trig = {}


for key1, key2, value in trig:
    key = f"{key1} {key2}"
    dict_trig.setdefault(key, []).append(value)


ini_word = "[A-Z].+[^\.\!\?]$"
final_word = "[A-z].+[\.\!\?]"

head = None
i = 1
sentence = []

while i <= 10:

    random.seed()
    head = get_head(head, ini_word)
    sentence.append(head)
    result_final = ""

    while not result_final:
        new_head = head.split()
        list_tail = [tail for tail in dict_trig[head]]
        dict_tail = Counter(list_tail) 
        word_tail = [key for key in dict_tail.keys()]
        weight_tail = [value for value in dict_tail.values()]
        head = "".join(random.choices(word_tail, weights=weight_tail, k=1))
        result_final = get_final(head, final_word)
        sentence.append(head)

        if result_final and len(sentence) < 4:
            result_final = None

        head = f"{new_head[1]} {head}"
    print(*sentence)
    sentence.clear()

    i += 1

f.close()