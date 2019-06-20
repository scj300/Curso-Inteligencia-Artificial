
import gym

MAX_NUM_EPISODES = 1000


if __name__ == '__main__':
    
    environment = gym.make('MountainCar-v0')

    
    for episode in range(MAX_NUM_EPISODES):
        
        done = False
        obs = environment.reset()
        total_reward = 0.0 # Recompensa obtenida por episodio
        step = 0
        
        while not done:
            environment.render() # Preparar el entorno
            action = environment.action_space.sample() # Acción al azar
            next_state, reward, done, info = environment.step(action)
            
            # Actualización de variables
            obs = next_state
            total_reward += reward
            step += 1
        
        print()
        print(f'Episodio número {episode} finalizado con {step} iteraciones. Recompensa final = {total_reward}')
    
    environment.close()
            