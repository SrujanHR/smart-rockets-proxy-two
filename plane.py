import pygame
import random
import math
import time


pygame.init()
sb =16*110
sh =9*110
screen = pygame.display.set_mode((sb, sh))
clock = pygame.time.Clock()
running = True
goal = [random.randint(50, (sb-50)//2), random.randint(10, 20)]
print(goal)
win= 0

steps = 0
#600,400
gen = 0
triangles = []
ang=[]
def birth (plane_count):
    for g in range(plane_count):
                x = sb//2
                y = sh*0.9
                angle = random.randint(0,360)
                ang.append(angle)

                color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                distance_travelled = 0
                global path
                path =[]
                for i in range(100):
                        path.append(random.randint(0,360))
                triangles.append([x, y, angle, color, distance_travelled,path,steps])
birth(100)




def create_triangle_surface(breadth, height, color):
        surface = pygame.Surface((breadth, height), pygame.SRCALPHA)
        points = [(0, height), (breadth, height), (breadth / 2, 0)]
        pygame.draw.polygon(surface, color, points)
        return surface

while running:

        gen += 1
        print('generation : ',gen)
        #print(u)
        '''for p in triangles:
                 p[ 0] = 300
                 p[1] = 350'''
        pygame.event.get()
        st = time.time()
        #print(st)

        while time.time() < st + 10:
            # Poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Fill the screen with black
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 255, 255), goal, 10)
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, int(sh*(2/3)), int(sb*6/10), 10))
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(int(sb*(4/10)), int(sh*(1/3)), int(sb*0.75), 10))
            text_surface = pygame.font.SysFont('Comic Sans MS', 20).render(f'Generation {gen}', False, (255, 255, 255))
            screen.blit(text_surface, (sb*0.01,sh*0.95))
            
            # Render each triangle
            for m in range(len(triangles)):
                x, y, angle, color, distance_travelled, path,steps= triangles[m]
                speed = 10
                # Update position
                #time.sleep(0.01)
                #print(pygame.mouse.get_pos())

                if x >= sb-10:
                    x = sb-10
                    speed = 0
                    color = (125, 125, 125)
                if x <= 10:
                    x = 10
                    speed = 0
                    color = (125, 125, 125)
                if y >= sh-10:
                    y = sh-10
                    speed = 0
                    color = (125, 125, 125)
                if y <= 10:
                    y = 10
                    speed = 0
                    color = (125, 125, 125)
                #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, , int(sb*6/10), 10))
                #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(int(sb*(4/10)), int(sh*(1/3)), int(sb*0.75), 10))
                if 0<x<int(sb*6/10) and int(sh*(2/3))-10<y<int(sh*(2/3))+10:
                     x = x
                     y = y
                     speed = 0
                     color = (125, 125, 125)
                if int(sb*(4/10))<x<sb and int(sh*(1/3))-10<y<int(sh*(1/3))+10:
                     x= x
                     y = y
                     speed = 0
                     color = (125, 125, 125)
                if goal[0]-10<x<goal[0]+10 and goal[1]-10<y<goal[1]+10: 
                     x= goal[0]
                     y = goal[1]
                     speed = 0
                     color = (255, 255, 255)
                     win += 1
                     #break

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
                breadth, height = 20, 40
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
            #await asyncio.sleep(0)
        while time.time() < st + 11:
            print('survivers : ', win,' Out of 100')
            with open('plane.txt','a+') as f:
                        f.writelines([str(gen),',',str(win),',',str(st),'\n'])
            
            print()
            #u = win
            win = 0
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
            c = triangles[distances[-1]['count']][3]
            d = triangles[distances[-2]['count']][3]
            #print(c,d)
            #print()
            #print(a)
            #print(b)#      b)
            #print()
            #triangles.append([x, y, angle, color, distance_travelled,path,steps])
            for i in triangles:
                t = []
                v = []
                #print(t)
                for j in range(100):
                    #print(a[j],b[j])
                    k = [a[j],b[j]]
                    k.sort()
                    v.append([k[0],k[1]]) #print(k)
                    if k[0]+1 == k[1]-1 or k[0] == k[1] or k[0] == k[1]-1:
                        t.append(k[0])
                    else:
                        t.append( random.randint(k[0]+1,k[1]-1))
                    k = []

                #print(t)
                #print()
                i[5]=t
                m = []
                for z in range(0,3):
                    n = [c[z],d[z]]
                    n.sort()
                    m.append(random.randint(n[0],n[1]))
                #print(m)
                i[3]=m
                '''de = [c,d]
                for m in de:
                     for l in m:
                          
                        print(l)'''
                    #i[3] = random.randint(de[0]-10,de[1]+10)
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
                 #x = sb//2
                 #y = sh*0.9
                 p[0] = sb//2
                 p[1] = sh*0.9
                 p[6] = 0
            pygame.display.update()


