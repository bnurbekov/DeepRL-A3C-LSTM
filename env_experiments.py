import gym
from gym import envs
import gym_pull
from gym import wrappers

if __name__ == "__main__":
	# env = gym.make('CartPole-v0')
	# env = wrappers.Monitor(env, '/tmp/cartpole-experiment-1', force=True)

	# for i_episode in range(20):
	# 	observation = env.reset()
	# 	for t in range(100):
	# 		env.render()
	# 		print(observation)
	# 		action = env.action_space.sample()
	# 		observation, reward, done, info = env.step(action)

	# 		if done:
	# 			print("Episode finished after {} timesteps".format(t+1))
	# 			break


	# # print(env.action_space)
	# # print(env.observation_space)
	# # print(envs.registry.all())
	gym_pull.pull('github.com/ppaquette/gym-doom')

