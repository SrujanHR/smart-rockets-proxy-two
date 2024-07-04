import pygame
import random
import math
import time


 
goal = [random.randint(50, 550), random.randint(0, 10)]
print(goal)


steps = 0

gen = 0
triangles = []
ang=[]
for g in range(5):
            x = 300
            y = 350
            angle = random.randint(0,360)
            ang.append(angle)

            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            distance_travelled = 0
            global path
            path =[]
            for i in range(100):
                    path.append(random.randint(0,360))
            triangles.append([x, y, angle, color, distance_travelled,path,steps])





def create_triangle_surface(breadth, height, color):
        surface = pygame.Surface((breadth, height), pygame.SRCALPHA)
        points = [(0, height), (breadth, height), (breadth / 2, 0)]
        pygame.draw.polygon(surface, color, points)
        return surface

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
running = True

while running:
        gen += 1
        print(gen)
        '''for p in triangles:
                 p[0] = 300
                 p[1] = 350'''
        pygame.event.get()
        st = time.time()
        print(st)

        while time.time() < st + 10:
            # Poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Fill the screen with black
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 255, 255), goal, 10)
            
            # Render each triangle
            for m in range(len(triangles)):
                x, y, angle, color, distance_travelled, path,steps= triangles[m]
                speed = 2
                # Update position

                if x >= 590:
                    x = 590
                    speed = 0
                    color = (125, 125, 125)
                if x <= 10:
                    x = 10
                    speed = 0
                    color = (125, 125, 125)
                if y >= 390:
                    y = 390
                    speed = 0
                    color = (125, 125, 125)
                if y <= 10:
                    y = 10
                    speed = 0
                    color = (125, 125, 125)
                if distance_travelled >=20:
                    #global s

                    #angle += random.randint(-30, 30) * speed
                    #f+=1
                    distance_travelled = 0
                    
                    #h = int(int(str(f)[0])/2+f%200)
                    #print(h)
                    #print(steps)
                    angle = path[steps]*speed
                    steps+=1
                angle_radians = math.radians(angle)
                x += math.cos(angle_radians) * speed  # Movement speed
                y += math.sin(angle_radians) * speed
                distance_travelled += 2

                # Create and rotate the triangles[m] surface
                breadth, height = 10, 20
                triangle_surface = create_triangle_surface(breadth, height, color)
                rotated_surface = pygame.transform.rotate(triangle_surface, angle)
                rect = rotated_surface.get_rect(center=(x, y))
                screen.blit(rotated_surface, rect.topleft)

                # Update the triangles[m] data
                triangles[m][0] = x
                triangles[m][1] = y
                triangles[m][2] = angle
                triangles[m][4] = distance_travelled
                triangles[m][6] = steps

            # Update the display
            pygame.display.flip()
            clock.tick(60)  # Limits FPS to 60
        while time.time() < st + 11:
            
            distances = []  # List to store distances and counts for each triangle
            count = -1
            for tri in triangles:
                xtri = goal[0] - tri[0]
                ytri = goal[1] - tri[1]
                dtri = ((xtri ** 2) + (ytri ** 2)) ** 0.5
                #print(dtri)
                count += 1
                distances.append({'count': count, 'dist': dtri})  # Store count and distance for each triangle

            # Sort distances based on distance
            distances.sort(key=lambda x: x['dist'], reverse=True)
            #print(distances[-1]['count'])  
            #print(distances[-2]['count'])        
            a = triangles[distances[-1]['count']][5]
            b = triangles[distances[-2]['count']][5]
            #print()
            #print(a)
            #print(b)#      b)
            #print()
            for i in triangles:
                t = []
                v = []
                #print(t)
                for j in range(100):
                    #print(a[j],b[j])
                    k = [a[j],b[j]]
                    k.sort()
                    v.append([k[0],k[1]]) #print(k)
                    t.append( random.randint(k[0]-10,k[1]+10))
                    k = []
                    g = list(str(t)+'\n')
                with open('plane.txt','a+') as f:
                        f.writelines(g)
                #print(t)
                #print()
                i[5]=t
                #print(i[5])
            #print()
            #print()
            #print()
            #print(triangles)
            time.sleep(1)
        else:
            #pygame.quit()
            
            
            s = triangles
            for p in triangles:
                 p[0] = 300
                 p[1] = 350
                 p[6] = 0
            pygame.display.update()


