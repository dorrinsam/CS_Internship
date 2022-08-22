import myfunctions

with open('moby_01') as input, open('moby_01_clean', "w") as output:
    for line in input:
        lower_line = myfunctions.lower(line)
        cleaned_line = myfunctions.delete_punctuation(lower_line)
        word = myfunctions.words(cleaned_line)
        output.write(word)

y = []
with open('moby_01_clean') as input:
    for word in input:
        y.append(word.strip())

count_1 = myfunctions.count(y)
common_words = myfunctions.most_used(count_1)