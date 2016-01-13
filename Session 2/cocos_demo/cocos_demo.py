from pyglet.window import key
import cocos


class Player(cocos.sprite.Sprite):
    scale = 2
    velocity_x = 0
    velocity_y = 0

    acceleration_x = 0
    acceleration_y = 0

    def update(self, dt):
        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y
        self.position = (self.position[0] + self.velocity_x, self.position[1] + self.velocity_y)


class HelloWorld(cocos.layer.Layer):

    is_event_handler = True     #: enable pyglet's events

    def __init__(self):
        super(HelloWorld, self).__init__()

        self.player = Player('fire.png')
        self.player.position = 320, 240

        self.add(self.player, z=1)

        self.schedule(self.update)

    def on_key_press(self, key_code, modifiers):
        """This function is called when a key is pressed.

        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
           modifiers are active at the time of the press (ctrl, shift, capslock, etc.)

        See also on_key_release situations when a key press does not fire an
         'on_key_press' event.
        """
        if key_code is key.LEFT:
            self.player.velocity_x -= 1
        elif key_code is key.RIGHT:
            self.player.velocity_x += 1
        elif key_code is key.UP:
            self.player.velocity_y += 1
        elif key_code is key.DOWN:
            self.player.velocity_y -= 1

    def update(self, dt):
        self.player.update(dt)



def main():
    cocos.director.director.init()

    main_scene = cocos.scene.Scene(HelloWorld())
    cocos.director.director.run(main_scene)


if __name__ == '__main__':
    main()
