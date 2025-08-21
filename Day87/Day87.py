'''
Topics to Cover:
- Using Python Turtle, build a clone of the 80s hit game Breakout.
'''

# Breakout clone using Python's turtle module
# ------------------------------------------
# Controls: Left/Right arrow keys (or A/D) to move the paddle. Press 'p' to pause/resume, 'q' to quit.
# Run with standard Python (no external libraries needed).

import turtle as t
import random
import time
import math
from dataclasses import dataclass

# --- Config ---
WIDTH, HEIGHT = 800, 600
WALL_LEFT, WALL_RIGHT = -WIDTH//2 + 10, WIDTH//2 - 10
WALL_TOP, WALL_BOTTOM = HEIGHT//2 - 10, -HEIGHT//2 + 10

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_SPEED = 20

BALL_SPEED = 5.0  # base pixel step per frame (scaled by dx/dy unit vector)
BALL_RADIUS = 8

ROWS = 6
COLS = 10
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
BRICK_GAP = 6
BRICK_TOP_OFFSET = 120

LIVES_START = 3
FPS = 120  # logical frames per second

# colors per row (from top to bottom)
ROW_COLORS = ["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#3498db", "#9b59b6"]

# --- Helpers ---

def make_turtle(shape="square", color="white", hidden=False):
    tr = t.Turtle(visible=not hidden)
    tr.shape(shape)
    tr.color(color)
    tr.penup()
    tr.speed(0)
    return tr

@dataclass
class Paddle:
    turt: t.Turtle
    half_w: float = PADDLE_WIDTH/2
    half_h: float = PADDLE_HEIGHT/2

    def move(self, dx):
        x = self.turt.xcor() + dx
        # clamp inside walls
        x = max(WALL_LEFT + self.half_w, min(WALL_RIGHT - self.half_w, x))
        self.turt.setx(x)

    def set_size(self, w, h):
        self.half_w, self.half_h = w/2, h/2
        # turtle stretch is relative to 20x20 base square
        self.turt.shapesize(stretch_wid=h/20, stretch_len=w/20)

@dataclass
class Ball:
    turt: t.Turtle
    dx: float
    dy: float
    speed_px: float = BALL_SPEED

    def step(self):
        self.turt.setx(self.turt.xcor() + self.dx * self.speed_px)
        self.turt.sety(self.turt.ycor() + self.dy * self.speed_px)

    def reset_on_paddle(self, paddle: Paddle):
        self.turt.goto(paddle.turt.xcor(), WALL_BOTTOM + 80)
        # launch with random slight angle upward
        angle = random.uniform(30, 150)
        rad = angle * 3.14159 / 180
        self.dx = math.cos(rad)
        self.dy = math.sin(rad)
        if self.dy < 0:
            self.dy *= -1

@dataclass
class Brick:
    turt: t.Turtle
    w: float
    h: float
    alive: bool = True

    def kill(self):
        self.alive = False
        self.turt.hideturtle()
        self.turt.goto(10000, 10000)  # move off-screen

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.lives = LIVES_START
        self.writer = make_turtle(hidden=True)
        self.writer.goto(0, WALL_TOP - 30)

    def draw(self):
        self.writer.clear()
        self.writer.color("#ecf0f1")
        self.writer.write(f"Score: {self.score}    Lives: {self.lives}", align="center", font=("Courier", 16, "bold"))

    def add(self, n):
        self.score += n
        self.draw()

    def lose_life(self):
        self.lives -= 1
        self.draw()

# --- Setup Screen ---
screen = t.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Breakout - Python Turtle Edition")
screen.bgcolor("#1e272e")
screen.tracer(0)  # manual animation

# Walls (visual borders)
border = make_turtle(hidden=True)
border.color("#95a5a6")
border.pensize(3)
border.goto(WALL_LEFT, WALL_BOTTOM)
border.pendown()
for x, y in [
    (WALL_RIGHT, WALL_BOTTOM),
    (WALL_RIGHT, WALL_TOP),
    (WALL_LEFT, WALL_TOP),
    (WALL_LEFT, WALL_BOTTOM)
]:
    border.goto(x, y)
border.penup()

# Paddle
paddle_t = make_turtle()
paddle_t.color("#ecf0f1")
paddle = Paddle(paddle_t)
paddle.set_size(PADDLE_WIDTH, PADDLE_HEIGHT)
paddle.turt.goto(0, WALL_BOTTOM + 60)

# Ball
ball_t = make_turtle(shape="circle")
ball_t.shapesize(stretch_len=BALL_RADIUS/10, stretch_wid=BALL_RADIUS/10)
ball_t.color("#f5f6fa")
ball = Ball(ball_t, dx=0.7, dy=0.7)
ball.reset_on_paddle(paddle)

# Bricks
bricks = []

# compute total width of a row
row_width = COLS * BRICK_WIDTH + (COLS - 1) * BRICK_GAP
start_x = -row_width / 2 + BRICK_WIDTH/2
start_y = WALL_TOP - BRICK_TOP_OFFSET

for r in range(ROWS):
    color = ROW_COLORS[r % len(ROW_COLORS)]
    for c in range(COLS):
        bx = start_x + c * (BRICK_WIDTH + BRICK_GAP)
        by = start_y - r * (BRICK_HEIGHT + BRICK_GAP)
        bt = make_turtle()
        bt.color(color)
        bt.shape("square")
        bt.shapesize(stretch_len=BRICK_WIDTH/20, stretch_wid=BRICK_HEIGHT/20)
        bt.goto(bx, by)
        bricks.append(Brick(bt, BRICK_WIDTH, BRICK_HEIGHT))

# HUD
hud = Scoreboard()
hud.draw()

# Input handling
keys = {"left": False, "right": False}
paused = False
running = True


def go_left():
    keys["left"] = True

def stop_left():
    keys["left"] = False

def go_right():
    keys["right"] = True

def stop_right():
    keys["right"] = False

def toggle_pause():
    global paused
    paused = not paused

def quit_game():
    global running
    running = False

screen.listen()
screen.onkeypress(go_left, "Left")
screen.onkeyrelease(stop_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeyrelease(stop_right, "Right")
screen.onkeypress(go_left, "a")
screen.onkeyrelease(stop_left, "a")
screen.onkeypress(go_right, "d")
screen.onkeyrelease(stop_right, "d")
screen.onkeypress(toggle_pause, "p")
screen.onkeypress(quit_game, "q")

# --- Collision helpers ---

def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def collide_ball_rect(ball: Ball, rx, ry, rw, rh):
    """Return the collision normal as (nx, ny) or (0,0) if no hit."""
    bx, by = ball.turt.xcor(), ball.turt.ycor()
    # closest point on rectangle to circle center
    cx = clamp(bx, rx - rw/2, rx + rw/2)
    cy = clamp(by, ry - rh/2, ry + rh/2)
    dx = bx - cx
    dy = by - cy
    if dx*dx + dy*dy <= BALL_RADIUS*BALL_RADIUS:
        # Determine side of impact by comparing penetration along axes
        if abs(dx) > abs(dy):
            return (1 if dx > 0 else -1, 0)  # horizontal normal
        else:
            return (0, 1 if dy > 0 else -1)  # vertical normal
    return (0, 0)


# --- Main loop ---
frame_delay = 1.0 / FPS
last_time = time.time()

while running:
    now = time.time()
    # simple frame pacing (best-effort)
    if now - last_time < frame_delay:
        time.sleep(frame_delay - (now - last_time))
    last_time = time.time()

    if paused:
        screen.update()
        continue

    # move paddle by keys
    if keys["left"]:
        paddle.move(-PADDLE_SPEED)
    if keys["right"]:
        paddle.move(PADDLE_SPEED)

    # move ball
    ball.step()

    bx, by = ball.turt.xcor(), ball.turt.ycor()

    # wall collisions (left/right)
    if bx - BALL_RADIUS <= WALL_LEFT:
        ball.turt.setx(WALL_LEFT + BALL_RADIUS)
        ball.dx *= -1
    elif bx + BALL_RADIUS >= WALL_RIGHT:
        ball.turt.setx(WALL_RIGHT - BALL_RADIUS)
        ball.dx *= -1

    # top wall
    if by + BALL_RADIUS >= WALL_TOP:
        ball.turt.sety(WALL_TOP - BALL_RADIUS)
        ball.dy *= -1

    # bottom (miss)
    if by - BALL_RADIUS <= WALL_BOTTOM:
        hud.lose_life()
        if hud.lives <= 0:
            # Game Over
            msg = make_turtle(hidden=True)
            msg.color("#e74c3c")
            msg.goto(0, 0)
            msg.write("GAME OVER", align="center", font=("Courier", 28, "bold"))
            screen.update()
            break
        ball.reset_on_paddle(paddle)

    # paddle collision
    nx, ny = collide_ball_rect(ball, paddle.turt.xcor(), paddle.turt.ycor(), PADDLE_WIDTH, PADDLE_HEIGHT)
    if nx or ny:
        # reflect
        if nx:
            ball.dx *= -1
        if ny:
            ball.dy = abs(ball.dy)  # ensure it goes upward
        # tweak angle based on where it hit the paddle
        offset = (bx - paddle.turt.xcor()) / paddle.half_w  # -1 .. 1
        ball.dx = clamp(ball.dx + 0.3 * offset, -1.2, 1.2)
        # normalize vector roughly
        mag = (ball.dx**2 + ball.dy**2) ** 0.5
        ball.dx /= mag
        ball.dy /= mag
        # nudge outside paddle to avoid sticking
        ball.turt.sety(paddle.turt.ycor() + PADDLE_HEIGHT/2 + BALL_RADIUS + 1)

    # brick collisions
    remaining = 0
    for br in bricks:
        if not br.alive:
            continue
        remaining += 1
        nx, ny = collide_ball_rect(ball, br.turt.xcor(), br.turt.ycor(), br.w, br.h)
        if nx or ny:
            br.kill()
            hud.add(10)
            if nx:
                ball.dx *= -1
            if ny:
                ball.dy *= -1
            # small acceleration after each brick to ramp difficulty
            ball.speed_px = min(ball.speed_px * 1.01, 12)
            # Break after first hit this frame to avoid tunneling through multiple bricks
            break

    if remaining == 0:
        msg = make_turtle(hidden=True)
        msg.color("#2ecc71")
        msg.goto(0, 0)
        msg.write("YOU WIN!", align="center", font=("Courier", 28, "bold"))
        screen.update()
        break

    screen.update()

# Clean exit when user closes the window or presses 'q'
try:
    while True:
        screen.update()
        time.sleep(0.05)
except t.Terminator:
    pass