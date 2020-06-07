from init import *

class snake_game:
	def __init__(self):
		self.snake_points = np.zeros((SNAKE_LENGTH, 2), dtype = int) 
		# Space Available for Snake Head and Food
		self.space_x = screen_width - UNIT_BLOCK - 1															
		self.space_y = screen_height - UNIT_BLOCK - 1
		self.direction = -1
		self.score = 0
		if(self.space_x <= 0 or self.space_y <= 0):
			print("Inconsistent Initilization Values")			
		for i in range(SNAKE_LENGTH):
			self.snake_points[i][0] = (int(self.space_x/2) // UNIT_BLOCK + i) * UNIT_BLOCK
			self.snake_points[i][1] = (int(self.space_y/2) // UNIT_BLOCK) * UNIT_BLOCK

	# Random Food Location
	def generate_food(self):																					
		self.food_x = (random.randint(0, self.space_x) // UNIT_BLOCK) * UNIT_BLOCK
		self.food_y = (random.randint(0, self.space_y) // UNIT_BLOCK) * UNIT_BLOCK
		self.food = np.array([self.food_x, self.food_y])	

	# Draw Snake and Food
	def refresh_screen(self, image):																			
		for i in range(SNAKE_LENGTH):
			image = cv2.rectangle(image, (int(self.snake_points[i][0]),int(self.snake_points[i][1])), (int(self.snake_points[i][0]+UNIT_BLOCK),int(self.snake_points[i][1]+UNIT_BLOCK)), GREEN, -1) 
		image = cv2.rectangle(image, (self.food_x, self.food_y), (self.food_x + UNIT_BLOCK, self.food_y + UNIT_BLOCK), RED, -1) 

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
		if((key == ord('a') or key == ord('j') or key == ord('A') or key == ord('J')) 	):		#and self.direction != RIGHT):										
			self.direction = LEFT
		elif((key == ord('s') or key == ord('k') or key == ord('S') or key == ord('K')) ):		#and self.direction != UP):
			self.direction = DOWN
		elif((key == ord('d') or key == ord('l') or key == ord('D') or key == ord('L')) ):		#and self.direction != LEFT):
			self.direction = RIGHT
		elif((key == ord('w') or key == ord('i') or key == ord('W') or key == ord('I')) ):		#and self.direction != DOWN):
			self.direction = UP

		if(self.direction == -1):
			snake_x = snake_x - UNIT_BLOCK
		elif(self.direction == 2):
			snake_y = snake_y + UNIT_BLOCK
		elif(self.direction == 1):
			snake_x = snake_x + UNIT_BLOCK
		elif(self.direction == -2):
			snake_y = snake_y - UNIT_BLOCK
			
		#for i in range(SNAKE_LENGTH):
		#	if(self.snake_points[i, 0] == snake_x and self.snake_points[i, 1] == snake_y):
		#		is_hit = 1
		is_boundary_hit = (snake_x < 0 or snake_y < 0 or snake_x >= screen_width or snake_y >= screen_height)
		is_exit = (key == EXIT_KEY)

		# Reached Boundaries or Pressed Exit Key or Hit self
		if(is_boundary_hit or is_exit or is_hit):	
			self.end_game(image)

		# Reached Food
		elif(snake_x == self.food_x and snake_y == self.food_y):												
			self.generate_food()
			self.score = self.score + 1

		self.snake_points[1 : SNAKE_LENGTH, :] = self.snake_points[0 : SNAKE_LENGTH - 1, :]
		self.snake_points[0, 0] = snake_x
		self.snake_points[0, 1] = snake_y
		return self.score
