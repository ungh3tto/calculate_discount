def calculate_discount(price, discount_percent):
    """Calculate final price after discount if discount is >= 20%."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt user for inputs
print("=== Discount Calculator ===")
original_price = float(input("Enter the original price ($): "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Output the result with friendly messages
if discount_percent >= 20:
    print(f"🎉 You got a {discount_percent:.0f}% discount!")
    print(f"Original price: ${original_price:.2f}")
    print(f"Final price after discount: ${final_price:.2f}")
else:
    print("ℹ️ Discount less than 20% — no discount applied.")
    print(f"Price remains: ${final_price:.2f}")
