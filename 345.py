def list_del_nth(list, index):
    try:
        del list_[index]
    except IndexError:
        print('Index Not Found')
    except:
        print('Unexpected Error')
    else:
        print('Successfully')

my_list = ['one', 'two', 'three']
list_del_nth(my_list, '4')
list_del_nth(my_list, '3')
list_del_nth(my_list, '7')

print(my_list)
