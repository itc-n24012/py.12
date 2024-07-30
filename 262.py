data = [
        ['01' , '0001' , 'Male' , 'Yamada' , 'Tarou' , 25 , 'Tokyo'],
        ['01' , '0002' , 'Male' , 'Satou' , 'Takeshi' , 27 , 'Kanagawa'],
        ['01' , '0003' , 'Female' , 'Tanaka' , 'Yuko' , 25 , 'Saitama'],
        ['02' , '0001' , 'Male' , 'Smith' , 'Mike' , 22 , 'NewJersey'],
        ['02' , '0002' , 'Male' , 'Tuener' , 'Tom' , 27 , 'kansas'],
        ['02' , '0003' , 'Male' , 'Jackson' , 'David' , 25 , 'Florida']
]
data

number_name = {}

for record in data:
    a = (record[0], record[1])
    b = record[2:]
    number_name[a] = b
    
print('number' , 'name')
for a, b in number_name.items():
    print(a, b)

        
