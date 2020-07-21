from random import randint
from PIL import Image, ImageTk


class TextAdventure:

    def generating_story(self):
        if len(game_system.design) > 0:
            for number in range(len(game_system.design)):
                canvas.delete(game_system.design[number].identifier)
                canvas.delete(game_system.design[number].identifier_text)
                game_system.design = []
        if len(game_system.character) > 0:
            for number in range(len(game_system.character)):
                canvas.delete(game_system.character[number].identifier)
                game_system.character = []

    class Player:
        def __init__(self, size, width, height, attribute):
            self.character_size = size
            self.character_width = width
            self.character_height = height
            self.character_attribute = attribute

    class Box:
        def creating_text_box(self, index):
            center_position = [(game_system.design[index].xy[0] +
                                game_system.design[index].xy[2]) / 2,
                               (game_system.design[index].xy[1] +
                                game_system.design[index].xy[3]) / 2]
            game_system.design[index].identifier = canvas.create_text(
                center_position, fill="white",
                font="Times 10",
                text=game_system.design[index].text[0])
            center_position[1] = center_position[1] + 15
            game_system.design[index].identifier_text = canvas.create_text(
                center_position, fill="white",
                font="Times 10",
                text=game_system.design[index].text[1])

        def __init__(self, xy, text=[]):
            self.xy = xy
            self.text = text

    def character_boxes(self):
        # creating Box
        game_system.design.append(self.Box([3 * w, 12 * h, 6 * w, 18 * h],
                                           ["He is fast",
                                            "maybe a bit too fast"]))
        game_system.design.append(self.Box([6 * w, 12 * h, 9 * w, 18 * h],
                                           ["Brave and Fearless",
                                            "he never go down"]))
        game_system.design.append(self.Box([3 * w, 18 * h, 6 * w, 24 * h],
                                           ["Only good",
                                            "at moving horizontally"]))
        game_system.design.append(self.Box([6 * w, 18 * h, 9 * w, 24 * h],
                                           ["He bends time", "randomly"]))

        for number in range(4):
            self.Box.creating_text_box(self, number)

    def character_creation(self):
        game_system.character.append(
            self.Player(900, 900 ** (1 / 2), 900 ** (1 / 2),
                        [10, 10, 10, 10, 10]))
        game_system.character[0].xy = [
            4.5 * w - game_system.character[0].character_width / 2,
            13.5 * h,
            4.5 * w + game_system.character[0].character_width / 2,
            13.5 * h + game_system.character[0].character_height]
        game_system.character[0].identifier = (
            canvas.create_rectangle(game_system.character[0].xy, fill="white"))
        game_system.character[0].ability = "Teleport"

        game_system.character.append(
            self.Player(900, 900 ** (1 / 2), 900 ** (1 / 2), [6, 4, 1, 4, 10]))
        game_system.character[1].xy = [
            7.5 * w - game_system.character[1].character_width / 2,
            13.5 * h,
            7.5 * w + game_system.character[1].character_width / 2,
            13.5 * h + game_system.character[1].character_height]
        game_system.character[1].identifier = (
            canvas.create_oval(game_system.character[1].xy, fill="white"))
        game_system.character[1].ability = None

        game_system.character.append(
            self.Player(900, 3 * 300 ** (1 / 2), 300 ** (1 / 2),
                        [1, 5, 1, 5, 10]))
        game_system.character[2].xy = [
            4.5 * w - game_system.character[2].character_width / 2,
            19.5 * h,
            4.5 * w + game_system.character[2].character_width / 2,
            19.5 * h + game_system.character[2].character_height]
        game_system.character[2].identifier = (
            canvas.create_rectangle(game_system.character[2].xy, fill="white"))
        game_system.character[2].ability = None

        game_system.character.append(
            self.Player(900, 900 ** (1 / 2), 900 ** (1 / 2), [2, 2, 2, 2, 10]))
        game_system.character[3].xy = [
            7.5 * w - game_system.character[3].character_width / 2,
            19.5 * h,
            7.5 * w + game_system.character[3].character_width / 2,
            19.5 * h + game_system.character[3].character_height]
        game_system.character[3].identifier = (
            canvas.create_rectangle(game_system.character[3].xy, fill="white"))
        game_system.character[3].ability = "bend_time"

    def __init__(self, battle):
        GameSystem.texture_size = [200, 200]
        self.theme = []
        self.battle = battle
        self.story = []
        self.choices = choices
        self.decisions = []