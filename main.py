import sys


def validate_branch_name(name) -> bool:
    # check pattern of given branch name with known valid patterns.
    print(f'[TO DEBBUG] call to method validate branch with name: {name}')
    # check param name for falsy
    check_entered_param(name)

    # check, if name has illegal chars
    check_invalid_chars(name)

    # compare with known patterns
    if check_known_patterns(name):
        return True

    # by default if invalid then is wrong
    return False


def check_known_patterns(name) -> bool:
    patterns = ["main", "develop", "feature/", "fix/"]
    if (name.startswith(p) for p in patterns):
        if name.startswith("f") and name.endswith("/"):
            print("branch name lacks exact description")
            return False
        return True
    sys.exit("space is un illegal character in branch name")


def check_invalid_chars(name):
    illegals = [" ", ";", ",", ".", "\\"]
    if any((i in illegals) for i in name):
        sys.exit("space is un illegal character in branch name")
    pass


def check_entered_param(name):
    if not name:
        sys.exit("mandatory param name was not given")
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = validate_branch_name(sys.argv[1])
    if result:
        sys.exit(0)
    else:
        sys.exit(1)
