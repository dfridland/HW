i = 0
goods = []
analytics = []
enter = ''
while enter == '':
    i += 1
    name = input("product name - ")
    price = input("product price - ")
    quantity = input("product quantity -  ")
    unit = input("product units - ")
    goods.append((i, {'name': name, 'price': price, 'quantity': quantity, "unit": unit}))
    print('\n', goods)
    enter = input("\nPress Enter to continue, any key+Enter to exit:  ")
enter = input("\n Press Enter to continue for analytics: ")
analytics = {'name': [], 'price': [], 'quantity': [], "unit": []}
for id, v in goods:
    analytics['name'].append(v['name'])
    analytics['price'].append(v['price'])
    analytics['quantity'].append(v['quantity'])
    analytics['unit'].append(v['unit'])
print(analytics)
