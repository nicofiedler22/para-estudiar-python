
import pygame
import random
import time

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ancho = 800
alto = 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("The Clicker")

# Colores
rojo = (255, 0, 0)
blanco = (255, 255, 255)
negro = (0, 0, 0)
amarillo = (255, 255, 0)

# Clase para los cubos
class Cubo(pygame.sprite.Sprite):
    def __init__(self, nivel):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(rojo)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ancho - self.rect.width)
        self.rect.y = random.randrange(100, alto - self.rect.height - 50)
        self.velocidad = 1  # Velocidad constante
        self.direccion_x = 0
        self.direccion_y = 0
        if nivel >= 3:
            if nivel < 5 and random.random() < 0.4:
                self.direccion_x = random.choice([-1, 1])
                self.direccion_y = random.choice([0]) # Inicialmente solo horizontal
                if random.random() < 0.5 and self.direccion_x == 0: # O solo vertical
                    self.direccion_x = 0
                    self.direccion_y = random.choice([-1, 1])
            elif nivel >= 5:
                self.direccion_x = random.choice([-1, 1])
                self.direccion_y = random.choice([0]) # Inicialmente solo horizontal
                if random.random() < 0.5 and self.direccion_x == 0: # O solo vertical
                    self.direccion_x = 0
                    self.direccion_y = random.choice([-1, 1])

    def update(self):
        if self.direccion_x != 0:
            self.rect.x += self.direccion_x * self.velocidad
            if self.rect.left < 0 or self.rect.right > ancho:
                self.direccion_x *= -1
        if self.direccion_y != 0:
            self.rect.y += self.direccion_y * self.velocidad
            if self.rect.top < 100 or self.rect.bottom > alto - 50:
                self.direccion_y *= -1

# Función para mostrar texto
def mostrar_texto(texto, tamaño, color, x, y):
    fuente = pygame.font.Font(None, tamaño)
    texto_surface = fuente.render(texto, True, color)
    texto_rect = texto_surface.get_rect(center=(x, y))
    pantalla.blit(texto_surface, texto_rect)

# Loop principal del juego
def juego():
    nivel_actual = 1
    cubos_restantes = 0
    cubos = pygame.sprite.Group()
    jugando = True
    perdido = False
    tiempo_inicio_nivel = 0
    tiempo_limite = 10
    mensaje_perdida = ""

    def generar_nivel(nivel):
        cantidad_cubos = 2 + nivel * 2  # Aumenta la cantidad de cubos con el nivel
        cubos.empty()
        for _ in range(cantidad_cubos):
            cubo = Cubo(nivel)
            # Asegurar que no se superpongan demasiado al generarlos
            while pygame.sprite.spritecollide(cubo, cubos, False):
                cubo.rect.x = random.randrange(ancho - cubo.rect.width)
                cubo.rect.y = random.randrange(100, alto - cubo.rect.height - 50)
            cubos.add(cubo)
        return cantidad_cubos

    cubos_restantes = generar_nivel(nivel_actual)
    tiempo_inicio_nivel = time.time()

    while jugando:
        pantalla.fill(negro)

        if perdido:
            mostrar_texto(mensaje_perdida, 74, rojo, ancho // 2, alto // 2)
            mostrar_texto("Presiona cualquier tecla para reiniciar", 36, blanco, ancho // 2, alto // 2 + 50)
            pygame.display.flip()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    jugando = False
                if evento.type == pygame.KEYDOWN:
                    nivel_actual = 1
                    cubos_restantes = generar_nivel(nivel_actual)
                    tiempo_inicio_nivel = time.time()
                    perdido = False
                    break

        cubos.draw(pantalla)
        mostrar_texto(f"Nivel: {nivel_actual}", 30, blanco, 70, 30)
        tiempo_transcurrido = int(tiempo_limite - (time.time() - tiempo_inicio_nivel))
        mostrar_texto(f"Tiempo: {tiempo_transcurrido}", 30, amarillo if tiempo_transcurrido <= 3 else blanco, ancho - 100, 30)

        if tiempo_transcurrido <= 0 and cubos_restantes > 0:
            perdido = True
            mensaje_perdida = "¡Tiempo agotado! Perdiste!"

        for cubo in cubos:
            cubo.update() # Actualizar la posición de los cubos

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                clic_en_cubo = False
                for cubo in cubos:
                    if cubo.rect.collidepoint(pos_mouse):
                        cubos.remove(cubo)
                        cubos_restantes -= 1
                        clic_en_cubo = True
                        break
                if not clic_en_cubo:
                    perdido = True
                    mensaje_perdida = "¡Tocaste el fondo, perdiste!"

        if cubos_restantes == 0 and not perdido:
            nivel_actual += 1
            if nivel_actual <= 10:
                mostrar_texto(f"¡Nivel {nivel_actual} completado!", 60, blanco, ancho // 2, alto // 2)
                pygame.display.flip()
                pygame.time.delay(1500)
                cubos_restantes = generar_nivel(nivel_actual)
                tiempo_inicio_nivel = time.time()
            else:
                mostrar_texto("¡Te lo pasaste, campeón!", 74, blanco, ancho // 2, alto // 2 - 30) # Mover un poco hacia arriba
                mostrar_texto("Juego creado por: Nicolás Fiedler", 24, blanco, ancho // 2, alto // 2 + 10)
                pygame.display.flip()
                pygame.time.delay(3000)
                jugando = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    juego()