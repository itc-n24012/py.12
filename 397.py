from datetime import datetime
a_str = '20180101120130'
b = datetime.strptime(a_str, '%Y%m%d%H%M%S')
print(b)
print(b.strftime('%Y%m%d%H%M%S'))
