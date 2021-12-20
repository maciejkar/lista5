class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def hanoi_problem(n=4):
    """Fuction solve hanoi problem with using stack and print each steps by printing each stacks
    @pam n:(Int) number of pucks"""
    pole_a = Stack()
    for i in range(n, 0, -1):
        pole_a.push(i)
    pole_b = Stack()
    pole_c = Stack()

    print(str(pole_a) + " " + str(pole_b) + " " + str(pole_c))

    def move_tower(n, start_pole, end_pole, buff_pole):
        if n == 0:
            print(str(pole_a) + " " + str(pole_b) + " " + str(pole_c))
        elif n == 1:
            end_pole.push(start_pole.pop())
            print(str(pole_a) + " " + str(pole_b) + " " + str(pole_c))
        elif n > 1:
            move_tower(n - 1, start_pole, buff_pole, end_pole)
            end_pole.push(start_pole.pop())
            print(str(pole_a) + " " + str(pole_b) + " " + str(pole_c))
            move_tower(n-1, buff_pole, end_pole, start_pole)

    move_tower(n, pole_a, pole_b, pole_c)


if __name__ == '__main__':
    hanoi_problem(6)
