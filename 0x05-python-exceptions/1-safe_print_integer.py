def safe_print_integer(value):
    try:
        print(("{}".format(value)))
        return True
    except:
        return False