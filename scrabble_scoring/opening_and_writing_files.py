def overwrite_file(file, first_item):
    try:
        with open(file, "w") as file:
            file.write(first_item + '\n')
    except FileNotFoundError:
        print("File not found")
        raise
    finally:
        print("\n--Execution complete\n")

def  open_and_print_file(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("File cannot be found or directory is wrong")
        raise
    finally:
        print("\n--Execution complete\n")

def write_to_file(file, next_item):
    try:
        with open(file, "a") as file:
            file.write(next_item + '\n')
    except FileNotFoundError:
        print("File not found")
        raise
    finally:
        print("\n--Execution complete\n")