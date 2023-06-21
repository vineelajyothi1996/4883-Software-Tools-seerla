import PySimpleGUI as sg
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

def buildWeatherURL(month=None, day=None, year=None, airport=None, filter=None):

    current_month,current_day,current_year = currentDate('tuple')

    if not month:
        month = current_month
    if not day:
        day = current_day
    if not year:
        year = current_year

# Create the GUI layout using drop-down boxes for user input
layout = [
    [sg.Text('Month')], [sg.DropDown([int(i) for i in range(1, 13)], size=(10, 1))],
    [sg.Text('Day')], [sg.DropDown([int(i) for i in range(1, 32)], size=(10, 1))],
    [sg.Text('Year')], [sg.DropDown([int(i) for i in range(2000, 2024)], size=(10, 1))],
    [sg.Text('Code')], [sg.InputText(size=(10, 1))],
    [sg.Text('daily / weekly / monthly')], [sg.DropDown(['daily', 'weekly', 'monthly'], size=(10, 1))],
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

# Return the URL to pass to wunderground to get appropriate weather data
url = f"https://www.wunderground.com/history/{filter}/{code}/date/{year}-{month:02d}-{day:02d}"

def rendering(url):
        driver = webdriver.Chrome() # run ChromeDriver
        driver.get(url)                                          # load the web page from the URL
        time.sleep(3)                                            # wait for the web page to load
        render = driver.page_source                              # get the page source HTML
        driver.quit()                                            # quit ChromeDriver
        return render                                            # return the page source HTML

# Rendering function to get the page source HTML from the URL
page = rendering(url)

# Parse the HTML
soup = BeautifulSoup(page, 'html.parser')

# Find the appropriate tag that contains the weather data
history = soup.find('lib-city-history-observation')

# Find the observation table
table = history.find('table')

# Get the table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Get the table rows
rows = []
for row in table.find_all('tr'):
    row_data = [data.text.strip() for data in row.find_all('td')]
    if row_data:
        rows.append(row_data)

# Create the output table layout
output_layout = [
    [sg.Table(values=rows, headings=headers, auto_size_columns=True, display_row_numbers=True, justification='center')],
    [sg.Button('Close')]
]

# Create the output window
output_window = sg.Window('Weather Data', output_layout)

# Read events from the output window
while True:
    event, values = output_window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break

output_window.close()
