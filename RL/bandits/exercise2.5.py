# Exercise 2.5
# Difficulties for simple average method for non stationary Bandit problems
import numpy as np
import matplotlib.pyplot as plt


# Adding non-stationary rewards
def calc_reward():
	# np.random.RandomState(1234)
	return np.random.normal(0, 1)


def simple_avg_non_stationary_bandit(init_reward,alpha, counter_max, prob_ctr_thres):
	# k actions Lets assume k=10
	k = 10
	# Initialize the value for all the k actions as 0
	# reward_action = {}
	# for i in range(1, 11):
	# 	reward_action[1] = []
	mean_reward = {}
	for i in range(1, 11):
		mean_reward[i] = [init_reward]
	# Loop forever (By forever means very long term say 20k times)
	counter = 0
	prob_ctr = 0
	while counter < counter_max:
		rewards = {}
		counter += 1
		prob_ctr += 1
		for i in range(1, 11):
			rewards[i] = calc_reward()

		if prob_ctr <= prob_ctr_thres:
			# Exploitation
			# Get the best action
			action, max_rewards = sorted(rewards.items(), key=lambda kv: (kv[1], kv[0]))[-1]
			# Update the mean reward using avg. method
		else:
			# Exploration
			action = np.random.randint(1, 11)
			max_rewards = rewards[action]
			prob_ctr = 0
		# Update the average rewards for each action
		mean_reward[action].append(mean_reward[action][-1] +
								   alpha*(max_rewards-mean_reward[action][-1]))
	print([(key,len(mean_reward[key]),sum(mean_reward[key])) for key in mean_reward.keys()])
	return mean_reward


def plot(reward_actions):
	for reward_action in reward_actions:
		x=range(len(reward_action))
		plt.plot(x, reward_action)
	plt.show()


def get_max_reward(reward_action):
	best_action = 0
	max_reward = 0
	for k in reward_action.keys():
		if sum(reward_action[k]) > max_reward:
			best_action = k
			max_reward = sum(reward_action[k])
	return best_action, max_reward


if __name__ == '__main__':
	reward_action = simple_avg_non_stationary_bandit(0, 0.005, 50000, 0)
	reward_action1 = simple_avg_non_stationary_bandit(0, 0.005, 50000, 2)
	reward_action2 = simple_avg_non_stationary_bandit(0, 0.005, 50000, 10)
	reward_action3 = simple_avg_non_stationary_bandit(2,0.005, 50000, 100)
	reward_action4 = simple_avg_non_stationary_bandit(2, 0.005, 50000, 1000)

	best_action, max_reward = get_max_reward(reward_action)
	best_action1, max_reward1 = get_max_reward(reward_action1)
	best_action2, max_reward2 = get_max_reward(reward_action2)
	best_action3, max_reward3 = get_max_reward(reward_action3)
	best_action4, max_reward4 = get_max_reward(reward_action4)
	print(max_reward,max_reward1, max_reward2,max_reward3, max_reward4)
	print(best_action, best_action1, best_action2, best_action3, best_action4)
	plot([reward_action[best_action],reward_action1[best_action1],
		  reward_action2[best_action2], reward_action3[best_action3],
		  reward_action4[best_action4]])
