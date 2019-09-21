fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
for k, v in {**vegetable_prices, **fruit_prices}.items():
    print(k, '->', v)