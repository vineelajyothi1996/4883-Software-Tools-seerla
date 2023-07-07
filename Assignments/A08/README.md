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


