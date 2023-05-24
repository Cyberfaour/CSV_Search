import csv
import random
from datetime import datetime,timedelta

def generate_random_csv(file_path,num_rows,num_columns):
    start_date=datetime(1980,1,1)
    fieldnames=['ID','Last Name','First Name','Date of Birth']

    with open(file_path,'w',newline='')as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1,num_rows+1):
            row=[]
            for _ in range(num_columns):

                last_name=generate_random_last_name()
                first_name=generate_random_first_name()
                date_of_birth=generate_random_date_of_birth(start_date)
                
            writer.writerow({'ID': str(i), 'Last Name': last_name, 'First Name': first_name, 'Date of Birth': date_of_birth})


def generate_random_last_name():
    last_names = ['Rossi', 'Gialli', 'Verdi', 'Bianchi', 'Neri']
    return random.choice(last_names)

def generate_random_first_name():
    first_names = ['Fabio', 'Alessandro', 'Alberto', 'Marco', 'Giovanni']
    return random.choice(first_names)

def generate_random_date_of_birth(start_date):
    end_date = datetime.now() - timedelta(days=365*20)  # Generate dates for people approximately 20 years old
    random_date = random_date_between(start_date, end_date)
    return random_date.strftime('%d/%m/%Y')

def random_date_between(start_date, end_date):
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

# Usage example
csv_file_path = './test.csv'
num_rows = 10
nums_cols=4

generate_random_csv(csv_file_path, num_rows,nums_cols)