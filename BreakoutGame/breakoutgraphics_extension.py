"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

BreakoutGraphics class sets out the skeleton for a typical Breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 5    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
NUM_LIVES = 5

class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width - paddle_width)/2, window_height-paddle_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, window_width/2-ball_radius,window_height/2-ball_radius)
        self.ball_radius = ball_radius
        # Create a score card
        self.score_label = GLabel('Score: 0')
        self.score_label.font = '-15'
        self.window.add(self.score_label, 8, 30)
        # Create a lives reminder
        self.num_lives = NUM_LIVES
        self.lives_label = GLabel('Lives:'+str(self.num_lives))
        self.lives_label.font = '-15'
        self.window.add(self.lives_label, 375, 30)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.reset_velocity)
        onmousemoved(self.paddle_track)
        # Draw bricks
        brick_y = brick_offset
        for i in range(1, brick_rows+1):
            brick_x = 0
            for j in range(1, brick_cols+1):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.window.add(self.brick, brick_x, brick_y)
                brick_x = brick_x + brick_width + brick_spacing
                if i <= 2:
                    self.brick.fill_color = 'Red'
                    self.brick.color = 'Red'
                elif 2 < i <= 4:
                    self.brick.fill_color = 'Orange'
                    self.brick.color = 'Orange'
                elif 4 < i <= 6:
                    self.brick.fill_color = 'Yellow'
                    self.brick.color = 'Yellow'
                elif 6 < i <= 8:
                    self.brick.fill_color = 'Green'
                    self.brick.color = 'Green'
                else:
                    self.brick.fill_color = 'Blue'
                    self.brick.color = 'Blue'
            brick_y = brick_y + brick_height + brick_spacing

    def paddle_track(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width/2
        half_paddle_length = self.paddle.width/2
        # right margin
        if self.window.width - mouse.x < half_paddle_length:
            self.paddle.x = self.window.width - self.paddle.width
        # left margin
        if mouse.x < half_paddle_length:
            self.paddle.x = 0

    def reset_velocity(self, mouse):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def reset_ball(self):
        self.ball.x = self.window.width/2-self.ball_radius
        self.ball.y = self.window.height/2-self.ball_radius
        self.__dx = 0
        self.__dy = 0

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy



