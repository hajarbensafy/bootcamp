import random

def get_random_temp(season=None):
    if season == "winter":
        return round(random.uniform(-10, 16), 1)
    elif season == "summer":
        return round(random.uniform(24, 40), 1)
    elif season == "autumn" or season == "fall":
        return round(random.uniform(16, 23), 1)
    elif season == "spring":
        return round(random.uniform(0, 16), 1)
    else:
        return round(random.uniform(-10, 40), 1)

def main():
    season = input("Enter the season (summer, autumn, winter, spring): ").lower()
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23:
        print("It's a pleasant day.")
    elif 24 <= temp < 32:
        print("It's warm outside.")
    elif 32 <= temp <= 40:
        print("It's hot! Stay hydrated.")

main()