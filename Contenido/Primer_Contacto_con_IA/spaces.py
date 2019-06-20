
import gym
from gym.spaces import *
import sys
# Box -> R^n (xq, x2, x3,..., xn) xi [low, high]
# gym.spaces.Box(low=-10, high=10, shape=(2,))  # (x, y) -10 < x,y < 10

# Discrete -> Números enteros entre 0 y n -1, {0, 1, 2, 3,...., n -1}
# gym.spaces.Discrete(5) # {0, 1, 2, 3, 4}

# Dict -> Diccionario de espacios más complejos
# gym.spaces.Dict({
#     'position': gym.spaces.Discrete(3), # {0, 1, 2}
#     'velocity': gym.spaces.Discrete(2), # {0, 1}
# })

# Multi Binary -> {0, 1} ^ n {x1, x2, x3,...., xn} xi {T, F}
# gym.spaces.Binary(3) # {x, y, z} ,, x, y, z = T|F

# Multi Discrete -> {a, a + 1, a + 2,...., b} ^ m
# gym.spaces.MultiDescrete([-10, 10], [0, 1])

# Tuple -> Producto de espacios simples
# gym.spaces.Tuple((gym.spaces.Discrete(3), gym.spaces.Discrete(2))) # {0, 1, 2} x {0, 1}

# prng -> random seed

def print_spaces(space):
    
    print(space)
    
    if isinstance(space, Box): # si el space es de tipo Box
        print('\n Cota inferior', space.low)
        print('\n Cota superior', space.high)
        


if __name__ == '__main__':
    
    # Llamar al script con el nombre del entorno
    environment = gym.make(sys.argv[1])
    
    print('Espacio de observaciones: ')
    print_spaces(environment.observation_space)
    
    print('\nEspacio de acciones: ')
    print_spaces(environment.action_space)
    
    try:
        print('Descripción de las acciones: ', environment.unwrapped.get_action_meanings())
    except AttributeError:
        pass
        
    environment.close()