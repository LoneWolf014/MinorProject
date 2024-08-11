import pygame
import sys

from Dependencies import *
from ColorPalette import *
from GUIPanel import *
from Tools import *

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

IPTxt = ''
PortTxt = ''

DroidCam = False
IP = False
Port = False
TI_1 = btn_font.render(IPTxt, True, white)
TI_2 = btn_font.render(PortTxt, True, white)

TextBox_Pressed = False
TextBox2_Pressed = False
# Button Functions -------------------------------------------------------------------------------#
def CameraID(DC):
    global DroidCam
    global IP
    global Port
    global TI_1
    global TI_2
    global IPTxt
    global PortTxt

    global TextBox_Pressed
    global TextBox2_Pressed

    DroidCam = DC
    if(DroidCam == True):
        # print("System able to take input of IP and Port")
        mouse_pos = pygame.mouse.get_pos()

        # IP Box --------------------------------------------------------#
        TextBox = pygame.Rect(TI_L_X+275, TI_L_Y+10, 200, 30)
        if(TextBox.collidepoint(mouse_pos)):
            if(pygame.mouse.get_pressed()[0]):
                TextBox_Pressed = True
                TextBox2_Pressed = False
                IP = True
                Port = False

        if(TextBox_Pressed == True):
            if (IP == True):
                TI_1 = btn_font.render(IPTxt, True, white)
        # ----------------------------------------------------------------#
        # Port Box -------------------------------------------------------#
        TextBox2 = pygame.Rect(TI_L_X+275, TI_L_Y+60, 200, 30)
        if(TextBox2.collidepoint(mouse_pos)):
            if(pygame.mouse.get_pressed()[0]):
                TextBox_Pressed = False
                TextBox2_Pressed = True
                Port = True
                IP = False
        
        if(TextBox2_Pressed == True):
            if (Port == True):
                TI_2 = btn_font.render(PortTxt, True, white)

        # ------------ ----------------------------------------------------#
        pygame.draw.rect(M_Frame, Lust, TextBox, 4)
        pygame.draw.rect(M_Frame, Lust, TextBox2, 4)
    else:
        # print("System is using WebCam")
        None

def W_Cam():
    global DroidCam
    global IPTxt
    global PortTxt
    global TI_1
    global TI_2

    DroidCam = False
    IPTxt = ''
    PortTxt = ''

    TI_1 = btn_font.render(IPTxt, True, white)
    TI_2 = btn_font.render(PortTxt, True, white)
    
def D_Cam():
    global DroidCam
    DroidCam = True

def Start():
    print("Recording Started")

def Stop():
    print("Recording Stopped")

def Submit():
    if (DroidCam == True):
        if (IPTxt != '' and PortTxt != ''):
            print("IP : ", IPTxt)
            print("Port : ", PortTxt)
        else:
            print("Fill the IPTxt and PortTxt")
    else:
        print("It is using Webcam", 0)
# ------------------------------------------------------------------------------------------------- #
radio1 = Button(M_Frame, "Webcam", 100, 30, (400, 60), 6, btn_font, onclick = W_Cam)
radio2 = Button(M_Frame, "DroidCam", 100, 30, (400, 110), 6, btn_font, onclick = D_Cam)

button1 = Button(M_Frame, "Start Recording", 200, 50, (175, 475), 6, btn_font, onclick = Start)
button2 = Button(M_Frame, "Stop Recording", 200, 50, (425, 475), 6, btn_font, onclick = Stop)

submit = Button(M_Frame, "Submit", 100, 30, (425, 312), 6, btn_font, onclick= Submit)

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

def drawButtons():
    radio1.draw()
    radio2.draw()

    button1.draw()
    button2.draw()

    submit.draw()

def draw():
    drawPanels()
    drawLabels()
    drawButtons()
    CameraID(DroidCam)
    if DroidCam == True:
        M_Frame.blit(TI_1, (TI_L_X+280, TI_L_Y+10))
        M_Frame.blit(TI_2, (TI_L_X+280, TI_L_Y+60))

Run = True
while(Run):
    for event in pygame.event.get():
        if ((event.type == pygame.QUIT) or 
            (event.type == pygame.KEYDOWN and 
             event.key == pygame.K_ESCAPE)):
            Run = False
            pygame.display.quit()
            sys.exit()

        if (DroidCam == True) :
            if event.type == pygame.KEYDOWN:
                if IP == True:
                    if event.key == pygame.K_BACKSPACE:
                        IPTxt = IPTxt[0:-1]
                    else:
                        IPTxt += event.unicode
                if Port == True:
                    if event.key == pygame.K_BACKSPACE:
                        PortTxt = PortTxt[0:-1]
                    else:
                        PortTxt += event.unicode

    M_Frame.fill((BroncosNavy))

    draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.display.quit()