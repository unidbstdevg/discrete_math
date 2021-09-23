import os

FILENAME_IN_U = "in_U"
FILENAME_IN_A = "in_A"
FILENAME_IN_B = "in_B"

ELEMENTS_LIMIT = 25

# can't be > 10
INTERACTIVE_PAGE_SIZE = 10

def clear_screen():
    os.system("cls||clear")

def get_set_from_file(filename):
    A = set()
    for line in open(filename):
        if len(A) >= ELEMENTS_LIMIT:
            print("[WARN] Cardinality limit ({}) reached in file \"{}\"".format(ELEMENTS_LIMIT, filename))
            break

        line = line[:-1]
        A.add(line)

    return A

def write_set_to_file(A, filename):
    with open(filename, 'w') as f:
        for x in A:
            f.write(x + "\n")

def interactive_create_universum(filename):
    print("Do you want to create universum? [Y/n] ", end="")
    if input() == "n":
        return False

    new_set = set()

    while True:
        clear_screen()
        print("Current universum (power = {}):".format(len(new_set)), new_set)
        print("Type string you want to add to universum (to finish press CTRL+D):")
        try:
            new_elem = input()
            new_set.add(new_elem)
        except EOFError:
            break
    clear_screen()
    print("Final universum set:", new_set)
    input("Press enter to continue")
    clear_screen()

    write_set_to_file(new_set, filename)

    return True

def print_indexed_page(page):
    for i in range(len(page)):
        print("{}: {}".format(i, page[i]))

# return True if file created successfully
def interactive_create_set_from_universum(U, filename):
    print("Do you want to create file \"{}\"? [Y/n] ".format(filename), end="")
    if input() == "n":
        return False

    new_set = set()

    U_list = sorted(U)
    pages = [U_list[i:i+INTERACTIVE_PAGE_SIZE] for i in range(0, len(U), INTERACTIVE_PAGE_SIZE)]
    for i in range(len(pages)):
        clear_screen()
        print_indexed_page(pages[i])
        print("Current set (power = {}):".format(len(new_set)), new_set)
        print("[{}/{}] Elements indices you want to add: ".format(i + 1, len(pages)),
                end="")
        choice = "".join(filter(type("").isdigit, input()))
        for j in choice:
            new_set.add(pages[i][int(j)])

    clear_screen()
    print("Final set for file \"{}\":".format(filename), new_set)
    input("Press enter to continue")
    clear_screen()

    write_set_to_file(new_set, filename)

    return True

def universum_verification(U, A):
    result = U & A
    diff = A.difference(result) # or: A.difference(U)
    if len(diff) != 0:
        print("[WARN] This elements is not in universum (ignoring):", diff)

    return result

if os.path.exists(FILENAME_IN_U):
    U = get_set_from_file(FILENAME_IN_U)
else:
    print("File \"{}\" does not exist. Please create and fill it.".format(FILENAME_IN_U))
    exit()

if not os.path.exists(FILENAME_IN_U):
    print("Universum is not defined")
    if not interactive_create_universum(FILENAME_IN_U):
        exit()
U = get_set_from_file(FILENAME_IN_U)

if not os.path.exists(FILENAME_IN_A):
    print("Set A is not defined")
    if not interactive_create_set_from_universum(U, FILENAME_IN_A):
        exit()
if not os.path.exists(FILENAME_IN_B):
    print("Set B is not defined")
    if not interactive_create_set_from_universum(U, FILENAME_IN_B):
        exit()
A = get_set_from_file(FILENAME_IN_A)
B = get_set_from_file(FILENAME_IN_B)

# ignore elements that do not belong to universum, and print warnings
A = universum_verification(U, A)
B = universum_verification(U, B)

print()
print("U =", U)
print("A =", A)
print("B =", B)
print()

print("--- Task 1 ---")
print("|U| =", len(U))
print("|A| =", len(A))
print("|B| =", len(B))
print()

print("--- Task 2 ---")
print("Does A = B?", A == B)
print("Does A ~ B?", len(A) == len(B))
print("Does A is subset of B?", A.issubset(B))
print("Does B is subset of A?", B.issubset(A))
print()

print("--- Task 3 ---")
C = A | B
print("C = A | B =", C)
print("|C| =", len(C))
print()
C = A & B
print("C = A & B =", C)
print("|C| =", len(C))
print()
C = A.difference(B)
print("C = A \\ B =", C)
print("|C| =", len(C))
print()
C = B.difference(A)
print("C = B \\ A =", C)
print("|C| =", len(C))
print()
C = A.symmetric_difference(B)
print("C = symmetric difference of A B =", C)
print("|C| =", len(C))
print()
C = U - A
print("C = complement of A =", C)
print("|C| =", len(C))
print()
C = U - B
print("C = complement of B =", C)
print("|C| =", len(C))
