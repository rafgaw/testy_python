# argumenty słownikowe

def connect(**opcje):
    print(opcje)
    print(type(opcje))
    connect_param = {
        'host': '127.0.0.7',
        'port': '6001'
    }

    connect_param['pwd'] = opcje
    print(connect_param)


connect()  # {} <class 'dict'
connect(a=9, name='Rafał')
