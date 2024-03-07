# --- PRIMITIVE ---
# first_name_client = "jOhN said something!"
# methods / functions str
# print(len(first_name_client))
# CRUD - Create Read Update Delete
# print(first_name_client.title())
# print(first_name_client.capitalize())
# print(first_name_client.lower())
# print(first_name_client.upper())
# print(first_name_client.replace("j", "#"))
# print(first_name_client.find("O"))
#
# first_name = "jAke"
# print("Hello, " + first_name.capitalize() + "!")
# print(f"Hello, {first_name.capitalize()}!")

# Input: johN DoE sEm
# Output: Doe J. S.

# fn = input("Enter fn: ").capitalize()
# ln = input("Enter ln: ").capitalize()
# fsn = input("Enter fsn: ").capitalize()
# print(f"{ln} {fn[0]}. {fsn[0]}.")

# txt = """Lorem ipsum — класичний варіант умовного беззмістовного тексту, що вставляється в макет сторінки. Lorem
# ipsum — це перекручений уривок з філософського трактату Цицерона «Про межі добра і зла», написаного в 45 році до
# нашої ери латиною"""

# clear_letter = (txt.replace(" ", "")
#                 .replace("—", "")
#                 .replace(",", '')
#                 .replace("«", "")
#                 .replace("»", '')
#                 .replace(".", ''))
#
# print(len(clear_letter))


# num_one = 2
# num_two = 3
# sum_num = num_one + num_two
# print(sum_num)
# print(num_one - num_two)
# print(round(num_one / num_two, 2))
# print(num_one * num_two)
# print(num_one**2)
# print(5 % 2)
#
# some_result = 5 < 7
# print(some_result)
# print(5 > 7)
# print(5 <= 5)
# print(5 >= 7)
# print(5 == 7)
# print(5 != 7)

# --- COMPLEX ---
# someList = [5, 2, 9, 2365, 4]
# someList.append("hello!")
# someList.remove("test")  # del by value
# someList.pop()  # del by index or last
# someList.clear()
# someList.sort(reverse=True)
# someList.reverse()


# # Primitives vs Complex
# num_one = 1
# num_two = num_one
# num_one = num_one + 1
# # print(num_one, num_two)
#
# arr_one = [1, 2]
# arr_two = arr_one.copy()
# arr_one[0] = arr_one[0] + 1
# print(arr_one, arr_two)

# some_dict = {
# }
# some_dict["first_name"] = "Jake"
# # del some_dict["id"]
#
# list_of_dict = [
#     {
#         "id": 1,
#         "name": "Jane"
#     }
# ]
#
# some_dict["id"] = len(list_of_dict) + 1
# list_of_dict.append(some_dict)
#
# print(list_of_dict)


# users_data = []
#
# # first_name =
# users_data.append({
#     "id": len(users_data) + 1,
#     "first_name": input("Enter name:").capitalize()
# })
# print(users_data)

# age = int(input("Enter your age: "))

# if 0 <= age < 12:
#     print("You're child!")
# elif 12 <= age < 18:
#     print("You're teen!")
# elif age >= 18:
#     print("You're adult!")
# else:
#     print("oops! Something wrong!")


print("Products: \n"
      "1. Phone\n"
      "2. TV\n"
      "3. Laptop\n\n")

ch = input("Enter number product: ")

if ch == '1':
    print("Phone")
elif ch == "2":
    print("TV")
elif ch == "3":
    print("Laptop")
else:
    print("oops!")
