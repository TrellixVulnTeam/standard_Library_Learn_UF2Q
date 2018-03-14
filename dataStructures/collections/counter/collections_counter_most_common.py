import collections

c = collections.Counter()
with open('./words.txt', 'rt') as f:
    for line in f:
        c.update(line.strip().lower())

print('Most common:')
for letter, count in c.most_common(3):
    print('{}: {:>7}'.format(letter, count))
