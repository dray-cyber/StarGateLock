from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import Tk, Label, Button
import json
from pathlib import Path
import time
import tkinter as tk
import tkinter.ttk as ttk
import os
import pygame
import sys
import time
from time import sleep
import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
from moviepy.editor import *
import pygame
import imageio
from moviepy.editor import VideoFileClip
from moviepy.video.fx.resize import resize
pygame.init()
root = Tk()
lb = tk.Listbox(root)
lb.pack()

apple = 3
if apple != 1:
    symb1 = 0
    symb2 = 0
    symb3 = 0
    symb4 = 0
    symb5 = 0
    symb6 = 0
    symb7 = 0
    symb8 = 0
    timeout = False
    symb9 = 0
    symb10 = 0

    symb11 = 0
    symb12 = 0
    symb13 = 0
    symb14 = 0
    symb15 = 0
    symb16 = 0
    symb17 = 0
    symb18 = 0
    symb19 = 0
    symb20 = 0

    symb21 = 0
    symb22 = 0
    symb23 = 0
    symb24 = 0
    symb25 = 0
    symb26 = 0
    symb27 = 0
    symb28 = 0
    symb29 = 0
    backgroundupdated = False
    symb30 = 0
    arraystatus = 0
    symb31 = 0
    symb32 = 0
    symb33 = 0
    symb34 = 0
    symb35 = 0
    symb36 = 0
    symb37 = 0
    symb38 = 0
    seq1 = 0
    seq2 = 0
    seq3 = 0
    seq4 = 0
    seq5 = 0
    seq6 = 0
    seq7 = 0
    seq8 = 0
    seq9 = 0
    apple = 1
    ourvar = 0
photo1 = PhotoImage(file=r"g1.png")
photo2 = PhotoImage(file=r"g2.png")
photo3 = PhotoImage(file=r"g3.png")
photo4 = PhotoImage(file=r"g4.png")
photo5 = PhotoImage(file=r"g5.png")
photo6 = PhotoImage(file=r"g6.png")
photo7 = PhotoImage(file=r"g7.png")
photo8 = PhotoImage(file=r"g8.png")
photo9 = PhotoImage(file=r"g9.png")
photo10 = PhotoImage(file=r"g10.png")

photo11 = PhotoImage(file=r"g11.png")
photo12 = PhotoImage(file=r"g12.png")
photo13 = PhotoImage(file=r"g13.png")
photo14 = PhotoImage(file=r"g14.png")
photo15 = PhotoImage(file=r"g15.png")
photo16 = PhotoImage(file=r"g16.png")
photo17 = PhotoImage(file=r"g17.png")
photo18 = PhotoImage(file=r"g18.png")
photo19 = PhotoImage(file=r"g19.png")
photo20 = PhotoImage(file=r"g20.png")

photo21 = PhotoImage(file=r"g21.png")
photo22 = PhotoImage(file=r"g22.png")
photo23 = PhotoImage(file=r"g23.png")
photo24 = PhotoImage(file=r"g24.png")
photo25 = PhotoImage(file=r"g25.png")
photo26 = PhotoImage(file=r"g26.png")
photo27 = PhotoImage(file=r"g27.png")
photo28 = PhotoImage(file=r"g28.png")
photo29 = PhotoImage(file=r"g29.png")
photo30 = PhotoImage(file=r"g30.png")

photo31 = PhotoImage(file=r"g31.png")
photo32 = PhotoImage(file=r"g32.png")
photo33 = PhotoImage(file=r"g33.png")
photo34 = PhotoImage(file=r"g34.png")
photo35 = PhotoImage(file=r"g35.png")
photo36 = PhotoImage(file=r"g36.png")
photo37 = PhotoImage(file=r"g37.png")
photo38 = PhotoImage(file=r"g38.png")
photodome = PhotoImage(file=r"dhd.png")
chev0 = PhotoImage(file=r"chev0.png")
chev1 = PhotoImage(file=r"chev1.png")
chev2 = PhotoImage(file=r"chev2.png")
chev3 = PhotoImage(file=r"chev3.png")
chev4 = PhotoImage(file=r"chev4.png")
chev5 = PhotoImage(file=r"chev5.png")
chev6 = PhotoImage(file=r"chev6.png")
chev7 = PhotoImage(file=r"chev7.png")
chev8 = PhotoImage(file=r"chev8.png")
chev9 = PhotoImage(file=r"chev9.png")
blank = PhotoImage(file=r"blank.png")
enter1 = PhotoImage(file=r"enter.png")

enter = enter1.zoom(3, 3)
blankpic = blank.subsample(3, 3)
photoimage1 = photo1.subsample(3, 3)
photoimage2 = photo2.subsample(3, 3)
photoimage3 = photo3.subsample(3, 3)
photoimage4 = photo4.subsample(3, 3)
photoimage5 = photo5.subsample(3, 3)
photoimage6 = photo6.subsample(3, 3)
photoimage7 = photo7.subsample(3, 3)
photoimage8 = photo8.subsample(3, 3)
photoimage9 = photo9.subsample(3, 3)
photoimage10 = photo10.subsample(3, 3)

photoimage11 = photo11.subsample(3, 3)
photoimage12 = photo12.subsample(3, 3)
photoimage13 = photo13.subsample(3, 3)
photoimage14 = photo14.subsample(3, 3)
photoimage15 = photo15.subsample(3, 3)
photoimage16 = photo16.subsample(3, 3)
photoimage17 = photo17.subsample(3, 3)
photoimage18 = photo18.subsample(3, 3)
photoimage19 = photo19.subsample(3, 3)
photoimage20 = photo20.subsample(3, 3)

photoimage21 = photo21.subsample(3, 3)
photoimage22 = photo22.subsample(3, 3)
photoimage23 = photo23.subsample(3, 3)
photoimage24 = photo24.subsample(3, 3)
photoimage25 = photo25.subsample(3, 3)
photoimage26 = photo26.subsample(3, 3)
photoimage27 = photo27.subsample(3, 3)
photoimage28 = photo28.subsample(3, 3)
photoimage29 = photo29.subsample(3, 3)
photoimage30 = photo30.subsample(3, 3)

photoimage31 = photo31.subsample(3, 3)
photoimage32 = photo32.subsample(3, 3)
photoimage33 = photo33.subsample(3, 3)
photoimage34 = photo34.subsample(3, 3)
photoimage35 = photo35.subsample(3, 3)
photoimage36 = photo36.subsample(3, 3)
photoimage37 = photo37.subsample(3, 3)
photoimage38 = photo38.subsample(3, 3)

chevron0 = chev0
chevron1 = chev1
chevron2 = chev2
chevron3 = chev3
chevron4 = chev4
chevron5 = chev5
chevron6 = chev6
chevron7 = chev7
chevron8 = chev8
chevron9 = chev9
pygame.mixer.init()
photoimagedome = photodome.subsample(3, 3)
global vardata
vardata = 0
arraystatuse = arraystatus
global sequence
sequence = []
global liste
def arraycheck():
    global liste
    global seq1
    global root
    global seq2
    global seq3
    global seq4
    global seq5
    global seq6
    global seq7
    global seq8
    global seq9
    global vardata
    global ourvar
    global theimage
    global thefileweneed
    global photot
    global photoimaget
    global custom
    global custom1
    global custom2
    global custom3
    global custom4
    global custom5
    global custom6
    global custom7
    global custom8
    global gate
    global img
    global chevron1
    global backgroundupdated
    global confirmed
    global myltwo
    global mylthree
    global mylfour
    global mylfive
    global mylsix
    global mylseven
    global myleight
    global mynine
    liste = len(sequence)
    ourvar = 0
    if liste == 1:
        seq1 = sequence[0]
        img = chevron1
        ourvarright = False
        while ourvarright == False:
            if vardata != ourvar:
                ourvar = ourvar + 1

            else:
                ourvarright = True
                thedata = str(ourvar)
                theimage = 'gg' + thedata + '.png'
                thefileweneed = str(theimage)
                photot = PhotoImage(file=thefileweneed)
                photot = photot.subsample(2,2)
                photoimaget = photot.subsample(1, 1)
                custom = photoimaget
                global mylone
                mylone = Button(root, image=custom, command=ref1)
                mylone.pack()
                mylone.place(x=950, y=98)
                pygame.mixer.music.load("stargatelock.mp3")
                pygame.mixer.music.play()
                sleep(1)
                img = chevron1
                panel.configure(image=img)
                panel.image = img

    if liste == 2:
        seq2 = sequence[1]
        ourvarright = False
        ourvar = 0
        while ourvarright == False:
            if vardata != ourvar:
                ourvar = ourvar + 1

            else:
                ourvarright = True
                thedata = str(ourvar)
                theimaget = 'gg' + thedata + '.png'
                thefileweneedt = str(theimaget)
                photot = PhotoImage(file=thefileweneedt)
                photot = photot.subsample(2, 2)
                photoimaget = photot.subsample(1, 1)
                custom1 = photoimaget
                img = chevron2
                pygame.mixer.music.load("stargatelock.mp3")
                pygame.mixer.music.play()
                sleep(1)
                global myltwo
                panel.configure(image=img)
                panel.image = img
                myltwo = Button(root, image=custom1, command=ref2)
                myltwo.pack()
                myltwo.place(x=950, y=192)
    if liste == 3:
        seq3 = sequence[2]
        ourvarright = False
        ourvar = 0
        while ourvarright == False:
            if vardata != ourvar:
                ourvar = ourvar + 1

            else:
                ourvarright = True
                thedata = str(ourvar)
                theimaget = 'gg' + thedata + '.png'
                thefileweneedt = str(theimaget)
                photot = PhotoImage(file=thefileweneedt)
                photot = photot.subsample(2, 2)
                photoimaget = photot.subsample(1, 1)
                custom2 = photoimaget
                global mylthree
                img = chevron3
                pygame.mixer.music.load("stargatelock.mp3")
                pygame.mixer.music.play()
                sleep(1)
                panel.configure(image=img)
                panel.image = img
                mylthree = Button(root, image=custom2, command=ref3)
                mylthree.pack()
                mylthree.place(x=950, y=266)

    if liste == 4:
        seq4 = sequence[3]
        ourvarright = False
        ourvar = 0
        while ourvarright == False:
            if vardata != ourvar:
                ourvar = ourvar + 1

            else:
                ourvarright = True
                thedata = str(ourvar)
                theimaget = 'gg' + thedata + '.png'
                thefileweneedt = str(theimaget)
                photot = PhotoImage(file=thefileweneedt)
                photot = photot.subsample(2, 2)
                photoimaget = photot.subsample(1, 1)
                custom3 = photoimaget
                global mylfour
                img = chevron4
                pygame.mixer.music.load("stargatelock.mp3")
                pygame.mixer.music.play()
                sleep(1)
                panel.configure(image=img)
                panel.image = img
                mylfour = Button(root, image=custom3, command=ref4)
                mylfour.pack()
                mylfour.place(x=950, y=350)
    if liste == 5:
        seq5 = sequence[4]
        ourvarright = False
        ourvar = 0
        while ourvarright == False:
            if vardata != ourvar:
                ourvar = ourvar + 1

            else:
                ourvarright = True
                thedata = str(ourvar)
                theimaget = 'gg' + thedata + '.png'
                thefileweneedt = str(theimaget)
                photot = PhotoImage(file=thefileweneedt)
                photot = photot.subsample(2, 2)
                photoimaget = photot.subsample(1, 1)
                custom4 = photoimaget
                global mylfive
                img = chevron5
                pygame.mixer.music.load("stargatelock.mp3")
                pygame.mixer.music.play()
                sleep(1)
                panel.configure(image=img)
                panel.image = img
                mylfive = Button(root, image=custom4, command=ref5)
                mylfive.pack()
                mylfive.place(x=950, y=434)
    if liste == 6:
        seq6 = sequence[5]
        ourvarright = False
        ourvar = 0
        while ourvarright == False:
            if vardata != ourvar:
                ourvar = ourvar + 1

            else:
                ourvarright = True
                thedata = str(ourvar)
                theimaget = 'gg' + thedata + '.png'
                thefileweneedt = str(theimaget)
                photot = PhotoImage(file=thefileweneedt)
                photot = photot.subsample(2, 2)
                photoimaget = photot.subsample(1, 1)
                custom5 = photoimaget
                global mylsix
                img = chevron6
                pygame.mixer.music.load("stargatelock.mp3")
                pygame.mixer.music.play()
                sleep(1)
                panel.configure(image=img)
                panel.image = img
                mylsix = Button(root, image=custom5, command=ref6)
                mylsix.pack()
                mylsix.place(x=950, y=520)
    if liste == 7:
        seq7 = sequence[6]
        ourvarright = False
        ourvar = 0
        while ourvarright == False:
            if vardata != ourvar:
                ourvar = ourvar + 1

            else:
                ourvarright = True
                thedata = str(ourvar)
                theimaget = 'gg' + thedata + '.png'
                thefileweneedt = str(theimaget)
                photot = PhotoImage(file=thefileweneedt)
                photot = photot.subsample(2, 2)
                photoimaget = photot.subsample(1, 1)
                custom6 = photoimaget
                global mylseven
                img = chevron7
                pygame.mixer.music.load("stargatelock.mp3")
                pygame.mixer.music.play()
                sleep(1)
                panel.configure(image=img)
                panel.image = img
                mylseven = Button(root, image=custom6, command=ref7)
                mylseven.pack()
                mylseven.place(x=950, y=604)
    if liste == 8:
        seq8 = sequence[7]
        ourvarright = False
        ourvar = 0
        while ourvarright == False:
            if vardata != ourvar:
                ourvar = ourvar + 1

            else:
                ourvarright = True
                thedata = str(ourvar)
                theimaget = 'gg' + thedata + '.png'
                thefileweneedt = str(theimaget)
                photot = PhotoImage(file=thefileweneedt)
                photot = photot.subsample(2, 2)
                photoimaget = photot.subsample(1, 1)
                custom7 = photoimaget
                ourvarright = True
                global myleight
                img = chevron8
                pygame.mixer.music.load("stargatelock.mp3")
                pygame.mixer.music.play()
                sleep(1)
                panel.configure(image=img)
                panel.image = img
                myleight = Button(root, image=custom7, command=ref8)
                myleight.pack()
                myleight.place(x=1117, y=98)

    if liste == 9:
        seq9 = sequence[8]
        ourvarright = False
        ourvar = 0
        while ourvarright == False:
            if vardata != ourvar:
                ourvar = ourvar + 1

            else:
                ourvarright = True
                global mylnine
                thedata = str(ourvar)
                theimaget = 'gg' + thedata + '.png'
                thefileweneedt = str(theimaget)
                photot = PhotoImage(file=thefileweneedt)
                photot = photot.subsample(2, 2)
                photoimaget = photot.subsample(1, 1)
                custom8 = photoimaget
                img = chevron9
                pygame.mixer.music.load("stargatelock.mp3")
                pygame.mixer.music.play()
                sleep(1)
                panel.configure(image=img)
                panel.image = img
                mylnine = Button(root, image=custom8, command=ref9)
                mylnine.pack()
                mylnine.place(x=1117, y=182)
def ref1():
    global mylone
    mylone.destroy()

def ref2():
    global myltwp
    myltwo.destroy()

def ref3():
    global mylthree
    mylthree.destroy()
def ref4():
    global mylfour
    mylfour.destroy()
def ref5():
    global mylfive
    mylfive.destroy()
def ref6():
    global mylsix
    mylsix.destroy()
def ref7():
    global mylseven
    mylseven.destroy()
def ref8():
    global myleight
    myleight.destroy()
def ref9():
    global mylnine
    mylnine.destroy()
def sym1():
    global symb1
    global vardata
    symb1 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym1")
        vardata = 1
        arraycheck()
def sym2():
    global symb2
    global vardata
    symb2 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym2")
        vardata = 2
        arraycheck()

def sym3():
    global symb3
    global vardata
    symb3 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym3")
        vardata = 3
        arraycheck()
def sym4():
    global symb4
    global vardata
    symb4 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym4")
        vardata = 4
        arraycheck()
def sym5():
    global symb5
    global vardata
    symb5 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym5")
        vardata = 5
        arraycheck()
def sym6():
    global symb6
    global vardata
    symb6 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym6")
        vardata = 6
        arraycheck()
def sym7():
    global symb7
    global vardata
    symb7 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym7")
        vardata = 7
        arraycheck()
def sym8():
    global symb8
    global vardata
    symb8 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym8")
        vardata = 8
        arraycheck()
def sym9():
    global symb9
    global vardata
    symb9 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym9")
        vardata = 9
        arraycheck()
def sym10():
    global symb10
    global vardata
    symb10 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym10")
        vardata = 10
        arraycheck()
def sym11():
    global symb11
    global vardata
    symb11 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym11")
        vardata = 11
        arraycheck()
def sym12():
    global symb12
    global vardata
    symb12 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym12")
        vardata = 12
        arraycheck()
def sym13():
    global symb13
    global vardata
    symb13 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym13")
        vardata = 13
        arraycheck()
def sym14():
    global symb14
    global vardata
    symb14 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym14")
        vardata = 14
        arraycheck()
def sym15():
    global symb15
    global vardata
    symb15 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym15")
        vardata = 15
        arraycheck()
def sym16():
    global symb16
    global vardata
    symb16 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym16")
        vardata = 16
        arraycheck()
def sym17():
    global symb17
    global vardata
    symb17 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym17")
        vardata = 17
        arraycheck()
def sym18():
    global symb18
    global vardata
    symb18 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym18")
        vardata = 18
        arraycheck()
def sym19():
    global symb19
    global vardata
    symb19 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym19")
        vardata = 19
        arraycheck()

def sym20():
    global symb20
    global vardata
    symb20 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym20")
        vardata = 20
        arraycheck()
def sym21():
    global symb21
    global vardata
    symb21 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym21")
        vardata = 21
        arraycheck()
def sym22():
    global symb22
    global vardata
    symb22 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym22")
        vardata = 22
        arraycheck()
def sym23():
    global symb23
    global vardata
    symb23 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym23")
        vardata = 23
        arraycheck()
def sym24():
    global symb24
    global vardata
    symb24 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym24")
        vardata = 24
        arraycheck()
def sym25():
    global symb25
    global vardata
    symb25 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym25")
        vardata = 25
        arraycheck()
def sym26():
    global symb26
    global vardata
    symb26 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym26")
        vardata = 26
        arraycheck()
def sym27():
    global symb27
    global vardata
    symb27 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym27")
        vardata = 27
        arraycheck()
def sym28():
    global symb28
    global vardata
    symb28 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym28")
        vardata = 28
        arraycheck()
def sym29():
    global symb29
    global vardata
    symb29 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym29")
        vardata = 29
        arraycheck()


def sym30():
    global symb30
    global vardata
    symb30 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym30")
        vardata = 30
        arraycheck()
def sym31():
    global symb31
    global vardata
    symb31 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym31")
        vardata = 31
        arraycheck()
def sym32():
    global symb32
    global vardata
    symb32 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym32")
        vardata = 32
        arraycheck()
def sym33():
    global symb33
    global vardata
    symb33 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym33")
        vardata = 33
        arraycheck()
def sym34():
    global symb34
    global vardata
    symb34 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym34")
        vardata = 34
        arraycheck()
def sym35():
    global symb35
    global vardata
    symb35 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym35")
        vardata = 35
        arraycheck()
def sym36():
    global symb36
    global vardata
    symb36 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym36")
        vardata = 36
        arraycheck()
def sym37():
    global symb37
    global vardata
    symb37 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym37")
        vardata = 37
        arraycheck()
def sym38():
    global symb38
    global vardata
    symb38 = 1
    global arraystatus
    arraystatus = arraystatus + 1
    global sequence
    if arraystatus <10:
        sequence.append("sym38")
        vardata = 38
        arraycheck()
datacompare = "data"
def playmyaudio():
    pygame.mixer.init()
    pygame.mixer.music.load("gatestart.mp3")
    pygame.mixer.music.play()
    sleep(2)
    activate()
kill = 1
img = chevron0
w, h = img.width(), img.height()
panel = img
panel = Label(root, image=img)
panel.place(x=0, y=25, relwidth=1, relheight=1)
btn1 = Button(root, image=photoimage1, command=sym1)
btn1.place(x=20,y=10)
def symdome():
    global sequence
    global root
    global frames
    global datacompare
    global img
    global enter
    global panel
    global kill
    stargatecode = Path("data.json")
    sequencestr = str(sequence)
    datat = sequencestr.replace(", ", "")
    datatt = datat.replace("\'", " ")
    datattt = datatt.replace("[", "")
    datatttt = datattt.replace("   ", "")
    datattttt = datatttt.replace("]", "")
    datatttttt = datattttt.replace(" \"", "")
    finaldata = datatttttt.replace("\" ", "")
    datacompare = finaldata.replace("  ", " ")
    pygame.mixer.init()
    if stargatecode.is_file():
        f = open('data.json', )
        data = json.load(f)
        comparestring = str(data)
        if datacompare == comparestring:
            f.close
            sleep(1)
            root.attributes('-topmost', False)
            playmyaudio()
    else:
        with open('data.json', 'w') as f:
            json.dump(datacompare, f)
            f.close
def proced():
    global img
    img = enter
    panel.configure(image=img)
    panel.image = img
def activate():
    pygame.display.set_caption('Desktop and beyond!')
    clip = VideoFileClip('wormhole.mp4')
    clip.preview(fps=60, fullscreen=True)
    root.destroy()
def reset():
    global sequence
    global arraystatus
    sequence.clear()
    arraystatus = 0
    img = chevron0
    panel.configure(image=img)
    panel.image = img
    ref1()
    ref2()
    ref3()
    ref4()
    ref5()
    ref6()
    ref7()
    ref8()
    ref9()




Button(root, image=photoimage2, # 2
       command=sym2).place(x=60,y=10)

Button(root, image=photoimage3, # 3
       command=sym3).place(x=100,y=10)

Button(root, image=photoimage4, # 4
       command=sym4).place(x=140,y=10)

Button(root, image=photoimage5, # 5
       command=sym5).place(x=180,y=10)

Button(root, image=photoimage6, # 6
       command=sym6).place(x=220,y=10)

Button(root, image=photoimage7, # 7
       command=sym7).place(x=260,y=10)

Button(root, image=photoimage8, # 8
       command=sym8).place(x=300,y=10)

Button(root, image=photoimage9, # 9
       command=sym9).place(x=340,y=10)

Button(root, image=photoimage10, #10
       command=sym10).place(x=380,y=10)

Button(root, image=photoimage11, #11
       command=sym11).place(x=420,y=10)

Button(root, image=photoimage12, #12
       command=sym12).place(x=460,y=10)

Button(root, image=photoimage13,#13
       command=sym13).place(x=500,y=10)

Button(root, image=photoimage14,#14
       command=sym14).place(x=540,y=10)

Button(root, image=photoimage15,#15
       command=sym15).place(x=580,y=10)

Button(root, image=photoimage16,#16
       command=sym16).place(x=620,y=10)

Button(root, image=photoimage17,#17
       command=sym17).place(x=660,y=10)

Button(root, image=photoimage18,#18
       command=sym18).place(x=700,y=10)

Button(root, image=photoimage19,#19
       command=sym19).place(x=740,y=10)

Button(root, image=photoimage20,#20
       command=sym20).place(x=780,y=10)

Button(root, image=photoimage21,#21
       command=sym21).place(x=820,y=10)

Button(root, image=photoimage22,#22
       command=sym22).place(x=860,y=10)

Button(root, image=photoimage23,#23
       command=sym23).place(x=900,y=10)

Button(root, image=photoimage24,#24
       command=sym24).place(x=940,y=10)

Button(root, image=photoimage25,#25
       command=sym25).place(x=980,y=10)

Button(root, image=photoimage26,#26
       command=sym26).place(x=1020,y=10)

Button(root, image=photoimage27,#27
       command=sym27).place(x=1060,y=10)

Button(root, image=photoimage28,#28
       command=sym28).place(x=1100,y=10)

Button(root, image=photoimage29,#29
       command=sym29).place(x=1140,y=10)

Button(root, image=photoimage30,#30
       command=sym30).place(x=1180,y=10)

Button(root, image=photoimage31,#31
       command=sym31).place(x=1220,y=10)

Button(root, image=photoimage32,#32
       command=sym32).place(x=20,y=50)

Button(root, image=photoimage33,#33
       command=sym33).place(x=60,y=50)

Button(root, image=photoimage34,#34
       command=sym34).place(x=100,y=50)

Button(root, image=photoimage35,#35
       command=sym35).place(x=140,y=50)

Button(root, image=photoimage36,#36
       command=sym36).place(x=180,y=50)

Button(root, image=photoimage37,#37
       command=sym37).place(x=220,y=50)

Button(root, image=photoimage38,#38
       command=sym38).place(x=260,y=50)
Button(root, text="reset",#reset
       command=reset).place(x=1125,y=290)
def resetw():
    root.destroy()
Button(root, text="reset window",#reset
       command=resetw).place(x=350,y=50)
bstart = ttk.Button(root, image=photoimagedome,#dome
       command=symdome)
bstart.pack()
bstart.place(x=1100,y=550)
def on_closing():
    root.lift()
    pass


root.attributes('-fullscreen', True)
root.resizable(False, False)
root.attributes('-topmost', True)
root.protocol("WM_DELETE_WINDOW", on_closing)

mainloop()
