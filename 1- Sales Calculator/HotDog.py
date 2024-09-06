#Joseph Bepo
#HotDog.py
# Enhanced Hot Dog Sales Program
# Enhanced Hot Dog Sales Program with Pricing and Profit Calculation

# Declaration
traditional_hot_dog = 0
veggie_hot_dog = 0
curry_hot_dog = 0
bbq_hot_dog = 0
spicy_hot_dog = 0
select_hot_dog = True

# Prices and production costs for each hot dog type
PRICES = {
    "Traditional": 5.00,  # $5.00 per traditional hot dog
    "Veggie": 6.00,       # $6.00 per veggie hot dog
    "Curry": 7.00,        # $7.00 per curry hot dog
    "BBQ": 10.00,         # $10.00 per BBQ hot dog
    "Spicy": 7.50         # $7.50 per spicy hot dog
}

PRODUCTION_COSTS = {
    "Traditional": 2.00,  # $2.00 production cost for traditional hot dog
    "Veggie": 2.50,       # $2.50 production cost for veggie hot dog
    "Curry": 3.00,        # $3.00 production cost for curry hot dog
    "BBQ": 4.10,          # $4.10 production cost for BBQ hot dog
    "Spicy": 3.00         # $3.00 production cost for spicy hot dog
}

def get_hot_dog_sales(hot_dog_type):
    """Get the sales for the selected hot dog type."""
    while True:
        try:
            sales_input = int(input(f"How many {hot_dog_type} hot dogs were sold?: "))
            return sales_input
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_profit(sales, hot_dog_type):
    """Calculate the profit for a given hot dog type based on sales."""
    price_per_hot_dog = PRICES[hot_dog_type]
    cost_per_hot_dog = PRODUCTION_COSTS[hot_dog_type]
    total_revenue = sales * price_per_hot_dog
    total_cost = sales * cost_per_hot_dog
    profit = total_revenue - total_cost
    return profit

def display_results(traditional_hot_dog, veggie_hot_dog, curry_hot_dog, bbq_hot_dog, spicy_hot_dog):
    """Display the total sales, percentage, and profit for each hot dog type."""
    total_hot_dog = traditional_hot_dog + veggie_hot_dog + curry_hot_dog + bbq_hot_dog + spicy_hot_dog
    if total_hot_dog == 0:
        print("No sales were made.")
    else:
        tradiona_percentage = format((traditional_hot_dog * 100.0) / total_hot_dog, ".1f")
        veggie_percentage = format((veggie_hot_dog * 100.0) / total_hot_dog, ".1f")
        curry_percentage = format((curry_hot_dog * 100.0) / total_hot_dog, ".1f")
        bbq_percentage = format((bbq_hot_dog * 100.0) / total_hot_dog, ".1f")
        spicy_percentage = format((spicy_hot_dog * 100.0) / total_hot_dog, ".1f")
        
        traditional_profit = calculate_profit(traditional_hot_dog, "Traditional")
        veggie_profit = calculate_profit(veggie_hot_dog, "Veggie")
        curry_profit = calculate_profit(curry_hot_dog, "Curry")
        bbq_profit = calculate_profit(bbq_hot_dog, "BBQ")
        spicy_profit = calculate_profit(spicy_hot_dog, "Spicy")
        
        # Display the result
        print("\nHot Dog Sales Report")
        print("--------------------------------------------------")
        print(f"Traditional Hot Dog   {traditional_hot_dog}               {tradiona_percentage}%       Profit: ${traditional_profit:.2f}")
        print(f"Veggie Hot Dog        {veggie_hot_dog}               {veggie_percentage}%       Profit: ${veggie_profit:.2f}")
        print(f"Curry Hot Dog         {curry_hot_dog}               {curry_percentage}%       Profit: ${curry_profit:.2f}")
        print(f"BBQ Hot Dog           {bbq_hot_dog}               {bbq_percentage}%       Profit: ${bbq_profit:.2f}")
        print(f"Spicy Hot Dog         {spicy_hot_dog}               {spicy_percentage}%       Profit: ${spicy_profit:.2f}")
        print("--------------------------------------------------")
        print(f"Total Hot-Dogs Sold: {total_hot_dog}")
        
        # Determine which hot dog has the highest profit
        best_profit = max(traditional_profit, veggie_profit, curry_profit, bbq_profit, spicy_profit)
        if best_profit == traditional_profit:
            best_hot_dog = "Traditional"
        elif best_profit == veggie_profit:
            best_hot_dog = "Veggie"
        elif best_profit == curry_profit:
            best_hot_dog = "Curry"
        elif best_profit == bbq_profit:
            best_hot_dog = "BBQ"
        else:
            best_hot_dog = "Spicy"
        
        print(f"\nThe Hot-Dog with the best profit margin is: {best_hot_dog} Hot-Dog with a profit of ${best_profit:.2f}")
        print("\n")

def main():
    global traditional_hot_dog, veggie_hot_dog, curry_hot_dog, bbq_hot_dog, spicy_hot_dog, select_hot_dog
    
    while select_hot_dog:
        # User input to request the hot dog type
        user_input = input("\nPlease choose the hot dog type:\n1. Traditional\n2. Veggie\n3. Curry\n4. BBQ\n5. Spicy\n6. View Report and Exit\nYour choice (1-6): ")

        # Try and except block to validate user input for not a number
        try:
            hot_dog = int(user_input)
        except ValueError:
            print("Hey, INCORRECT input. Please try again!")
            continue

        # Validate user input within the range (1 to 6)
        if 1 <= hot_dog <= 6:
            if hot_dog == 1:
                traditional_hot_dog += get_hot_dog_sales("Traditional")
            elif hot_dog == 2:
                veggie_hot_dog += get_hot_dog_sales("Veggie")
            elif hot_dog == 3:
                curry_hot_dog += get_hot_dog_sales("Curry")
            elif hot_dog == 4:
                bbq_hot_dog += get_hot_dog_sales("BBQ")
            elif hot_dog == 5:
                spicy_hot_dog += get_hot_dog_sales("Spicy")
            elif hot_dog == 6:
                if traditional_hot_dog == 0 and veggie_hot_dog == 0 and curry_hot_dog == 0 and bbq_hot_dog == 0 and spicy_hot_dog == 0:
                    print("No sales have been made yet!")
                else:
                    # Calculate and display the total hot dog sales and percentages
                    display_results(traditional_hot_dog, veggie_hot_dog, curry_hot_dog, bbq_hot_dog, spicy_hot_dog)
                
                # Ask if the user wants to make another entry or exit
                continue_input = input("Do you want to continue entering sales? (yes/no): ").strip().lower()
                if continue_input in ['no', 'n']:
                    print("Thank you! Exiting the program.")
                    break
        else:
            print("Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
