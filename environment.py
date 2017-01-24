from vizdoom import *
import numpy as np
from time import sleep

class Environment:
    def __init__(self, 
                config_file_path, 
                mod=Mode.PLAYER, 
                set_window_visible=False, 
                screen_format=ScreenFormat.GRAY8, 
                screen_resolution=ScreenResolution.RES_640X480,
                sleep_time=0):
        print("Initializing doom...")
        self.game = DoomGame()
        self.game.load_config(config_file_path)
        self.game.set_window_visible(set_window_visible)
        self.game.set_mode(mod)
        self.game.set_screen_format(screen_format)
        self.game.set_screen_resolution(screen_resolution)
        self.game.init()
        self.action_space = np.diag([1]*self.game.get_available_buttons_size())
        self.frame_repeat = 12
        self.sleep_time = sleep_time
        print("Doom initialized.")

    def reset(self):
        self.game.new_episode()
        return self.game.get_state().screen_buffer

    def step(self, action):
        reward = self.game.make_action(action, self.frame_repeat)

        if self.sleep_time > 0:
            sleep(self.sleep_time)

        return self.game.get_state().screen_buffer, reward, self.game.is_episode_finished(), None





