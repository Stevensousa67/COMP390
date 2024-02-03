"""
This module will print the two lists generated by data_filter.py in an easy and elegant format.
Author:Steven Sousa
version 1.0
copyright 2023
"""

blank_label = ''
name_label = 'NAME'
mass_label = "MASS (g)"
year_label = "YEAR"


def print_filtered_mass_list(filtered_mass):
    print('Table of meteors with mass greater than 2900000g:')
    print(f'{blank_label: <5}{name_label: <24}{mass_label: <20}')
    print("=" * 60)
    for x, meteorite in enumerate(filtered_mass, 1):
        print(f'{x: < 5}{meteorite.name: <24}{meteorite.mass: <20}')


def print_filtered_year_list(filtered_year):
    print()
    print('Table of meteors that fell on or after 2013:')
    print(f'{blank_label: <5}{name_label: <24}{year_label: <20}')
    print("=" * 60)
    for x, meteorite in enumerate(filtered_year, 1):
        print(f'{x: < 5}{meteorite.name: <24}{meteorite.year: <20}')