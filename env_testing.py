from environment import Environment
import numpy as np
import random

if __name__ == "__main__":
    config_file_path = "assets/simpler_basic.cfg"
    # Sets time that will pause the engine after each action (in seconds)
    # Without this everything would go too fast for you to keep track of what's happening.
    sleep_time = 1.0 / 35 # = 0.028
    env = Environment(config_file_path, set_window_visible=True, sleep_time=sleep_time)

    for i_episode in range(20):
        observation = env.reset()
        for t in range(100):
            action = random.choice(env.action_space).tolist()
            observation, reward, done, info = env.step(action)
            print(observation)

            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break

