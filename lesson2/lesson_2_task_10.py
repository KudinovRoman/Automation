
def calculation_deposit_in_bank(summa, years):
    for i in range(years):
        summa = summa * 1.1
    return round(summa, 2)

print(calculation_deposit_in_bank(1000, 5))