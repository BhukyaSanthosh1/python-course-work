product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Title: ")
price = float(input("Enter Product Price (in ₹): "))
categories = input("Enter Categories (comma-separated): ").split(",")

available_stock = int(input("Enter Available Quantity: "))
sold_stock = int(input("Enter Sold Quantity: "))
stock_details = (available_stock, sold_stock)

discount = float(input("Enter Discount Percentage: "))
features = set(input("Enter Product Features (comma-separated): ").split(","))

seller_name = input("Enter Seller Name: ")
seller_contact = input("Enter Seller Contact Number: ")
seller_location = input("Enter Seller Location: ")
seller_details = {
    "name": seller_name,
    "contact": seller_contact,
    "location": seller_location
}

print("\n Product Basic Info (Using sep=',' )")
print("Product ID, Name, Price:", product_id, product_name, price, sep=", ")

print("\n Discount Info (Using % formatting)")
print("Product Discount: %.2f%%" % discount)

print("\n Product Details (Using f-strings)")
print(f"Title: {product_name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount}%")
print(f"Available Units: {stock_details[0]}")

print("\n Seller Details (Using .format() method)")
print("Seller Info: Name - {}, Contact - {}, Location - {}".format(
    seller_details["name"],
    seller_details["contact"],
    seller_details["location"]
))