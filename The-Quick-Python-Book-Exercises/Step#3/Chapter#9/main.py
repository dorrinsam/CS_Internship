def lower(l):
    lowline = l.lower()
    return lowline

def delete_punctuation(l):
    s = l.maketrans('.,?!:;','      ')
    a = l.translate(s)
    return a

def words(l):
    words = l.split()
    c = '\n'.join(words)
    return c

with open("moby_01") as input, open("moby_01_clean", "w") as output:
    for l in input:
        lower_line = lower(l)
        r = delete_punctuation(lower_line)
        txt = words(r)
        output.write(txt)


def count(y):
    x = {}
    for b in y:
        x[b] = x.get(b, 0) + 1
    return x

def most_used(x):
    list_1 = list(x.items())
    list_1.sort(key = lambda x : x[1])
    print(list_1[0], list_1[-1])

y = []

with open('moby_01_clean') as infile:
    for word in infile:
        y.append(word.strip())

count_1 = count(y)
common = most_used(count_1)