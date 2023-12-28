import pygame
import math
pygame.init()

'''
r= distance between center of two bodies, sqrt(a^2+b^2)
F = G(M1*M2)/r^2
now we break down the force into two components: movement in x and movement in y
tan(theta) = O/A
arctan(y/x) = theta
Sin(theta) = O/H

'''

WIDTH, HEIGHT = 800,645
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Planet simulation")

WHITE = (255,255,255)
YELLOW = (255,255,0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
BG = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))
FONT = pygame.font.SysFont("Helvetica", 16)

class Planet:
    AU = 149.6e6*1000 
    '''(149 million 600 thousand meters *1000)'''
    G = 6.67428e-11
    SCALE = 180/AU # 1AU = 100pixels
    TIMESTEP = 60*60*24 #1/2 day


    def __init__(self,x,y,radius,color,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = None

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2

        if len(self.orbit) >2:
            updated_points=[]
            for point in self.orbit:
                x,y = point
                x= x*self.SCALE+WIDTH/2
                y= y*self.SCALE+HEIGHT/2
                updated_points.append((x,y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)
        if not self.sun:#drawing txt
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x-distance_text.get_width()/2,y-distance_text.get_width()/2))

    def attraction(self,other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G*self.mass*other.mass/distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta)*force
        force_y = math.sin(theta)*force
        return force_x, force_y
    
    def create_ship(Location, mouse):
        t_x, t_y = Location
        m_x, m_y = mouse
        vel_x = (m_x - t_x)
        vel_y = (m_y - t_y)
        obj = Planet(t_x, t_y, vel_x, vel_y, 5*10*15)
        return obj

    def update_position(self,planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy, = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx/self.mass*self.TIMESTEP
        self.y_vel += total_fy/self.mass*self.TIMESTEP

        self.x += self.x_vel*self.TIMESTEP
        self.y += self.y_vel*self.TIMESTEP
        self.orbit.append((self.x,self.y))

def main():
    running = True
    clock =  pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892*10**30)
    sun.sun = True

    earth = Planet(-1*Planet.AU, 0, 16, BLUE, 5.9742*10**24)
    earth.y_vel = 29.793*1000
    temp_obj_pos = None

    planets = [sun, earth]

    while running:
        clock.tick(60)
        WIN.blit(BG,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if temp_obj_pos:
                    obj = Planet.create_ship(temp_obj_pos, mouse_pos)
                    planets.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos

            if temp_obj_pos:
                pygame.draw.circle(WIN, RED, temp_obj_pos, 100)
                pygame.draw.line(WIN, WHITE, temp_obj_pos, mouse_pos)

 
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
        


        pygame.display.update()

    pygame.quit()

main()



















'''
import tkinter as tk

def click_handler(event):
    global click_count
    if click_count == 0:
        print("First click")
        click_count = 1
    else:
        print("Second click")
        click_count = 0

click_count = 0

# Create a Tkinter window
root = tk.Tk()
root.title("Click Tracker")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Bind the mouse click event to the click_handler function
canvas.bind("<Button-1>", click_handler)

# Start the Tkinter main loop
root.mainloop()
'''