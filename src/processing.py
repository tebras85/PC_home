spisok = [{'id': 41428829, 'satet': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

def filter_by_state(spisok) :
    new_spisok_ex = []
    new_spisok_can = []
    for slovar in spisok:
        for value in slovar.values():
            if value == 'EXECUTED':
                new_spisok_ex.append(slovar)
            if value == 'CANCELED':
                new_spisok_can.append(slovar)

    return new_spisok_ex , new_spisok_can

x=filter_by_state(spisok)
print(x)