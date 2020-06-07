from init import *
from snake_game import *
from cheat_code import *

if __name__ == "__main__":
	score = 0
	mode = 0
	wait_time = pause_time
	py_game = snake_game()
	py_game.generate_food()
	ai_gamer = cheat_code()

	while True:
		d_image = np.zeros((screen_height, screen_width, 3))
		py_game.refresh_screen(d_image)
		cv2.imshow("Python_Snake_Game", d_image)

		if(wait_time > min_time):
			wait_time = pause_time - inc_level * score
		
		key = cv2.waitKey(wait_time)
		if(key != EXIT_KEY and (AI_MODE)):
			key = ai_gamer.hack(py_game.snake_points, py_game.food)

		score = py_game.run_snake(d_image, key)
