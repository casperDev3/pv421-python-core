# Function
def say_hello(txt="Hello", qty=5):
    for i in range(qty):
        print(txt)


def pib(first_name, last_name, fathers_name):
    initials = f"{last_name} {first_name[0]}. {fathers_name[0]}."
    return initials


def get_data_from_user():
    # JOhn DOE PAtrick
    # [{"f": John, "l": "Doe", "fn": "Patrick",
    # "initials": "Doe J. P."},....]
    # 2-3

    users_data = []
    for i in range(3):
        # get data from user
        fn = input("Enter fn: ").title()
        ln = input("Enter ln: ").title()
        frn = input("Enter frn: ").title()
        # create temp user
        user_frame = {
            "first_name": fn,
            "last_name": ln,
            "fathers_name": frn,
            "initials": pib(fn, ln, frn)
        }
        # add to user list
        users_data.append(user_frame)

    print(users_data)


def run():
    say_hello(qty=2)
    # user_initials = pib("John", "Doe", "Patrick")
    # print(user_initials)


if __name__ == "__main__":
    run()
