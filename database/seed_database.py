"""Script to seed database."""

import os, sys, json
from datetime import datetime

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import model, server, crud
from model import db, connect_to_db
# from crud import create_month, create_holiday, create_monthly_holiday

# os.system('dropdb holidaydb')
# os.system('createdb holidaydb')

model.db.create_all()

months = ["january", 
          "february", 
          "march", 
          "april",
          "may",
          "june",
          "july",
          "august",
          "september",
          "october",
          "november",
          "december"]


""" Seed Months """
def seed_months():
        for month in months:
                crud.create_month(month)


""" Seed Daily Holidays """
def seed_daily_holidays():
    holiday_data = []
    month_num = 1

    for month in months:
        with open(f'{root_directory}/json/holidays/{month_num}-{month}.json') as m:
            month_data = json.loads(m.read())
            holiday_data.append(month_data)
        month_num += 1

    for month in holiday_data:
        for holiday in month:
            holiday_name = (holiday['holiday_name'])
            holiday_month = (holiday['holiday_month'])
            holiday_date = (holiday['holiday_date'])
            holiday_img = (holiday['holiday_img'])
            holiday_blurb = (holiday['holiday_blurb'])
            holiday_email = (holiday['holiday_email'])

            crud.create_holiday(holiday_name, 
                           holiday_month,
                           holiday_date,
                           holiday_img,
                           holiday_blurb,
                           holiday_email)
        

""" SEED MONTHLY HOLIDAYS """
def seed_monthly_holidays():
    monthly_holiday_data = []
    month_num = 1

    for month in months:
        with open(f'{root_directory}/json/monthly-holidays/{month_num}-{month}.json') as m:
            month_data = json.loads(m.read())
            monthly_holiday_data.append(month_data)
        month_num += 1

    for month in monthly_holiday_data:
        for holiday in month:
            monthly_holiday_name = (holiday['monthly_holiday_name'])
            monthly_holiday_month = (holiday['monthly_holiday_month'])

            crud.create_monthly_holiday(monthly_holiday_name, monthly_holiday_month)


seed_months()
seed_daily_holidays()
seed_monthly_holidays()