from pprint import pprint

temperature_in_city = {
    "city": "Москва", 
    "temperature": "20"}
pprint(temperature_in_city["city"])
temperature_in_city["temperature"] = int(temperature_in_city["temperature"]) - 5
pprint(temperature_in_city)
pprint(temperature_in_city.get("country"))
pprint(temperature_in_city.get("country", "Россия"))
temperature_in_city["date"] = "27.05.2019"
pprint(len(temperature_in_city))