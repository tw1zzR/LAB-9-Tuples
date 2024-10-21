

orbital_r = {}
planets = ("Меркурій", "Венера", "Земля", "Марс", "Юпітер", "Сатурн", "Уран", "Нептун")

for planet in planets:
    radius = float(input(f"Введіть радіус орбіти для {planet} (в астрономічних одиницях): "))
    orbital_r[planet] = radius

def add_planet():
    new_planet = input("\nВведіть назву нової планети: ")
    radius = float(input(f"Введіть радіус орбіти для {new_planet} (в астрономічних одиницях): "))
    orbital_r[new_planet] = radius
    print(f"{new_planet} додано до словника з радіусом {radius} астрономічних одиниць.")

def search_planet():
    planet_name = input("\nВведіть назву планети для пошуку: ")
    if planet_name in orbital_r:
        print(f"Радіус орбіти для {planet_name}: {orbital_r[planet_name]} астрономічних одиниць.")
    else:
        print(f"{planet_name} не знайдено в словнику.")


while True:
    print("\nМеню:")
    print("1. Додати нову планету")
    print("2. Пошук за назвою планети")
    print("3. Вихід")

    choice = input("Виберіть дію (1/2/3): ")

    if choice == '1':
        add_planet()
    elif choice == '2':
        search_planet()
    elif choice == '3':
        print("Вихід з програми.")
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")