
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import date

import os
os.system('cls' if os.name == 'nt' else 'clear')

url = 'http://neumont.smartcatalogiq.com/2020-2021/Catalog/Academic-Calendar-2020-2021'
page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

combined_child = soup.find(class_='combinedChild')
the_h2s = combined_child.find_all('h2')
the_tables = combined_child.find_all('table')

year, month, day = date.today().year, date.today().month, date.today().day
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

neumont_list = []
quarter_list = []
for h2 in the_h2s:        
    h2 = str(h2).split('\r')    
    quarter = h2[1].replace('\n', '')    
    quarter = quarter.replace('\t', '')    
    quarter_list.append(quarter)    
    
quarter_count = 0
for table in the_tables:    
    the_trs = table.find_all('tr')

    for tr in the_trs:
        the_tds = tr.find_all('td')

        data_list = []        
        for td in the_tds:    
            the_value = str(td)
            begin_value = the_value.index('>')
            end_value = the_value.index('<', begin_value)
            the_value = the_value[begin_value + 1 : end_value]
            data_list.append(the_value)
    
        # Calculate the date from the dates on the site
        date_year = int(quarter_list[quarter_count][-4:])
        date_parts = data_list[0].split('-')
        date_parts = date_parts[-1].lstrip().split(' ')
        if len(date_parts) < 2:
            date_month = months.index(data_list[0].split(' ')[0]) + 1
            date_day = data_list[0].split(' ')[0]
            try:
                date_day = int(date_parts[0])
            except:
                pass
        else:
            date_month = months.index(date_parts[0]) + 1
            date_day = int(date_parts[1].split('-')[0])
        
        # Only include those schedules that are occuring today or in the future
        if date_year >= year and \
            (date_month >= month or \
            (date_month == month and date_day >= day)):
            
            data_dict = {}
            data_dict['quarter'] = quarter_list[quarter_count]
            data_dict['date'] = data_list[0]
            data_dict['description'] = data_list[1]        
            neumont_list.append(data_dict)

    quarter_count += 1
    
with open('report.txt', 'w') as file:
    for d in neumont_list:
        file.writelines(f"{d['quarter']}\t\t{d['date']}:  {d['description']}\n")
        print(f"{d['quarter']}\t\t{d['date']}:   {d['description']}")




