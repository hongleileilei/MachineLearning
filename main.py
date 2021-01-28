## Ke Ma
## Honglei Liu

### Main Program ###
import pygame
from  helper import get_output_image
import cv2
import numpy as np

# predefined colors, pen radius and font color
black = [0, 0, 0]
white = [255, 255, 255]
blue = [128, 224, 230]
red = [255, 0, 0]
green = [0, 255, 0]
last_pos = (0, 0)
color = (255, 128, 0)
radius = 7
font_size = 500

#image size
width = 640
height = 640

vec_calcu = []

# initializing screen
screen = pygame.display.set_mode((width*2, height))
screen.fill(white)
pygame.font.init()


### Show the result image with labels
def show_output_image(n, img):
    surf = pygame.pixelcopy.make_surface(img)
    surf = pygame.transform.rotate(surf, -270)
    surf = pygame.transform.flip(surf, 0, 1)
    screen.blit(surf, (n*width+2, 0))


### Cut the image
def crope(orginal):
    cropped = pygame.Surface((width-5, height-5))
    cropped.blit(orginal, (0, 0), (0, 0, width-5, height-5))
    #source, dest, area, special_flags
    return cropped

### Circle the digit detected
def roundline(srf, color, start, end, radius=1):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(srf, color, (x, y), radius)

### For division of Left and Right Pad
def draw_partition_line():
    pygame.draw.line(screen, black, [width, 0], [width,height], 8)

### Simple calculators
def calculation(label, op):
    if op == "+":
        if len(vec_calcu) == 0:
            result = int(label)
            vec_calcu.append(int(label))
        else:
            result = vec_calcu[-1] + int(label)
            vec_calcu.append(result)    
    if op == '-':
        if len(vec_calcu) == 0:
            result = -int(label)
            vec_calcu.append(result)
        else:
            result = vec_calcu[-1] - int(label)
            vec_calcu.append(result)       
    if op == '*':
        if len(vec_calcu) == 0:
            result = int(label)
            vec_calcu.append(result)
        else:
            result = vec_calcu[-1] * int(label)
            vec_calcu.append(result)   
    if op == '/':
        if len(vec_calcu) == 0:
            result = int(label)
            vec_calcu.append(result)
        else:
            if int(label) != 0:
                result = vec_calcu[-1] / int(label)
                vec_calcu.append(result)   

    img = np.ones((635, 635, 3))
    cv2.putText(img,str(result),(250,340), cv2.FONT_HERSHEY_SIMPLEX,5,(255,0,0),1,cv2.LINE_AA)
    if len(vec_calcu) == 1:
        cv2.putText(img,"previous result: "+str(0),(10,50), cv2.FONT_HERSHEY_SIMPLEX,1.8,(255,0,0),1,cv2.LINE_AA)
        cv2.putText(img,"op: "+op,(10,100), cv2.FONT_HERSHEY_SIMPLEX,1.8,(255,0,0),1,cv2.LINE_AA)
    else:
        cv2.putText(img,"previous result: "+str(vec_calcu[-2]),(0,50), cv2.FONT_HERSHEY_SIMPLEX,1.8,(255,0,0),1,cv2.LINE_AA)
        cv2.putText(img,"op: "+op,(0,100), cv2.FONT_HERSHEY_SIMPLEX,1.8,(255,0,0),1,cv2.LINE_AA)

    cv2.putText(img,"result: ",(0,150), cv2.FONT_HERSHEY_SIMPLEX,1.8,(255,0,0),1,cv2.LINE_AA)
    cv2.imshow("Image", img) 
    cv2.waitKey(0)


def main():
    draw_on = False
    try:
        while True:
            # get all events
            e = pygame.event.wait()
            draw_partition_line() # Surface, color, start, end, width
            # clear screen after right click
            if(e.type == pygame.MOUSEBUTTONDOWN and e.button == 3):
                screen.fill(white)
            # quit
            if e.type == pygame.QUIT:
                raise StopIteration
            # start drawing after left click
            if(e.type == pygame.MOUSEBUTTONDOWN and e.button != 3):
                color = black
                pygame.draw.circle(screen, color, e.pos, radius) # surface, color, 圆心坐标， 半径
                draw_on = True
            # stop drawing after releasing left click
            if e.type == pygame.MOUSEBUTTONUP and e.button != 3:
                draw_on = False
                fname = "out.png"
                img = crope(screen)
                pygame.image.save(img, "out.png")
                output_img, label = get_output_image(fname)
                show_output_image(1, output_img)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LSHIFT]:
                if keys[pygame.K_EQUALS]:
                    calculation(label, "+")
                if keys[pygame.K_MINUS]:
                    calculation(label, "-")
                if keys[pygame.K_8]:
                    calculation(label, "*")
                if keys[pygame.K_SLASH]:
                    calculation(label, "/")

            # start drawing line on screen if draw is true
            if e.type == pygame.MOUSEMOTION:
                if draw_on:
                    pygame.draw.circle(screen, color, e.pos, radius)
                    roundline(screen, color, e.pos, last_pos, radius)
                last_pos = e.pos


            pygame.display.flip()

    except StopIteration:
        pass

    pygame.quit()
    return

if __name__ == "__main__":
    main()