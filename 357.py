name = 'out_test.txt'
one = 'Hello out_test.txt'
with open(name, 'w') as a:
    a.write(one)

with open(name, 'r') as a:
    for line in a:
        print(line, end='')
