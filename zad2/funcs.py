from copy import deepcopy

EMPTY_CELL = -1

class GroupGenerator:
    def __init__(self, N, interactive):
        self.N = N
        self.interactive = interactive

        self.g = [[EMPTY_CELL for _ in range(N)] for _ in range(N)]
        self.neutral_elem = -1
        self.print_highlight = (-1, -1)

    def fix_neutral_elem(self, neutral_elem):
        self.neutral_elem = neutral_elem

        for j in range(self.N):
            self.g[neutral_elem][j] = j
        for i in range(self.N):
            self.g[i][neutral_elem] = i

    # возвращает отсортированный список элементов которые не встречаются в
    # строке и столбце на пересечении которых лежит элемент (fixed_i, fixed_j)
    # (используется для заполнения латинского квадрата)
    # (сортировка нужно потому, что тип set в python не гарантирует порядок
    # элементов, а нам бы хотелось иметь одинаковый результат работы программы
    # при каждом запуске (с точностью до шагов генерации))
    def __get_uniqs_for(self, fixed_i, fixed_j):
        uniqs = set([x for x in range(self.N)])
        for i in range(self.N):
            uniqs.discard(self.g[i][fixed_j])
        for j in range(self.N):
            uniqs.discard(self.g[fixed_i][j])

        return sorted(uniqs)

    # перебирает таблицы заполняя их по правилу латинского квадрата и вызывает
    # функцию проверки на ассоциативность для каждой полученной таблицы
    def latin_square_fill(self, last_i=0):
        for i in range(last_i, self.N):
            for j in range(0, self.N):
                if self.g[i][j] != EMPTY_CELL:
                    continue

                self.print_highlight = (i, j)

                uniqs = self.__get_uniqs_for(i, j)
                if len(uniqs) == 0:
                    self.print_msg(
                            "stuck at {0}\n(следуя правилу латинского квадрата, нет элементов которые можно установить в эту ячейку)"
                            .format((i, j))
                            )
                    self.print_highlight = (-1, -1)
                    return

                for uniq in uniqs:
                    prev_self = deepcopy(self)

                    self.g[i][j] = uniq

                    if len(uniqs) == 1:
                        self.print_msg("For {0} only one item possible, set {1}".format((i, j), uniq))
                    else:
                        self.print_msg("uniqs for {0}: {1}\nselect {2}".format((i, j), uniqs, uniq))
                    yield from self.latin_square_fill(i)

                    self = prev_self

                self.print_highlight = (-1, -1)

                # skip incomplete tables
                # complete tables appears only if all cells is not empty, so for them this line is unreachable
                return

        self.print_msg("Table filled")

        yield self

    def is_associative(self):
        for a in range(0, self.N):
            for b in range(0, self.N):
                for c in range(0, self.N):
                    left = self.g [a] [self.g[b][c]]
                    right = self.g [self.g[a][b]] [c]
                    if left != right:
                        self.print_highlight = (-1, -1)
                        self.print_msg("Not assoc for {0}x{1}x{2}".format(a, b, c))
                        return False

        return True


    def print_msg(self, msg):
        if not self.interactive:
            return

        clear_screen()
        print("neutral element:", self.neutral_elem, "\n")
        self.print_table()
        print("\n" + msg)
        input()

    def print_table(self):
        # header - columns names
        print(" ", end=" ")
        for i in range(self.N):
            print(Colors.black_on_white + str(i) + Colors.restore, end=" ")
        print(Colors.restore)

        for i in range(self.N):
            # header - row name
            print(Colors.black_on_white + str(i) + Colors.restore, end=" ")

            for j in range(self.N):
                cur_item = self.g[i][j]
                if cur_item == EMPTY_CELL:
                    cur_item = " "
                else:
                    cur_item = str(cur_item)
                # cur_item = str(cur_item) if cur_item != -1 else " "

                if self.print_highlight == (i, j):
                    print(Colors.highlight + cur_item + Colors.restore, end=" ")
                else:
                    print(cur_item, end=" ")

            print()

class Colors:
    restore = "\033[0m"
    black_on_white = "\033[30m\033[47m"
    highlight = "\033[41m"


import os
def clear_screen():
    os.system("cls||clear")

