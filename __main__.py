from init import np, cv2
from init import PAUSE_TIME, MIN_TIME, INC_LEVEL, screen_height, screen_width, EXIT_KEY, AI_MODE
from snake_game import snake_game
from cheat_code import cheat_code

if __name__ == "__main__":
	score = 0
	mode = 0
	wait_time = PAUSE_TIME
	py_game = snake_game()
	py_game.generate_food()
	ai_gamer = cheat_code()

	while True:
		d_image = np.zeros((screen_height, screen_width, 3))
		py_game.refresh_screen(d_image)

		if wait_time > MIN_TIME:
			wait_time = PAUSE_TIME - INC_LEVEL * score

		cv2.imshow("Python_Snake_Game", d_image)		
		key = cv2.waitKey(wait_time)

		if key != EXIT_KEY and AI_MODE:
			key = ai_gamer.hack(py_game.snake_points, py_game.food)

		if cv2.getWindowProperty('Python_Snake_Game', cv2.WND_PROP_VISIBLE) < 1:
			d_message = " Your Score  " + str(py_game.score)
			print(d_message)
			break

		score = py_game.run_snake(d_image, key)
