## 1. Storing Data ##

content_ratings = ['4+', '9+', '12+', '17+']

numbers = [4433, 987, 1155, 622]

content_rating_numbers = [content_ratings, numbers]

## 2. Dictionaries ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

print(content_ratings)



## 3. Indexing ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

over_9 = content_ratings['9+']

over_17= content_ratings['17+']

print(over_9)
print(over_17)

## 4. Alternative Way of Creating a Dictionary ##

content_ratings = {}

content_ratings['4+'] = 4433
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622

over_12_n_apps = content_ratings['12+']


## 5. Key-Value Pairs ##

d_1 = {'key_1': 'first_value', 
 'key_2': 2,
 'key_3': 3.14,
 'key_4': True,
 'key_5': [4,2,1],
 'key_6': {'inner_key' : 6}
 }

error = True


## 6. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1 = '9+' in content_ratings

is_in_dictionary_2 = '987' in content_ratings

if '17+' in content_ratings:
    result = 'It exists'

print(result)

## 7. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {'4+':0,'9+':0,'12+':0,'17+':0}

for each_list in apps_data[1:]:
    c_rating = each_list[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1

print(content_ratings)

## 8. Finding the Unique Values ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {}

for each_list in apps_data[1:]:
    c_rating = each_list[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
        
print(content_ratings)

## 9. Proportions and Percentages ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = {}

for each_list in apps_data[1:]:
    genre = each_list[11]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1
        
print(genre_counting)

## 10. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for iteration_variable in content_ratings:
    content_ratings[iteration_variable] /= total_number_of_apps
    content_ratings[iteration_variable] *= 100
    
percentage_17_plus = content_ratings['17+']
percentage_15_allowed = content_ratings['4+'] + content_ratings['12+'] + content_ratings['9+']
 

## 11. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_proportions = {}
c_ratings_percentages = {}

for key in content_ratings:
    proportion = content_ratings[key] / total_number_of_apps
    percentage = proportion * 100
    c_ratings_proportions[key] = proportion
    c_ratings_percentages[key] = percentage

## 12. Frequency Tables for Numerical Columns ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = []

for each_list in apps_data[1:]:
    size = float(each_list[2])
    data_sizes.append(size)
   
min_size = min(data_sizes)
max_size = max(data_sizes)

## 13. Filtering for the Intervals ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_column = []

for each_list in apps_data[1:]:
    rating = int(each_list[5])
    data_column.append(rating)

min_column = min(data_column)
max_column = max(data_column)

print(min_column)
print(max_column)

interval_dic = {'0 - 100k': 0, '100k - 200k': 0, '200k - 300k': 0, '300k - 400k':0, 'Above 400k':0}

for each_list in apps_data[1:]:
    rating = int(each_list[5])
    if 0 < rating <= 100000:
        interval_dic['0 - 100k'] += 1
    elif 100000 < rating <= 200000:
        interval_dic['100k - 200k'] += 1
    elif 200000 < rating <= 300000:
        interval_dic['200k - 300k'] += 1
    elif 300000 < rating <= 400000:
        interval_dic['300k - 400k'] += 1
    elif 400000 < rating:
        interval_dic['Above 400k'] += 1
        
print(interval_dic)
