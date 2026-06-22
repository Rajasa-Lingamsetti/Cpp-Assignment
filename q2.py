# q2.py
# CS253 Assignment
# Question 2
# Name: Rajasa Lingamsetti
# Roll Number: 240596

# Recursive function to calculate raw materials
def calculate_raw_materials(item, quantity, recipes):

    # If item is not in recipes, it is already a raw material
    if item not in recipes:
        return {item: quantity}

    result = {}

    # Recursively break each component into raw materials
    for component, needed in recipes[item].items():

        # Multiply required quantity
        sub_result = calculate_raw_materials(
            component,
            quantity * needed,
            recipes
        )

        # Add quantities to final result dictionary
        for material, amount in sub_result.items():
            if material in result:
                result[material] += amount
            else:
                result[material] = amount

    return result


# Sample test
recipes = {
    "SteelSword": {
        "SteelIngot": 2,
        "LeatherGrip": 1
    },
    "SteelIngot": {
        "IronOre": 3,
        "Coal": 2
    },
    "LeatherGrip": {
        "Leather": 1,
        "String": 2
    },
    "String": {
        "PlantFibers": 3
    }
}

print(calculate_raw_materials("SteelSword", 5, recipes))