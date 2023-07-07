from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
import uvicorn
import csv

description = """🚀
## 4883 Software Tools
### Create a RESTful API using FastAPI that provides access to COVID-19 data. The API will fetch the data from a publicly available data source and expose endpoints to retrieve various statistics related to COVID-19 cases.
"""

app = FastAPI(

    description=description,

)

# Open the CSV file and populate the `db` list with all the CSV data
db = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    db = list(reader)


def get_unique_countries():
    """
    Get a list of unique countries in the dataset.
    """
    countries = set()
    for row in db:
        countries.add(row[2])
    return list(countries)


def get_unique_regions():
    """
    Get a list of unique regions in the dataset.
    """
    regions = set()
    for row in db:
        regions.add(row[3])
    return list(regions)


def filter_data(country=None, region=None, year=None):
    """
    Filter the dataset based on the provided filters.
    
    Parameters:
        country (str): Filter by country.
        region (str): Filter by region.
        year (str): Filter by year.
    
    Returns:
        filtered_data (list): Filtered dataset.
    """
    filtered_data = []
    for row in db:
        if country and row[2] != country:
            continue
        if region and row[3] != region:
            continue
        if year and row[0][:4] != year:
            continue
        filtered_data.append(row)
    return filtered_data


@app.get("/")
async def docs_redirect():
    """
    Redirect to the Swagger UI documentation page.
    """
    return RedirectResponse(url="/docs")


@app.get("/countries/")
async def get_countries():
    """
    Get a list of unique countries in the dataset.
    """
    return {"countries": get_unique_countries()}


@app.get("/regions/")
async def get_regions():
    """
    Get a list of unique regions in the dataset.
    """
    return {"regions": get_unique_regions()}


@app.get("/deaths/")
async def get_total_deaths():
    """
    Get the total number of deaths across all countries and regions.
    """
    total_deaths = sum(int(row[7]) for row in db)
    return {"total_deaths": total_deaths}


@app.get("/deaths/{year}")
async def get_total_deaths(year: str = None):
    """
    Get the total number of deaths for the given year.
    
    Parameters:
        year (str, optional): Filter by year.
    
    Returns:
        total_deaths (int): Total number of deaths.
        year (str): Year of the data.
    """
    filtered_data = filter_data(year=year)
    total_deaths = sum(int(row[7]) for row in filtered_data)
    return {"total_deaths": total_deaths, "year": year}


@app.get("/avg_deaths/{year}")
async def get_average_deaths(year: str = None):
    """
    Get the average number of deaths per country for the given year.
    
    Parameters:
        year (str, optional): Filter by year.
    
    Returns:
        average_deaths (float): Average number of deaths per country.
        year (str): Year of the data.
    """
    filtered_data = filter_data(year=year)
    total_deaths = sum(int(row[7]) for row in filtered_data)
    num_countries = len(get_unique_countries())
    average_deaths = total_deaths / num_countries
    return {"average_deaths": average_deaths, "year": year}


@app.get("/deaths_by_country/{country}")
async def get_deaths_by_country(country: str):
    """
    Get the total number of deaths for the given country.
    
    Parameters:
        country (str): Filter by country.
    
    Returns:
        total_deaths (int): Total number of deaths.
        country (str): Name of the country.
    """
    filtered_data = filter_data(country=country)
    total_deaths = sum(int(row[7]) for row in filtered_data)
    return {"total_deaths": total_deaths, "country": country}


@app.get("/deaths_by_region/{region}")
async def get_deaths_by_region(region: str):
    """
    Get the total number of deaths for the given region.
    
    Parameters:
        region (str): Filter by region.
    
    Returns:
        total_deaths (int): Total number of deaths.
        region (str): Name of the region.
    """
    filtered_data = filter_data(region=region)
    total_deaths = sum(int(row[7]) for row in filtered_data)
    return {"total_deaths": total_deaths, "region": region}


@app.get("/deaths_by_country_year/{country}/{year}")
async def get_deaths_by_country_year(country: str, year: str):
    """
    Get the total number of deaths for the given country and year.
    
    Parameters:
        country (str): Filter by country.
        year (str): Filter by year.
    
    Returns:
        total_deaths (int): Total number of deaths.
        country (str): Name of the country.
        year (str): Year of the data.
    """
    filtered_data = filter_data(country=country, year=year)
    total_deaths = sum(int(row[7]) for row in filtered_data)
    return {"total_deaths": total_deaths, "country": country, "year": year}


@app.get("/deaths_by_region_year/{region}/{year}")
async def get_deaths_by_region_year(region: str, year: str):
    """
    Get the total number of deaths for the given region and year.
    
    Parameters:
        region (str): Filter by region.
        year (str): Filter by year.
    
    Returns:
        total_deaths (int): Total number of deaths.
        region (str): Name of the region.
        year (str): Year of the data.
    """
    filtered_data = filter_data(region=region, year=year)
    total_deaths = sum(int(row[7]) for row in filtered_data)
    return {"total_deaths": total_deaths, "region": region, "year": year}


@app.get("/cases/")
async def get_total_cases():
    """
    Get the total number of cases across all countries and regions.
    """
    total_cases = sum(int(row[5]) for row in db)
    return {"total_cases": total_cases}


@app.get("/cases/{year}")
async def get_total_cases(year: str = None):
    """
    Get the total number of cases for the given year.
    
    Parameters:
        year (str, optional): Filter by year.
    
    Returns:
        total_cases (int): Total number of cases.
        year (str): Year of the data.
    """
    filtered_data = filter_data(year=year)
    total_cases = sum(int(row[5]) for row in filtered_data)
    return {"total_cases": total_cases, "year": year}


@app.get("/avg_cases/{year}")
async def get_average_cases(year: str = None):
    """
    Get the average number of cases per country for the given year.
    
    Parameters:
        year (str, optional): Filter by year.
    
    Returns:
        average_cases (float): Average number of casesper country.
        year (str): Year of the data.
    """
    filtered_data = filter_data(year=year)
    total_cases = sum(int(row[5]) for row in filtered_data)
    num_countries = len(get_unique_countries())
    average_cases = total_cases / num_countries
    return {"average_cases": average_cases, "year": year}


@app.get("/cases_by_country/{country}")
async def get_cases_by_country(country: str):
    """
    Get the total number of cases for the given country.
    
    Parameters:
        country (str): Filter by country.
    
    Returns:
        total_cases (int): Total number of cases.
        country (str): Name of the country.
    """
    filtered_data = filter_data(country=country)
    total_cases = sum(int(row[5]) for row in filtered_data)
    return {"total_cases": total_cases, "country": country}


@app.get("/cases_by_region/{region}")
async def get_cases_by_region(region: str):
    """
    Get the total number of cases for the given region.
    
    Parameters:
        region (str): Filter by region.
    
    Returns:
        total_cases (int): Total number of cases.
        region (str): Name of the region.
    """
    filtered_data = filter_data(region=region)
    total_cases = sum(int(row[5]) for row in filtered_data)
    return {"total_cases": total_cases, "region": region}


@app.get("/cases_by_country_year/{country}/{year}")
async def get_cases_by_country_year(country: str, year: str):
    """
    Get the total number of cases for the given country and year.
    
    Parameters:
        country (str): Filter by country.
        year (str): Filter by year.
    
    Returns:
        total_cases (int): Total number of cases.
        country (str): Name of the country.
        year (str): Year of the data.
    """
    filtered_data = filter_data(country=country, year=year)
    total_cases = sum(int(row[5]) for row in filtered_data)
    return {"total_cases": total_cases, "country": country, "year": year}


@app.get("/cases_by_region_year/{region}/{year}")
async def get_cases_by_region_year(region: str, year: str):
    """
    Get the total number of cases for the given region and year.
    
    Parameters:
        region (str): Filter by region.
        year (str): Filter by year.
    
    Returns:
        total_cases (int): Total number of cases.
        region (str): Name of the region.
        year (str): Year of the data.
    """
    filtered_data = filter_data(region=region, year=year)
    total_cases = sum(int(row[5]) for row in filtered_data)
    return {"total_cases": total_cases, "region": region, "year": year}


@app.get("/min_deaths/")
async def get_min_deaths():
    """
    Get the country with the minimum number of deaths across all years.
    """
    countries = get_unique_countries()
    min_deaths_country = None
    min_deaths = float('inf')  # Initialize with a very large number
    
    for country in countries:
        filtered_data = filter_data(country=country)
        total_deaths = sum(int(row[7]) for row in filtered_data)
        
        if total_deaths < min_deaths:
            min_deaths = total_deaths
            min_deaths_country = country
    
    return {"min_deaths_country": min_deaths_country, "total_deaths": min_deaths}


@app.get("/max_deaths/")
async def get_max_deaths():
    """
    Get the country with the maximum number of deaths across all years.
    """
    countries = get_unique_countries()
    max_deaths_country = None
    max_deaths = 0  # Initialize with 0
    
    for country in countries:
        filtered_data = filter_data(country=country)
        total_deaths = sum(int(row[7]) for row in filtered_data)
        
        if total_deaths > max_deaths:
            max_deaths = total_deaths
            max_deaths_country = country
    
    return {"max_deaths_country": max_deaths_country, "total_deaths": max_deaths}


@app.get("/min_deaths/{min_date}/{max_date}")
async def get_min_deaths(min_date: str = None, max_date: str = None):
    """
    Get the country with the minimum number of deaths within the specified date range.
    
    Parameters:
        min_date (str, optional): Minimum date for filtering.
        max_date (str, optional): Maximum date for filtering.
    """
    countries = get_unique_countries()
    min_deaths_country = None
    min_deaths = float('inf')  # Initialize with a very large number
    
    for country in countries:
        filtered_data = filter_data(country=country)
        
        # Apply date range filtering
        if min_date:
            filtered_data = [row for row in filtered_data if row[0] >= min_date]
        if max_date:
            filtered_data = [row for row in filtered_data if row[0] <= max_date]
        
        total_deaths = sum(int(row[7]) for row in filtered_data)
        
        if total_deaths < min_deaths:
            min_deaths = total_deaths
            min_deaths_country = country
    
    return {"min_deaths_country": min_deaths_country, "total_deaths": min_deaths}


@app.get("/max_deaths/{min_date}/{max_date}")
async def get_max_deaths(min_date: str = None, max_date: str = None):
    """
    Get the country with the maximum number of deaths within the specified date range.
    
    Parameters:
        min_date (str, optional): Minimum date for filtering.
        max_date (str, optional): Maximum date for filtering.
    """
    countries = get_unique_countries()
    max_deaths_country = None
    max_deaths = float('-inf')  # Initialize with a very small number
    
    for country in countries:
        filtered_data = filter_data(country=country)
        
        # Apply date range filtering
        if min_date:
            filtered_data = [row for row in filtered_data if row[0] >= min_date]
        if max_date:
            filtered_data = [row for row in filtered_data if row[0] <= max_date]
        
        total_deaths = sum(int(row[7]) for row in filtered_data)
        
        if total_deaths > max_deaths:
            max_deaths = total_deaths
            max_deaths_country = country
    
    return {"max_deaths_country": max_deaths_country, "total_deaths": max_deaths}


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="debug", reload=True)
