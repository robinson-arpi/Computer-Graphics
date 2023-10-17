import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Función para dibujar un triángulo
def draw_triangle(vertices):
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()

# Función para dividir un segmento en dos partes
def divide_segment(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

# Función recursiva para generar el Sierpinski Gasket
def sierpinski(vertices, depth):
    if depth == 0:
        draw_triangle(vertices)
    else:
        v1, v2, v3 = vertices
        middle1 = divide_segment(v1, v2)
        middle2 = divide_segment(v2, v3)
        middle3 = divide_segment(v1, v3)

        sierpinski([v1, middle1, middle3], depth - 1)
        sierpinski([middle1, v2, middle2], depth - 1)
        sierpinski([middle3, middle2, v3], depth - 1)

def main2D():
    # Configuración de Pygame
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(-1, 1, -1, 1)

    # Parámetros del triángulo inicial
    vertices = [(-0.5, -0.5), (0.5, -0.5), (0, 0.5)]

    # Profundidad de la recursión
    depth = 4

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        sierpinski(vertices, depth)
        pygame.display.flip()

if __name__ == "__main__":
    main2D()
