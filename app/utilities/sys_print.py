def sys_print_scheduler(msgs: list = None):
    if msgs is None:
        msgs = []

    print("#" * 100)
    print("# SCHEDULER")
    print("#", "-" * 99)
    for msg in msgs:
        print(msg)
    print("")


def sys_print_websockets(msgs: list = None):
    if msgs is None:
        msgs = []

    print(" ")
    print("# WEBSOCKETS")
    print("#", "-" * 99)
    for msg in msgs:
        print(msg)
    print("")


def sys_print_wsgi(msgs: list = None):
    if msgs is None:
        msgs = []

    print(" ")
    print("# WSGI")
    print("#", "-" * 99)
    for msg in msgs:
        print(msg)
    print("")
