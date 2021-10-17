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
ans = input("Хотите генерировать в интерактивном режиме? [Y/n] ")
if ans == "n":
    interactive = False

for neutral_elem in range(N):
    g = f.GroupGenerator(N, interactive)
    g.fix_neutral_elem(neutral_elem)
    g.latin_square_fill()

