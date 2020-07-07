def calc(data):
    data.last_ex = data.income - data.food_ex - data.daily_ex- data.hobby_ex- data.rent_cost - data.scholar - data.utility_cost - data.other
    data.food_ex2 = data.food_st - data.food_ex
    data.daily_ex = data.daily_st - data.daily_ex
    data.hobby_ex = data.hobby_st - data.hobby_ex
    return data