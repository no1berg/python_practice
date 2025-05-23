# 3. In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year.
#
#    Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.
#
#    For example, the key `1932` would yield the value: `[{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United States'], 'Damage': 'Damage not recorded', 'Deaths': 16}, {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}]`.
#
#    Test your function on your hurricane dictionary.

# In[291]:


# names of hurricanes
names = [
    "Cuba I",
    "San Felipe II Okeechobee",
    "Bahamas",
    "Cuba II",
    "CubaBrownsville",
    "Tampico",
    "Labor Day",
    "New England",
    "Carol",
    "Janet",
    "Carla",
    "Hattie",
    "Beulah",
    "Camille",
    "Edith",
    "Anita",
    "David",
    "Allen",
    "Gilbert",
    "Hugo",
    "Andrew",
    "Mitch",
    "Isabel",
    "Ivan",
    "Emily",
    "Katrina",
    "Rita",
    "Wilma",
    "Dean",
    "Felix",
    "Matthew",
    "Irma",
    "Maria",
    "Michael",
]

# months of hurricanes
months = [
    "October",
    "September",
    "September",
    "November",
    "August",
    "September",
    "September",
    "September",
    "September",
    "September",
    "September",
    "October",
    "September",
    "August",
    "September",
    "September",
    "August",
    "August",
    "September",
    "September",
    "August",
    "October",
    "September",
    "September",
    "July",
    "August",
    "September",
    "October",
    "August",
    "September",
    "October",
    "September",
    "September",
    "October",
]

# years of hurricanes
years = [
    1924,
    1928,
    1932,
    1932,
    1933,
    1933,
    1935,
    1938,
    1953,
    1955,
    1961,
    1961,
    1967,
    1969,
    1971,
    1977,
    1979,
    1980,
    1988,
    1989,
    1992,
    1998,
    2003,
    2004,
    2005,
    2005,
    2005,
    2005,
    2007,
    2007,
    2016,
    2017,
    2017,
    2018,
]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [
    165,
    160,
    160,
    175,
    160,
    160,
    185,
    160,
    160,
    175,
    175,
    160,
    160,
    175,
    160,
    175,
    175,
    190,
    185,
    160,
    175,
    180,
    165,
    165,
    160,
    175,
    180,
    185,
    175,
    175,
    165,
    180,
    175,
    160,
]

# areas affected by each hurricane
areas_affected = [
    ["Central America", "Mexico", "Cuba", "Florida", "The Bahamas"],
    ["Lesser Antilles", "The Bahamas", "United States East Coast", "Atlantic Canada"],
    ["The Bahamas", "Northeastern United States"],
    ["Lesser Antilles", "Jamaica", "Cayman Islands", "Cuba", "The Bahamas", "Bermuda"],
    ["The Bahamas", "Cuba", "Florida", "Texas", "Tamaulipas"],
    ["Jamaica", "Yucatn Peninsula"],
    ["The Bahamas", "Florida", "Georgia", "The Carolinas", "Virginia"],
    ["Southeastern United States", "Northeastern United States", "Southwestern Quebec"],
    ["Bermuda", "New England", "Atlantic Canada"],
    ["Lesser Antilles", "Central America"],
    ["Texas", "Louisiana", "Midwestern United States"],
    ["Central America"],
    ["The Caribbean", "Mexico", "Texas"],
    ["Cuba", "United States Gulf Coast"],
    ["The Caribbean", "Central America", "Mexico", "United States Gulf Coast"],
    ["Mexico"],
    ["The Caribbean", "United States East coast"],
    ["The Caribbean", "Yucatn Peninsula", "Mexico", "South Texas"],
    ["Jamaica", "Venezuela", "Central America", "Hispaniola", "Mexico"],
    ["The Caribbean", "United States East Coast"],
    ["The Bahamas", "Florida", "United States Gulf Coast"],
    ["Central America", "Yucatn Peninsula", "South Florida"],
    ["Greater Antilles", "Bahamas", "Eastern United States", "Ontario"],
    ["The Caribbean", "Venezuela", "United States Gulf Coast"],
    ["Windward Islands", "Jamaica", "Mexico", "Texas"],
    ["Bahamas", "United States Gulf Coast"],
    ["Cuba", "United States Gulf Coast"],
    ["Greater Antilles", "Central America", "Florida"],
    ["The Caribbean", "Central America"],
    ["Nicaragua", "Honduras"],
    [
        "Antilles",
        "Venezuela",
        "Colombia",
        "United States East Coast",
        "Atlantic Canada",
    ],
    [
        "Cape Verde",
        "The Caribbean",
        "British Virgin Islands",
        "U.S. Virgin Islands",
        "Cuba",
        "Florida",
    ],
    [
        "Lesser Antilles",
        "Virgin Islands",
        "Puerto Rico",
        "Dominican Republic",
        "Turks and Caicos Islands",
    ],
    ["Central America", "United States Gulf Coast (especially Florida Panhandle)"],
]

# damages (USD($)) of hurricanes
damages = [
    "Damages not recorded",
    "100M",
    "Damages not recorded",
    "40M",
    "27.9M",
    "5M",
    "Damages not recorded",
    "306M",
    "2M",
    "65.8M",
    "326M",
    "60.3M",
    "208M",
    "1.42B",
    "25.4M",
    "Damages not recorded",
    "1.54B",
    "1.24B",
    "7.1B",
    "10B",
    "26.5B",
    "6.2B",
    "5.37B",
    "23.3B",
    "1.01B",
    "125B",
    "12B",
    "29.4B",
    "1.76B",
    "720M",
    "15.1B",
    "64.8B",
    "91.6B",
    "25.1B",
]

# deaths for each hurricane
deaths = [
    90,
    4000,
    16,
    3103,
    179,
    184,
    408,
    682,
    5,
    1023,
    43,
    319,
    688,
    259,
    37,
    11,
    2068,
    269,
    318,
    107,
    65,
    19325,
    51,
    124,
    17,
    1836,
    125,
    87,
    45,
    133,
    603,
    138,
    3057,
    74,
]
# 1
# Update Recorded Damages
conversion = {"M": 1000000, "B": 1000000000}


# Function to convert damages from custom format into floats
def custom_to_float(custom_list):
    updated_list = []
    for record in custom_list:
        if record == "Damages not recorded":
            updated_list.append(record)
        else:
            record_converted = float(record[:-1]) * conversion[record[-1]]
            updated_list.append(record_converted)
    return updated_list


# test function by updating damages
damages = custom_to_float(damages)


# 2
# Create a Table
def dict_constructor(
    names, months, years, max_sustained_winds, areas_affected, damages, deaths
):
    main_dict = {}
    index = 0
    for name in names:
        main_dict[name] = {
            "Name": name,
            "Month": months[index],
            "Year": years[index],
            "Max Sustained Wind": max_sustained_winds[index],
            "Areas Affected": areas_affected[index],
            "Damage": damages[index],
            "Deaths": deaths[index],
        }
        index += 1
    return main_dict


# Create and view the hurricanes dictionary
hurricane_data = dict_constructor(
    names, months, years, max_sustained_winds, areas_affected, damages, deaths
)


# 3
# Organizing by Year
# Function that constructs a dict with years as the key and the values are the a list of old dict per year
##def testing_dict():


## OLD CODE
##    dict_test = {}
##
##    last_entry = 0
##    for entry, rest in hurricane_data.items():
##        tmp_list = []
##        tmp_list.append(rest)
##        # if the year was added previously, append it to rest and overwrite
##        if hurricane_data[entry].get("Year") == last_entry:
##            tmp_list.append(previous_rest)
##        dict_test[hurricane_data[entry].get("Year")] = tmp_list
##        last_entry = hurricane_data[entry].get("Year")
##        previous_rest = rest
##    return dict_test
##print(testing_dict())


# Better implementation
def create_hurricane_dict_by_year(data):
    hurricane_by_year = {}
    # Assuming data in the format {'Name1: {'Year': Y, ...}}
    for hurricane_details in data.values():  # Iterate directly through detail dicts
        year = hurricane_details.get("Year")
        if year is None:  # Skip year if key is missing
            continue

        if year not in hurricane_by_year:
            hurricane_by_year[year] = []  # Create a new list if year is first seen

        hurricane_by_year[year].append(hurricane_details)  # Append current details

    return hurricane_by_year


print(create_hurricane_dict_by_year(hurricane_data))
print("\n")


# Alternative better implementation using setdefault
def create_hurricane_dict_by_year_set_default(data):
    hurricanes_by_year = {}
    for hurricane_details in data.values():
        year = hurricane_details.get("Year")
        if year is None:
            continue
        # setdefault gets the list if the key exists, or creates an empty list if not,
        # then appends to that list
        hurricanes_by_year.setdefault(year, []).append(hurricane_details)
    return hurricanes_by_year


print(create_hurricane_dict_by_year_set_default(hurricane_data))
print("\n")


# Implementation using collections.defaultdict (Most pythonic)
import collections


def create_hurricane_dict_by_year_defaultdict(data):
    # defaultdict(list) automatically creates an empty list,
    # the first time a key is accessed that doesn't exist
    hurricane_by_year = collections.defaultdict(list)

    for hurricane_details in data.values():
        year = hurricane_details.get("Year")
        if year is None:
            continue
        hurricane_by_year[year].append(hurricane_details)  # Append directly

    return dict(hurricane_by_year)  # Convert back to dict, if needed. Often not


create_hurricane_dict_by_year_defaultdict(hurricane_data)
