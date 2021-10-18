import funcs as f

try:
    N = int(input("Введите мощность множества: "))
except ValueError:
    print("[error] Мощность должна быть числом")
    exit(1)

if N > 9:
    print("[error] По условию задачи мощность <= 9")
    exit(1)
if N < 0:
    print("[error] Мощность не может быть меньше нуля")
    exit(1)

interactive = True
ans_for_interactive = input("Хотите генерировать в интерактивном режиме? [Y/n] ")
if ans_for_interactive == "n":
    interactive = False

loops_count = 0
groups_count = 0
for neutral_elem in range(N):
    g = f.GroupGenerator(N, interactive)
    g.fix_neutral_elem(neutral_elem)

    for filled_g in g.latin_square_fill():
        loops_count += 1
        if not filled_g.is_associative():
            continue

        groups_count += 1
        filled_g.print_msg("Completely filled and associatve. Good\nCurrent groups count: {0}".format(groups_count))

        filled_g.print_highlight = (-1, -1)
        if not filled_g.interactive:
            filled_g.print_table()
            print()

print("Loops count(associative is not necessary):", loops_count)
print("Groups count:", groups_count)
