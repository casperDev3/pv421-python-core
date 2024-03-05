user_first_name = "John"  # snake_case
userFirstName = "Jane"  # camelCase
UserFirstName = "Josh"  # PascalCase
# user-first-name = "Ann"  # kebab-case
COUNTRY = "Ukraine"  # constants
USER_FIRST_NAME = "Rayn"  # constants

# print(user_first_name)

# --- PRIMITIVES ---
str_one = "Lorem Ipsum"  # string (str)
str_two = 'Lorem Ipsum'
str_three = """ "Harry Potter" J. K. R. """
str_four = ''' Joe's food! '''

num_one = 21  # integer (int)
num_two = 3.14  # float
num_three = 12j  # complex

bool_one = True  # boolean (bool)
bool_two = False

empty_one = None  # None

# --- COMPLEX ---
list_one = ["test", 44, True, 3.14]  # list (array)
# print(list_one[2])

dict_one = {
    "first_name": "John",
    "last_name": "Doe",
    'has_children': True,
    "age": 25,
    "address": {
        "country": "UA",
        "city": "Dro",
        "street": "Halytskoho",
        "No": 12,
        "zip_code": 82100
    }
}  # dict (obj)
print(dict_one['first_name'], dict_one['address']['zip_code'])

# --- ENTER DATA ---
employee_first_name = input("Enter first name your employee: ")
print("__Name: ", type(employee_first_name))
employee_age = int(input("Enter age your employee: "))   # float(), str()
print("__Age: ", type(employee_age))
