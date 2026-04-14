"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""
# Phase 1
def get_menu_options():
    menu = {}
    while True:
        print("\nType 'Q' when finished")
        category = input("Give category for this part of menu: ").strip().upper()

        if category == "Q":
            break

        items = input(f"Enter items for {category} (seperated by commas): ").strip().upper()
        menu[category] = items
    return menu

def save_to_file(menu):
    with open("menu_config.txt", "w") as file:
        for category, items in menu.items():
            output = f"{category}:{items}"
            file.write(output + "\n")

# Phase 2
def read_menu():
    menus = {}
    try: 
        with open("menu_config.txt", 'r') as file:
            for line in file:
                parts_of_line = line.strip().split(':')
                if len(parts_of_line) == 2:
                    category = parts_of_line[0].strip()
                    detail = parts_of_line[1].strip()
                    menus[category] = detail
        return menus
    except FileNotFoundError:
        print("\nError: 'menu_config.txt' not found.")
        return None

def split_into_variables(menu_items):
    # dictionary to individual varibales
    appetizer_data = menu_items.get("APPETIZERS", "No data")
    entree_data = menu_items.get("ENTREES", "No data")
    dessert_data = menu_items.get("DESSERTS", "No data")
    drink_data = menu_items.get("DRINKS", "No data")
    return appetizer_data, entree_data, dessert_data, drink_data

def print_menu(apps, entrees, desserts, drinks):
    # Put them in list to print easier
    sections = [("APPETIZERS", apps), ("ENTREES", entrees), ("DESSERTS", desserts), ("DRINKS", drinks)]

    print("\n" + "=" * 35)
    print(" RESTAURANT MENU AUDIT")
    print("=" * 35)

    for title, data in sections:
        print(f"\nSECTION: {title}")
        individual_items = data.split(",")
        for food in individual_items:
            print(f"  * {food.strip()}")
    print("\n" + "*" * 35)
    print("  AUDIT SUCCESSFUL")
    print("*" * 35)

def main():
    # Phase 1
    print("--- PHASE 1: MENU CREATOR ---")
    my_menu = get_menu_options()
    save_to_file(my_menu)

    # Phase 2
    print("\n--- PHASE 2: Auditor ---")
    loaded_data = read_menu()

    if loaded_data:
        app_var, entree_var, dessert_var, drink_var = split_into_variables(loaded_data)
        print_menu(apps=app_var, entrees=entree_var, desserts=dessert_var, drinks=drink_var)

main()







