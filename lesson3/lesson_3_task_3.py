from address import Adress
from mailing import Mailing

to_address = Adress("789456", "Владивосток", "Ленина", "35", "125")
from_address = Adress("123456", "Калининград", "Тюленина", "11", "22")
mailing = Mailing(to_address, from_address, 1000, "6500144846414346886")

print(f'Отправление {mailing.track} из {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment} в {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} -{mailing.from_address.apartment}. Стоимость {mailing.cost} рублей.')