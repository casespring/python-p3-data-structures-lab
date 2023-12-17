spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [spicy['name'] for spicy in spicy_foods ]

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for spicy in spicy_foods:
        if spicy['heat_level'] > 5:
            spiciest_foods.append(spicy)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for spicy in spicy_foods:
        print(f'{spicy["name"]} ({spicy["cuisine"]}) | Heat Level: {"🌶" * spicy["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy in spicy_foods:
            if spicy['cuisine'] == cuisine:
                return spicy

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
    

def get_average_heat_level(spicy_foods):
    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods