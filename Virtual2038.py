# *****************************************
#
# Virtual2038 - Virtual 2038 Problem Python Software
#
#
# Copyright (c) 2020 Furcht968
# Released under the MIT license
# https://github.com/Furcht968/Virtual2038/blob/master/License/LICENSE.txt
# https://github.com/Furcht968/Virtual2038/blob/master/License/LICENSE_jp.txt
#
#
# *****************************************


import time
import json
from datetime import datetime
import sys

if __name__ == "Virtual2038":
    class now():
        def __init__(self, bit=32):
            bitover = (2**int(bit-1))*2
            time32u2 = format(int(time.time()), "b")[-bit:]
            time32u10 = int(time32u2, 2)
            time32d10 = datetime.fromtimestamp(time32u10)
            self.RealTime = time32d10
            self.binary = time32u2
            self.decimal = time32u10
            self.until = bitover-time32u10

if __name__ == "__main__":
    if len(sys.argv) == 1:
        bit = 31
    else:
        bit = int(sys.argv[1])-1

    with open("config.json") as f:
        config = json.loads(f.read())
    backcolor = []
    textcolor = []
    backimage = config["background_image"]
    for i in range(0, 6, 2):
        backcolor += [int(config["backcolor"][i:i+2], 16)]
        textcolor += [int(config["textcolor"][i:i+2], 16)]

    bitover = (2**int(bit))*2

    import pygame
    from pygame.locals import *
    pygame.init()
    screen = pygame.display.set_mode((640, 360))
    if(bit != 31):
        pygame.display.set_caption(f"Virtual2038 on {bit+1}bit")
    else:
        pygame.display.set_caption(f"Virtual2038")

    font = pygame.font.SysFont(None, 32)
    font2 = pygame.font.SysFont(None, 70)
    pygame.display.set_icon(pygame.image.load('icons/icon.png'))
    while(1):
        screen.fill(backcolor)
        if(backimage != None):
            img = pygame.image.load(backimage)
            img = pygame.transform.scale(img, (640, 360))
            screen.blit(img, (0, 0))
        time32u2 = format(int(time.time()), "b")[-bit:]
        time32u10 = int(time32u2, 2)
        time32d10 = datetime.fromtimestamp(time32u10)
        bin = font.render(f"Binary: {time32u2}", True, textcolor)
        dec = font.render(f"Decimal: {time32u10}", True, textcolor)
        txt = font2.render("RealTime:", True, textcolor)
        utc = font2.render(str(time32d10).replace("-", "/"), True, textcolor)
        ovrt = f"Until Overflow: {bitover-time32u10}"
        if(bitover-time32u10 <= 10):
            ovr = font.render(ovrt, True, (255, 0, 0))
        else:
            ovr = font.render(ovrt, True, textcolor)
        screen.blit(bin, (90, 60))
        screen.blit(dec, (90, 80))
        screen.blit(txt, (90, 140))
        screen.blit(utc, (90, 190))
        screen.blit(ovr, (90, 270))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
