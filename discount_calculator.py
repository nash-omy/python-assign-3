# Function to calculate the price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Ask the user for the original price
original_price = float(input("Enter the original price of the item: "))

# Ask the user for the discount percentage
discount = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount)

# Check if discount was applied
if discount >= 20:
    print(f"Discount applied. Final price is: {final_price}")
else:
    print(f"No discount applied. Final price is: {original_price}")
