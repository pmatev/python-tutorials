#
# cocos2d
# http://python.cocos2d.org
#

from __future__ import division, print_function, unicode_literals

# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

import cocos



class Ball(cocos.sprite.Sprite):

    def update(self):
        self.position = (self.position[0] + 1, self.position[1] + 1)


class GameWorld(cocos.layer.Layer):

    is_event_handler = True     #: enable pyglet's events

    def __init__(self):
        super(GameWorld, self).__init__()

        self.ball = Ball('ball.png')

        self.add(self.ball)
        self.schedule(self.update)

    def update(self, dt):
        self.ball.update()


if __name__ == "__main__":
    # director init takes the same arguments as pyglet.window
    cocos.director.director.init()

    # We create a new layer, an instance of GameWorld
    hello_layer = GameWorld()

    # A scene that contains the layer hello_layer
    main_scene = cocos.scene.Scene(hello_layer)

    # And now, start the application, starting with main_scene
    cocos.director.director.run(main_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( GameWorld() ) )
