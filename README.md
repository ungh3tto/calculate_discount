
This is a simple Python program that calculates the final price of an item after applying a discount — only if the discount is 20% or higher.
If the discount is less than 20%, the program returns the original price without changes.
It’s designed for easy interaction with the user and displays friendly messages.

**Features**

Prompts the user to enter:
The original price of an item.
The discount percentage.
Applies the discount only if it is 20% or higher.


**Displays:**

Original price
Discount percentage (if applicable)
Final price after discount (if applicable)
Prints a message when no discount is applied.

**How It Works**

1) Function calculate_discount(price, discount_percent)
     Checks if the discount percentage is greater than or equal to 20%.
     If yes, calculates the discounted price and returns it.
     If no, returns the original price unchanged.

2) User Input & Output
     Asks the user for the original price and discount percentage.
     Calls calculate_discount() to determine the final price.
     Displays friendly output with either:
        Discount details and the reduced price, or
        A message saying no discount was applied.
