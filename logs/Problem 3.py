price = float(input('Цена еды?: '))
percent = float(input('Процент чаевых?: '))
chai = round(price*percent/100, 2)
print(f' Цена еды: ', price, '\n Чаевые:', chai, '\n Итого: ', price+chai)

