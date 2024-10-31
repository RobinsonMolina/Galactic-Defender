import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Nave vs Enemigos")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

FPS = 60
RELOJ = pygame.time.Clock()

PUNTUACION = 0

pygame.mixer.music.load("Resources/dark_alien_ambiance-55246.mp3")
pygame.mixer.music.play(-1)

disparo = pygame.mixer.Sound("Resources/laser-gun-81720.mp3")
disparo.set_volume(0.5)

IMG_NAVE = pygame.image.load("Resources/espacialNave.png")
IMG_NAVE = pygame.transform.scale(IMG_NAVE, (60, 60))

IMG_ENEMIGO = pygame.image.load("Resources/enemigo.png")
IMG_ENEMIGO = pygame.transform.scale(IMG_ENEMIGO, (50, 50))

IMG_FONDO = pygame.image.load("Resources\espace3.webp")
IMG_FONDO = pygame.transform.scale(IMG_FONDO, (ANCHO, ALTO))

IMG_FONDO_INICIO = pygame.image.load("Resources\espace.webp")
IMG_FONDO_INICIO = pygame.transform.scale(IMG_FONDO_INICIO, (ANCHO, ALTO))

IMG_FONDO_GAME_OVER = pygame.image.load("Resources\espace2.webp")
IMG_FONDO_GAME_OVER = pygame.transform.scale(IMG_FONDO_GAME_OVER, (ANCHO, ALTO))

class Nave:
    def __init__(self):
        self.rect = IMG_NAVE.get_rect(midbottom=(ANCHO // 2, ALTO - 50))

    def mover(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += 5

    def dibujar(self, ventana):
        ventana.blit(IMG_NAVE, self.rect)

class Enemigo:
    def __init__(self):
        self.rect = IMG_ENEMIGO.get_rect(topleft=(random.randint(0, ANCHO - 50), -50))
        self.velocidad = random.uniform(1.5, 3.0)

    def mover(self):
        self.rect.y += self.velocidad

    def dibujar(self, ventana):
        ventana.blit(IMG_ENEMIGO, self.rect)

    def fuera_pantalla(self):
        return self.rect.top > ALTO


def mostrar_texto(texto, tamano, y, x=None):
    fuente = pygame.font.SysFont("Arial", tamano)
    if x is None:
        x = (ANCHO - fuente.size(texto)[0]) // 2

    superficie_borde = fuente.render(texto, True, NEGRO)
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]: 
        VENTANA.blit(superficie_borde, (x + dx, y + dy))

    superficie_texto = fuente.render(texto, True, ROJO)
    VENTANA.blit(superficie_texto, (x, y))

def detectar_colision(nave, enemigos):
    for enemigo in enemigos[:]:
        if nave.rect.colliderect(enemigo.rect):
            menu_game_over()
        elif enemigo.fuera_pantalla():
            enemigos.remove(enemigo)

def disparar(nave, balas):
    bala = pygame.Rect(nave.rect.centerx - 5, nave.rect.top, 10, 20)
    balas.append(bala)
    disparo.play()

def actualizar_balas(balas, enemigos):
    global PUNTUACION
    balas_a_eliminar = []

    for bala in balas:
        bala.y -= 7
        if bala.bottom < 0:
            balas_a_eliminar.append(bala) 
        else:
            for enemigo in enemigos[:]:
                if bala.colliderect(enemigo.rect):
                    enemigos.remove(enemigo)
                    balas_a_eliminar.append(bala) 
                    PUNTUACION += 1

    for bala in balas_a_eliminar:
        if bala in balas:
            balas.remove(bala)

def generar_enemigos(enemigos):
    if len(enemigos) < 5:
        if random.randint(1, 100) <= 5:
            enemigos.append(Enemigo())

def mostrar_instrucciones():
    while True:
        VENTANA.blit(IMG_FONDO_INICIO, (0, 0))
        
        mostrar_texto("Instrucciones",80, ALTO // 2 - 160)
        mostrar_texto("Mueve la nave con las flechas IZQUIERDA/DERECHA", 40, ALTO // 2 - 60)
        mostrar_texto("Dispara con la tecla ESPACIO", 40, ALTO // 2 - 20)
        mostrar_texto("Presiona ENTER para comenzar", 40, ALTO // 2 + 60)
        mostrar_texto("Presiona X para salir", 40, ALTO // 2 + 120)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    main()
                if evento.key == pygame.K_x:
                    pygame.quit()
                    sys.exit()

def menu_game_over():
    while True:
        VENTANA.blit(IMG_FONDO_GAME_OVER, (0, 0))

        mostrar_texto("¡Game Over!", 80, ALTO // 2 - 160)
        mostrar_texto(f"Puntuación: {PUNTUACION}", 60, ALTO // 2 - 50)
        mostrar_texto("Presiona ENTER para reiniciar", 50, ALTO // 2 + 40)
        mostrar_texto("Presiona X para salir", 50, ALTO // 2 + 120)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    main()
                if evento.key == pygame.K_x:
                    pygame.quit()
                    sys.exit()

def main():
    global PUNTUACION
    PUNTUACION = 0

    nave = Nave()
    enemigos = []
    balas = []

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                disparar(nave, balas)
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_x:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        nave.mover(keys)

        generar_enemigos(enemigos)

        # Dibujar fondo del juego
        VENTANA.blit(IMG_FONDO, (0, 0))

        for enemigo in enemigos:
            enemigo.mover()
            enemigo.dibujar(VENTANA)

        for bala in balas:
            pygame.draw.rect(VENTANA, ROJO, bala)
        actualizar_balas(balas, enemigos)

        nave.dibujar(VENTANA)

        detectar_colision(nave, enemigos)

        mostrar_texto(f"Puntuación: {PUNTUACION}", 50, 10, 10)

        pygame.display.flip()
        RELOJ.tick(FPS)

mostrar_instrucciones()
