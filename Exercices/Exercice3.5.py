def check_asci(s):
    try:
        s.encode("ascii")
        print(f"<<{s}>> contient uniquement des caractères ascii")
    except UnicodeEncodeError:
        print(f"<<{s}>> contient des caractères non-ascii")

check_asci("Hello")
check_asci("Café")
check_asci("Test123")
check_asci("émoji 😀")