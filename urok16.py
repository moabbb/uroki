# Задача 1
class Kassa(object):

    def __init__(self, m):
        self.money = m

    def top_up(self, x):
         self.money += x

    def count_1000(self):
        return self.money // 1000

    def take_away(self, y):
        if y > self.money:
            print("Недостаточно денег")
        else:
            self.money -= y

# Задача 2

class Turtle(object):
    def __init__(self, x, y, s):
        self.pos_x = x
        self.pos_y = y
        self.move = s

    def go_up(self):
        self.pos_y += self.move

    def go_down(self):
        self.pos_y -= self.move

    def go_left(self):
        self.pos_x -= self.move

    def go_right(self):
        self.pos_x += self.move

    def evolve(self):
        self.move += 1

    def degrade(self):
        if self.move <= 1:
            print("Ошибка")
        else:
            self.move -= 1

    def count_moves(self, x2, y2):
        dx = x2 - self.pos_x
        if dx < 0:
            dx = -dx

        dy = y2 - self.pos_y
        if dy < 0:
            dy = -dy

        move_x = (dx + self.move - 1) // self.move
        move_y = (dy + self.move - 1) // self.move
        return move_x + move_y
