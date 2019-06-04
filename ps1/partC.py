#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:38:39 2019

@author: lamnguyen
"""

# User input:

from saving import cal_saving

a_sal = float(input('enter starting annual salary: '))
s_raise = float(input('semi annual raise: '))
#p_save = float(input('portion of salary saved: '))
total_cost = float(input('the cost of home: '))

portion_down_payment = 0.25*total_cost

a_return = 0.04

n_mon = 36

margin = 100.0

low = 0.0

p_low = 0.0

p_high = 1.0

savings = cal_saving(a_sal, s_raise, p_high, a_return, n_mon)

if savings + margin < portion_down_payment:
    print('not possible to save enough in 3 years')

else:

    p_save = 0.5

    savings = cal_saving(a_sal, s_raise, p_save, a_return, n_mon)

    ncount = 0

    while abs(savings - portion_down_payment) > margin and p_high - p_low > 0.0001:

        if savings > portion_down_payment:
            p_high = p_save
        else:
            p_low = p_save

        p_save = (p_low + p_high)/2

        savings = cal_saving(a_sal, s_raise, p_save, a_return, n_mon)

        ncount += 1

    print('best saving rate = ', p_save)
    print('# of bisections = ', ncount)
