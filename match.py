"""
Match case

"""
month = input("Enter a month name: ").lower()

match month:
    case "january" | "march" | "may" | "july" | "august" | "october" | "december":
        print("There are 31 days in this month.")
    case "april" | "june" | "september" | "november":
        print("There are 30 days in this month.")
    case "february":
        print("There are 28 or 29 days in this month.")
    case _:
        print("That is not a valid month name.")