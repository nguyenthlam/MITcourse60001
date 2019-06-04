#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:38:39 2019

@author: lamnguyen
"""

# User input:
annual_salary = input('enter starting annual salary: ')
annual_salary = float(annual_salary)
# print(annual_salary)
portion_saved = input('portion of salary saved: ')
portion_saved = float(portion_saved)
total_cost = input('the cost of home: ')
total_cost = float(total_cost)

portion_down_payment = 0.25*total_cost
current_savings = 0.0
r = 0.04

mon = 0

monthly_salary = annual_salary/12

while current_savings < portion_down_payment:
    mon += 1
    current_savings += + current_savings*r/12
    current_savings += monthly_salary*portion_saved

print('number of months waited = ', mon)
