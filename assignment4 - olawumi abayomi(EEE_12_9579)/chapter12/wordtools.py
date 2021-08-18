import re
import sys
def test(status):
    lineno = sys._getframe(1).f_lineno
    if status == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)



def cleanword(word):
    stripped_string = re.sub(r'\W+', '', word)
    return stripped_string

def has_dashdash(word):
    return '-' in word

def extract_words(sentence):
    new_words = []
    words = sentence.split()
    for word in words:
        new_words.append(cleanword(word))
    return new_words

def word_count(sent_word, sentence):
    counter = 0
    for word in sentence:
        if sent_word == word:
            counter+=1
    return counter

def wordset(set1):
    # The set command removes duplicates in each list
    set1 = set(set1)
    return list(set1)


def longestword(word_list):
    max = word_list[0]
    for each_word in word_list:
        if len(each_word) >= len(max):
            max = each_word

    return len(max)


test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@s()'") == 'word')

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(has_dashdash("-yo-yo_"))

test(extract_words("Now is the time! 'Now', is the time? Yes, now.") ==['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtesy as she spoke--fancy") ==['she','tried','to','curtesy','as','she','the','spoke','fancy'])

test(word_count("now",["now","is","time","is","now","is","is"])==2)

test(wordset(["now","is","time","is","now","is","is"]) ==["is","now","time"])

test(longestword(['a','apple','pear','grape']) == 5)



