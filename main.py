import sys


def validate_branch_name(name):
    # check pattern of given branch name with known valid patterns.
    print(f'[TO DEBBUG] call to method validate branch with name: {name}')
    # check param name for falsy
    check_entered_param(name)

    # TODO check, if name has wrong chars

    # TODO compare with known patterns

    # TODO return default - false


def check_entered_param(name):
    if not name:
        sys.exit("mandatory param name was not given")
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    validate_branch_name(sys.argv[1])
