def list_average(x):
    try:
        return sum(x)/len(x)
    except:
        print('list_a:', len(x))
        return None

print(list_average([5.4, 3.4]))
print(list_average([]))
