##################### Extra Hard Starting Project ######################
import datetime
from send_mail import send_mail
from random import choice, randint
import pandas

date = datetime.datetime.now()
month = date.month
day = date.day

data = pandas.read_csv('DAY-32\\ABW\\birthdays.csv')
contact_details = data.to_dict(orient='records')
contact_names = [contact['name'] for contact in contact_details]

due_birthdays = []
for name in contact_names:
    row_data = data[data.name == name]
    row_month = row_data['month'].iloc[0]
    row_day = row_data['day'].iloc[0]
    
    if row_month == month and row_day == day:
        due_birthdays.append(name)

for name in due_birthdays:
    with open(f'DAY-32\\ABW\\letter_templates\\letter_{randint(1, 3)}.txt') as data:
        letter = data.read()
        new_letter = letter.replace('[NAME]', name)
        send_mail(message=f"Subject:Happy Birthday!\n\n{new_letter}")

