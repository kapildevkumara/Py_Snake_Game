from init import *
from snake_game import *

if __name__ == "__main__":
	score = 0
	py_game = snake_game()
	py_game.generate_food()

	while True:
		d_image = np.zeros((screen_height, screen_width, 3))
		py_game.refresh_screen(d_image)
		cv2.imshow("Python_Snake_Game", d_image)
		key = cv2.waitKey(pause_time - inc_level * score)
		score = py_game.run_snake(d_image, key)
