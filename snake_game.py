from init import *

class snake_game:
	def __init__(self):
		self.snake_points = np.zeros((snake_length, 2)) 
		# Space Available for Snake Head and Food
		self.space_x = screen_width - unit_block - 1															
		self.space_y = screen_height - unit_block - 1
		self.direction = -1
		self.score = 0
		for i in range(snake_length):
			self.snake_points[i][0] = (int(self.space_x/2) // unit_block + i) * unit_block
			self.snake_points[i][1] = (int(self.space_y/2) // unit_block) * unit_block

	# Random Food Location
	def generate_food(self):																					
		self.food_x = (random.randint(0, self.space_x) // unit_block) * unit_block
		self.food_y = (random.randint(0, self.space_y) // unit_block) * unit_block	

	# Draw Snake and Food
	def refresh_screen(self, image):																			
		for i in range(snake_length):
			image = cv2.rectangle(image, (int(self.snake_points[i][0]),int(self.snake_points[i][1])), (int(self.snake_points[i][0]+unit_block),int(self.snake_points[i][1]+unit_block)), (0, 255, 0), -1) 
		image = cv2.rectangle(image, (self.food_x, self.food_y), (self.food_x + unit_block, self.food_y + unit_block), (0, 0, 255), -1) 

	# End Game
	def end_game(self, image):
		d_message = " Your Score  " + str(self.score)
		cv2.putText(image, d_message, (int(self.space_x/3), int(self.space_y/3)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
		cv2.imshow("Python_Snake_Game", image)
		key = cv2.waitKey(0)		
		sys.exit(d_message)

	# Run Snake
	def run_snake(self, image, key):
		snake_x = self.snake_points[0, 0]		
		snake_y = self.snake_points[0, 1]		
		is_hit = 0

		# Check Key Press Event; Validate if it doesnot reverse direction
		if((key == ord('a') or key == ord('j') or key == ord('A') or key == ord('J')) and self.direction != 1):										
			self.direction = -1
		elif((key == ord('s') or key == ord('k') or key == ord('S') or key == ord('K')) and self.direction != -2):
			self.direction = 2
		elif((key == ord('d') or key == ord('l') or key == ord('D') or key == ord('L')) and self.direction != -1):
			self.direction = 1
		elif((key == ord('w') or key == ord('i') or key == ord('W') or key == ord('I')) and self.direction != -2):
			self.direction = -2

		if(self.direction == -1):
			snake_x = snake_x - unit_block
		elif(self.direction == 2):
			snake_y = snake_y + unit_block
		elif(self.direction == 1):
			snake_x = snake_x + unit_block
		elif(self.direction == -2):
			snake_y = snake_y - unit_block
			
		for i in range(snake_length):
			if(self.snake_points[i, 0] == snake_x and self.snake_points[i, 1] == snake_y):
				is_hit = 1
		is_boundary_hit = (snake_x < 0 or snake_y < 0 or snake_x >= screen_width or snake_y >= screen_height)
		is_exit = (key == 27)

		# Reached Boundaries or Pressed Exit Key or Hit self
		if(is_boundary_hit or is_exit or is_hit):	
			self.end_game(image)

		# Reached Food
		elif(snake_x == self.food_x and snake_y == self.food_y):												
			self.generate_food()
			self.score = self.score + 1

		self.snake_points[1 : snake_length, :] = self.snake_points[0 : snake_length - 1, :]
		self.snake_points[0, 0] = snake_x
		self.snake_points[0, 1] = snake_y
		return self.score
