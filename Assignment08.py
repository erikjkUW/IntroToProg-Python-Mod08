# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# erikjk,6.4.2020,Modified code to complete assignment 8
# erikjk,6.4.2020,Added setter/getter for all fields in class Product
# erikjk,6.4.2020,Successful test of setter/getter for product_name/product_price
# erikjk,6.4.2020,Completed FileProcessor class of methods
# erikjk,6.4.2020,Error Handling for FileProcessor: FileNotFoundError/EOFError
# erikjk,6.5.2020,Completed IO class of methods other than Menu and Choice
# erikjk,6.5.2020,Completed Product class methods for string and add to list
# erikjk,6.5.2020,Completed Menu and Choice methods in IO class
# erikjk,6.5.2020,Added DocStrings, Comments
# erikjk,6.5.2020,Final Main Body edits, Debug, Error Handling
# erikjk,6.6.2020,Added ASCII header and intro print statements
# ------------------------------------------------------------------------ #


# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ""
strProductName = ""
fltProductPrice = None
objProduct = None

class Product():
    """Stores data about a product:

    constructor:
        __product_name: private attribute
        __product_price: private attribute
    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
        __str__(self): -> comma separated string for printing/storing
        product_add_to_list(object, list_of_product_objects): -> list_of_product_objects
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        erikjk.6.4.2020,Defined constructor and attributes for initalization
        erikjk.6.5.2020,Added Getter/Setter for both attributes with exceptions
        erikjk.6.5.2020,Created string method and Add to List function
    """
    # -- Constructor
    def __init__(self, product_name, product_price):
        # -- Attributes
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties
    @property
    def product_name(self):
        return str(self.__product_name).title() # Display string with capitalization

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False: # Checks alphabet only name
            self.__product_name = value
        else:
            raise Exception("Product Name Cannot Include Numbers!")

    @property
    def product_price(self):
        return round(self.__product_price, 2) # Display float to 2 decimal places

    @product_price.setter
    def product_price(self, value):
        if value.isalpha() == False: # Checks number only price
            self.__product_price = float(value)
        else:
            raise Exception("Product Price Must Be a Number!")

    # -- Methods
    def __str__(self):
        """Redefines string method for this class
        Comma separated string for writing to file and displaying to user
        :param product_name: string attribute
        :param product_price: float attribute converted to string
        :return: string
        """
        return self.product_name + "," + str(self.product_price)

    def product_add_to_list(object, list_of_product_objects):
        """ Adds new object to list of objects
        :param list_of_product_objects: list of objects
        :return: list of objects
        """
        list_of_product_objects.append(object)
        return list_of_product_objects


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        erikjk,6.4.2020,Completed Read function
        erikjk,6.5.2020,Completed Write function
        erikjk,6.5.2020,Added Error Handling
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """ Reads lines from file and adds to list as objects
        :param file_name: name of target file
        :param file: object for target file
        :param product_name: attribute of object
        :param product_price: attribute of object
        :param list_of_product_objects: list of objects
        :return: list of objects
        """
        list_of_product_objects.clear()
        while True:
            try:
                with open(file_name, "r+") as file:
                    for line in file:
                        product_name, product_price = line.split(",")
                        row = Product(product_name, float(product_price))
                        list_of_product_objects.append(row)
            except EOFError: # End read loop if end of file error
                break
            except FileNotFoundError: # Create file if it doesn't exist
                print("File not found! Creating Now...")
                print()  # Add extra line for looks
                file = open(file_name, "a+")
                file.close()
                break
            finally: # End read loop if no errors found and file is blank
                print("File contents loaded successfully!\n")
                break
        return list_of_product_objects

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Saves objects from list to text file as lines
        :param file_name: name of target file
        :param file: object for target file
        :return: list
        """
        with open(file_name, "w+") as file:
            for product in list_of_product_objects:
                # Strings formatted with __str__ method in Product class
                file.write(str(product) + "\n")
        return list_of_product_objects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Prints menu, lists, and captures input for new object attributes:

    methods:
        print_main_menu_options():

        input_menu_choice():

        print_list_of_products(list_of_product_objects):

        input_product_details(): -> new_product_object

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        erikjk,6.4.2020,Worked on Object input function
        erikjk,6.5.2020,Completed Object input function
        erikjk,6.5.2020,Added Show List function
        erikjk,6.5.2020,Added Menu and Choice functions
    """

    # TODO: Add code to show menu to user
    @staticmethod
    def print_main_menu_options():
        """ Displays a menu of options to user
        :return: nothing
        """
        print("""
        Menu of Options:
       	1 - Show Current List
        2 - Add A New Product
        3 - Save Product List
        4 - Exit Program
        """)

    @staticmethod
    def input_menu_choice():
        """ Captures input for menu choice from user
        :param choice: int from available options 1-4
        :return: string
        """
        choice = str(input("Please choose an option [1-4]: ")).strip()
        print() # Add extra line for looks
        return choice
    @staticmethod
    def print_list_of_products(list_of_product_objects):
        """ Shows current list of products
        :param product_object: objects in list
        :param list_of_product_objects: (list) of objects you want to display
        :return: nothing
        """
        print("*****************PRODUCTS*****************")
        if len(list_of_product_objects) > 0:
            for product_object in list_of_product_objects:
                print(product_object.product_name + " at $" +
                      str(product_object.product_price))
        else:
            print("No Product Information to Display.")
        print("******************************************")

    @staticmethod
    def input_product_details():
        """ Create a new Product class object, initialize, then fill with user input
        :param new_product_object: object
        :param product_name: attribute of object
        :param product_price: attribute of object
        :return: object
        """
        new_product_object = Product("", None) # Initialize new object
        new_product_object.product_name = input("What is the Product's Name?: ")
        new_product_object.product_price = input("What is the Product's Price?: ")
        return new_product_object


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
print("""
  ,--./,-.      Welcome to the:
 / #      \ 
|          |    Product
 \        /         Producer  
  `._,._,'              Program!
""")


# Show user a menu of options
while True:
    IO.print_main_menu_options()

    # Get user's menu option choice
    strChoice = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if strChoice.strip() == "1":
        IO.print_list_of_products(lstOfProductObjects)

    # Let user add data to the list of product objects
    if strChoice.strip() == "2":
        try:
            objProduct = IO.input_product_details()
            Product.product_add_to_list(objProduct, lstOfProductObjects)
            print("\n\"" + objProduct.product_name + "\"" +
                  " has been added to the List of Products for $" +
                  str(objProduct.product_price))
        except Exception as e: # Error handling for attribute.setter exceptions
            print(e)

    # Let user save current data to file and exit program
    if strChoice.strip() == "3":
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print("The List of Products has been saved!")

    # Let user exit program when finished
    if strChoice.strip() == "4":
        print("Have a Productive Day")
        break

# Main Body of Script  ---------------------------------------------------- #















