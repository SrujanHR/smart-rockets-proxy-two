import pygame
import random
import math
import time
time.sleep(5)
good_tri = []
excluded_ranges = []  
goal = [random.randint(50, 550), random.randint(0, 10)]
print(goal)




    # Create random positions for the triangles
def test():
    st = time.time()


    def random_with_exclusion(start, end, excluded_ranges):
            while True:
                num = random.randint(start, end)
                if not any(x <= num <= y for x, y in excluded_ranges):
                    return num


    # Example usage:
    start_range = 0
    end_range = 360
# Exclude ranges from 20 to 30 and from 50 to 60

    


    # Function to create a triangle surface
    def create_triangle_surface(breadth, height, color):
        surface = pygame.Surface((breadth, height), pygame.SRCALPHA)
        points = [(0, height), (breadth, height), (breadth / 2, 0)]
        pygame.draw.polygon(surface, color, points)
        return surface


    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    running = True
    triangles = []
    ang=[]
    for _ in range(3000):
        x = 300
        y = 350
        angle = random_with_exclusion(start_range, end_range, excluded_ranges) 
        ang.append(angle)
        #print(ang,excluded_ranges) # Initial random rotation angle
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        distance_travelled = 0
        triangles.append([x, y, angle, color, distance_travelled])

    while True:
        pygame.event.get()
        if time.time() < st + 10:
            # Poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the screen with black
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 255, 255), goal, 10)
            # Render each triangle
            for m in range(len(triangles)):
                x, y, angle, color, distance_travelled, path = triangles[m]
                speed = 1
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
                if distance_travelled >=10:
                    #angle += random.randint(-30, 30) * speed
                    f+=1
                    distance_travelled = 0
                    
                    h = f%200
                    print(h)
                    angle = path[h]
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

            # Update the display
            pygame.display.flip()
            clock.tick(60)  # Limits FPS to 60
        elif time.time() < st + 11:
            distances = []  # List to store distances and counts for each triangle
            count = -1
            for tri in triangles:
                xtri = goal[0] - tri[0]
                ytri = goal[1] - tri[1]
                dtri = ((xtri ** 2) + (ytri ** 2)) ** 0.5
                count += 1
                distances.append({'count': count, 'dist': dtri})  # Store count and distance for each triangle

            # Sort distances based on distance
            distances.sort(key=lambda x: x['dist'], reverse=True)


            # Find the first distance that is greater than 10
            max_distance_count = None
            for dist_info in distances:
                    max_distance_count = dist_info['count']
                    break

            if max_distance_count is not None:
                good_tri.append(triangles[max_distance_count])
                gx = goal[0]-good_tri[-1][0]
                gy =  goal[1]-good_tri[-1][1]
                gd = ((gx ** 2) + (gy ** 2)) ** 0.5
        
                worst_angle = good_tri[-1][2]  # Get angle of the triangle with maximum distance
                excluded_ranges.append((worst_angle - 5, worst_angle + 5))  # Exclude range of angles near the worst triangle
                print('bad angles:', excluded_ranges[-1], 'worst triangle distance:', gd,'bad angle : ',worst_angle)

                time.sleep(1)
            elif max_distance_count is None:
                print('task complete')
                time.sleep(60)
                pygame.quit()
                exit()
        else:
            #pygame.quit()
            pygame.display.update()
            test()


test()
