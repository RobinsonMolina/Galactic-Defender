# Galactic Defender

Este proyecto es un juego interactivo en el que controlas una nave espacial que debe esquivar y disparar a los enemigos que aparecen en el espacio. Ha sido desarrollado en Python utilizando la librería Pygame.

## Objetivo
El objetivo principal del juego es sobrevivir el mayor tiempo posible evitando colisiones con los enemigos y disparándoles para aumentar tu puntuación.

## Características del Proyecto
- **Funciones Personalizadas**: El proyecto incluye varias funciones personalizadas para manejar diferentes aspectos del juego, como el movimiento de la nave, el disparo, la generación de enemigos, y la detección de colisiones.
- **Uso de Menús y Pantallas de Inicio/Game Over**:
  - Pantalla de instrucciones al inicio del juego.
  - Pantalla de "Game Over" que permite reiniciar el juego o salir.
- **Implementación de Enemigos**: Los enemigos se generan aleatoriamente y se mueven hacia la parte inferior de la pantalla, aumentando la dificultad del juego.

## Descripción del Código

### Variables Globales
- **ANCHO, ALTO**: Dimensiones de la ventana del juego.
- **VENTANA**: Superficie de la ventana del juego.
- **FPS**: Frecuencia de cuadros por segundo.
- **PUNTUACION**: Puntuación del jugador.

### Clases

#### `Nave`
Representa la nave del jugador.
- **Método `__init__()`**: Inicializa la nave y establece su posición.
- **Método `mover(keys)`**: Mueve la nave a la izquierda o derecha según las teclas presionadas.
- **Método `dibujar(ventana)`**: Dibuja la nave en la ventana.

#### `Enemigo`
Representa a los enemigos en el juego.
- **Método `__init__()`**: Inicializa un enemigo con una posición aleatoria y una velocidad.
- **Método `mover()`**: Mueve el enemigo hacia abajo en la pantalla.
- **Método `dibujar(ventana)`**: Dibuja el enemigo en la ventana.
- **Método `fuera_pantalla()`**: Devuelve `True` si el enemigo ha salido de la pantalla.

### Funciones
- **`mostrar_texto(texto, tamano, y, x=None)`**: Muestra texto en la ventana, con un contorno negro y texto rojo.
- **`detectar_colision(nave, enemigos)`**: Detecta colisiones entre la nave y los enemigos. Si hay una colisión, llama a `menu_game_over()`.
- **`disparar(nave, balas)`**: Dispara una bala desde la nave y reproduce un sonido de disparo.
- **`actualizar_balas(balas, enemigos)`**: Actualiza la posición de las balas, detecta colisiones con enemigos y actualiza la puntuación.
- **`generar_enemigos(enemigos)`**: Genera nuevos enemigos aleatoriamente si hay menos de 5 en pantalla.
- **`mostrar_instrucciones()`**: Muestra la pantalla de instrucciones del juego.
- **`menu_game_over()`**: Muestra la pantalla de "Game Over" y permite reiniciar o salir.
- **`main()`**: Función principal del juego que contiene el bucle del juego, maneja eventos, dibuja elementos y actualiza el estado del juego.

## Cómo Jugar
- **Movimiento**: Usa las flechas IZQUIERDA y DERECHA para mover la nave.
- **Disparo**: Presiona la tecla ESPACIO para disparar a los enemigos.
- **Inicio y Reinicio**: Presiona ENTER para comenzar o reiniciar el juego.
- **Salir**: Presiona la tecla X para salir del juego.

## Recursos
Asegúrate de tener los siguientes archivos en la carpeta `Resources`:
- **dark_alien_ambiance-55246.mp3**: Música de fondo.
- **laser-gun-81720.mp3**: Sonido de disparo.
- **espacialNave.png**: Imagen de la nave.
- **enemigo.png**: Imagen del enemigo.
- **espace3.webp**: Imagen de fondo del juego.
- **espace.webp**: Imagen de fondo de instrucciones.
- **espace2.webp**: Imagen de fondo de Game Over.

## Instalación
1. Asegúrate de tener Python y Pygame instalados:
   ```bash
   pip install pygame
   ```

2. Clonar el repositorio:
   ```bash
   https://github.com/RobinsonMolina/Galactic-Defender.git
   ```

## Ejecuta el juego
   ```bash
   python main.py
   ```
