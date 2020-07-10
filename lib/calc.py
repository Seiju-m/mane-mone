def calc(data):
    # 使用額の計算
    data.last_ex = data.food_ex + data.daily_ex + data.hobby_ex + data.rent_cost + data.scholar + data.utility_cost + data.other
    data.c_last_ex = data.income - data.last_ex
    data.c_food_ex = data.food_st - data.food_ex
    data.c_daily_ex = data.daily_st - data.daily_ex
    data.c_hobby_ex = data.hobby_st - data.hobby_ex
    # 3桁区切り
    data.income= "{:,}".format(data.income)
    data.last_ex= "{:,}".format(data.last_ex)
    data.c_last_ex= "{:,}".format(data.c_last_ex)
    data.food_ex= "{:,}".format(data.food_ex)
    data.c_food_ex= "{:,}".format(data.c_food_ex)
    data.food_st= "{:,}".format(data.food_st)
    data.daily_ex= "{:,}".format(data.daily_ex)
    data.c_daily_ex= "{:,}".format(data.c_daily_ex)
    data.daily_st= "{:,}".format(data.daily_st)
    data.hobby_ex= "{:,}".format(data.hobby_ex)
    data.c_hobby_ex= "{:,}".format(data.c_hobby_ex)
    data.hobby_st= "{:,}".format(data.hobby_st)
    data.rent_cost= "{:,}".format(data.rent_cost)
    data.scholar= "{:,}".format(data.scholar)
    data.utility_cost= "{:,}".format(data.utility_cost)
    data.other= "{:,}".format(data.other)

    return data