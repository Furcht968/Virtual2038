import time
from datetime import datetime
import os
import pygame
import sys
from pygame.locals import *

if len(sys.argv)==1:
	bit=32
else:
	bit=int(sys.argv[1])
if len(sys.argv)<=2:
	backcolor=(255,255,255)
	textcolor=(0,0,0)
	modetext=None
else:
	if(sys.argv[2]=="-dark" or sys.argv[2]=="-d"):
		backcolor=(20,20,20)
		textcolor=(255,255,255)
		modetext="Dark"


for i in range(bit):
	bitover=2**int(i)

bitover=bitover+bitover

pygame.init()
screen = pygame.display.set_mode((640, 360))

if(bit!=32):
	if(modetext!=None):
		pygame.display.set_caption("Virtual2038 on "+str(bit)+"bit, "+modetext+" mode")
	else:
		pygame.display.set_caption("Virtual2038 on "+str(bit)+"bit")

else:
	if(modetext!=None):
		pygame.display.set_caption("Virtual2038 on Default "+str(bit)+"bit. "+modetext+" mode")
	else:
		pygame.display.set_caption("Virtual2038 on Default"+str(bit)+"bit")

font = pygame.font.SysFont(None, 32)
font2 = pygame.font.SysFont(None, 70)
pygame.display.set_icon(pygame.image.load('icon.png'))
while(1):
	screen.fill(backcolor)
	time32u2=format(int(time.time()),"b")[-bit:]
	time32u10=int(time32u2,2)
	time32d10=datetime.fromtimestamp(time32u10)
	bin = font.render("Binary: "+time32u2, True, textcolor)
	dec = font.render("Decimal: "+str(time32u10), True, textcolor)
	txt = font2.render("RealTime:", True, textcolor)
	utc = font2.render(str(time32d10).replace("-","/"), True, textcolor)
	if(bitover-time32u10<=10):
		ovr = font.render("Until Overflow: "+str(bitover-time32u10), True, (255,0,0))
	else:
		ovr = font.render("Until Overflow: "+str(bitover-time32u10), True, textcolor)
	screen.blit(bin, (90,60))
	screen.blit(dec, (90,80))
	screen.blit(txt, (90,140))
	screen.blit(utc, (90,190))
	screen.blit(ovr, (90,270))

	pygame.display.update()
	for event in pygame.event.get(): # 終了処理
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
