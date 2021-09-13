f = open('alices/alice_story.txt', 'r')
count = {}

for line in f:
    for word in line.split():
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        word = word.lower()

        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

    keys = count.keys()
    keys = sorted(keys)
    out = open('alices/alice_words.txt', 'w')
    for word in keys:
        out.write(word + " " + str(count[word]))
        out.write('\n')



