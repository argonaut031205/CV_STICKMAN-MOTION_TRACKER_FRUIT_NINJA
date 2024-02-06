import cv2
import mediapipe as mp
import pygame
import random
# Initialize pygame
pygame.init()
screen = pygame.display.set_mode([1000, 1000])

# Set up the ball
width, height = 1000,1000
ball_radius = 20
ball_color = (100, 100, 0)  # black
num_balls =4

# Generate random starting positions for each ball
ball_positions = [[random.uniform(0, width), ball_radius] for j in range(num_balls)]

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
        pygame.draw.line(screen,(0,0,255), (getpose(pos1)), (getpose(pos2)))
    except:
        print()
        
while cap.isOpened():
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
    
    # HAND STUFF STARTS
    
    
    # Check if hands are detected
    '''if results_hands.multi_hand_landmarks:
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
                """pygame.draw.circle(screen, (0,0,255), (x,y), 5)"""
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            
            i+=1
            
    # Hand Drawing
    if coordsx_hands!=[]:
        #print(coordsx_hands)
        for itr in range(len(coordsx_hands)):
            
            # Thumb
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][0],coordsy_hands[itr][0]), (coordsx_hands[itr][1],coordsy_hands[itr][1]))
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][1],coordsy_hands[itr][1]), (coordsx_hands[itr][2],coordsy_hands[itr][2]))
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][2],coordsy_hands[itr][2]), (coordsx_hands[itr][3],coordsy_hands[itr][3]))
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][3],coordsy_hands[itr][3]), (coordsx_hands[itr][4],coordsy_hands[itr][4]))
            
            # Middle
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][9],coordsy_hands[itr][9]), (coordsx_hands[itr][10],coordsy_hands[itr][10]))
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][10],coordsy_hands[itr][10]), (coordsx_hands[itr][11],coordsy_hands[itr][11]))
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][11],coordsy_hands[itr][11]), (coordsx_hands[itr][12],coordsy_hands[itr][12]))
            
            # Ring
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][13],coordsy_hands[itr][13]), (coordsx_hands[itr][14],coordsy_hands[itr][14]))
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][14],coordsy_hands[itr][14]), (coordsx_hands[itr][15],coordsy_hands[itr][15]))
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][15],coordsy_hands[itr][15]), (coordsx_hands[itr][16],coordsy_hands[itr][16]))
            
            # Little
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][17],coordsy_hands[itr][17]), (coordsx_hands[itr][18],coordsy_hands[itr][18]))
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][18],coordsy_hands[itr][18]), (coordsx_hands[itr][19],coordsy_hands[itr][19]))
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][19],coordsy_hands[itr][19]), (coordsx_hands[itr][20],coordsy_hands[itr][20]))
            
            # Index
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][5],coordsy_hands[itr][5]), (coordsx_hands[itr][6],coordsy_hands[itr][6]))
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][6],coordsy_hands[itr][6]), (coordsx_hands[itr][7],coordsy_hands[itr][7]))
            pygame.draw.line(screen,(0,0,255), (coordsx_hands[itr][7],coordsy_hands[itr][7]), (coordsx_hands[itr][8],coordsy_hands[itr][8]))'''
            
    
    # HAND STUFF ENDS
 
    # BODY STUFF STARTS
    
    # Check if bodies are detected
    if results_pose.pose_landmarks:
        landmarks=results_pose.pose_landmarks
        
        # A function to fet the position of a particular landmark.
        
        # Drawing landmarks in opencv display.
        for point in landmarks.landmark:
            # Extract landmarks (x, y, z) and put them in the respective sub-list.
            x, y, _ = int(point.x * frame.shape[1]), int(point.y * frame.shape[0]), int(point.z * frame.shape[0])
            cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)
        

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
        
        radius=(((x_a-x_b)**2+(y_a-y_b)**2)**(0.5))*2
        
        pygame.draw.circle(screen,(0,0,255), (getpose(0)), radius)
    except:
        print()
    
    

    # BODY STUFF ENDS
    
    
    
    # Display the frame
    cv2.imshow('Hand Tracking', frame)
    
    for i in range(num_balls):
        if(ball_positions[i][1]<=600):
            ball_speed=random.uniform(0,15)
            ball_positions[i][1] += ball_speed

        else:
            ball_color= (random.uniform(0,255),random.uniform(0,255), random.uniform(0,255)) 
            ball_positions[i][0]=random.uniform(0,width)
            ball_positions[i][1]=0
        


    # Clear the screen
    #screen.fill((255, 255, 255))  # White

    # Draw each ball
    for i in range(num_balls):
        pygame.draw.circle(screen, ball_color, (int(ball_positions[i][0]), int(ball_positions[i][1])), ball_radius)
    
    
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
    # Flip display to show stuff
    pygame.display.flip()


# Release the webcam and close all windows
pygame.quit()
cap.release()
cv2.destroyAllWindows()
