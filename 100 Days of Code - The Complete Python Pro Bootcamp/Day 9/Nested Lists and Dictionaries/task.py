travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A","B",["C","D"]]

print(nested_list[2][1])

nested_list.append(travel_log)

print(nested_list)
print(nested_list[3]["France"][1])

travel_log2 = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log2["Germany"]["cities_visited"][2])
