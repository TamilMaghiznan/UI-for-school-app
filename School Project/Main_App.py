import pygame
from pygame.locals import *

pygame.init()

#All about the screen
info=pygame.display.Info()
winsize=(info.current_w,info.current_h)
screen=pygame.display.set_mode(winsize)
pygame.display.set_caption("School app...")

#Font for displaying text
font=pygame.font.Font('Assets/font.ttf',17)
font1=pygame.font.Font('Assets/font.ttf',35)

#Animations
def option_state_animation_push():
    global left_rect_state
    left_rect_state+=5
    return left_rect_state
def option_state_animation_pull():
    global left_rect_state
    left_rect_state-=5
    return left_rect_state

#Colours
search_bar_colour=(90,90,90)
search_bar_border_colour=(150,150,150)
search_bar_text_colour=(180,180,180)
close_text_colour=(150,150,150)
_text_colour=(150,150,150)
_text2_colour=(150,150,150)

#Buttons
button_rect1=pygame.Rect(winsize[0]-370,4,300,22)
pygame.draw.rect(screen,(255,255,255),button_rect1,0,7)
button_rect2=pygame.Rect(winsize[0]-30,0,30,30)
pygame.draw.rect(screen,(70,70,70),button_rect2,0)
button_rect3=pygame.Rect(winsize[0]-60,0,30,30)
pygame.draw.rect(screen,(70,70,70),button_rect3,0)
button_rect4=pygame.Rect(0,0,30,30)
pygame.draw.rect(screen,(70,70,70),button_rect4,0)

#Search icon
search_icon=pygame.image.load('Assets/search_off.png')
search_icon_size=search_icon.get_size()
search_icon_newsize=(search_icon_size[0]//30,search_icon_size[1]//30)
search_icon_main=pygame.transform.smoothscale(search_icon,search_icon_newsize)
search_icon1=pygame.image.load('Assets/search_on.png')
search_icon_main1=pygame.transform.smoothscale(search_icon1,search_icon_newsize)

#button for option/icon
button_recta=pygame.Rect(0,32,50,50)
button_rectb=pygame.Rect(0,82,50,50)
button_rectc=pygame.Rect(0,132,50,50)
button_rectd=pygame.Rect(0,182,50,50)
button_recte=pygame.Rect(0,237,50,50)

school=pygame.image.load('Assets/school_off.png')
school_size=school.get_size()
school_newsize=(school_size[0]//15,school_size[1]//15)
school_main=pygame.transform.smoothscale(school,school_newsize)
school1=pygame.image.load('Assets/school_on.png')
school_main1=pygame.transform.smoothscale(school1,school_newsize)
school_xy=school_main.get_rect(center=button_recta.center)

ai=pygame.image.load('Assets/ai_off.png')
ai_size=ai.get_size()
ai_newsize=(ai_size[0]//15,ai_size[1]//15)
ai_main=pygame.transform.smoothscale(ai,ai_newsize)
ai1=pygame.image.load('Assets/ai_on.png')
ai_main1=pygame.transform.smoothscale(ai1,ai_newsize)
ai_xy=ai_main.get_rect(center=button_rectb.center)

pen=pygame.image.load('Assets/pen_off.png')
pen_size=pen.get_size()
pen_newsize=(pen_size[0]//15,pen_size[1]//15)
pen_main=pygame.transform.smoothscale(pen,pen_newsize)
pen1=pygame.image.load('Assets/pen_on.png')
pen_main1=pygame.transform.smoothscale(pen1,pen_newsize)
pen_xy=pen_main.get_rect(center=button_rectc.center)

game=pygame.image.load('Assets/game_off.png')
game_size=game.get_size()
game_newsize=(game_size[0]//15,game_size[1]//15)
game_main=pygame.transform.smoothscale(game,game_newsize)
game1=pygame.image.load('Assets/game_on.png')
game_main1=pygame.transform.smoothscale(game1,game_newsize)
game_xy=game_main.get_rect(center=button_rectd.center)

news=pygame.image.load('Assets/news_off.png')
news_size=news.get_size()
news_newsize=(news_size[0]//15,news_size[1]//15)
news_main=pygame.transform.smoothscale(news,news_newsize)
news1=pygame.image.load('Assets/news_on.png')
news_main1=pygame.transform.smoothscale(news1,news_newsize)
news_xy=news_main.get_rect(center=button_recte.center)

#Colours for button
coloura=(70,70,70)
colourb=(70,70,70)
colourc=(70,70,70)
colourd=(70,70,70)
coloure=(70,70,70)

#Variables
search_icon_state=0
option_state=1
left_rect_state=55
left2_rect_state=180
school_state=0
ai_state=0
pen_state=0
game_state=0
news_state=0
ss=ais=ps=gs=ns=0
sss=1
aiss=pss=gss=nss=0
squarey=32
text="School"

run=True
while run:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_ESCAPE:
              run=False
 
        if event.type==pygame.MOUSEBUTTONDOWN:
            if button_rect2.collidepoint(event.pos):
                run=False
            if button_rect3.collidepoint(event.pos):
                pygame.display.iconify()
            if button_rect4.collidepoint(event.pos) and option_state==0:
                  _text2_colour=(150,150,150)
                  option_state=1
            elif button_rect4.collidepoint(event.pos) and option_state==1:
                _text2_colour=(255,255,255)
                option_state=0
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            if button_recta.collidepoint(event.pos):
                  ss=1
                  sss=1
                  aiss=pss=gss=nss=0
            if button_rectb.collidepoint(event.pos):
                  aiss=1
                  sss=pss=gss=nss=0
                  ais=1
            if button_rectc.collidepoint(event.pos):
                  pss=1
                  sss=aiss=gss=nss=0
                  ps=1
            if button_rectd.collidepoint(event.pos):
                  gss=1
                  sss=aiss=pss=nss=0
                  gs=1
            if button_recte.collidepoint(event.pos):
                  nss=1
                  sss=aiss=gss=pss=0
                  ns=1

        if event.type==pygame.MOUSEMOTION:
              if button_rect1.collidepoint(event.pos):
                  search_bar_colour=(100,100,100)
                  search_bar_border_colour=(255,255,255)
                  search_bar_text_colour=(255,255,255)
                  search_icon_state=1
              else:
                  search_bar_colour=(90,90,90)
                  search_bar_border_colour=(150,150,150)
                  search_bar_text_colour=(180,180,180)
                  search_icon_state=0
              if button_rect2.collidepoint(event.pos):
                close_text_colour=(255,255,255)
              else:
                  close_text_colour=(150,150,150)
              if button_rect3.collidepoint(event.pos):
                  _text_colour=(255,255,255)
              else:
                 _text_colour=(150,150,150)
              if button_rect4.collidepoint(event.pos):
                  _text2_colour=(255,255,255)
              elif option_state==1:
                  _text2_colour=(150,150,150)
              if button_recta.collidepoint(event.pos):
                  school_state=1
              else: 
                  school_state=0
              if button_rectb.collidepoint(event.pos):
                  ai_state=1
              else:
                  ai_state=0
              if button_rectc.collidepoint(event.pos):
                  pen_state=1
              else:
                  pen_state=0
              if button_rectd.collidepoint(event.pos):
                  game_state=1
              else:
                  game_state=0
              if button_recte.collidepoint(event.pos):
                  news_state=1
              else:
                  news_state=0

    #Animation
    if option_state==0 and left_rect_state<=100:
        option_state_animation_push()
    elif option_state==1 and left_rect_state>=55:
        option_state_animation_pull()

    #Background
    screen.fill((30,30,30))#main_Background
    top_rect=pygame.draw.rect(screen,(70,70,70),[0,0,winsize[0],30])#Top bar/menu bar
    left2_rect=pygame.draw.rect(screen,(45,45,45),[left_rect_state+10,32,left2_rect_state+left_rect_state,winsize[1]])#option bar pair
    left_rect=pygame.draw.rect(screen,(70,70,70),[0,32,left_rect_state,winsize[1]])#left bar/menu bar
    square=pygame.draw.rect(screen,(45,45,45),[50,squarey,left_rect_state,50])

    #Option in options
    if text=="School":
        None

    #Change button colour
    if sss==1:
        coloura=(45,45,45)
        ss=1
        squarey=32
        text="School"
    elif sss==0:
        coloura=(70,70,70)
        ss=0
    if aiss==1:
        colourb=(45,45,45)
        ais=1
        squarey=82
        text="Bot1"
    elif aiss==0:
        colourb=(70,70,70)
        ais=0
    if pss==1:
        ps=1
        colourc=(45,45,45)
        squarey=132
        text="Bot2"
    elif pss==0:
        ps=0
        colourc=(70,70,70)
    if gss==1:
        gs=1
        colourd=(45,45,45)
        squarey=182
        text="Games"
    elif gss==0:
        gs=0
        colourd=(70,70,70)
    if nss==1:
        ns=1
        coloure=(45,45,45)
        squarey=237
        text="News"
    elif nss==0:
        ns=0
        coloure=(70,70,70)
    #Buttons for options
    pygame.draw.rect(screen,coloura,button_recta,0,-1,10,-1,10,-1)
    pygame.draw.rect(screen,colourb,button_rectb,0,-1,10,-1,10,-1)
    pygame.draw.rect(screen,colourc,button_rectc,0,-1,10,-1,10,-1)
    pygame.draw.rect(screen,colourd,button_rectd,0,-1,10,-1,10,-1)
    pygame.draw.rect(screen,coloure,button_recte,0,-1,10,-1,10,-1)

    #Text for options
    option_text=font.render(text,True,(255,255,255))
    if left_rect_state>=100:
       screen.blit(option_text,(50,squarey+15))

    #Search icon/search bar
    search_bar=pygame.draw.rect(screen,search_bar_colour,[winsize[0]-370,4,300,22],0,7)
    search_bar_border=pygame.draw.rect(screen,search_bar_border_colour,[winsize[0]-370,4,300,22],1,7)
    search_bar_text=font.render("Search",True,search_bar_text_colour)
    search_bar_text_xy=search_bar_text.get_rect(center=button_rect1.center)
    screen.blit(search_bar_text,(search_bar_text_xy[0]+15,search_bar_text_xy[1]))
    if search_icon_state==1:
      screen.blit(search_icon_main1,(search_bar_text_xy[0]-5,search_bar_text_xy[1]+2))
    else:
      screen.blit(search_icon_main,(search_bar_text_xy[0]-5,search_bar_text_xy[1]+2))

    #Close and - button
    close_text=font.render("X",True,close_text_colour)
    close_text_xy=close_text.get_rect(center=button_rect2.center)
    screen.blit(close_text,close_text_xy)
    _text=font1.render("-",True,_text_colour)
    _text_xy=_text.get_rect(center=button_rect3.center)
    screen.blit(_text,(_text_xy[0],_text_xy[1]-1))

    #Option menu button
    _text2=font1.render("_",True,_text2_colour)
    _text2_xy=_text2.get_rect(center=button_rect4.center)
    screen.blit(_text2,(_text2_xy[0],_text2_xy[1]-10))
    screen.blit(_text2,(_text2_xy[0],_text2_xy[1]-15))
    screen.blit(_text2,(_text2_xy[0],_text2_xy[1]-20))
    screen.blit(_text2,(_text2_xy[0],_text2_xy[1]-25))
    
    #=========================================[For options]
    #School
    if school_state==0 and ss==0:
       screen.blit(school_main,(school_xy[0],school_xy[1]+5))
    elif school_state==1 or ss==1:
       screen.blit(school_main1,school_xy)
    #AI
    if ai_state==0 and ais==0:
        screen.blit(ai_main,(ai_xy[0],ai_xy[1]+5))
    elif ai_state==1 or ais==1:
        screen.blit(ai_main1,ai_xy)
    #Pen AI
    if pen_state==0 and ps==0:
        screen.blit(pen_main,(pen_xy[0],pen_xy[1]+5))
    elif pen_state==1 or ps==1:
        screen.blit(pen_main1,pen_xy)
    #Games
    if game_state==0 and gs==0:
        screen.blit(game_main,(game_xy[0],game_xy[1]+5))
    elif game_state==1 or gs==1:
        screen.blit(game_main1,game_xy)
    #news
    if news_state==0 and ns==0:
        screen.blit(news_main,(news_xy[0],news_xy[1]+5))
    elif news_state==1 or ns==1:
        screen.blit(news_main1,(news_xy[0],news_xy[1]))

    pygame.display.update()
pygame.quit()