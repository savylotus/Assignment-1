# question 2

def calculate_discount(month, total_price, is_member, length_of_stay):
    # Initial discount
    total_discount = 0

    # Seasonal Discount
    if month in ["January", "February", "September"]:
        total_discount += 10

    # Membership Discount
    if is_member:
        total_discount += 15

    # Length of Stay Discount
    if length_of_stay >= 7:
        total_discount += 5

    # Ensure the total discount does not exceed 25%
    if total_discount > 25:
        total_discount = 25

    # Calculate final price
    discount_amount = (total_discount / 100) * total_price
    final_price = total_price - discount_amount

    return total_discount, final_price


def main():
    # Input details
    month = input("Enter the booking month: ")
    total_price = float(input("Enter the total price of the stay: $"))
    is_member = input("Is the guest a member? (yes/no): ").strip().lower() == "yes"
    length_of_stay = int(input("Enter the length of stay (in nights): "))

    # Calculate discount and final price
    discount_percentage, final_price = calculate_discount(month, total_price, is_member, length_of_stay)

    # Output results
    print(f"\nTotal Discount: {discount_percentage}%")
    print(f"Final Price: ${final_price:.2f}")


if __name__ == "__main__":
    main()
