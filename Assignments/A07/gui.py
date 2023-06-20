import PySimpleGUI as sg
from bs4 import BeautifulSoup
from selenium import webdriver                          # used to render the web page

import time
from datetime import datetime , timedelta
import csv

def currentDate(returnType='tuple'):
    """ Get the current date and return it as a tuple, list, or dictionary.
    Args:
        returnType (str): The type of object to return.  Valid values are 'tuple', 'list', or 'dict'.
    """
    
    if returnType == 'tuple':
        return (datetime.now().month, datetime.now().day, datetime.now().year)
    elif returnType == 'list':
        return [datetime.now().month, datetime.now().day, datetime.now().year]

    return {
        'day':datetime.now().day,
        'month':datetime.now().month,
        'year':datetime.now().year
    }

def buildWeatherURL(month=None, day=None, year=None, airport=None, filter=None):

    current_month,current_day,current_year = currentDate('tuple')

    if not month:
        month = current_month
    if not day:
        day = current_day
    if not year:
        year = current_year

    # Create the gui's layout using drop down boxes that allow for user input without checking for valid input
    layout = [
        [sg.Text('Month')],[sg.DropDown([int(i) for i in range(1, 13)],size=(10, 1))],
        [sg.Text('Day')],[sg.DropDown([int(i) for i in range(1, 32)],size=(10, 1))],
        [sg.Text('Year')],[sg.DropDown([int(i) for i in range(2000, 2024)],size=(10, 1))],
        [sg.Text('Code')],[sg.InputText(size=(10, 1))],
        [sg.Text('daily / weekly / monthly')],[sg.DropDown(['daily', 'weekly', 'monthly'],
                                     size=(10, 1))],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Get The Weather', layout)

    event, values = window.read()
    window.close()

    month = values[0]
    day = values[1]
    year = values[2]
    code = values[3]
    filter = values[4]

    sg.popup('You entered', f"Month: {month}, Day: {day}, Year: {year}, Code: {code}, Filter: {filter}")

    # return the URL to pass to wunderground to get appropriate weather data
    return f"https://www.wunderground.com/history/{filter}/{code}/date/{year}-{month:02d}-{day:02d}"


def rendering(url):
        driver = webdriver.Chrome() # run ChromeDriver
        driver.get(url)                                          # load the web page from the URL
        time.sleep(3)                                            # wait for the web page to load
        render = driver.page_source                              # get the page source HTML
        driver.quit()                                            # quit ChromeDriver
        return render                                            # return the page source HTML

url = buildWeatherURL()
html = rendering(url)
html_soup = BeautifulSoup(html, "html.parser")
soup_container = html_soup.find('lib-city-history-summary')
soup_data = soup_container.find_all('tbody', class_='ng-star-inserted')

outfile = "weather_data.csv"

with open(outfile, 'w') as f:
    # Write column headers for each parameter into the file for later use
    f.write('date,'
            'Actual High Temp,'
            'Historic Avg High Temp,'
            'Record High Temp,'
            'Actual Low Temp,'
            'Historic Avg Low Temp,'
            'Record Low Temp,'
            'Actual Avg Temp,'
            'Historic Avg Avg Temp,'
            'Record Avg Temp,'
            'Actual Precipitation,'
            'Historic Avg Precipitation,'
            'Record Precipitation\n')

    start_date = datetime.strptime(f"{url[-10:]}", "%Y-%m-%d")
    result = []

    for i, dat in enumerate(soup_data):
        # Loops through High Temp, Low Temp, etc.
        for j, d in enumerate(dat.find_all('tr', class_='ng-star-inserted')):
            # Loops through Actual, Historic Avg., Record
            for k in d.find_all('td', class_='ng-star-inserted'):
                tmp = k.text
                tmp = tmp.strip('  ')  # Remove any extra spaces
                result.append(tmp)

    # Write the observation date into the file
    f.write('{}-{}-{},'.format(start_date.year, start_date.month, start_date.day))
    # Write just the temperature and precipitation data into the file
    f.write(','.join(result[:12]))
    # New line, in case you want to append more rows to the same file later on
    f.write('\n')

    
    # Read the data from the output file
data = []
with open(outfile, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

# Create the layout for the output table
layout = [
    [sg.Table(values=data[1:], headings=data[0], auto_size_columns=True, display_row_numbers=True, justification='center')],
    [sg.Button('Close')]
]

# Create the window
window = sg.Window('Weather Data', layout)
    
event, values = window.read()
event == sg.WINDOW_CLOSED or event == 'Close'

window.close()
