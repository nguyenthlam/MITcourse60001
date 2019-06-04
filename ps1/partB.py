#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:38:39 2019

@author: lamnguyen
"""

# User input:
annual_salary = float(input('enter starting annual salary: '))
semi_annual_raise = float(input('semi annual raise: '))
portion_saved = float(input('portion of salary saved: '))
total_cost = float(input('the cost of home: '))

portion_down_payment = 0.25*total_cost
current_savings = 0.0
r = 0.04

mon = 0

monthly_salary = annual_salary/12

while current_savings < portion_down_payment:
    mon += 1
    current_savings += + current_savings*r/12
    current_savings += monthly_salary*portion_saved

    if mon % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise

print('number of months waited = ', mon)
