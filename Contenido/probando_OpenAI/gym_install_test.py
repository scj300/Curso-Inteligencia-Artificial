
import gym


# Crear un entorno del videojuego de la montaña Rusa
envioronment = gym.make('SpaceInvaders-v0')

# Limpiamos el entorno para tomar decisiones
envioronment.reset()


if __name__ == '__main__':
    
    # Durante 2000 iteraciones
    for _ in range(2000):
        
        # Pintar en pantalla la acción
        envioronment.render()
        
        # Tomamos una decisión aleatoria
        envioronment.step(envioronment.action_space.sample())

    # Cerrar el entorno
    envioronment.close()