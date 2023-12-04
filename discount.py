from datetime import date, timedelta, datetime

today = date.today()
print(today)

time = datetime.now()
print(time)

tomorrow = today + timedelta(days=1)
print(tomorrow)

print(time.hour)
print(time.minute)

print(today.day)

formated_date = datetime.now().strftime('%d/%m/%r')
print(formated_date)

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tomorrow, 'price': 100.0},
    {'sku': 3, 'exp_date': today, 'price': 200.0}
]

for product in products:
    if product['exp_date'] != today:
