import requests

# Download csv from OWID github

url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
data = requests.get(url).content