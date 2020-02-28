# Exercise 2.5
# Difficulties for simple average method for non stationary Bandit problems
import numpy as np
import matplotlib.pyplot as plt


# Adding non-stationary rewards
def calc_reward():
	return np.random.normal(0,0.01)


def simple_avg_non_stationary_bandit():
	# k actions Lets assume k=10
	k = 10
	# Initialize the value for all the k actions as 0
	# reward_action = {}
	# for i in range(1, 11):
	# 	reward_action[1] = []
	mean_reward={}
	for i in range(1,11):
		mean_reward[i]=[0]
	alpha=0.2
	# Loop forever (By forever means very long term say 20k times)
	counter = 0
	prob_ctr = 0
	while counter < 20000:
		rewards = {}
		counter += 1
		prob_ctr += 1
		for i in range(1, 11):
			rewards[i] = calc_reward()

		if prob_ctr< 10:
			# Exploitation
			# Get the best action
			action, max_rewards = sorted(rewards.items(), key= lambda kv:(kv[1],kv[0]))[-1]
			# Update the mean reward using avg. method
		else:
			# Exploration
			action = np.random.randint(1,11)
			max_rewards = rewards[action]
			prob_ctr = 0
		mean_reward[action].append(mean_reward[action][-1] +
								   alpha*(max_rewards-mean_reward[action][-1]))
	return mean_reward
	# Update the average rewards for each action


def plot(reward_action):
	plt.plot()


if __name__ == '__main__':
	reward_action = simple_avg_non_stationary_bandit()
	best_action = 0
	max_reward=0
	for k in reward_action.keys():
		if sum(reward_action[k]) > max_reward:
			best_action = k
			max_reward = sum(reward_action[k])
	# plot(reward_action[best_action])
	print(max_reward)
	print(best_action)
	print(reward_action)
