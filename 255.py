data = [
        ['0001' , 'Male' , 'Yamada' , 'Tarou' , 25 , 'Tokyou'],
        ['0002' , 'Male' , 'Satou' , 'Takeshi' , 27 , 'Kanagawa'],
        ['0003' , 'Female' , 'Tanaka' , 'Yuko' , 25 , 'Saitama'],
        ['0004' , 'Male' , 'Suzuki' , 'Ichirou' , 35 , 'Hokkaido'],
]
data

number_list = {}
for record in data:
    a = record[0]
    b = record[1:]
    number_list[a] = b

print('number', 'list')
for a, b in number_list.items():
    print(a, b)
