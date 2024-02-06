import cv2
import mediapipe as mp
import pygame
import random
import time
import sys
# Initialize pygame
def prog():
    pygame.init()
screen = pygame.display.set_mode([1000, 1000])

width,height=1000,1000
# Set up the font
font_size = 50
font = pygame.font.Font(None, font_size)  # None uses the default font

# Set up the multiline text
multiline_text = [
    "BALL NINJA",
    "Enter the duration of your playtime in terminal window",
]

text_color = (0, 255, 0)  # White
pp=0
# Main game loop
while(pp<=5):
    pp=pp+1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0,0,0))  # Fill with black background

    # Render and display each line of text
    y_position = height // 2 - (font_size * len(multiline_text)) // 2
    for line in multiline_text:
        text_surface = font.render(line, True, text_color)
        text_rect = text_surface.get_rect(center=(width // 2, y_position))
        screen.blit(text_surface, text_rect)
        y_position += font_size  # Move down for the next line

    # Update the display
    pygame.display.flip()

# Set up the ball
width, height = 500,400
ball_radius = 20
ball_color = (100, 100, 0)
ball_color1=(0,100,100) 
num_balls=2
co=0

# Generate random starting positions for each ball
ball_positions = [[random.uniform(0, 600), ball_radius] for j in range(num_balls)]

# Set up the clock
clock = pygame.time.Clock()

# Initialize mediapipe
mp_hands = mp.solutions.hands
mp_pose=mp.solutions.pose
hands = mp_hands.Hands()
pose = mp_pose.Pose()

# Open webcam
cap = cv2.VideoCapture(0)

def getpose(pos):
    landmarks=results_pose.pose_landmarks
    point=landmarks.landmark[pos]
    x, y, _ = int(point.x * frame.shape[1]), int(point.y * frame.shape[0]), int(point.z * frame.shape[0])
    return x,y


# A function to draw a line between two given landmarks.
def drawlinepose(pos1, pos2):
    try:
        pygame.draw.line(screen,(0,0,255), (getpose(pos1)), (getpose(pos2)),3)
    except:
        print()

inp=int(input("enter the duration of your play time:") )
tim_i=time.time()
c=0
while (c==0):
    while cap.isOpened() and time.time()-tim_i<=inp:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with mediapipe hands
    results_hands = hands.process(rgb_frame)
    results_pose = pose.process(rgb_frame)
    
    screen.fill((255, 255, 255))
   

    

   
    # Create empty lists to store the x & y values of the landmarks. The lists will contain n sub-lists where n is the number of hands seen
    coordsx_hands=[]
    coordsy_hands=[]
    
    coordsx_pose=[]
    coordsy_pose=[]
    


    # Iterative variable
    i=0


        # BODY STUFF STARTS
    
    # Check if bodies are detected
    if results_pose.pose_landmarks:
        landmarks=results_pose.pose_landmarks
        
        # A function to fet the position of a particular landmark.
        
        # Drawing landmarks in opencv display.
        for point in landmarks.landmark:
            # Extract landmarks (x, y, z) and put them in the respective sub-list.
            x, y, _ = int(point.x * frame.shape[1]), int(point.y * frame.shape[0]), int(point.z * frame.shape[0])
            #cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)
        

    # Body Drawing:

    #print(coordsx_hands)
    #for itr in range(len(coordsx_hands)):
        
    drawlinepose(15,13)
    drawlinepose(13,11)
    drawlinepose(11,12)
    drawlinepose(12,14)
    drawlinepose(14,16)
    drawlinepose(11,23)
    drawlinepose(12,24)
    drawlinepose(23,24)
    drawlinepose(23,25)
    drawlinepose(25,27)
    drawlinepose(24,26)
    drawlinepose(26,28)
    try:
        x_a,y_a=getpose(0)
        x_b,y_b=getpose(9)
        
        radius=((x_a-x_b)**2+(y_a-y_b)**2)**(0.5)
        
        pygame.draw.circle(screen,(0,0,255), (getpose(0)), radius)
        pygame.draw.circle(screen,(255,255,255), (getpose(0)), radius-2)
    except:
        print()
    
    

    # BODY STUFF ENDS
    
   #face details
    
    x1, y1= getpose(14)
    x2,y2= getpose(16)
    x3, y3= getpose(13)
    x4,y4= getpose(15)
    a,b=getpose(2)
    
    c,d=getpose(5)
    
    e,f=getpose(0)
    
    g,h=getpose(10)
    r,s=getpose(9)
    l,m=getpose(12)
    o,t=getpose(11)
 
    pygame.draw.circle(screen, (255,0,0),(e-20,f-10), 7)
    pygame.draw.circle(screen, (255,0,0),(e+20,f-10), 7)
#eyebrows
    pygame.draw.line(screen,(255,255,255), (e-25,(f-23)),(e-5,(f-23)),4)
    pygame.draw.line(screen,(255,255,255), (e+15,(f-23)),(e+35,(f-23)),4)


    pygame.draw.line(screen,(0,0,0), (e-25,(f-23)),(e-5,(f-23)),2)
    pygame.draw.line(screen,(0,0,0), (e+15,(f-23)),(e+35,(f-23)),2)
    #eyes
    pygame.draw.circle(screen, (255,255,255),(e-20,f-10), 5)
    pygame.draw.circle(screen, (255,255,255),(e+20,f-10), 5)

    pygame.draw.circle(screen, (0,0,0),(e-20,f-10), 2)
    pygame.draw.circle(screen, (0,0,0),(e+20,f-10), 2)
    
    #nose
    pygame.draw.line(screen,(0,0,0), (e,(f-10)),(e+3,(f+10)))
    pygame.draw.line(screen,(0,0,0), (e,(f-10)),(e-3,(f+10)))
    
    pygame.draw.circle(screen, (0,0,0),(e-3,f+15), 3)
    pygame.draw.circle(screen, (0,0,0),(e+3,f+15), 3)
    pygame.draw.circle(screen, (255,255,255),(e-3,f+15), 2)
    pygame.draw.circle(screen, (255,255,255),(e+3,f+15), 2)

#mouth
    pygame.draw.line(screen,(0,0,0), (r-10,s-5),(g+10,h-5),5)
    pygame.draw.line(screen,(255,0,0), (r-10,s-5),(g+10,h-5),3)
    
    #neck
    pygame.draw.line(screen,(0,0,255), (g,h+5),(g,h+60),2)
    pygame.draw.line(screen,(0,0,255), (l,m),(g,h+60),2)
    pygame.draw.line(screen,(0,0,255), (o,t),(r,s+60),2)
    pygame.draw.line(screen,(0,0,255), (r,s+60),(r,s+5),2)
    
    #hair
    pygame.draw.line(screen,(0,0,0), (c,d-2),(c,d-20),2)
    pygame.draw.line(screen,(0,0,0), (c+30,d-5),(c+30,d-20),2)
    pygame.draw.line(screen,(0,0,0), (c+10,d-2),(c+10,d-20),2)
    pygame.draw.line(screen,(0,0,0), (c+40,d-2),(c+40,d-20),2)
    pygame.draw.line(screen,(0,0,0), (c+20,d-5),(c+20,d-20),2)
    pygame.draw.line(screen,(0,0,0), (c+50,d-1),(c+50,d-20),2)
    pygame.draw.line(screen,(0,0,0), (c+60,d+5),(c+60,d-20),2)
    pygame.draw.line(screen,(0,0,0), (c-10,d+5),(c-10,d-20),2)


    #chest 
    '''pygame.draw.circle(screen, (0,0,0),(g-20,h+200), 40)
    pygame.draw.circle(screen, (0,0,0),(r+20,s+200), 40)
    pygame.draw.circle(screen, (255,255,255),(g-20,h+200), 38)
    pygame.draw.circle(screen, (255,255,255),(r+20,s+200), 38)
    pygame.draw.circle(screen, (0,0,0),(g-20,h+200), 5)
    pygame.draw.circle(screen, (0,0,0),(r+20,s+200), 5)

    #6packs
    pygame.draw.line(screen,(0,0,0), (e,f+300),(e,f+500),2)
    pygame.draw.line(screen,(0,0,0), (e-50,f+350),(e+50,f+350),2)
    pygame.draw.line(screen,(0,0,0), (e-50,f+400),(e+50,f+400),2)
    pygame.draw.line(screen,(0,0,0), (e-50,f+450),(e+50,f+450),2)'''
    




     # HAND STUFF STARTS
 
    # Check if hands are detected
    if results_hands.multi_hand_landmarks:
        for landmarks in results_hands.multi_hand_landmarks:

            # Create an empty sub-list for each hand.
            coordsx_hands.append([])
            coordsy_hands.append([])
            
            for point in landmarks.landmark:
                
                # Extract hand landmarks (x, y, z) and put them in the respective sub-list.
                x, y, _ = int(point.x * frame.shape[1]), int(point.y * frame.shape[0]), int(point.z * frame.shape[0])
                coordsx_hands[i].append(x)
                coordsy_hands[i].append(y)
                
 
                # Draw a circle at each hand landmark
                #pygame.draw.circle(screen, (0,0,255), (x,y), 5)
                #cv2.circle(frame, (x, y), 5, (0,255, 0), -1)
            
            i+=1
           
    # Hand Drawing
    if coordsx_hands!=[]:
        #print(coordsx_hands)
        for itr in range(len(coordsx_hands)):
            
            # Thumb
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][0],coordsy_hands[itr][0]), (coordsx_hands[itr][1],coordsy_hands[itr][1]),3)
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][1],coordsy_hands[itr][1]), (coordsx_hands[itr][2],coordsy_hands[itr][2]),3)
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][2],coordsy_hands[itr][2]), (coordsx_hands[itr][3],coordsy_hands[itr][3]),3)
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][3],coordsy_hands[itr][3]), (coordsx_hands[itr][4],coordsy_hands[itr][4]),3)
            
            # Middle
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][9],coordsy_hands[itr][9]), (coordsx_hands[itr][10],coordsy_hands[itr][10]),3)
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][10],coordsy_hands[itr][10]), (coordsx_hands[itr][11],coordsy_hands[itr][11]),3)
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][11],coordsy_hands[itr][11]), (coordsx_hands[itr][12],coordsy_hands[itr][12]),3)
            
            # Ring
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][13],coordsy_hands[itr][13]), (coordsx_hands[itr][14],coordsy_hands[itr][14]),3)
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][14],coordsy_hands[itr][14]), (coordsx_hands[itr][15],coordsy_hands[itr][15]),3)
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][15],coordsy_hands[itr][15]), (coordsx_hands[itr][16],coordsy_hands[itr][16]),3)
            
            # Little
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][17],coordsy_hands[itr][17]), (coordsx_hands[itr][18],coordsy_hands[itr][18]),3)
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][18],coordsy_hands[itr][18]), (coordsx_hands[itr][19],coordsy_hands[itr][19]),3)
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][19],coordsy_hands[itr][19]), (coordsx_hands[itr][20],coordsy_hands[itr][20]),3)
            
            # Index
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][5],coordsy_hands[itr][5]), (coordsx_hands[itr][6],coordsy_hands[itr][6]),3)
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][6],coordsy_hands[itr][6]), (coordsx_hands[itr][7],coordsy_hands[itr][7]),3)
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][7],coordsy_hands[itr][7]), (coordsx_hands[itr][8],coordsy_hands[itr][8]),3)
            

    for i in range(num_balls):
        if(ball_positions[i][1]<=600):
            ball_speed=random.uniform(0,10)
            ball_positions[i][1] += ball_speed
            if(ball_positions[i][1]==0):
                 x=random.uniform(0,255)
                 y=random.uniform(0,255) 
                 z=random.uniform(0,255)
                 ball_color=((x,y,z))
                 ball_color1=((z,y,x))


           
        else:
            x=random.uniform(0,255)
            y=random.uniform(0,255) 
            z=random.uniform(0,255)
            ball_color=((x,y,z))
            ball_color1=((z,y,x))
            ball_positions[i][0]=random.uniform(0,width)
            ball_positions[i][1]=0
 
    # Clear the screen
    #screen.fill((255, 255, 255))  # White

    # Draw each ball
    for i in range(num_balls):
        p,q=int(ball_positions[i][0]), int(ball_positions[i][1])
        pygame.draw.circle(screen, ball_color, (int(ball_positions[i][0]), int(ball_positions[i][1])), ball_radius)
        cv2.circle(frame,(int(ball_positions[i][0]), int(ball_positions[i][1])), ball_radius, ball_color1,-1)
        area=abs(((x1)*(y2-q)+(x2)*(q-y1)+(p)*(y1-y2)))
        area1=abs(((x3)*(y4-q)+(x4)*(q-y3)+(p)*(y3-y4)))
        d1=((p-x1)**2+(q-y1)**2)**0.5
        d2=((p-x2)**2+(q-y2)**2)**0.5
        d3=((x2-x1)**2+(y2-y1)**2)**0.5
        d4=((p-x3)**2+(q-y3)**2)**0.5
        d5=((p-x4)**2+(q-y4)**2)**0.5
        d6=((x4-x3)**2+(y4-y3)**2)**0.5

        #if i==0:
           # print("og ball ",i," ",area1 )

        if(d1>d2):
            if((area<1000) and ((d1*2)<=(d22 + d3*2))):
                co=co+1
                ball_positions[i][1]=0
                ball_positions[i][0]=random.uniform(0,width)
                #print("ball ",i," ",area)
        if(d2>d1):
            if((area<1000) and (d2*2)<=(d12 + d3*2)):
                 co=co+1
                 ball_positions[i][1]=0
                 ball_positions[i][0]=random.uniform(0,width)
                 

        if(d4>d5):
            if((area1<1000) and (d4*2)<=(d52 + d6*2)):
                 co=co+1
                 ball_positions[i][1]=0
                 ball_positions[i][0]=random.uniform(0,width)
                 
        if(d5>d4):
            if(( area1<1000) and (d5*2)<=(d42 + d6*2)):
                 co=co+1
                 ball_positions[i][1]=0
                 ball_positions[i][0]=random.uniform(0,width)

    


    # Update the display
    #pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
    # Display the frame
    cv2.imshow('Hand Tracking', frame)
    
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Set up the font
    font = pygame.font.Font(None, 30)  # None uses the default font, 36 is the font size

    # Set up the text
    text = "TIME LEFT:"
    tl=inp-time.time()+tim_i
    text1=text +"  "+ str(int(tl))+" secs"
    text_color = (0,0,0)
   # Render the text
    text_surface = font.render(text1, True, text_color)

    # Get the rectangle containing the text surface
    text_rect = text_surface.get_rect()

    # Center the text on the screen
    text_rect.center = (500,100)

    # Blit the text surface onto the screen
    screen.blit(text_surface, text_rect)

    # Set up the text
    text = "POINTS SCORED:"
    text1=text +"  "+ str(co)
    text_color = (0,0,0)
   # Render the text
    text_surface = font.render(text1, True, text_color)

    # Get the rectangle containing the text surface
    text_rect = text_surface.get_rect()

    # Center the text on the screen
    text_rect.center = (500,130)

    # Blit the text surface onto the screen
    screen.blit(text_surface, text_rect)

    pygame.draw.line(screen,(0,0,0),(300,0),(300,160))
    
    
    # Flip display to show stuff
    pygame.display.flip()


print("points scored:", co)
# Release the webcam and close all windows
pygame.quit()
cap.release()
cv2.destroyAllWindows()
