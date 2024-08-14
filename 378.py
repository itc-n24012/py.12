import collections
data = 'すもももももももものうち'
count = collections.Counter(data)
count_dict = collections.defaultdict(list)
for a, b in count.items():
    count_dict[b].append(a)
c = count_dict[1]
print(c)
