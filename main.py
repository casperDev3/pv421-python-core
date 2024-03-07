first_name_client = "jOhN said something!"

# methods / functions str
# print(len(first_name_client))
# CRUD - Create Read Update Delete
print(first_name_client.title())
print(first_name_client.capitalize())
print(first_name_client.lower())
print(first_name_client.upper())
print(first_name_client.replace("j", "#"))
print(first_name_client.find("O"))

first_name = "jAke"
print("Hello, " + first_name.capitalize() + "!")
print(f"Hello, {first_name.capitalize()}!")

# Input: johN DoE sEm
# Output: Doe J. S.

# fn = input("Enter fn: ").capitalize()
# ln = input("Enter ln: ").capitalize()
# fsn = input("Enter fsn: ").capitalize()
# print(f"{ln} {fn[0]}. {fsn[0]}.")

txt = """Lorem ipsum — класичний варіант умовного беззмістовного тексту, що вставляється в макет сторінки. Lorem 
ipsum — це перекручений уривок з філософського трактату Цицерона «Про межі добра і зла», написаного в 45 році до 
нашої ери латиною"""

clear_letter = (txt.replace(" ", "")
                .replace("—", "")
                .replace(",", '')
                .replace("«", "")
                .replace("»", '')
                .replace(".", ''))

print(len(clear_letter))
