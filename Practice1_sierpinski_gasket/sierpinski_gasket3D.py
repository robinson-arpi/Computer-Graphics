import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Definir las coordenadas de los vértices del tetraedro regular
vertices = [
    (0.0, 1.0, 0.0),
    (1.0, -1.0, -1.0 / math.sqrt(3)),
    (-1.0, -1.0, -1.0 / math.sqrt(3)),
    (0.0, -1.0, 2.0 / math.sqrt(3))
]

# Definir el tamaño de la ventana de visualización
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Definir colores para las caras del tetraedro
colors = [
    (1.0, 0.0, 0.0),  # Color rojo
    (0.0, 1.0, 0.0),  # Color verde
    (0.0, 0.0, 1.0),  # Color azul
    (0.0, 0.0, 0.0)   # Color negro
]

# Factor de escala para cambiar el tamaño del tetraedro
scale_factor = 2.0  # Aumenta o disminuye según se desee

# Escalar los vértices del tetraedro para cambiar su tamaño
scaled_vertices = [
    (x * scale_factor, y * scale_factor, z * scale_factor)
    for x, y, z in vertices
]

# Función para dibujar el tetraedro de manera recursiva
def draw_tetrahedron(vertices, depth):
    if depth == 0:
        # Dibuja las caras del tetraedro
        for i, face in enumerate([
            [vertices[0], vertices[1], vertices[2]],
            [vertices[0], vertices[2], vertices[3]],
            [vertices[0], vertices[3], vertices[1]],
            [vertices[1], vertices[2], vertices[3]]
        ]):
            glBegin(GL_TRIANGLES)
            glColor3fv(colors[i])  # Establece el color de la cara
            for vertex in face:
                glVertex3fv(vertex)  # Dibuja los vértices de la cara
            glEnd()
    else:
        midpoints = [
            # Calcula los puntos medios entre los vértices
            ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2, (vertices[0][2] + vertices[1][2]) / 2),
            ((vertices[0][0] + vertices[2][0]) / 2, (vertices[0][1] + vertices[2][1]) / 2, (vertices[0][2] + vertices[2][2]) / 2),
            ((vertices[0][0] + vertices[3][0]) / 2, (vertices[0][1] + vertices[3][1]) / 2, (vertices[0][2] + vertices[3][2]) / 2),
            ((vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2, (vertices[1][2] + vertices[2][2]) / 2),
            ((vertices[1][0] + vertices[3][0]) / 2, (vertices[1][1] + vertices[3][1]) / 2, (vertices[1][2] + vertices[3][2]) / 2),
            ((vertices[2][0] + vertices[3][0]) / 2, (vertices[2][1] + vertices[3][1]) / 2, (vertices[2][2] + vertices[3][2]) / 2)
        ]

        # Realiza llamadas recursivas para cada nuevo tetraedro
        draw_tetrahedron([vertices[0], midpoints[0], midpoints[1], midpoints[2]], depth - 1)
        draw_tetrahedron([midpoints[0], vertices[1], midpoints[3], midpoints[4]], depth - 1)
        draw_tetrahedron([midpoints[1], midpoints[3], vertices[2], midpoints[5]], depth - 1)
        draw_tetrahedron([midpoints[2], midpoints[4], midpoints[5], vertices[3]], depth - 1)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    
    # Habilitar el Z-buffer para la representación 3D
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    
    # Cambiar el color de fondo a blanco
    glClearColor(1.0, 1.0, 1.0, 1.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Rotación del tetraedro
        glRotatef(1, 2, 1, 0)  # El primer parámetro es el ángulo, y los tres siguientes son los ejes de rotación

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Dibujar el tetraedro
        draw_tetrahedron(vertices, depth=3)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
