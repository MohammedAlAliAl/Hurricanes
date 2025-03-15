from collections import defaultdict
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages


def convert_damages(damages):
    damages_list = []
    for damag in damages:
        if "M" in damag:
            try:
                price = damag.split("M")
                damages_list.append(int(price[0]) * 1000000)
            except ValueError:
                damages_list.append(0)  
        elif "B" in damag:
            try:
                price = damag.split("B")
                damages_list.append(int(price[0]) * 1000000000)
            except ValueError:
                damages_list.append(0)  
        else:
            try:
                damages_list.append(int(damag))
            except ValueError:
                damages_list.append(0)  

    return damages_list

updated_damaged_list = convert_damages(damages)



def map_names_to_damages(names):
    names_damages = {}
    i = 0
    for name in names:
        names_damages[name] = updated_damaged_list[i]
        i += 1
    return names_damages


names_damages = map_names_to_damages(names)

#print(names_damages)

################################
################################
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


def max_damage(name_damage_dict):
    damage_dict = defaultdict(list)
    for name, damage in name_damage_dict.items():
        if damage == 0:
            continue
        temp_list = []
        for k, v in damage_scale.items():
            if damage < v:
                temp_list.append(k)
        if temp_list:
            rating = min(temp_list)
            damage_dict[rating].append(name)
    return damage_dict


# print(max_damage(names_damages))

##############################
##############################
# 2
# Create a Table


def table(hurricane_names):
    """
    Create a dictionary of hurricanes with their details.

    Args:
    hurricane_names (list): List of hurricane names.

    Returns:
    dict: Dictionary containing details of each hurricane.
    """
    hurricanes = {}
    for name, month, damage, year, wind, areas, death in zip(hurricane_names, months, damages, years, max_sustained_winds, areas_affected, deaths):
        hurricanes[name] = {
            "Name": name,
            "Month": month,
            "Damage": damage,
            "Year": year,
            "Max Sustained Wind": wind,
            "Areas Affected": areas,
            "Deaths": death
        }
    return hurricanes


hurricane_dictionary = table(names)
# print(hurricane_dictionary)


# Create and view the hurricanes dictionary
def area_count(locations):
    areas = {}

    for list in locations:
        for location in list:
            if location in areas:
                tem_pop = areas.pop(location)
                areas[location] = tem_pop + 1
            if location not in areas:
                areas[location] = 1
    # print(areas)


# area_count(areas_affected)

# 3
# create a new dictionary of hurricanes with year and key
def organized_by_year(hurricanes_dic):
    h_year_dic = {}
    for value in hurricanes_dic.values():
        current_year = value["Year"]
        current_cane = []
        if current_year in h_year_dic:
            temp_pop = h_year_dic.pop(current_year)

            current_cane.append(value)
            current_cane.append(temp_pop)
            h_year_dic[current_year] = current_cane

        if current_year not in h_year_dic:
            current_cane.append(value)
            h_year_dic[current_year] = current_cane
    return h_year_dic


year_dictionary = organized_by_year(hurricane_dictionary)
# print(year_dictionary)


# 6
# Calculating Maximum Hurricane Count
def counting(max_hurricanes_num):
    count = 0
    for hurricanes in max_hurricanes_num:
        count += 1
    print(count)


# counting(names)

# find most frequently affected area and the number of hurricanes involved in


def affected_area(hurricanes_dictionary):
    location_dict = {}
    for value in hurricanes_dictionary.values():
        affected_areas = value["Areas Affected"]

        for location in affected_areas:
            if location not in location_dict:
                location_dict[location] = 1

            if location in location_dict:
                tem_pop = location_dict.pop(location)
                location_dict[location] = tem_pop + 1
    return location_dict


affected_areas = affected_area(hurricane_dictionary)
# print(affected_areas)


def max(affected_areas):
    most_affected = [1, []]
    for key, value in affected_areas.items():
        if value not in most_affected and value > most_affected[0]:
            most_affected[0] = value
            most_affected[1] = key
    print(most_affected)

# max(affected_areas)


#
# find highest mortality hurricane and the number of deaths


def find_greatest_no_of_deaths(h_dictionary):
    most_deaths = [-1, []]
    # print(h_dictionary)
    for name, h_data in h_dictionary.items():

        if h_data["Death"] not in most_deaths:
            if h_data["Death"] > most_deaths[0]:
                most_deaths[0] = h_data["Death"]
                most_deaths[1] = [name]
            elif h_data["Death"] == most_deaths[0]:
                most_deaths[0] = h_data["Death"]
                most_deaths[1].append(name)
    return most_deaths


hurricanes_news = find_greatest_no_of_deaths(hurricane_dictionary)
# print(hurricanes_news)


# 8
# Rating Hurricanes by Mortality
def hurricanes_rated_by_mortality(hurricane_dictionary):
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: []}
    for key, value in hurricane_dictionary.items():

        if value["Death"] == 0:
            hurricanes_by_mortality[0] = value["Name"]

        if value["Death"] >= 100 and value["Death"] < 500:
            names = value["Name"]
            hurricanes_by_mortality[1] += [names]

        if value["Death"] >= 500 and value["Death"] < 1000:
            names = value["Name"]
            hurricanes_by_mortality[2] += [names]

        if value["Death"] >= 1000 and value["Death"] < 10000:
            names = value["Name"]
            hurricanes_by_mortality[3] += [names]
        if value["Death"] >= 10000:
            names = value["Name"]
            hurricanes_by_mortality[4] += [names]

    print(hurricanes_by_mortality)


# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_rated_by_mortality(hurricane_dictionary)


# 8 Calculating Hurricane Maximum Damage
def hurricane_max_damage(hurricane_dictionary):
    for value in hurricane_dictionary.values():
        if "M" in value["Damage"] and "Damages not recorded" in value["Damage"]:
            damage_in_million = value["Damage"].replace("M", "000000")
            print(damage_in_million)
        if "B" in value["Damage"]:
            damage_in_billion = value["Damage"].replace("B", "00000000")
            print(damage_in_billion)

    #  if "Damages not recorded" in value["Damage"]:
    #    return value["Damage"]
# hurricane_max_damage(hurricane_dictionary)


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
