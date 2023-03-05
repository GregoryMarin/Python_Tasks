# Дополните приведенный код, используя форматирование строк с помощью метода format,
# так чтобы он вывел текст:
# «In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).

# year = 2010
# price = '10k'
# currency = 'Bitcoin'
# s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, price, currency)
#
# print(s)

year = 2010
amount = '10K'
currency = 'Bitcoin'

print(f'In {year}, someone paid {amount} {currency} for two pizzas.')

