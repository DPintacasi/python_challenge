#import modules
import os
import csv

emp_id = []
first_names = []
last_names = []
new_dates = []
new_ssns = []
new_states = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


with open("employee_data.csv", 'r') as employee_data_file:
    
    data = csv.reader(employee_data_file, delimiter = ",")
    data_header = next(data)

    for row in data:

        #extract employee ID number
        emp_id.append(row[0])

        #split names
        names = row[1].split(" ")
        first_names.append(names[0])
        last_names.append(names[1])

        #reformat dates
        dates = row[2].split("-")
        new_dates.append(f"{dates[1]}/{dates[2]}/{dates[0]}")

        #reformat ssn
        new_ssn = row[3][-4:]
        new_ssn = f"***-**-{new_ssn}"
        new_ssns.append(new_ssn)

        #replace state
        state = row[4]
        new_state = us_state_abbrev[state]
        new_states.append(new_state)


header = ["Emp ID", "First Name", "Last Name", "DOB",
            "SSN", "State"]

reformatted_data = zip(emp_id,first_names,last_names,new_dates,new_ssns,new_states)

with open("reformatted_employee_data.csv", "w") as output_data_file:
    
    data = csv.writer(output_data_file)
    
    data.writerow(header)
    data.writerows(reformatted_data)

