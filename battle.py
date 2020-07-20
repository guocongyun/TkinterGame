from random import randint
from PIL import Image, ImageTk

class Battle:
    def generating_statistic(self):
        try:
            self.canvas.delete(game_system.score_identifier)
        except:
            pass
        try:
            self.canvas.delete(game_system.level_identifier)
        except:
            pass
        try:
            for number in range(len(game_system.life_identifier)):
                self.canvas.delete(game_system.life_identifier[number])
        except:
            pass

        self.life = Image.open("./texture/pixel_heart.png")
        self.life = ImageTk.PhotoImage(self.life)

        for number in range(game_system.life):
            game_system.life_identifier.append(
                self.canvas.tag_raise(self.canvas.create_image(self.h + number * 30, self.h,
                                                     image=self.life,
                                                     anchor=NW)))

        game_system.score_identifier = self.canvas.create_text( self.WINDOW_WIDTH - 100, self.h, fill="white", font="Times 10 bold", text="Score : " + str(game_system.score), anchor=NW)
        game_system.level_identifier = self.canvas.create_text(
            6 * self.w, self.h,
            fill="white", font="Times 10 bold",
            text="Level-" + str(game_system.level), anchor=NW)

        return self.life

    def move_start_position(self):
        self.position = self.canvas.coords(game_system.character[0].identifier)
        if (self.position[0] + self.position[2]) / 2 < self.start_position[0] - 2:
            self.canvas.move(game_system.character[0].identifier, 1, 0)
            self.canvas.after(5, self.move_start_position)
        elif (self.position[0] + self.position[2]) / 2 > self.start_position[0] + 2:
            self.canvas.move(game_system.character[0].identifier, -1, 0)
            self.canvas.after(5, self.move_start_position)
        elif (self.position[1] + self.position[3]) / 2 < self.start_position[1] - 2:
            self.canvas.move(game_system.character[0].identifier, 0, 1)
            self.canvas.after(5, self.move_start_position)
        elif (self.position[1] + self.position[3]) / 2 > self.start_position[1] + 2:
            self.canvas.move(game_system.character[0].identifier, 0, -1)
            self.canvas.after(5, self.move_start_position)
        else:
            game_system.save_game = False
            self.character_movement()
            self.enemy_creation()
            self.enemy_movement()
            self.character_ability()

    class NormalEnemy:
        def __init__(self, character_size):
            x = randint(50, 200) / 100
            y = randint(50, 200) / 100
            self.character_attribute = [x, y]
            self.character_height = character_size ** (1 / 2)
            self.character_width = character_size ** (1 / 2)
            self.character_size = character_size
            self.color = "#cc33ff"

    class WeakEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            self.color = "yellow"

    class HorizontalEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            x = 0.5
            y = 2
            self.character_attribute = [x, y]
            self.color = "#ff0000"

    class VerticalEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            x = 2
            y = 0.5
            self.character_attribute = [x, y]
            self.color = "#ff6600"

    class TallEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            self.character_height = 3 * (character_size / 3) ** (1 / 2)
            self.character_width = (character_size / 3) ** (1 / 2)
            self.color = "#cc99ff"

    class WideEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            self.character_height = (character_size / 3) ** (1 / 2)
            self.character_width = 3 * (character_size / 3) ** (1 / 2)
            self.color = "#9900cc"

    class InvisibleEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            self.color = ""

    class BetterEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            x = 2
            y = 2
            self.character_attribute = [x, y]
            self.color = "#ff0066"

    class StupidEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            x = 0
            y = 0
            self.character_attribute = [x, y]
            self.color = "white"

    class TrapEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            x = 0
            y = 0
            self.character_attribute = [x, y]
            self.color = "Trap"

    class CrazyEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            x = 5
            y = 5
            self.character_attribute = [x, y]
            self.color = "#ff99cc"

    class TrickyEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            self.color = "#ffff99"

    class WeirdEnemy(NormalEnemy):
        def __init__(self, character_size):
            super().__init__(character_size)
            if randint(0, 1) == 1:
                x = 0
                y = randint(0, 8)
            else:
                x = randint(0, 8)
                y = 0
            self.character_attribute = [x, y]
            self.color = "grey"

    def enemy_creation(self):
        number_of_enemy = game_system.level * 2
        weak_enemy = 1 + int(number_of_enemy / 10)
        enemy_count = 0
        while enemy_count < number_of_enemy:
            overlap = False
            if enemy_count < weak_enemy:
                character_size = (game_system.character[0].character_width *
                                  game_system.character[0].character_height - 120) * game_system.scale_factor
                enemy = self.WeakEnemy(character_size)
            else:
                character_size = (game_system.character[0].character_width *
                                  game_system.character[0].character_height + 80 *
                                  (enemy_count - weak_enemy)) * \
                                  game_system.scale_factor
                enemy = ""
                if game_system.level >= 2:
                    random_number = randint(0, 100)
                    if random_number <= 10:
                        enemy = self.VerticalEnemy(character_size)
                if game_system.level >= 3:
                    random_number = randint(0, 100)
                    if random_number <= 10:
                        enemy = self.HorizontalEnemy(character_size)
                if game_system.level >= 4:
                    random_number = randint(0, 100)
                    if random_number <= 10:
                        enemy = self.TallEnemy(character_size)
                if game_system.level >= 5:
                    random_number = randint(0, 100)
                    if random_number <= 10:
                        enemy = self.WideEnemy(character_size)
                if game_system.level >= 6:
                    random_number = randint(0, 100)
                    if random_number <= 10:
                        enemy = self.InvisibleEnemy(character_size)
                if game_system.level >= 7:
                    random_number = randint(0, 100)
                    if random_number <= 10:
                        enemy = self.StupidEnemy(character_size)
                if game_system.level >= 8:
                    random_number = randint(0, 100)
                    if random_number <= 10:
                        enemy = self.BetterEnemy(character_size)
                if game_system.level >= 9:
                    random_number = randint(0, 100)
                    if random_number <= 10:
                        enemy = self.TrapEnemy(character_size)
                if game_system.level >= 10:
                    random_number = randint(0, 100)
                    if random_number <= 10:
                        enemy = self.CrazyEnemy(character_size)
                if game_system.level >= 11:
                    random_number = randint(0, 100)
                    if random_number <= 10:
                        enemy = self.TrickyEnemy(character_size)
                if game_system.level >= 12:
                    random_number = randint(0, 100)
                    if random_number <= 10:
                        enemy = self.WeirdEnemy(character_size)
                if enemy == "":
                    enemy = self.NormalEnemy(character_size)

            enemy_x_pos = randint(0,int(self.WINDOW_WIDTH - enemy.character_width))
            enemy_y_pos = randint(0, 26 * int(h))
            enemy_position = [enemy_x_pos, enemy_y_pos,
                              enemy_x_pos + enemy.character_width,
                              enemy_y_pos + enemy.character_height]

            for number in range(len(game_system.character)):
                if number == 0:
                    existing_position = self.canvas.coords(game_system.character[0].identifier)
                else:
                    existing_position = game_system.character[number].xy
                if existing_position[0] - 3 < enemy_position[2] and \
                        existing_position[2] > enemy_position[0] - 3 \
                        and existing_position[1] - 3 < enemy_position[3] and \
                        existing_position[3] > enemy_position[1] - 3:
                    overlap = True
            if not overlap:
                enemy.xy = enemy_position
                if enemy.color == "":
                    enemy.identifier = self.canvas.create_rectangle(
                        enemy.xy, width=3)
                elif enemy.color == "Trap":
                    enemy.identifier = self.canvas.create_rectangle(
                        enemy.xy, width=1)
                else:
                    enemy.identifier = self.canvas.create_rectangle(
                        enemy.xy, fill=enemy.color)
                game_system.character.append(enemy)
                enemy_count += 1

    def character_growth(self):
        game_system.score = game_system.score + 10
        self.life = self.generating_statistic()
        game_system.character[0].character_size = \
            game_system.character[0].character_size \
            * game_system.scale_factor + 100 \
            * game_system.difficulty * game_system.scale_factor
        if game_system.player_choice == 0:
            game_system.character[0].character_height = \
                game_system.character[0].character_size ** (1 / 2)
            game_system.character[0].character_width = \
                game_system.character[0].character_size ** (1 / 2)
        elif game_system.player_choice == 1:
            game_system.character[0].character_height = \
                game_system.character[0].character_size ** (1 / 2)
            game_system.character[0].character_width = \
                game_system.character[0].character_size ** (1 / 2)
        elif game_system.player_choice == 2:
            game_system.character[0].character_height = \
                (game_system.character[0].character_size / 3) ** (1 / 2)
            game_system.character[0].character_width = \
                (game_system.character[0].character_size / 3) ** (1 / 2) * 3
        elif game_system.player_choice == 3:
            game_system.character[0].character_height = \
                game_system.character[0].character_size ** (1 / 2)
            game_system.character[0].character_width = \
                game_system.character[0].character_size ** (1 / 2)

        position = self.canvas.coords(game_system.character[0].identifier)
        center_position = [(position[0] + position[2]) / 2,
                           (position[1] + position[3]) / 2]
        new_position = [
            center_position[0] - game_system.character[0].character_width / 2,
            center_position[1] - game_system.character[0].character_height / 2,
            center_position[0] + game_system.character[0].character_width / 2,
            center_position[1] + game_system.character[0].character_height / 2
        ]
        game_system.character[0].xy = new_position
        self.canvas.coords(game_system.character[0].identifier,
                      game_system.character[0].xy)
        self.enemy_recolor()

    def enemy_recolor(self):
        for number in range(len(game_system.character) - 1):
            enemy_number = number + 1
            if game_system.character[enemy_number].color != "" and \
                    game_system.character[enemy_number].color != "Trap":
                self.canvas.itemconfig(
                    game_system.character[enemy_number].identifier,
                    fill="grey")
            if game_system.character[enemy_number].color != "" and \
                    game_system.character[enemy_number].color != "Trap":
                self.canvas.itemconfig(
                    game_system.character[enemy_number].identifier,
                    fill=game_system.character[enemy_number].color)

            if game_system.character[enemy_number].character_size < \
                    game_system.character[0].character_size:
                self.canvas.itemconfig(
                    game_system.character[enemy_number].identifier,
                    fill="yellow")

    def check_character_boarder(self):
        if game_system.life > 0:
            self.character_save = open("./saves/character_saves.txt", "w+")
            position = self.canvas.coords(game_system.character[0].identifier)
            self.character_save.write(str(game_system.score))
            self.character_save.write("\n" + str(game_system.life))
            self.character_save.write("\n" + str(
                (position[0] + position[2]) / 2 * game_system.scale_factor))
            self.character_save.write("\n" + str(
                (position[1] + position[3]) / 2 * game_system.scale_factor))
        if game_system.entry.get() != "":
            self.character_save.write("\n" + str(game_system.entry.get()))
        else:
            self.character_save.write("\n" + "bob")
        self.character_save.write("\n" + str(game_system.player_choice))
        self.character_save.write("\n" + str(game_system.level))

        self.character_save.close()

        if position[0] < 0:
            self.canvas.coords(game_system.character[0].identifier, WINDOW_WIDTH,
                          position[1],
                          WINDOW_WIDTH -
                          game_system.character[0].character_width,
                          position[3])
        elif position[2] > WINDOW_WIDTH:
            self.canvas.coords(game_system.character[0].identifier,
                          game_system.character[0].character_width,
                          position[1], 0,
                          position[3])
        elif position[3] > WINDOW_HEIGHT:
            self.canvas.coords(game_system.character[0].identifier,
                          position[0],
                          game_system.character[0].character_height,
                          position[2],
                          0)
        elif position[1] < 0:
            self.canvas.coords(game_system.character[0].identifier, position[0],
                          WINDOW_HEIGHT, position[2],
                          WINDOW_HEIGHT -
                          game_system.character[0].character_height)
        removed_character = 0
        for character_i in range(len(game_system.character) - 1):
            character_i = character_i + 1 - removed_character
            position_i = self.canvas.coords(
                game_system.character[character_i].identifier)
            if position_i[0] < position[2] and position_i[2] > \
                    position[0] and position_i[1] < position[3] and \
                    position_i[3] > position[1]:

                if game_system.character[character_i].character_size < \
                        game_system.character[0].character_size or \
                        game_system.cheat:
                    self.canvas.delete(game_system.character[
                                      character_i].identifier)
                    game_system.character.remove(
                        game_system.character[character_i])
                    self.character_growth()
                    removed_character += 1
                else:
                    self.lose_life()
                    print(position_i, position)
                    if position[0] > position_i[0]:
                        self.collide[0] = -5
                    if position[2] < position_i[2]:
                        self.collide[1] = -5
                    if position[1] < position_i[1]:
                        self.collide[3] = -5
                    if position[3] > position_i[3]:
                        self.collide[2] = -5

    def check_enemy_boarder(self):
        removed_character = 0
        self.saved_file = open("./saves/enemy_saves.txt", "w+")
        for character_i in range(len(game_system.character) - 1):
            character_i = character_i + 1 - removed_character
            count = 1
            position_i = self.canvas.coords(
                game_system.character[character_i].identifier)

            # save_position_i = []
            # current_score = self.score
            for number in range(4):
                self.saved_file.write("\n" + str(
                    position_i[number] * game_system.scale_factor))

            if position_i[0] <= 0:
                game_system.character[character_i].character_attribute[0] = - \
                    game_system.character[character_i].character_attribute[0]
            elif position_i[2] >= WINDOW_WIDTH:
                game_system.character[character_i].character_attribute[0] = - \
                    game_system.character[character_i].character_attribute[0]
            elif position_i[3] >= WINDOW_HEIGHT:
                game_system.character[character_i].character_attribute[1] = - \
                    game_system.character[character_i].character_attribute[1]
            elif position_i[1] <= 0:
                game_system.character[character_i].character_attribute[1] = - \
                    game_system.character[character_i].character_attribute[1]
            else:
                count -= 1
                for character_j in range(len(game_system.character)):
                    character_j = character_j - removed_character
                    if character_i != character_j:
                        position_j = self.canvas.coords(
                            game_system.character[character_j].identifier)
                        if position_i[0] < position_j[2] and position_i[2] > \
                                position_j[0] and position_i[1] < \
                                position_j[3] and position_i[3] > \
                                position_j[1]:
                            if character_j == 0:
                                if game_system.character[
                                    character_i].character_size < \
                                        game_system.character[
                                            character_j].character_size or \
                                        game_system.cheat:
                                    self.canvas.delete(game_system.character[
                                                      character_i].identifier)
                                    game_system.character.remove(
                                        game_system.character[character_i])
                                    removed_character += 1
                                    self.character_growth()
                                    break
                                else:
                                    self.lose_life()
                            count += 1
                            if count <= 1:
                                game_system.character[
                                    character_i].character_attribute[0] = - \
                                    game_system.character[
                                        character_i].character_attribute[0]
                                game_system.character[
                                    character_i].character_attribute[1] = - \
                                    game_system.character[
                                        character_i].character_attribute[1]
        self.saved_file.close()

    def lose_life(self):
        game_system.lost_life = True

    def character_movement(self):
        if game_system.game_running:
            if not game_system.pause:
                self.check_character_boarder()
                if self.direction == "left":
                    self.canvas.move(game_system.character[0].identifier,
                                game_system.scale_factor * self.collide[0] * -
                                game_system.character[0].character_attribute[
                                    1], 0)
                elif self.direction == "right":
                    self.canvas.move(game_system.character[0].identifier,
                                game_system.scale_factor * self.collide[1] *
                                game_system.character[0].character_attribute[
                                    3], 0)
                elif self.direction == "up":
                    self.canvas.move(game_system.character[0].identifier, 0,
                                game_system.scale_factor * self.collide[2] * -
                                game_system.character[0].character_attribute[
                                    0])
                elif self.direction == "down":
                    self.canvas.move(game_system.character[0].identifier, 0,
                                game_system.scale_factor * self.collide[3] *
                                game_system.character[0].character_attribute[
                                    2])
                    # repeat movement
                self.collide = [1, 1, 1, 1]
            self.canvas.after(game_system.character[0].character_attribute[4],
                         self.character_movement)

    def enemy_movement(self):
        if game_system.game_running:
            self.check_enemy_boarder()
            if not game_system.pause and self.ability != "stop":
                if len(game_system.character) == 1:
                    game_system.win = True
                    game_system.game_running = False
                else:
                    for character in range(len(game_system.character) - 1):
                        enemy = character + 1
                        self.canvas.move(game_system.character[enemy].identifier,
                                    game_system.scale_factor *
                                    game_system.character[
                                        enemy].character_attribute[0],
                                    game_system.scale_factor *
                                    game_system.character[
                                        enemy].character_attribute[1])
            self.canvas.after(10, self.enemy_movement)

    def character_ability(self):
        if game_system.character[0].ability == "bend_time":
            self.ability_mechanism += 1
            frequency = randint(0, 50)
            if self.ability_mechanism >= frequency:
                self.ability = "stop"
                self.enemy_recolor()
                self.ability_mechanism = 0
            if self.ability_mechanism == 4 and self.ability == "stop":
                self.ability = "continue"
                self.enemy_recolor()
                self.ability_mechanism = 0
            self.canvas.after(1000, self.character_ability)

    def __init__(self, system):
        self.WINDOW_WIDTH = system.WINDOW_WIDTH
        self.WINDOW_HEIGHT = system.WINDOW_HEIGHT
        self.canvas = system.canvas
        self.w = system.w
        self.h = system.h
        self.start_position = [6 * w, 29 * h]
        self.position = []
        self.collide = [1, 1, 1, 1]
        self.key = [0, 0, 0, 0]
        self.direction = "0"
        self.ability = False
        self.ability_mechanism = 0
        self.character_ability
        self.life = None