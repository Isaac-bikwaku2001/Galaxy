

from kivy.uix.relativelayout import RelativeLayout


def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None
    
def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    """
        Cette fonction se déclanche à l'appuie de la touche de direction gauche et droite du clavier
    """
    if keycode[1] == 'left':
        self.current_speed_x = self.SPEED_X
    elif keycode[1] == 'right':
        self.current_speed_x = -self.SPEED_X
    return True

def on_keyboard_up(self, keyboard, keycode):
    """
        Cette fonction se déclanche quand on rélache la touche
    """
    self.current_speed_x = 0
    
def on_touch_down(self, touch):
    """
        Cette fonction se déclenche quand on appuie sur l'écran (pour des téléphones)
    """
    # state_game_over = False
    # state_game_as_started = False

    if not self.state_game_over and self.state_game_as_started:
        if touch.x < self.width/2:
            # print("<--")
            self.current_speed_x = self.SPEED_X
        else:
            # print("-->")
            self.current_speed_x = -self.SPEED_X
    return super(RelativeLayout, self).on_touch_down(touch)

def on_touch_up(self, touch):
    """
        Cette fonction se déclenche quand on lache l'appuie sur l'écran (pour des téléphones)
    """
    # print("UP")
    self.current_speed_x = 0
