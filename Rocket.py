import pygame
import math

'''
Force = (G*M1*M2)/(D^2)

math.sqrt((obj.x-planet.x)**2 + (obj.y - planet.y)**2), to find distance between two points.

A = F/M

TAN(theta)= O/A so arctan(0/A) = theta

Ay = Sin(theta)*A 
Ax = cos(theta)*A

'''

pygame.init()

WIDTH, HEIGHT = 1200,650
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot Effect")

PLANET_MASS = 10
SHIP_MASS = 10000
G = 5
FPS = 60
PLANET_SIZE = 50#(RADIUS)
OBJ_SIZE = 5
VEL_SCALE = 100

BG = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("jupiter.png"), (PLANET_SIZE*2, PLANET_SIZE*2))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255) 

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass

    def move(self, spacecrafts):
        # Calculate gravitational force from spacecrafts
        acceleration_x = 0
        acceleration_y = 0

        for spacecraft in spacecrafts:
            distance = math.sqrt((self.x - spacecraft.x)**2 + (self.y - spacecraft.y)**2)
            force = (G * self.mass * spacecraft.mass) / distance ** 2
            angle = math.atan2(spacecraft.y - self.y, spacecraft.x - self.x)
            acceleration_x += force / self.mass * math.cos(angle)
            acceleration_y += force / self.mass * math.sin(angle)

        # Update position based on total acceleration
        self.x += acceleration_x
        self.y += acceleration_y

    def draw(self):
        win.blit(PLANET, (int(self.x) - PLANET_SIZE, int(self.y) - PLANET_SIZE))



class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass

    def move(self, planet, other_objects):
            # Calculate gravitational force from the planet
            distance_planet = math.sqrt((self.x - planet.x)**2 + (self.y - planet.y)**2)
            force_planet = (G * self.mass * planet.mass) / distance_planet ** 2
            acceleration_planet = force_planet / self.mass
            angle_planet = math.atan2(planet.y - self.y, planet.x - self.x)
            acceleration_x_planet = acceleration_planet * math.cos(angle_planet)
            acceleration_y_planet = acceleration_planet * math.sin(angle_planet)

            # Calculate gravitational force from other spacecraft
            for obj in other_objects:
                if obj != self:  # Avoid calculating gravity from itself
                    distance_obj = math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)
                    force_obj = (G * self.mass * obj.mass) / distance_obj ** 2
                    acceleration_obj = force_obj / self.mass
                    angle_obj = math.atan2(obj.y - self.y, obj.x - self.x)
                    acceleration_x_obj = acceleration_obj * math.cos(angle_obj)
                    acceleration_y_obj = acceleration_obj * math.sin(angle_obj)

                    # Sum the accelerations from all objects
                    acceleration_x_planet += acceleration_x_obj
                    acceleration_y_planet += acceleration_y_obj

            # Update velocity and position based on total acceleration
            self.vel_x += acceleration_x_planet
            self.vel_y += acceleration_y_planet
            self.x += self.vel_x
            self.y += self.vel_y

    def draw(self):
        pygame.draw.circle(win, RED, (int(self.x), int(self.y)), OBJ_SIZE)

def create_ship(Location, mouse):
    t_x, t_y = Location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / VEL_SCALE
    vel_y = (m_y - t_y) / VEL_SCALE
    obj = Spacecraft(t_x, t_y, vel_x, vel_y, SHIP_MASS)
    return obj

def main():
    running = True
    clock = pygame.time.Clock()

    planet = Planet(WIDTH//2, HEIGHT//2, PLANET_MASS)
    objects = []
    temp_obj_pos = None

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    obj = create_ship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos

        win.blit(BG, (0, 0))

        if temp_obj_pos:
            pygame.draw.circle(win, RED, temp_obj_pos, OBJ_SIZE)
            pygame.draw.line(win, WHITE, temp_obj_pos, mouse_pos)

        # Inside the main loop
        for obj1 in objects[:]:
            obj1.draw()
            obj1.move(planet, objects)

            off_screen = obj1.x < 0 or obj1.x > WIDTH or obj1.y < 0 or obj1.y > HEIGHT

            # Check for collisions with the planet
            collided_planet = math.sqrt((obj1.x - planet.x)**2 + (obj1.y - planet.y)**2) <= PLANET_SIZE

            # Check for collisions with other spacecraft
            for obj2 in objects:
                if obj1 != obj2:  # Avoid checking collision with itself
                    distance = math.sqrt((obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2)
                    if distance < 2 * OBJ_SIZE:  # Adjust this value based on your object sizes
                        collided_spacecraft = True
                        objects.remove(obj2)
                        break
            else:
                collided_spacecraft = False

            if collided_planet or off_screen or collided_spacecraft:
                objects.remove(obj1)

        planet.move(objects)

        planet.draw()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__" and SHIP_MASS!=0 and PLANET_MASS!=0:
    main()
else:
    print("Mass cannot be zero\n-Newtonian physics doesn't deal with objects with zero mass")
