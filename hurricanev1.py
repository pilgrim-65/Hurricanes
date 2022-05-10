from collections import defaultdict
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(dmgs):
    conversion = {"M": 1000000,
              "B": 1000000000}
    dmgs_upd = []
    for d in dmgs:
        if d == "Damages not recorded":
            dmgs_upd.append(d)
        else:
            factor = conversion[d[-1]]
            dmgs_upd.append(float(d[:-1])*factor)
    return dmgs_upd

updated_damages = update_damages(damages)

# write your construct hurricane dictionary function here:
def build_hurr_dic():
    hurricanes = dict()
    for i in range(len(names)):
        hurricanes[names[i]] = \
        {"Name": names[i],
         "Month": months[i],
         "Year": years[i],
         "Max Sustained Wind": max_sustained_winds[i],
         "Areas Affected": areas_affected[i],
         "Damage": updated_damages[i],
         "Deaths": deaths[i]}
         
    return hurricanes

hurricanes = build_hurr_dic()
# print(hurricanes)

# write your construct hurricane by year dictionary function here:
def build_years():
    years_dic = {}
    for h in hurricanes:
        current_year = hurricanes[h]['Year']
        current_cane = hurricanes[h]
        try:
            years_dic[current_year].append(current_cane)
        except KeyError:
            years_dic[current_year] = [current_cane]
    return years_dic
            
years_hurricanes =  build_years()  

# print(years_hurricanes)

# write your count affected areas function here:
def count_affected():
    af_areas = defaultdict(int)
    for h in hurricanes:
        for area in hurricanes[h]['Areas Affected']:
            af_areas[area] += 1
    return af_areas
    
areas_affected = count_affected()
# print(areas_affected)
   
# print(areas_affected)

# write your find most affected area function here:
def max_count_area():
  max_area = ''
  max_area_count = 0
  for area in areas_affected:
    if areas_affected[area] > max_area_count:
      max_area = area
      max_area_count = areas_affected[area]
  return max_area, max_area_count

max_area, max_area_count = max_count_area()
print("The most frequently affected area is: {0} with {1} hurricanes".
      format(max_area, max_area_count))

# write your greatest number of deaths function here:
    
def max_deaths_count():
    max_count = 0
    most_deadly = ''
    for h in hurricanes:
        if hurricanes[h]['Deaths'] > max_count:
            max_count = hurricanes[h]['Deaths']
            most_deadly = h
    return most_deadly, max_count

most_deadly, max_count = max_deaths_count()
print("The deadliest hurricane was {0} with {1} deaths".format(most_deadly,
                                                               max_count))

# write your categorize by mortality function here:
def mortality():
    def rate(deaths):
        mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000,4: 10000}
        rates = sorted(mortality_scale.items(),key = lambda x: x[1])
        for i in range(len(rates)):
            if deaths <= rates[i][1]: scale = rates[i][0]; return scale
        return 5 #deaths > 10000
    hurricanes_mort = defaultdict(list)
    for h in hurricanes:
        rating = rate(hurricanes[h]["Deaths"])
        hurricanes_mort[rating].append(hurricanes[h])
    return hurricanes_mort
    
hurricanes_by_mortality = mortality()

# write your greatest damage function here:
def find_max_damage():
    max_damage= 0
    greatest_damage_h =names[0]
    for h in hurricanes:
        if hurricanes[h]['Damage'] == 'Damages not recorded':
            continue
        elif hurricanes[h]['Damage'] > max_damage:
            max_damage = hurricanes[h]['Damage']
            greatest_damage_h = h
    return greatest_damage_h, max_damage
greatest_damage_hurricane, max_damage = find_max_damage()

print("The hurricane that caused the greagest damage was {0} with {1:,}  dollars".format(greatest_damage_hurricane, int(max_damage)))
    
# write your categorize by damage function here:
def rating_by_damage():
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 
                  4: 50000000000}
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    scales = sorted(damage_scale.items())
    for h in hurricanes:
        rating = 0
        if type(hurricanes[h]['Damage']) == float: 
            if hurricanes[h]['Damage'] > 50000000000:
                rating = 5
            else:
                for s in scales:
                    if hurricanes[h]['Damage'] < s[1]: 
                        rating = s[0]
                        break

        hurricanes_by_damage[rating].append(hurricanes[h])
    
    return hurricanes_by_damage

hurricanes_by_damage = rating_by_damage()
# now we print the 10 most costly hurricanes
counter = 0
print("The 10 most costly hurricanes were:")
print("{0:^8} {1:^28} {2:^10}".format('Year','Hurricane','cost'))
print("{0:^8} {1:^28} {2:^10}".format('----','---------','---------------'))
while counter < 10:
    for i in range(5,0,-1):
        for h in hurricanes_by_damage[i]:
            print("{0:^8} {1:^28} {2:>10,} M$".format(h['Year'], h['Name'],
                         int(h['Damage'])//10**6))
            counter +=1 
            if counter > 9: break
        if counter > 9: break

