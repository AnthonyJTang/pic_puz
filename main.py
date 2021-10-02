
import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image as im


Builder.load_file('images.kv')
Window.size = (800, 800)


def get_image():
    return "./doge.jpg"
    # copy from url


def splitter(pic):
    os.system(f'split-image {pic} 3 3 -s'.format(pic))


class MyLayout(Widget):
    pass


class PicPuz(Widget):

    def update(self, dt):
        pass

    def shuffle(self):
        print("Shuffling images")
        grid = GridLayout(rows=3, cols=3)
        i = 0
        img = im(source=f"_{i}.png".format(i))
        for _ in range(grid.rows * grid.cols):
            grid.add_widget(img)
            i += 1
        return grid

    def switch_tiles(self):
        pass

    def on_touch(self):
        pass
        # if first click note
        # if second is valid to swap click switch


tiles = []


class PicGame(App):
    def build(self):
        game = PicPuz()
        Window.clearcolor = (1,1,1,1)
        game.shuffle()
        return game


if __name__ == '__main__':

    image = get_image()
    splitter(image)
    # read in the split images as an array
    PicGame().run()

    # start main kivy gameloop



