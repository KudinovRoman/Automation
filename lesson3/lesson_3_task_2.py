from smartphone import Smartphone

phone1 = Smartphone('Samsung', 'A50', '+79233333333')
phone2 = Smartphone('Samsung', 'A51', '+79244444444')
phone3 = Smartphone('Samsung', 'A70', '+79255555555')
phone4 = Smartphone('Samsung', 'A71', '+79255555555')
phone5 = Smartphone('iphon', '5S', '+79998887766')

catalog = [phone1, phone2, phone3, phone4, phone5]

for phone in catalog :
    print(f'{phone.brand} - {phone.model}. {phone.number}')
