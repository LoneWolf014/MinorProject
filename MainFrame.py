import pygame
import sys

from Dependencies import *
from ColorPalette import *
from GUIPanel import *
from Tools import *

class RadioButtonGroup(Button):
    def __init__(self, buttonList):
        self.R_ButtonList = buttonList

    def printList(self):
        for button in self.R_ButtonList:
            print(button.printText)


buttonList = []

pygame.init()

btn_font = pygame.font.Font("Fonts/unispace bd.ttf", 18)

clock = pygame.time.Clock()
FPS = 60

M_Frame = pygame.display.set_mode((MainFrame_Width, MainFrame_Height), vsync=1)
pygame.display.set_caption("Meta Cam InterFace")

GUIFrame = GUIPanel(M_Frame, GUIFrame_Width, GUIFrame_Height, GUIFrame_X_Pos, GUIFrame_Y_Pos, GrizzliesBlue)

OptionsPane = CreateSurface(M_Frame, OptionsPane_Width, OptionsPane_Height, OptionsPane_X, OptionsPane_Y, CadetBlue)
OP_LabelPane = CreateSurface(M_Frame, OP_L_Width, OP_L_Height, OP_L_X, OP_L_Y, GrizzliesBlue)

TextInputPane = CreateSurface(M_Frame, Text_Input_Width, Text_Input_Height, Text_Input_X, Text_Input_Y, EaglesMidnightGreen)
TI_LabelPane = CreateSurface(M_Frame, TI_L_Width, TI_L_Height, TI_L_X, TI_L_Y, DolphinAqua)

OP_Label = CreateLabel("Choose Camera:", white, "unispace bd.ttf", OP_T_Size, True, OP_T_X, OP_T_Y)

TI_Label_1 = CreateLabel("WIFI IP: ", white, "OCRAEXT.TTF", 30, True, TI_L_X+10, TI_L_Y+10)
TI_Label_2 = CreateLabel("Port: ", white, "OCRAEXT.TTF", 30, True, TI_L_X+10, TI_L_Y+60)

button1 = Button(M_Frame, "Start Recording", 200, 50, (175, 475), 6, btn_font, "Start Button")
button2 = Button(M_Frame, "Stop Recording", 200, 50, (425, 475), 6, btn_font, "Stop Button")

radio1 = Button(M_Frame, "Webcam", 100, 30, (400, 60), 6, btn_font, "Webcam Button")
radio2 = Button(M_Frame, "DroidCam", 100, 30, (400, 110), 6, btn_font, "DroidCam Button")
buttonList.append(radio1)
buttonList.append(radio2)
buttonGroup = RadioButtonGroup(buttonList)

def drawPanels():
    GUIFrame.Create_GUI_Panel()

    OptionsPane.DrawSurface()
    OP_LabelPane.DrawSurface()

    TextInputPane.DrawSurface()
    TI_LabelPane.DrawSurface()


def drawLabels():
    OP_Label.DrawLabel(M_Frame)

    TI_Label_1.DrawLabel(M_Frame)
    TI_Label_2.DrawLabel(M_Frame)

def draw():
    drawPanels()
    drawLabels()

buttonGroup.printList()

Run = True
while(Run):
    for event in pygame.event.get():
        if ((event.type == pygame.QUIT) or 
            (event.type == pygame.KEYDOWN and 
             event.key == pygame.K_ESCAPE)):
            Run = False
            pygame.display.quit()
            sys.exit()

    M_Frame.fill((BroncosNavy))

    draw()

    radio1.draw()
    radio2.draw()

    button1.draw()
    button2.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.display.quit()