"""
This module will open the meteorite_landings_data.txt file and filter the data into two different lists where one list
contains the meteorites that weigh more than 2900000g and the other with meteorites that fell on or after 2013.
Author:Steven Sousa
version 1.0
copyright 2023
"""
import display_table
from meteor_data_class import MeteorDataEntry

file = open('meteorite_landings_data.txt')
header = file.readline()

# List to store meteor data objects
filtered_mass = []
filtered_years = []

for x in file:
    data_fields = x.strip().split('\t')

    if len(data_fields) >= 7:
        # Check if meteorite mass field isn't empty and it if it has mass > 2,900,000g
        if data_fields[4] != '' and float(data_fields[4]) > 2900000:
            meteorite = MeteorDataEntry(*data_fields)
            filtered_mass.append(meteorite)

        # Check if meteorite fell year is empty and if it fell on or after 2013
        if data_fields[6] != '' and int(data_fields[6]) >= 2013:
            meteorite = MeteorDataEntry(*data_fields)
            filtered_years.append(meteorite)

file.close()
display_table.print_filtered_mass_list(filtered_mass)
display_table.print_filtered_year_list(filtered_years)
