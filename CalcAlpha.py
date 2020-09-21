import pygame
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (255, 145, 255)

pygame.display.set_caption("Calculator")
display = pygame.display.set_mode((650, 700))
font = pygame.font.SysFont('arial.ttf', 80)

outputButtonText = font.render('=', True, black)
text7 = font.render('7', True, black)
text8 = font.render('8', True, black)
text9 = font.render('9', True, black)
textPlus = font.render('+', True, black)
text4 = font.render('4', True, black)
text5 = font.render('5', True, black)
text6 = font.render('6', True, black)
textMinus = font.render('-', True, black)
text1 = font.render('1', True, black)
text2 = font.render('2', True, black)
text3 = font.render('3', True, black)
textReset = font.render('R', True, black)

num1 = 0
num2 = 0
numAmount = 0
displaying = 0
resultDone = 0
mouse = 0


def output():
    pygame.draw.rect(display, white, (50, 50, 400, 100))


def outputButton():
    pygame.draw.rect(display, white, (500, 50, 100, 100))


def button7():
    pygame.draw.rect(display, white, (50, 200, 100, 100))


def button8():
    pygame.draw.rect(display, white, (200, 200, 100, 100))


def button9():
    pygame.draw.rect(display, white, (350, 200, 100, 100))


def buttonPlus():
    pygame.draw.rect(display, white, (500, 200, 100, 100))


def button4():
    pygame.draw.rect(display, white, (50, 350, 100, 100))


def button5():
    pygame.draw.rect(display, white, (200, 350, 100, 100))


def button6():
    pygame.draw.rect(display, white, (350, 350, 100, 100))


def buttonMinus():
    pygame.draw.rect(display, white, (500, 350, 100, 100))


def button1():
    pygame.draw.rect(display, white, (50, 500, 100, 100))


def button2():
    pygame.draw.rect(display, white, (200, 500, 100, 100))


def button3():
    pygame.draw.rect(display, white, (350, 500, 100, 100))


def buttonReset():
    pygame.draw.rect(display, white, (500, 500, 100, 100))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 150 >= mouse[0] >= 50:
                if 300 >= mouse[1] >= 200:
                    if numAmount == 0:
                        num1 = 7
                        numAmount = 1
                    elif numAmount == 1:
                        if displaying == 1 or displaying == 2:
                            num2 = 7
                            numAmount = 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 300 >= mouse[0] >= 200:
                if 300 >= mouse[1] >= 200:
                    if numAmount == 0:
                        num1 = 8
                        numAmount = 1
                    elif numAmount == 1:
                        if displaying == 1 or displaying == 2:
                            num2 = 8
                            numAmount = 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 450 >= mouse[0] >= 350:
                if 300 >= mouse[1] >= 200:
                    if numAmount == 0:
                        num1 = 9
                        numAmount = 1
                    elif numAmount == 1:
                        if displaying == 1 or displaying == 2:
                            num2 = 9
                            numAmount = 2

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 150 >= mouse[0] >= 50:
                if 450 >= mouse[1] >= 350:
                    if numAmount == 0:
                        num1 = 4
                        numAmount = 1
                    elif numAmount == 1:
                        if displaying == 1 or displaying == 2:
                            num2 = 4
                            numAmount = 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 300 >= mouse[0] >= 200:
                if 450 >= mouse[1] >= 350:
                    if numAmount == 0:
                        num1 = 5
                        numAmount = 1
                    elif numAmount == 1:
                        if displaying == 1 or displaying == 2:
                            num2 = 5
                            numAmount = 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 450 >= mouse[0] >= 350:
                if 450 >= mouse[1] >= 350:
                    if numAmount == 0:
                        num1 = 6
                        numAmount = 1
                    elif numAmount == 1:
                        if displaying == 1 or displaying == 2:
                            num2 = 6
                            numAmount = 2

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 150 >= mouse[0] >= 50:
                if 600 >= mouse[1] >= 500:
                    if numAmount == 0:
                        num1 = 1
                        numAmount = 1
                    elif numAmount == 1:
                        if displaying == 1 or displaying == 2:
                            num2 = 1
                            numAmount = 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 300 >= mouse[0] >= 200:
                if 600 >= mouse[1] >= 500:
                    if numAmount == 0:
                        num1 = 2
                        numAmount = 1
                    elif numAmount == 1:
                        if displaying == 1 or displaying == 2:
                            num2 = 2
                            numAmount = 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 450 >= mouse[0] >= 350:
                if 600 >= mouse[1] >= 500:
                    if numAmount == 0:
                        num1 = 3
                        numAmount = 1
                    elif numAmount == 1:
                        if displaying == 1 or displaying == 2:
                            num2 = 3
                            numAmount = 2

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 600 >= mouse[0] >= 500:
                if 150 >= mouse[1] >= 100:
                    if numAmount == 2:
                        resultDone = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 600 >= mouse[0] >= 500:
                if 300 >= mouse[1] >= 200:
                    if numAmount == 1:
                        displaying = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 600 >= mouse[0] >= 500:
                if 450 >= mouse[1] >= 350:
                    if numAmount == 1:
                        displaying = 2

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 600 >= mouse[0] >= 500:
                if 600 >= mouse[1] >= 500:
                    numAmount = 0
                    num1 = 0
                    num2 = 0
                    displaying = 0
                    resultDone = False

    mouse = pygame.mouse.get_pos()
    addResult = num1 + num2
    subResult = num1 - num2
    addResultText = font.render(str(addResult), True, black)
    subResultText = font.render(str(subResult), True, black)

    output()
    outputButton()
    button7()
    button8()
    button9()
    buttonPlus()
    button4()
    button5()
    button6()
    buttonMinus()
    button1()
    button2()
    button3()
    buttonReset()

    display.blit(outputButtonText, (535, 70))
    display.blit(text7, (83, 225))
    display.blit(text8, (233, 225))
    display.blit(text9, (383, 225))
    display.blit(textPlus, (533, 225))
    display.blit(text4, (83, 375))
    display.blit(text5, (233, 375))
    display.blit(text6, (383, 375))
    display.blit(textMinus, (543, 375))
    display.blit(text1, (83, 525))
    display.blit(text2, (233, 525))
    display.blit(text3, (383, 525))
    display.blit(textReset, (533, 525))

    if resultDone:
        if displaying == 1:
            display.blit(addResultText, (300, 70))
        elif displaying == 2:
            display.blit(subResultText, (300, 70))

    pygame.display.update()
