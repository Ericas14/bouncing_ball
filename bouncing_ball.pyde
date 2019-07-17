ball_y = 100
y_speed = 6
ball_x = 100
x_speed = 6

ball2_y = 100
y2_speed = 6
ball2_x = 100
x2_speed = 6

def setup():    #runs once
    size(500,500)
    
def draw():     #runs multiple times
    global ball_y
    global y_speed
    global ball_x
    global x_speed
    global ball2_y
    global y2_speed
    global ball2_x
    global x2_speed
    background(200,200,200)
    ellipse(ball_x,ball_y,100,100)
    ellipse(ball2_x,ball2_y,100,100)
    line(0,400,500,400)
    
    ball_y = ball_y + y_speed #ball_y += 1
    ball_x = ball_x + x_speed
    
    #ball2_y = ball2_y + y2_speed #ball_y += 1
    #ball2_x = ball2_x + x2_speed
    
    if ball_y > 350:
        fill(random(0,255),random(0,255),random(0,255))
        y_speed = y_speed*-1
    if ball_y < 50:
        fill(random(0,255),random(0,255),random(0,255))
        y_speed = y_speed * -1
    if ball_x < 50:
        fill(random(0,255),random(0,255),random(0,255))
        x_speed = x_speed * -1
    if ball_x > 450:
        fill(random(0,255),random(0,255),random(0,255))
        x_speed = x_speed * -1
        
    if ball2_y > 350:
        fill(random(0,255),random(0,255),random(0,255))
        y2_speed = y2_speed*-1
    if ball2_y < 50:
        fill(random(0,255),random(0,255),random(0,255))
        y2_speed = y2_speed * -1
    if ball2_x < 50:
        fill(random(0,255),random(0,255),random(0,255))
        x2_speed = x2_speed * -1
    if ball2_x > 450:
        fill(random(0,255),random(0,255),random(0,255))
        x2_speed = x2_speed * -1   
    
        
   # elif 
    
