"""
This module will open the meteorite_landings_data.txt file and allow the user to set the filters to be used by d
ata_filter.py.

Author:Steven Sousa
version 1.1
release date - October 2023
"""
import data_filter

print('Author: Steven Sousa / Version: 1.1 / Release Date: October 2023\n\n'
      'Welcome to the meteor filtering program! This program allows you to select a .txt file to filter the data by'
      'choosing either the mass of the meteorite or the year it fell on Earth and displays it neatly.\n')

file_name = input('Enter a valid file name (ex. "file_name.txt") with its file extension (if applicable) or\n'
                  'To EXIT in Windows, type ">q" or ">Q". In macOS, type ":Q" or ":q": ')

print("\nFile name: ", file_name)

if file_name.lower() in ['>q', ':q']:
    print('\nProgram is now exiting. Goodbye!')
    exit()

read_mode = input('\nFrom the list below, what mode would you like to open this file with?\n '
                  '"r" - open for reading (default)\n'
                  '"w" - open for writing, truncating the file first\n'
                  '"x" - open for exclusive creation, failing if the file already exists\n'
                  '"a" - open for writing, appending to the end of file if it exists\n'
                  '"b" - binary mode\n'
                  '"t" - text mode (default)\n'
                  '"+" - open for updating (reading and writing)\n'
                  'To EXIT in Windows, type ">q" or ">Q". In macOS, type ":Q" or ":q": ')

print('\nFile mode: ', read_mode)

if read_mode.lower() in ['>q', ':q']:
    print('\nProgram is now exiting. Goodbye!')
    exit()

filter_on = int(input('\nFrom the list below, what attribute would you like to filter the data on?\n'
                      '"1" - Meteor Mass (g)\n'
                      '"2" - The year the meteor fell to Earth\n'
                      '"3" - Quit\n'))

print("\nFilter selected: ", filter_on)

if filter_on >= 3:
    print('\nProgram is now exiting. Goodbye!')
    exit()

if filter_on == 1:
    mass_lower_limit = input("\nEnter the LOWER limit (inclusive) for the meteor's mass (g) without commas or decimal "
                             "points. (To EXIT in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if mass_lower_limit.lower() in ['>q', ':q']:
        print('\nProgram is now exiting. Goodbye!')
        exit()

    mass_upper_limit = input("Enter the UPPER limit (inclusive) for the meteor's mass (g) without commas or decimal "
                             "points. (To EXIT in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if mass_upper_limit.lower() in ['>q', ':q']:
        print('\nProgram is now exiting. Goodbye!')
        exit()

    print('\nSelected mass range (g): ', mass_lower_limit, ' - ', mass_upper_limit)
    data_filter.filter_mass(file_name, read_mode, int(mass_lower_limit), int(mass_upper_limit))

if filter_on == 2:
    year_lower_limit = input("\nIn YYYY format, enter the LOWER limit (inclusive) for the year the meteorite fell on "
                             "Earth. \nThis allows the table to display meteors from that year onward only. "
                             "(To EXIT in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if year_lower_limit.lower() in [">q", ":q"]:
        print('\nProgram is now exiting. Goodbye!')
        exit()

    year_upper_limit = input("\nIn YYYY format, enter the LOWER limit (inclusive) for the year the meteorite fell on "
                             "Earth. \nThis allows the table to display meteors from that year onward only. "
                             "(To EXIT in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if year_upper_limit.lower() in [">q", ":q"]:
        print('\nProgram is now exiting. Goodbye!')
        exit()

    data_filter.filter_year(file_name, read_mode, int(year_lower_limit), int(year_upper_limit))
