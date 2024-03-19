import rotatescreen
import time

screen = rotatescreen.get_primary_display()
start_pos = screen.current_orientation
for i in range(1,4):
    pos = abs((start_pos -i*90) % 360) 
    screen.rotate_to(pos)
    time.sleep(0.00000001)