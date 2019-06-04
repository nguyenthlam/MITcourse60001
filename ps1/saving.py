#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:38:39 2019

@author: lamnguyen
"""

# User input:
# annual_salary = a_sal
# semi_annual_raise = s_raise
# portion_saved = p_save
# total_cost

#portion_down_payment = 0.25*total_cost
#current_savings = 0.0
# annual return = a_return


def cal_saving(a_sal, s_raise, p_save, a_return, n_mon):
    """
    a_sal = annual_salary
    s_raise = semi_annual_raise
    p_save = portion_saved of salary
    a_return = annual interest return of savings
    n_mon = number of months

    This is to calculate savings after a number of months
    """
    current_savings = 0.0
    mon_sal = a_sal / 12

    for n in range(n_mon):
        current_savings += current_savings * a_return / 12
        current_savings += mon_sal * p_save

        if (n+1) % 6 == 0:
            mon_sal += mon_sal * s_raise

    return current_savings
