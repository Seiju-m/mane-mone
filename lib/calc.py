# coding: UTF-8
def calc(data):
  
    # 使用額の計算
    data.last_ex = data.food_ex + data.daily_ex + data.hobby_ex + data.transport_ex + data.other_ex + data.rent_cost + data.scholar + data.utility_cost + data.commu
    data.c_last_ex = data.income - data.last_ex
    data.c_food_ex = data.food_st - data.food_ex
    data.c_daily_ex = data.daily_st - data.daily_ex
    data.c_hobby_ex = data.hobby_st - data.hobby_ex
    data.c_transport_ex = data.transport_st - data.transport_ex
    data.c_other_ex = data.other_st - data.other_ex
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
    data.transport_ex_d= "{:,}".format(data.transport_ex)
    data.c_transport_ex_d= "{:,}".format(data.c_transport_ex)
    data.transport_st_d= "{:,}".format(data.transport_st)
    data.other_ex_d= "{:,}".format(data.other_ex)
    data.c_other_ex_d= "{:,}".format(data.c_other_ex)
    data.other_st_d= "{:,}".format(data.other_st)
    data.rent_cost_d= "{:,}".format(data.rent_cost)
    data.scholar_d= "{:,}".format(data.scholar)
    data.utility_cost_d= "{:,}".format(data.utility_cost)
    data.commu_d= "{:,}".format(data.commu)

    return data