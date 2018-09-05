############################################################
#Project 7
#Asks user to input three files
#Reads three files
#Asks user if they want to display data and displays data
#Displays the top ten countries
#Asks user if they want to plot data and plots data
############################################################


import csv
import pylab
from operator import itemgetter

def open_file(message):
    '''prompts user to enter a file name, opens the file and returns it. 
    If there is an error it tells the user then prompts for another filename.'''
    filename = input(message)
    while filename != ' ':
        try:
            fo = open(filename, 'r', encoding="UTF-8") #file operator
            return fo
            break
        except FileNotFoundError:
            print("File is not found! Try Again!") 
            filename = input(message)
    #pass
            

# 1.2.3.4 --> 001002003004
def zfillip(ip):
    '''allows user to enter a list and then applies the 
    zfill function to each value and returns the list as a string'''
    string = ""
    ip = ip.split('.') 
    for value in ip:    #applies z fill to each value in the list
        value = value.zfill(3)
        string += value
    return string
    
def read_ip_location(file):
    '''takes opened file and returns a list of three tuple
    items with the start ip address, end ip address, and country code. '''
    data_list = [] #list with start ip address, end ip address, and country code for items in file
    for line in file:   #finds start ip end ip and country code for each line in the file
        line = line.strip()
        line = line.split(',')
        start_ip = zfillip(line[0]) #start ip address
        end_ip = zfillip(line[1])  #end ip address
        country_code = line[2]    #country code     
        tup =  (int(start_ip),int(end_ip),country_code)
        data_list.append(tup)
    return data_list
    
def read_ip_attack(file):
    '''takes opened file and returns a list of tuples which 
    has the ip address with xxx at the end or with zeros '''
    data = []  #list of tuples with two ip addresses
    for line in file:   #goes through each line in file and adjusts the ip addresses
        new_value = line.strip()
        line = line.strip()
        add = '.xxx'
        line = line + add  #ip address with xxx 
        new_value = zfillip(new_value) 
        add1 = '000'
        new_value = new_value + add1 #ip address with zeros
        tuple1 =(int(new_value) , line)
        data.append(tuple1)
    return data
    
        
        
    #pass

def read_country_name(file):
    '''takes opened file and returns a list of two tuples of 
    the country code and the full name of the country '''
    data1 = [] #list of two tuples country code and name
    for line in file:   #gives country name and country code for each line in the file
        line = line.strip()
        line = line.split(';')
        country_name = line[0]  #full name of the country
        country_code = line[1] #country code
        tup1 = (country_code, country_name)
        data1.append(tup1)
    return data1
    #pass
    
def locate_address(ip_list, ip_attack):
    '''takes a list of ip addresses and a specific ip attack and 
    searches for the attack in the list of ip address, returns 
    the country code'''
    for i in ip_list:   #returns country code associated with the ip address
        if ip_attack >= i[0] and ip_attack <= i[1]:
            return i[2]  #country code
    #pass

def get_country_name(country_list, code):
    '''takes a list of countries and a specific country code and returns
    the country name corresponding with the code '''
    for i in country_list: #goes through each country code in list and returns name assoicated 
        if code == i[0]:
            return i[1]  #country name
    #pass

def bar_plot(count_list, countries):
    pylab.figure(figsize=(10,6))
    pylab.bar(list(range(len(count_list))), count_list, tick_label = countries)
    pylab.title("Countries with highest number of attacks")
    pylab.xlabel("Countries")
    pylab.ylabel("Number of attacks")
    
def main():
    '''Calls all the other functions in order to read files, ask user to display data,
    display top ten countries, and ask user to plot data'''
    file = open_file("Enter the filename for the IP Address location list: ")
    
    ip_data = read_ip_location(file)  #data in ip location file
    
    file = open_file("Enter the filename for the IP Address attacks: ")
    attack_data = read_ip_attack(file)  #data for ip attacks
    
    file = open_file("Enter the filename for the country codes: ")
    country_data = read_country_name(file)  #country data
    country_count = [] 
    unique_countries =[]
    uc_tuples = []
    for data in attack_data:
        country = locate_address(ip_data , data[0]) #country in attack data
        country_count.append(country)
        if country not in unique_countries :
            unique_countries.append(country)
        
    for unique_country in unique_countries:
        unique_country_count = country_count.count(unique_country)
        count_tup = (unique_country, unique_country_count)
        uc_tuples.append(count_tup)
    
    sorted_tuples = sorted(uc_tuples, key = itemgetter(0), reverse = True)
    sorted_tuples2 = sorted(sorted_tuples, key = itemgetter(1), reverse = True)
    tuple_count = 0
    top_ten_countries = [] #list of top ten countries
    
    for i in sorted_tuples2:
        tuple_count += 1
        top_ten_countries.append(i)
        if tuple_count == 10:
            break
        
    display_data = input("\nDo you want to display all data? ")
    display_data = display_data.lower()
    if display_data == 'yes':
        for data in attack_data:
            ip_address1 = data[1]
            country = locate_address(ip_data , data[0])
            country_name= get_country_name(country_data, country) #name of country attack came from
            print("{:14s} {:19s}{:16s}{:s}".format("The IP Address:", ip_address1,\
                  "originated from ", country_name))
      
    print("\nTop 10 Attack Countries")
    print("{:9s}{:5s}".format("Country", "Count"))
    for countries in top_ten_countries:  
        print("{:9s}{:5d}".format(countries[0], countries[1]))
        
    
    
    
    
    answer = input("\nDo you want to plot? ")
    answer = answer.lower()
    if answer == 'yes':
        count_list = []
        countries_list =[]
        for countries in top_ten_countries:
            country_count1 = str(countries[1])
            country_names = (countries[0])
            count_list.append(country_count1)
            countries_list.append(country_names)
        bar_plot(count_list, countries_list)   
        
    
if __name__ == "__main__":
    
    
   main()
  
