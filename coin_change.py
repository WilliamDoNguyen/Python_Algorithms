def coins(amount):
    change_values = [( 'quarters', 25), ('dimes', 10), ('nickels', 5), ('pennies', 1)]
    answer = {}
    for coin_name, coin_value in change_values:
        num_coins = amount//coin_value
        amount = amount % coin_value
        if coin_value == 25:
            answer[coin_name] = num_coins
        elif coin_value == 10:
            answer[coin_name] = num_coins
        elif coin_value == 5:
            answer[coin_name] = num_coins
        else:
            answer[coin_name] = num_coins
    return answer

print(coins(81))
print(coins(12))
