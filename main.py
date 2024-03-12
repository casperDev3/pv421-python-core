import random


# FUNCTIONS
def gen_people(qty):
    temp_user = {
        "name": "John",
        "address": {
            "city": "Lviv",
            "street": "Hrushevskoho"
        }
    }

    data = []
    people_gen_counter = 0
    while people_gen_counter < qty:
        # get age & children
        temp_user['age'] = random.randint(0, 150)
        temp_user['children'] = random.randint(0, 10)
        # gen address
        address = temp_user['address'].copy()
        address['No'] = random.randint(1, 500)
        temp_user['address'] = address
        # add new element
        data.append(temp_user.copy())
        # print(f"User #{people_gen_counter} was added!")
        people_gen_counter += 1  # people_gen_counter = people_gen_counter + 1
        pass
    return data


# LOOPS
if __name__ == "__main__":

    # 2 <= iterator < 10, step 2
    # for iterator in range(2, 10, 2):
    #     print(iterator)
    # for item in fruits:
    #     print(item)
    #     if item[0] == "p":
    #         print("Success! ---")
    #         print(item)
    #         break
    #     else:
    #         continue
    #     pass

    # a = 5
    # while a <= 10:
    #     a = a + 1
    #     print(a)
    #     # if a == 0:
    #     #     break
    #     # else:
    #     #     continue
    #     pass

    # Count Adult - > has children -> No: 50 - 70
    # adults = []
    # for user in users_data:
    #     if user['age'] >= 18:
    #         adults.append(user)
    #
    # has_children = []
    # for user in adults:
    #     if user['children'] > 0:
    #         has_children.append(user)
    #
    # finish_pool = []
    # for user in has_children:
    #     if 50 <= int(user['address']['No']) <= 70:
    #         finish_pool.append(user)

    # is_adult = True
    # children = 5
    # if is_adult and children >= 5:
    #     print("You are beaty!")
    # elif is_adult or children > 0:
    #     print("Nice!")
    # else:
    #     print("Something! Else!")
    users_data = gen_people(5000)
    filtered_data = []
    for user in users_data:
        # prepare data
        age = user['age']
        children = user["children"]
        number = int(user['address']["No"])

        # filtering data
        if age >= 18 and children > 1 and 50 <= number <= 70:
            filtered_data.append(user)

    print(f"Users {len(filtered_data)}")
