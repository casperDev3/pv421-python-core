def crop_text(txt, qty_symbols, end_symbol="..."):
    # try:
    #     int("Hello World!")
    # except Exception as err:
    #     print("Opps some error!", err)
    # finally:
    #     print("Script Ended!")

    try:
        # result = 1 / 0
        if len(txt) > qty_symbols:
            c_text = ""
            counter_symbols = 0
            for s in txt:
                if counter_symbols < qty_symbols:
                    counter_symbols += 1
                    c_text += s
            return c_text + end_symbol
        else:
            return txt
    except ZeroDivisionError:
        print("Opps... u can't division on 0!")
    except TypeError:
        print("Maybe u use incorrect types!")
    except Exception as err:
        print("Error", err)



def main():
    txt = "Lorem Ipsum"
    txt = crop_text(txt, "200")
    print("TXT: ", txt)


if __name__ == "__main__":
    main()
