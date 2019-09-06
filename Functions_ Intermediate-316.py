## 1. Interfering with the Built-in Functions ##

def max(one_list):
    return "No max value returned"

a_list = [1, 8, 10, 9, 7]

max_val_test_0 = max(a_list)

print(max_val_test_0)

## 3. Default Arguments ##

# INITIAL CODE
def open_dataset(file_name="AppleStore.csv"):
    
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data

apps_data = open_dataset()

print(apps_data)

## 4. The Official Python Documentation ##

one_decimal = round(3.43, 1)

two_decimals = round(0.23321, 2)

five_decimals = round(921.2225227, 5)

## 5. Multiple Return Statements ##

# INITIAL CODE
def open_dataset(file_name='AppleStore.csv', header=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    if header == True:
        return data[1:]
    return data

apps_data = open_dataset()

## 6. Returning Multiple Variables ##

# INITIAL CODE
def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
    
all_data = open_dataset()
header = all_data[1]
apps_data = all_data[0]

## 7. More About Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
    
    header, apps_data = open_dataset()

## 8. Functions — Code Running Quirks ##

def print_constant():
    x = 3.14
    print(x)
    
print_constant()

## 9. Scopes — Global and Local ##

e = 'mathematical constant'
a_sum = 1000
length = 50

def exponential(x):
    e = 2.72
    print(e)
    return e ** x

result = exponential(5)

print(e)
    
def divide():
    print(a_sum)
    print(length)
    return a_sum / length

result_2 = divide()