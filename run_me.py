import os
from tkinter import *
from random import *
from battle import Battle
from text_adventure import TextAdventure
from system import System

class GameSystem:

    def boss_key(self):
        if not self.boss:
            game_system.pause = True
            screen_shot = PhotoImage(file="./texture/boss_key.png")
            self.boss = self.canvas.create_image(0, 0, image=screen_shot, anchor=NW)
            self.fullscreen()
            return screen_shot
        else:
            self.canvas.delete(self.boss)
            game_system.pause = False
            self.boss = False
            self.fullscreen()

    def deactivate_mouse(self):
        self.canvas.unbind("<Button-1>")

    def activate_mouse(self):
        self.canvas.bind("<Button-1>", self.click_event)

    def activate_keyboard(self):
        self.canvas.bind("<KeyPress>", self.key_pressed)
        self.canvas.bind("<KeyRelease>", self.key_released)
        self.canvas.focus_set()

    def click_event(self, event):
        x = event.x
        y = event.y
        for number in range(len(game_system.character)):
            if game_system.design[number].xy[0] <= x <= \
                    game_system.design[number].xy[2] and \
                    game_system.design[number].xy[
                        1] <= y <= \
                    game_system.design[number].xy[3]:
                game_system.player_choice = number
                self.text_adventure.clear_screen()
                self.deactivate_mouse()
                self.activate_keyboard()
                self.battle.move_start_position()

    def key_pressed(self, event):
        if event.keysym == "Left":
            self.battle.direction = "left"
            self.battle.key[0] = 1
        elif event.keysym == "Right":
            self.battle.direction = "right"
            self.battle.key[1] = 1
        elif event.keysym == "Up":
            self.battle.direction = "up"
            self.battle.key[2] = 1
        elif event.keysym == "Down":
            self.battle.direction = "down"
            self.battle.key[3] = 1
        elif event.keysym == "c":
            game_system.cheat = not game_system.cheat
        elif event.keysym == "s":
            game_system.score = game_system.score + 10
            self.battle.life = self.battle.generating_statistic()
        elif event.keysym == "h":
            game_system.life = game_system.life + 1
            self.battle.life = self.battle.generating_statistic()
        elif event.keysym == "space":
            self.pause_count = 0
            self.pausing()
        elif event.keysym == "b":
            self.screen_shot = self.boss_key()

    def pausing(self):
        try:
            self.canvas.delete(self.pause_text)
        except:
            pass

        if self.pause_count > 3:
            self.pause_text = ""
        if self.pause_count == 3:
            game_system.pause = not game_system.pause
            try:
                self.battle.enemy_recolor()
            except:
                pass
            if game_system.pause:
                self.pause_text = self.canvas.create_text(
                    6 * w, 6 * h,
                    text="PAUSED",
                    font="times 30 bold italic",
                    fill="white")
            elif not game_system.pause:
                self.pause_text = self.canvas.create_text(
                    6 * w, 6 * h,
                    text="UNPAUSE",
                    font="times 30 bold italic",
                    fill="white")
            self.pause_count += 1

        if 0 <= self.pause_count < 3:
            self.pause_text = self.canvas.create_text(6 * w, 6 * h, text=str(
                3 - self.pause_count), font="times 30 bold italic",
                                                 fill="white")
            self.pause_count += 1

        if self.pause_text != "":
            self.canvas.after(1000, self.pausing)

    def key_released(self, event):
        if sum(self.battle.key) <= 1:
            self.battle.direction = "0"
        if event.keysym == "Left":
            self.battle.key[0] = 0
        if event.keysym == "Right":
            self.battle.key[1] = 0
        if event.keysym == "Up":
            self.battle.key[2] = 0
        if event.keysym == "Down":
            self.battle.key[3] = 0
        for number in range(4):
            if self.battle.key[number] == 1:
                if number == 0:
                    self.battle.direction = "left"
                elif number == 1:
                    self.battle.direction = "right"
                elif number == 2:
                    self.battle.direction = "up"
                elif number == 3:
                    self.battle.direction = "down"

    def play(self, saved_game):
        self.game_running = True
        self.save_game = saved_game
        for number in range(len(self.textures)):
            self.canvas.delete(self.textures[number])
        self.text_adventure.texture_a, self.text_adventure.texture_b = \
            self.text_adventure.generating_texture(
                True)
        if not self.save_game:
            self.text_adventure.clear_screen()
            self.text_adventure.character_boxes()
            self.text_adventure.character_creation()
        elif self.save_game:
            character_save = open("./saves/character_saves.txt", "r+")
            character = [line.rstrip("\n") for line in
                         character_save.readlines()]
            character_save.close()

            self.text_adventure.clear_screen()

            self.life = int(character[1])
            self.battle.start_position[0] = float(character[2])
            self.battle.start_position[1] = float(character[3])

            self.player_choice = int(character[5])
            if self.level < int(character[6]):
                self.level = int(character[6])
            if self.score < int(character[0]):
                self.score = int(character[0])
            self.text_adventure.character_creation()
            self.deactivate_mouse()
            self.text_adventure.clear_screen()

            self.battle.move_start_position()
            self.battle.life = self.battle.generating_statistic()

        return self.battle.generating_statistic(), \
               self.text_adventure.texture_a, \
               self.text_adventure.texture_b

    def check_game_status(self):
        if self.lost_life:
            game_system.life = game_system.life - 1
            self.battle.life = self.battle.generating_statistic()
            self.lost_life = False
            if game_system.life <= 0:
                game_system.lose = True
                self.game_running = False
        if self.win or self.lose or self.you_win != 0:
            self.game_running = False
            self.text_adventure.clear_screen()
            if self.lose:
                try:
                    self.canvas.delete(game_system.character[0].identifier)
                    self.canvas.delete(game_system.level_identifier)
                    self.canvas.delete(game_system.score_identifier)
                    for number in range(len(game_system.life_identifier)):
                        self.canvas.delete(game_system.life_identifier[number])
                    game_system.character = []
                    self.user_name = self.entry.get()
                    if self.user_name == "":
                        self.user_name = "Bob"
                except:
                    pass
                self.leader_list = open("./saves/player_records.txt", "r+")
                self.leaders[int(self.score)] = self.user_name
                self.leader_list.seek(0,
                                      os.SEEK_END)
                self.leader_list.write(
                    "\n" + str(self.score) + "\n" + str(self.user_name))
                self.leader_list.close()
                if self.you_lost == 0:
                    self.final_message = self.canvas.create_text(
                        6 * w, 15 * h,
                        text="YOU LOST",
                        fill="white",
                        font="times 40 bold italic")
                self.you_lost += 1
                if self.you_lost == 10:
                    self.canvas.delete(self.final_message)
                    self.level = 1
                    self.game_setup()
                    self.menu()
            if self.level >= 13 and self.final_message == "":
                self.final_message = self.canvas.create_text(
                    6 * w, 15 * h,
                    text="YOU WIN",
                    fill="white",
                    font="times 40 bold italic")
                self.win = False
                self.score = int(self.score) + 10
                self.canvas.delete(game_system.character[0].identifier)
                self.canvas.delete(game_system.level_identifier)
                self.canvas.delete(game_system.score_identifier)
                for number in range(len(self.textures)):
                    self.canvas.delete(self.textures[number])
                    self.text_adventure.texture_a, \
                    self.text_adventure.texture_b = \
                        self.text_adventure.generating_texture(
                            True)
                game_system.character = []
                for number in range(len(game_system.life_identifier)):
                    self.canvas.delete(game_system.life_identifier[number])
                try:
                    for number in range(len(game_system.character)):
                        if number != game_system.player_choice:
                            self.canvas.delete(
                                game_system.character[number].identifier)
                except:
                    pass
            if self.level >= 13:
                self.you_win += 1
            if self.you_win == 15:
                self.canvas.delete(self.final_message)
                self.lose = True
                self.level = 1
                self.game_setup()
                self.menu()
            if self.win:
                self.score = int(self.score) + 10
                self.win = False
                self.canvas.delete(game_system.character[0].identifier)
                self.canvas.delete(game_system.level_identifier)
                self.canvas.delete(game_system.score_identifier)
                for number in range(len(self.textures)):
                    self.canvas.delete(self.textures[number])
                    self.text_adventure.texture_a, \
                    self.text_adventure.texture_b = \
                        self.text_adventure.generating_texture(
                            True)
                game_system.character = []
                for number in range(len(game_system.life_identifier)):
                    self.canvas.delete(game_system.life_identifier[number])
                self.level = self.level + 1
                self.play(True)
        self.canvas.after(500, self.check_game_status)

    def menu(self):
        self.activate_mouse()
        self.text_adventure.texture_a, self.text_adventure.texture_b = \
            self.text_adventure.generating_texture(
                True)

        new_game = Button(text='Begin', command=lambda: self.play(False),
                          font="Times 8")
        saved_game = Button(text='Continue', command=lambda: self.play(True),
                            font="Times 8")

        self.entry = Entry(canvas)

        if self.leaders == {}:
            leaders = [line.rstrip("\n") for line in
                       self.leader_list.readlines()]  # strip line breaks
            for number in range(len(leaders)):
                if number % 2 == 0:
                    leaders[number] = int(leaders[number])
            for number in range(int(len(leaders) / 2)):
                self.leaders[leaders[2 * number]] = leaders[2 * number + 1]
        sorted_values = sorted(self.leaders.keys())

        character_save = open("./saves/character_saves.txt", "r+")
        character = [line.rstrip("\n") for line in character_save.readlines()]

        user_name = []
        user_score = []
        count = 0
        if count < len(sorted_values):
            for sorted_key in sorted_values:
                user_name.append(self.leaders[sorted_key])
                user_score.append(sorted_key)
                count += 1
        self.identifier.append(canvas.create_text(10.5 * w, 3 * h, text="F",
                                                  font="Times 120 italic",
                                                  fill="black"))
        self.identifier.append(canvas.create_text(7.5 * w, 3 * h, text="D",
                                                  font="Times 120 italic",
                                                  fill="white"))
        self.identifier.append(canvas.create_text(4.5 * w, 3 * h, text="S",
                                                  font="Times 120 italic",
                                                  fill="black"))
        self.identifier.append(canvas.create_text(1.5 * w, 3 * h, text="A",
                                                  font="Times 120 italic",
                                                  fill="white"))
        self.identifier.append(
            self.canvas.create_text(4.5 * w, 9 * h, text="LEADER",
                               font="Times 20 bold italic", fill="white"))
        self.identifier.append(
            self.canvas.create_text(7.5 * w, 9 * h, text="BOARD",
                               font="Times 20 bold italic", fill="white"))
        self.identifier.append(
            self.canvas.create_text(4.5 * w, 14 * h, text="First place",
                               font="Times 15 bold italic", fill="white"))
        self.identifier.append(
            self.canvas.create_text(7.5 * w, 14 * h, text="Second place",
                               font="Times 15 bold italic", fill="white"))
        self.identifier.append(
            self.canvas.create_text(4.5 * w, 20 * h, text="Third place",
                               font="Times 15 bold italic", fill="white"))
        self.identifier.append(
            self.canvas.create_text(7.5 * w, 20 * h, text="Forth place",
                               font="Times 15 bold italic", fill="white"))
        self.identifier.append(
            self.canvas.create_text(4.5 * w, 15.5 * h,
                               text=str(user_name[-1]) + " " + str(
                                   user_score[-1]),
                               font="Times 13 italic", fill="white"))
        self.identifier.append(
            self.canvas.create_text(7.5 * w, 15.5 * h,
                               text=str(user_name[-2]) + " " + str(
                                   user_score[-2]),
                               font="Times 13 italic", fill="white"))
        self.identifier.append(
            self.canvas.create_text(4.5 * w, 21.5 * h,
                               text=str(user_name[-3]) + " " + str(
                                   user_score[-3]),
                               font="Times 13 italic", fill="white"))
        self.identifier.append(
            self.canvas.create_text(7.5 * w, 21.5 * h,
                               text=str(user_name[-4]) + " " + str(
                                   user_score[-4]),
                               font="Times 13 italic", fill="white"))
        self.identifier.append(
            self.canvas.create_text(4.5 * w, 26 * h, text="And you are",
                               font="Times 15 bold italic", fill="white"))
        self.identifier.append(
            self.canvas.create_window(4.5 * w, 27 * h, self.window=self.entry,
                                 height=0.75 * h, width=2 * w))
        self.identifier.append(
            self.canvas.create_window(4.5 * w, 28 * h, self.window=new_game,
                                 width=1.5 * w, height=0.75 * h))

        self.identifier.append(
            self.canvas.create_text(7.5 * w, 26 * h, text="Or you were",
                               font="Times 15 bold italic", fill="white"))
        self.identifier.append(
            self.canvas.create_text(7.5 * w, 27 * h, text=str(character[4]),
                               font="Times 13 bold italic", fill="white"))
        self.identifier.append(
            self.canvas.create_window(7.5 * w, 28 * h, self.window=saved_game,
                                 width=1.5 * w, height=0.75 * h))

    def game_setup(self):
        self.pause_count = 0
        self.pause_text = ""
        self.you_lost = 0
        self.final_message = ""
        self.you_win = 0
        self.textures = []
        self.lost_life = False
        self.life_identifier = []
        self.player_choice = ""
        self.lose = False
        self.win = False
        self.game_running = False
        self.entry = None
        self.score = 0
        self.difficulty = 1
        self.cheat = False
        self.boss = False
        self.pause = False
        self.life = 10 * self.difficulty
        self.user_name = "BoB"
        self.xy = [[], []]
        self.design = []
        self.identifier = []
        self.activate_keyboard()

    def __init__(self, battle, text_adventure):
        self.pause_count = 0
        self.pause_text = ""
        self.you_lost = 0
        self.final_message = ""
        self.you_win = 0
        self.textures = []
        self.lost_life = False
        self.life_identifier = []
        self.player_choice = ""
        self.save_game = False
        self.lose = False
        self.win = False
        self.game_running = False
        self.entry = None
        self.score = 0
        self.difficulty = 1
        self.level = 1
        self.cheat = False
        self.boss = False
        self.pause = False
        self.life = 10 * self.difficulty
        self.user_name = "BoB"
        self.xy = [[], []]
        self.design = []
        self.identifier = []
        self.activate_keyboard()

        self.check_game_status()
        self.leader_list = open("./saves/player_records.txt", "r+")
        self.entry = None
        self.leaders = {}
        self.texture_size = [200, 200]
        self.battle = battle
        self.text_adventure = text_adventure
        self.default_size = 900
        self.character = []
        self.screen_shot = None
        self.menu()


system = System()
battle = Battle(system)

text_adventure = TextAdventure(battle)
game_system = GameSystem(battle, text_adventure)

# ball dissappear
# exit function
# collision bugs
# scoring
# save and quit
# double running play

# checked
# cheats
# better color
# bondary downward
# pause 3,2,1

system.window.mainloop()
