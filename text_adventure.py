class TextAdventure:

    def generating_texture(self, change_color):
        if self.theme == [] or change_color:
            styles = [3, 2, 1, 1, 3, 2, 1, 6, 0, 0, 0, 3, 5, 4]
            texture_num_a = styles[randint(0, 6)] + 1
            texture_num_b = styles[-randint(0, 6) - 1] + 1
            while texture_num_a == texture_num_b or texture_num_a == 0 or \
                    texture_num_b == 0:
                texture_num_a = randint(0, 4)
            self.theme = []
            self.theme.append(texture_num_a)
            self.theme.append(texture_num_b)

        self.texture_a = Image.open("./texture/tile_" + str(self.theme[0]) + "_full.png")
        self.texture_b = Image.open("./texture/tile_" + str(self.theme[1]) + "_full.png")
        self.texture_a = self.texture_a.resize((int(
            GameSystem.texture_size[0]), int(GameSystem.texture_size[1])),
            Image.ANTIALIAS)
        self.texture_a = ImageTk.PhotoImage(self.texture_a)
        self.texture_b = self.texture_b.resize((int(
            GameSystem.texture_size[0]), int(GameSystem.texture_size[1])),
            Image.ANTIALIAS)
        self.texture_b = ImageTk.PhotoImage(self.texture_b)

        count = 0
        for number in range(int(WINDOW_HEIGHT / GameSystem.texture_size[1])):

            #
            height = GameSystem.texture_size[1] * number
            if int(WINDOW_WIDTH / GameSystem.texture_size[0]) % 2 == 0:
                count += 1
            for number in range(int(WINDOW_WIDTH /
                                    GameSystem.texture_size[0])):
                width = GameSystem.texture_size[0] * number
                count += 1
                GameSystem.textures = []
                if count % 2 == 0:
                    GameSystem.textures.append(
                        canvas.tag_lower(
                            canvas.create_image(
                                width,
                                height,
                                image=self.texture_a, anchor=NW)))
                else:
                    GameSystem.textures.append(
                        canvas.tag_lower(canvas.create_image(
                            width,
                            height,
                            image=self.texture_b, anchor=NW)))
        return self.texture_b, self.texture_a

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

    def clear_screen(self):
        try:
            for number in range(len(game_system.character)):
                if number != game_system.player_choice:
                    canvas.delete(game_system.character[number].identifier)
        except:
            pass
        try:
            if game_system.player_choice != "":
                game_system.character = [game_system.character[
                                             game_system.player_choice]]
        except:
            pass
        try:
            for number in range(len(game_system.design)):
                canvas.delete(game_system.design[number].identifier)
        except:
            pass
        try:
            for number in range(len(game_system.design)):
                canvas.delete(game_system.design[number].identifier_text)
        except:
            pass
        if len(game_system.identifier) > 0:
            for number in range(len(game_system.identifier)):
                canvas.delete(game_system.identifier[number])

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