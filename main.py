import random


# Function
def say_hello(txt="Hello", qty=5):
    for i in range(qty):
        print(txt)


def is_exist_in_our_base(uid):
    if uid == 1:
        return True
    return False


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


def cond_and_func():
    if is_exist_in_our_base(2):
        print("Welcome!")
    else:
        print("You need start reg!")


def is_continue_game():
    # continue game ch
    print("Чи бажаєте ви продовжити гру?\n"
          "1. Так\n"
          "2. Ні")
    ch_continue = int(input("Зробіть вибір: "))
    if ch_continue == 1:
        return True
    elif ch_continue == 2:
        return False
    else:
        print("Ваш вибір не вірний!")
        is_continue_game()


def truth_or_action():
    # assets
    questions = [
        "Яким чином ти описав би свій найгірший побутовий предмет?",
        "Яка найбільша гафа, яку ти коли-небудь вчинив?",
        "Що було найбільшою помилкою твого життя?",
        "Яка твоя найбільша нелюбов до їжі?",
        "Який твій найнелепший страх?",
        "Яке найбільше ризиковане рішення, яке ти коли-небудь приймав?",
        "Яке найбільше ризиковане рішення, яке ти коли-небудь приймав?",
        "Яка найбільша твоя секретна фантазія?",
        "Яке найгірше погане звичка, яке ти коли-небудь мав?",
        "Яка найбільша біда, в яку ти коли-небудь потрапляв?",
        "Яка твоя найбільша несподівана перемога?",
        "Яка найгірша ситуація, в якій ти коли-небудь був?",
        "Яке найбільше незвичайне місце, де ти коли-небудь спав?",
        "Яка твоя найбільша сором'язлива мить?",
        "Яке найнелегше завдання, яке ти коли-небудь виконував?",
        "Яке найбільше лякало тебе в дитинстві?",
        "Яке найнезвичайніше місце, де ти коли-небудь побував?",
        "Яка твоя найбільша дурна звичка?",
        "Який твій найгірший звичай під час їжі?",
        "Яке найбільше провалене рандеву, яке ти коли-небудь мав?"
    ]
    actions = [
        "Продавай кому-небудь своє найбільше нелюблене предмет",
        "Виконай 20 присідань",
        "Розповісти жарт, навідміну від залишніх",
        "Виконай відомий танець",
        "Співай пісню в стилі опери",
        "Скажи комплімент всім гравцям в грі",
        "Покажи свій найкращий акторський навик",
        "Виконай імпровізовану пісню про кого-небудь в кімнаті",
        "Зроби фото якого-небудь гравця у забавному костюмі",
        "Розкажи анекдот",
        "Зроби масаж спицями усім гравцям у кімнаті",
        "Погладь вухо якогось гравця",
        "Подаруй підвіску відразу двом гравцям",
        "Розкажи свою найсмішнішу історію",
        "Виконай веселий танець",
        "Співай пісню, яку вибере інший гравець",
        "Розкажи про свій найбільший страх",
        "Виконай акробатичні фігури",
        "Розкажи про найгіршу подію в своєму житті",
        "Знайди щось смішне в інтернеті та покажи іншим"
    ]
    truth_counter = 0
    print("Start game!")
    while True:
        # menus round
        print("1. Правда\n"
              "2. Дія\n")
        # get choice user
        ch = int(input("Зробіть свій вибір: "))
        # flow game
        if ch == 1 and truth_counter < 2:
            truth_counter += 1
            print(questions[random.randint(0, len(questions) - 1)])
        elif ch == 1 and truth_counter >= 2:
            truth_counter = 0
            print("Тепер повинна бути дія")
            print(actions[random.randint(0, len(actions) - 1)])
        elif ch == 2:
            truth_counter = 0
            print(actions[random.randint(0, len(actions) - 1)])
        else:
            print("Ой.. Ви обрали не вірний варіант! Оберіть щераз!")

        # controller ext
        if is_continue_game():
            continue
        break


def run():
    truth_or_action()


if __name__ == "__main__":
    run()
