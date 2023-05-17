def suggest_outfit(temperature, is_raining):
    if temperature < 50:
        return "Wear a coat, hat, scarf, and gloves."
    elif 50 <= temperature <= 70:
        if is_raining:
            return "Wear a rain jacket and boots."
        else:
            return "Wear a sweater or light jacket."
    else:
        if is_raining:
            return "Wear a light jacket and rain boots."
        else:
            return "Wear a t-shirt and shorts."

temperature = float(input("Enter the current temperature in Fahrenheit: "))
is_raining = input("Is it currently raining? (yes/no): ").lower() == "yes"

outfit_suggestion = suggest_outfit(temperature, is_raining)
print("Based on the current weather conditions, it is suggested to:", outfit_suggestion)