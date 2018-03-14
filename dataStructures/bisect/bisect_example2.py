import bisect

value = [14, 85, 77, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New  Pos  Contents')
print('---  ---  --------')

l = []

for i in value:
    position = bisect.bisect(l, i)
    bisect.insort_left(l, i)
    print('{:3}  {:3}  '.format(i, position), l)
