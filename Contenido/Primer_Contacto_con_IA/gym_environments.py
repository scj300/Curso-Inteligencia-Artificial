

__author__ = 'Sergio Cuesta Jiménez Curso de Udemy'

from gym import envs

# Guardamos en una lista los entornos que tenemos disponibles
env_games = [env.id for env in envs.registry.all()]

# Imprimimos cada nombre
[print(name) for name in sorted(env_games)]
print(f'Número de juegos: {len(env_games)}')