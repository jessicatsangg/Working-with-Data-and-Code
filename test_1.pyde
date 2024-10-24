# Variables
speed = 0  # Current speed of the treadmill
characters = []  # List to hold character images
current_unlocked = None  # To track the currently unlocked character
distance = 0  # Total distance travelled
time_elapsed = 0  # Total time elapsed
frame_counter = 0  # To measure time
grass_visible = False  # To track if grass should be displayed

# Starts it and then loads the images
def setup():
    global characters
    size(800, 600)
    characters.append(loadImage("monkey.png"))
    characters.append(loadImage("tiger.png"))
    characters.append(loadImage("lion.png"))
    characters.append(loadImage("grass.png"))  

    textAlign(LEFT, TOP)  
    textSize(24)          
    fill(255)

# Main draw loop
def draw():
    global speed, distance, time_elapsed, frame_counter
    background(0)
    
    # Simulating speed increase
    if frame_counter % 100 == 0:  # Every 100 frames, we simulate a speed increase
        speed += 0.5
    
    # Determine time increment based on speed
    time_increment = 1.0  # Default time increment
    if speed < 3:
        time_increment = 0.5  # Faster time progression at lower speeds

    # Simulate time and distance
    time_elapsed += time_increment / 60.0  # Adjust time based on increment
    distance = speed * (time_elapsed / 60.0)  # Distance is speed * time
    
    # Unlock characters based on speed
    unlock_characters(speed)
    
    # Draw the grass at the bottom if it is visible
    if grass_visible:
        x = 0  # X coordinate for grass 
        y = height - characters[3].height  # Y coordinate for grass (bottom of the screen)
        image(characters[3], x, y) 

    # Draw the currently unlocked character
    draw_current_character()
    
    # Display speed, distance, and time
    display_stats(speed, distance, time_elapsed)
    
    frame_counter += 1

# Function to display the stats (speed, distance, time)
def display_stats(speed, distance, time_elapsed):
    text("Speed: " + str(round(speed, 2)) + " km/h", 10, 10) 
    text("Distance: " + str(round(distance, 2)) + " km", 10, 40)
    text("Time: " + str(round(time_elapsed, 2)) + " minutes", 10, 70)

# Function to unlock characters based on speed
def unlock_characters(speed):
    global current_unlocked, grass_visible
    if speed >= 7:
        current_unlocked = "lion"  # Lion is unlocked at speed 7
        grass_visible = True  # Make grass visible when lion is unlocked
    elif speed >= 5:
        current_unlocked = "tiger"  # Tiger is unlocked at speed 5
        grass_visible = True  # Make grass visible for tiger
    elif speed >= 3:
        current_unlocked = "monkey"  # Monkey is unlocked at speed 3
        grass_visible = True  # Make grass visible for monkey

# Function to draw the currently unlocked character
def draw_current_character():
    global current_unlocked
    
    # Define coordinates for each character
    if current_unlocked == "monkey":
        x = 300  # X coordinate for monkey
        y = 200  # Y coordinate for monkey
        image(characters[0], x, y)  # Draw monkey at specified coordinates
        
    elif current_unlocked == "tiger":
        x = 400  # X coordinate for tiger
        y = 200  # Y coordinate for tiger
        image(characters[1], x, y)  # Draw tiger at specified coordinates
        
    elif current_unlocked == "lion":
        x = 300  # X coordinate for lion
        y = 200  # Y coordinate for lion
        image(characters[2], x, y)  # Draw lion at specified coordinates
