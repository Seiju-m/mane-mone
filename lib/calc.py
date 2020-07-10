def calc(data):
    # try:
    #     data.income= int(data.income.replace(',', ''))
    #     data.last_ex= int(data.last_ex.replace(',', ''))
    #     data.c_last_ex= int(data.c_last_ex.replace(',', ''))
    #     data.food_ex= int(data.food_ex.replace(',', ''))
    #     data.c_food_ex= int(data.c_food_ex.replace(',', ''))
    #     data.food_st= int(data.food_st.replace(',', ''))
    #     data.daily_ex= int(data.daily_ex.replace(',', ''))
    #     data.c_daily_ex= int(data.c_daily_ex.replace(',', ''))
    #     data.daily_st= int(data.daily_st.replace(',', ''))
    #     data.hobby_ex= int(data.hobby_ex.replace(',', ''))
    #     data.c_hobby_ex= int(data.c_hobby_ex.replace(',', ''))
    #     data.hobby_st= int(data.hobby_st.replace(',', ''))
    #     data.rent_cost= int(data.rent_cost.replace(',', ''))
    #     data.scholar= int(data.scholar.replace(',', ''))
    #     data.utility_cost= int(data.utility_cost.replace(',', ''))
    #     data.other= int(data.other.replace(',', ''))
    # except:
    #     pass


    # 使用額の計算
    data.last_ex = data.food_ex + data.daily_ex + data.hobby_ex + data.rent_cost + data.scholar + data.utility_cost + data.other
    data.c_last_ex = data.income - data.last_ex
    data.c_food_ex = data.food_st - data.food_ex
    data.c_daily_ex = data.daily_st - data.daily_ex
    data.c_hobby_ex = data.hobby_st - data.hobby_ex
    # 3桁区切り
    data.income_d= "{:,}".format(data.income)
    data.last_ex_d= "{:,}".format(data.last_ex)
    data.c_last_ex_d= "{:,}".format(data.c_last_ex)
    data.food_ex_d= "{:,}".format(data.food_ex)
    data.c_food_ex_d= "{:,}".format(data.c_food_ex)
    data.food_st_d= "{:,}".format(data.food_st)
    data.daily_ex_d= "{:,}".format(data.daily_ex)
    data.c_daily_ex_d= "{:,}".format(data.c_daily_ex)
    data.daily_s_dt= "{:,}".format(data.daily_st)
    data.hobby_ex_d= "{:,}".format(data.hobby_ex)
    data.c_hobby_ex_d= "{:,}".format(data.c_hobby_ex)
    data.hobby_st_d= "{:,}".format(data.hobby_st)
    data.rent_cost_d= "{:,}".format(data.rent_cost)
    data.scholar_d= "{:,}".format(data.scholar)
    data.utility_cost_d= "{:,}".format(data.utility_cost)
    data.other_d= "{:,}".format(data.other)

    return data