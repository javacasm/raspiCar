#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Test of cámara functionality
    Licencia CC by @javacasm    
    Julio de 2020
 """


import os
from os import path
from time import sleep

import config
import camara

camera = camara.initCamera() # creamos el objeto camara


def testISO():
    for iso in range(100,900,100):
        message = 'ISO:' + str(iso)
        print(message)
        camara.addText(message)
        camara.setIso(iso)
        camara.getImage()

def testImage():
    for i in range(1, 3):
        camara.addDate()
        camara.getImage()
        sleep(1)

def testImageNight():
    for i in range(1, 3):
        camara.addDateNight()
        camara.getImageNight()
        sleep(1)


if not os.path.exists(config.ImagesDirectory):
     os.mkdir(config.ImagesDirectory)


print('Testing image')
testImage()

print('Testing ISO')
testISO()

print('Testing night image')
testImageNight()

