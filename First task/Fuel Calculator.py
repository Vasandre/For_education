
# https://www.codewars.com//kata/57b58827d2a31c57720012e8

def fuel_price(litres, price_per_litre):

    if litres <= 0:
        cost = 0

    if 0 < litres < 2:
        cost = price_per_litre * litres

    if 2 <= litres < 4:
        cost = litres * (price_per_litre - 0.05)

    if 4 <= litres < 8:
        cost = litres * (price_per_litre - 0.1)

    if 8 <= litres < 10:
        cost = litres * (price_per_litre - 0.15)

    if 10 <= litres:
        cost = litres * (price_per_litre - 0.25)

    return round(cost, 2)

