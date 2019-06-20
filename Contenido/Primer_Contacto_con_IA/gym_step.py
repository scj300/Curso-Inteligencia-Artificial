
import gym

MAX_NUM_EPISODES = 10
MAX_STEPS_PER_EPISODE = 500

if __name__ == '__main__':
    
    environment = gym.make('Qbert-v0')

    
    for episode in range(MAX_NUM_EPISODES):
        obs = environment.reset()
        
        for step in range(MAX_STEPS_PER_EPISODE):
            environment.render()
            action = environment.action_space.sample()
            next_state, reward, done, info = environment.step(action)
            obs = next_state
            
            if done:
                print(f'\n Episodio #{episode} terminado en {step} steps')
                break