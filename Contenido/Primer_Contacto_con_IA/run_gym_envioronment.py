
import gym
import sys


def run_gym_environment(argv):
    
    # Primer parámetro der 'argv' será el nombre del entorno a ejecutar
    environment = gym.make(argv[1])
    
    # resetamos / preparamos el entorno
    obs = environment.reset()
    
    for _ in range(int(argv[2])):
        # Mostramos por pantalla
        environment.render()
        
        # Escogemos una acción al azar y obtenemos un resultado
        # Devuelve 4 parámetros:
        #   next_state -> object
        #   reward -> Float (recompensa)
        #   done -> Boolean (si a acabado o no)
        #   info -> Dictionary (opcional) información adicional que no utiliza el agente para tomar la decisión pero puede ser útil cara al usuario
        environment.step(environment.action_space.sample())

    # Cerramos el entorno
    environment.close()
    



if __name__ == '__main__':    
    run_gym_environment(sys.argv)
