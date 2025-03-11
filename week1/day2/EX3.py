#Qst1:
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

#Qst2:
brand["number_stores"] = 2
#Qst3:
print(f"Zara's clients are: {', '.join(brand['type_of_clothes'])}")
#Qst4:
brand["country_creation"] = "Spain"
#Qst5:
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
#Qst6:
del brand["creation_date"]
#Qst7:
print(f"Last international competitor: {brand['international_competitors'][-1]}")
#Qst8:
print(f"Major clothes colors in the US: {', '.join(brand['major_color']['US'])}")
#Qst9:
print(f"Number of key-value pairs: {len(brand)}")
#Qst10:
print(f"Keys of the dictionary: {', '.join(brand.keys())}")
#Qst11:
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
#Qst12:
brand.update(more_on_zara)
#Qst13:
print(f"Number of stores: {brand['number_stores']}")
