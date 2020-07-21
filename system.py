from tkinter import Tk

class System:

    def clear_screen(self):
        try:
            for number in range(len(game_system.character)):
                if number != game_system.player_choice:
                    canvas.delete(game_system.character[number].identifier)
        except: pass
        try:
            if game_system.player_choice != "":
                game_system.character = [game_system.character[
                                             game_system.player_choice]]
        except: pass
        try:
            for number in range(len(game_system.design)):
                canvas.delete(game_system.design[number].identifier)
        except: pass
        try:
            for number in range(len(game_system.design)):
                canvas.delete(game_system.design[number].identifier_text)
        except: pass
        if len(game_system.identifier) > 0:
            for number in range(len(game_system.identifier)):
                canvas.delete(game_system.identifier[number])


    def fullscreen(self):
        if self.window.attributes('-fullscreen'):
            self.window.attributes('-fullscreen', False)
        else:
            self.window.attributes('-fullscreen', True)

    def resize_canvas(self, event):
        GameSystem.pause = True
        self.window_ratio = self.WINDOW_WIDTH /  self.WINDOW_HEIGHT
        self.zoom_ratio = [event.height * self.window_ratio / self.WINDOW_WIDTH,
                           event.height /  self.WINDOW_HEIGHT]
        WINDOW_HEIGHT = event.height
        WINDOW_WIDTH = event.height * self.window_ratio
        GameSystem.texture_size = [WINDOW_WIDTH / 4, WINDOW_HEIGHT / 5]
        self.canvas.addtag_all("all")
        self.canvas.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.scale("all", 0, 0,  self.zoom_ratio[0], self.zoom_ratio[1])

        w = WINDOW_WIDTH / 12
        h = WINDOW_HEIGHT / 30
        self.scale_factor = self.zoom_ratio[1] * WINDOW_HEIGHT / 1000
        self.text_adventure.texture_a, self.text_adventure.texture_b = self.text_adventure.generating_texture(False)
        GameSystem.pause = False

    def __init__(self):
        # configuring self.window
        self.window = Tk()
        self.SCREEN_WIDTH = self.window.winfo_screenwidth()
        self.SCREEN_HEIGHT = 1000
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = self.SCREEN_HEIGHT
        CENTER_WIDTH = self.SCREEN_WIDTH / 2 - self.WINDOW_WIDTH / 2
        CENTER_HEIGHT = 0
        self.window.title("ASDF")
        self.window.geometry("%dx%d+%d+%d" % (WINDOW_WIDTH, WINDOW_HEIGHT, CENTER_WIDTH, CENTER_HEIGHT))

        # TODO make self.w and self.h into properties
        # defining width and height unit
        self.w = self.WINDOW_WIDTH / 12
        self.h = self.WINDOW_HEIGHT / 30

        # configuring self.canvas
        self.canvas = Canvas(self.window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack(fill="both", expand=TRUE)

        self.canvas.bind("<Configure>", self.resize_canvas)
        self.zoom_ratio = [1, 1]
        self.scale_factor = self.zoom_ratio[1] * WINDOW_HEIGHT / 1000