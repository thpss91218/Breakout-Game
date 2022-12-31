"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This user file runs a classic Breakout game.
Players can control the paddle with their mouse and score by hitting the colored bricks.
Extension: Added score and lives on the top of window.
Click mouse to start the game!
"""
from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second


def main():
    graphics = BreakoutGraphics()
    dx = 0
    dy = 0
    hit_bricks = 0
    lives = graphics.num_lives

    while True:
        pause(FRAME_RATE)
        # Ball drop to the bottom of window
        if graphics.ball.y + graphics.ball_radius*2 > graphics.window.height:
            lives -= 1
            graphics.lives_label.text = "Lives: " + str(lives)
            graphics.reset_ball()
            dx = graphics.get_dx()
            dy = graphics.get_dy()
        # If new round then get initial dx and dy
        if dx == 0 and dy == 0:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
        # Check if still alive and if user click to start and if all the bricks are gone
        if lives > 0 and dx != 0 and hit_bricks < 100:
            graphics.ball.move(dx, dy)
            # Check if touch walls
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball_radius*2 >= graphics.window.width:
                dx = -dx
            elif graphics.ball.y <= 0:
                dy = -dy
            # Check if four corners hit anything
            upper_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            lower_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball_radius*2)
            upper_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius*2, graphics.ball.y)
            lower_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius*2, graphics.ball.y + graphics.ball_radius*2)
            corners = [upper_left, lower_left, upper_right, lower_right]
            for corner in corners:
                if corner is graphics.paddle:
                    dy = -dy
                    graphics.ball.move(0, graphics.paddle.y - graphics.ball.y - graphics.ball_radius * 2)
                    break
                elif corner is not graphics.paddle and corner is not graphics.score_label and corner is not graphics.lives_label and corner is not None:
                    dy = -dy
                    graphics.window.remove(corner)
                    hit_bricks += 1
                    graphics.score_label.text = "Score: "+str(hit_bricks)
                    break


if __name__ == '__main__':
    main()
