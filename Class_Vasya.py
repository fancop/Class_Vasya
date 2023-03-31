import random

class Human:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, opponent):
        damage = random.randint(1, self.strength)
        opponent.health -= damage
        print(f"{self.name} атаковал {opponent.name} и нанёс {damage} урона!")
        if opponent.health <= 0:
            print(f"{opponent.name} был повержен!")

    def is_alive(self):
        return self.health > 0

class Vasiliy(Human):
    def __init__(self):
        super().__init__("Василий", 100, 10)

class Enemy(Human):
    def __init__(self):
        super().__init__("Злыдень", 80, 12)

vasiliy = Vasiliy()
enemy = Enemy()

round_num = 1
while vasiliy.is_alive() and enemy.is_alive():
    print(f"раунд {round_num}")
    vasiliy.attack(enemy)
    print("У Злыденя осталось", enemy.health, "здоровья")
    if not enemy.is_alive():
        break
    enemy.attack(vasiliy)
    print("У Васи осталось", vasiliy.health, "здоровья")
    if not vasiliy.is_alive():
        break
    round_num += 1
    input("Нажмите ENTER чтобы начать следующий раунд")
    print("---------------------------------------------------------")

print("Битва закончена!")