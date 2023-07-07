### A08 - Fast Api with Covid Data
### VINEELA SEERLA
### Description:

Create a RESTful API using FastAPI that provides access to COVID-19 data.
The API will fetch the data from a publicly available data source and expose endpoints to retrieve various statistics related to COVID-19 cases.

### Files

|   #   | File                  | Description                                        |
| :---: | :-------------------- | -------------------------------------------------- |
|   1   | [api.py](api.py)      | Main driver of my project that launches game.      |
|   2   | [data.csv](data.csv)  | Helper class that holds movement functions         |


### Instructions

- Install libraries- unicorn, fastapi, rich.
- Run api.py file/ Use command: uvicorn api.app --reload 
- copy the URL(http://127.0.0.1:8000) and use browser to invoke.
- click on try it out on which endpoint you want to access
- Insert valid input parameters and execute.

### OUTPUT
### BASE URL: http://127.0.0.1:8000
### Route: /deaths
Get the total number of deaths across all countries and regions.
URL: http://127.0.0.1:8000/deaths/
# RESPONSE: 
{
  "total_deaths": 5158501455
}

### A08 - Fast Api with Covid Data
### VINEELA SEERLA
### Description:

Create a RESTful API using FastAPI that provides access to COVID-19 data.
The API will fetch the data from a publicly available data source and expose endpoints to retrieve various statistics related to COVID-19 cases.

### Files

|   #   | File                  | Description                                        |
| :---: | :-------------------- | -------------------------------------------------- |
|   1   | [api.py](api.py)      | Main driver of my project that launches game.      |
|   2   | [data.csv](data.csv)  | Helper class that holds movement functions         |


### Instructions

- Install libraries- unicorn, fastapi, rich.
- Run api.py file/ Use command: uvicorn api.app --reload 
- copy the URL(http://127.0.0.1:8000) and use browser to invoke.
- click on try it out on which endpoint you want to access
- Insert valid input parameters and execute.

### OUTPUT
### BASE URL: http://127.0.0.1:8000
### Route: /deaths
Get the total number of deaths across all countries and regions.
URL: http://127.0.0.1:8000/deaths/
# RESPONSE: 
{
  "total_deaths": 5158501455
}


### A08 - Fast Api with Covid Data
### VINEELA SEERLA
### Description:

Create a RESTful API using FastAPI that provides access to COVID-19 data.
The API will fetch the data from a publicly available data source and expose endpoints to retrieve various statistics related to COVID-19 cases.

### Files

|   #   | File                  | Description                                        |
| :---: | :-------------------- | -------------------------------------------------- |
|   1   | [api.py](api.py)      | Main driver of my project that launches game.      |
|   2   | [data.csv](data.csv)  | Helper class that holds movement functions         |


### Instructions

- Install libraries- unicorn, fastapi, rich.
- Run api.py file/ Use command: uvicorn api.app --reload 
- copy the URL(http://127.0.0.1:8000) and use browser to invoke.
- click on try it out on which endpoint you want to access
- Insert valid input parameters and execute.

### OUTPUT
### BASE URL: http://127.0.0.1:8000
### Route: /deaths
Get the total number of deaths across all countries and regions.
URL: http://127.0.0.1:8000/deaths/
### RESPONSE: 
{
  "total_deaths": 5158501455
}

### Route: /deaths/{year}
Get the total number of deaths for the given year.
Parameters: year (str, optional): Filter by year.
Returns: total_deaths (int): Total number of deaths. year (str): Year of the data.

URL: [http://127.0.0.1:8000/deaths/](http://127.0.0.1:8000/deaths/2020)
### RESPONSE: 
{
  "total_deaths": 243435399,
  "year": "2020"
}

### Route: /avg_deaths/{year}
Get the average number of deaths per country for the given year.
Parameters: year (str, optional): Filter by year.
Returns: average_deaths (float): Average number of deaths per country. year (str): Year of the data.

URL: http://127.0.0.1:8000/avg_deaths/2021
### RESPONSE: 
{
  "average_deaths": 6021470.354430379,
  "year": "2021"
}

### Route: /deaths_by_country/{country}
Get the total number of deaths for the given country.
Parameters: country (str): Filter by country.
Returns: total_deaths (int): Total number of deaths. country (str): Name of the country.

URL: http://127.0.0.1:8000/deaths_by_country/Afghanistan
### RESPONSE: 
{
  "total_deaths": 6239328,
  "country": "Afghanistan"
}

### Route: /deaths_by_region/{region}
Get the total number of deaths for the given region.
Parameters: region (str): Filter by region.
Returns: total_deaths (int): Total number of deaths. region (str): Name of the region.

URL: http://127.0.0.1:8000/deaths_by_region/AMRO
### RESPONSE: 
{
  "total_deaths": 2307805539,
  "region": "AMRO"
}

### Route: /deaths_by_country_yearn/{country}/{year}
Get the total number of deaths for the given country and year.
Parameters: country (str): Filter by country. year (str): Filter by year.
Returns: total_deaths (int): Total number of deaths. country (str): Name of the country. year (str): Year of the data.

URL: http://127.0.0.1:8000/deaths_by_country_year/Afghanistan/2023
### RESPONSE: 
{
  "total_deaths": 1356418,
  "country": "Afghanistan",
  "year": "2023"
}

### Route: /deaths_by_country_yearn/{region}/{year}
Get the total number of deaths for the given region and year.
Parameters: region (str): Filter by region. year (str): Filter by year.
Returns: total_deaths (int): Total number of deaths. region (str): Name of the region. year (str): Year of the data.

URL: http://127.0.0.1:8000/deaths_by_region_year/EMRO/2020
### RESPONSE: 
{
  "total_deaths": 13501765,
  "region": "EMRO",
  "year": "2020"
}

### Route: /cases_by_country_yearn/{region}/{year}
Get the total number of cases for the given region and year.
Parameters: region (str): Filter by region. year (str): Filter by year.
Returns: total_cases (int): Total number of cases. region (str): Name of the region. year (str): Year of the data.

URL: http://127.0.0.1:8000/cases_by_region_year/AMRO/2020
### RESPONSE: 
{
  "total_cases": 3509057698,
  "region": "AMRO",
  "year": "2020"
}
