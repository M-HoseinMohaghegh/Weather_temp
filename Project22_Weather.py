import requests

cities = [
    "Tehran", "Mashhad", "Isfahan", "Tabriz", "Shiraz", "Ahvaz", "Qom",
    "Kermanshah", "Urmia", "Rasht", "Zahedan", "Karaj", "Hamedan",
    "Arak", "Yazd", "Bandar Abbas", "Sanandaj", "Zanjan", "Kerman",
    "Birjand", "Gorgan", "Sari", "Bushehr", "Khorramabad", "Ilam",
    "Qazvin", "Bojnurd", "Semnan", "Yasuj",
    "Gonbad-e Kavus", "Mahabad"
]

API_KEY = '936e6bd36ea1c58e0845abc33742723c'


def get_weather(city_name):
    url = f"https://api.weatherstack.com/current?access_key={API_KEY}&query={city_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['temperature']
        return temperature
    else:
        return None


def main():
    while True:
        print("Hello you want to know the temperature of which city?")
        for i, city in enumerate(cities, 1):
            print(f"{i}. {city}")
        try:
            choice = int(input("import the number of the city: "))
            if 1 <= choice <= 32:
                selected_city = cities[choice - 1]
                temperature = get_weather(selected_city)
                if temperature is not None:
                    print(f"The temperature of {selected_city} is {temperature} centigrade")
                else:
                    print("No Connection")
            else:
                print("Please insert a valid number")
        except ValueError:
            print("Please insert a number.")
        out = input("Do you want to exit(Y/N)? ").lower()
        if out == "y":
            break


if __name__ == "__main__":
    main()
