import openpyxl

file =openpyxl.load_workbook("C:/Users/dell/Desktop/me_you/new_company.xlsx")
company_list = file["Inventory"]
our_sells = {}
Quantity_of_product_less_than_10 = {}

for product_row in range(2,company_list.max_row + 1):
    Product_name = company_list.cell(product_row,2).value
    Quantity_sold = company_list.cell(product_row,5).value
    Price = company_list.cell(product_row,3).value
    Remaining_Quantity = company_list.cell(product_row,4).value
    

    if Product_name in our_sells:
        name =our_sells.get(Product_name)
        our_sells[Product_name] = str(name + Quantity_sold * Price) + "$"
    else:
        our_sells[Product_name] = str(Quantity_sold * Price) + "$"
    if Remaining_Quantity < 10:
        Quantity_of_product_less_than_10[Product_name] = Remaining_Quantity

print("\nusing this automation program".title())
print("you can access information sepecific to this data file".title())
print("to find out the profit for each produt type: 1".title())
print("to find out which products are runing low in stock type: 2".title())

X = input("Enter which number: ")
if X == "1":
  print("*********************************************************************")
  print("               The profit for each product is:".upper())
  print("*********************************************************************")
  for product,sells in our_sells.items():
    print(f"The profit from this product {product} is : {sells}")

elif X == "2":
  print("*********************************************************************")
  print("       warning the qunatity of this product is less than 10".upper())
  print("*********************************************************************")
  for product,quantity in Quantity_of_product_less_than_10.items():
      print(f"Be careful the quantity of {product} is {quantity} Warning!! ")
else:
   print("Invalid Choice, Please Enter 1 or 2")
