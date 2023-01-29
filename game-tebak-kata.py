import string                                                               
import os                                                                  
import time                                                                 
import random                                                             
from tkinter import *                                                       
import tkinter as tk                                                     
from tkinter import messagebox                                              
from PIL import Image, ImageTk, ImageDraw, ImageFont
'''
    Permulaian dari kodingan konsole Code
'''
class hangman:
    played_word = ""                                                      
    gameboard = []                                                          
    gameboard_finished = []                                                 
    guess = ''                                                              
    guess_archieve = ['Jumlah Tebakan:']                                           
    lives = ['Kesempatan Bermain:']                                                     
    end_state = False                                                       
    # Daftar kata-kata
    # word_list = ["a"*9]
    word_list = ['mutlak','benar','terserap','menonjolkan','aktivis','sebenarnya','aktualitas','remaja','mempengaruhi','terpengaruh','udara','waspada','sepanjangwaktu','mengalegorisasikan','persekutuan','aliansi','kiasan','sindiran','baik','samasekali','memperkuat','analisis','semu','tampaknya','penampilan','menangkap','menilai','penilaian','anggapan','astronomis','sikap','rata-rata','sadar','kesadaran','bayi','padadasarnya','tongkat','kepercayaan','keyakinan','besar','darah','berbasisluas','tanpahenti','pusat','bersertifikat','nyanyian','klaim','rahasia','memikirkan','tanggungjawab','komentar','komentator','lengkap','samasekali','memahami','terpadu','curhat','dugaan','hatinurani','kesadaran','besar','sangat']
    def __init__(self):
        self.played_word = ""                                                      
        self.gameboard = []                                                          
        self.gameboard_finished = []                                                 
        self.guess = ''                                                              
        self.guess_archieve = ['Jumlah Tebakan:']                                           
        self.lives = ['Kesempatan Bermain:']                                                     
        self.end_state = False                                                       
        # self.word_list = ["a"*5]
    def set_Word(self):
        word = random.choice(self.word_list)                               
        self.played_word = word

    def set_finished_board(self,word):
        word_list_finished = list(word)
        self.gameboard_finished = word_list_finished

    def set_create_board(self,word):
        word_list_playing = ['_'] * len(word)
        self.gameboard = word_list_playing

    def set_move(self,guess,location):
        self.gameboard[location] = guess

    def set_guess(self,player_guess):
        if(player_guess in self.guess_archieve):                            
            print("Anda telah coba bermain " + player_guess)
            return (-2,player_guess)    
        elif(player_guess in self.gameboard_finished):                     
            for position,char in enumerate(self.gameboard_finished):
                if char== player_guess:                                    
                    self.set_move(player_guess,position)
            self.guess_archieve.append(player_guess)
            return (1,"")
        else:
            self.lives.append('x')                                          
            self.guess_archieve.append(player_guess)
            return (0,player_guess)                    


    def get_eg_status(self):
        if(len(self.lives) == 6):
            os.system('cls' if os.name == 'nt' else 'clear')                
            self.end_state = True
            # messagebox.showinfo("PERMAINAN SELESAI!", "PERMAINAN SELESAI: Terima kasih telah bermain! \n Jawaban:\t" + str(''.join([str(elem) for elem in self.gameboard_finished])))
            # main_form.quit()
            return (-1,"PERMAINAN SELESAI: Terima kasih telah bermain! \n Jawaban:\n" + str(''.join([str(elem) for elem in self.gameboard_finished])))

        elif(self.gameboard == self.gameboard_finished):
            os.system('cls' if os.name == 'nt' else 'clear')                
            self.end_state = True
            # messagebox.showinfo("Selamat!", "Anda menang! Terima kasih telah bermain")
            # main_form.quit()
            return (1,"Anda menang! Terima kasih telah bermain!")
        else:
            return (0,"")

    def get_user_guess(self,letter):
        char = str(letter)
        if(len(char) == 1 and char.isalpha()):
            return self.set_guess(char.lower())
        else:
            print("Tebakan harus satu kata!")
            return (-1,"Tebakan harus satu kata!")
            
# game = hangman                                                             
# game.set_Word(game)                                                         
# game.set_create_board(game,game.played_word)                               
# game.set_finished_board(game,game.played_word)                               
'''
    Akhir dari kodingan Console
'''


'''
TNS TKINTER START
'''

def setupWindow():
    window = tk.Tk()
    window.geometry("1280x832")

    canvas = tk.Canvas(window, width = 1280, height = 832)
    canvas.pack()
    return canvas,window

def startGame():
    def startGame(window):
        game = hangman()
        game.set_Word()
        game.set_create_board(game.played_word)
        game.set_finished_board(game.played_word)
        while len(game.played_word) > 9:
            game.set_Word()
            game.set_create_board(game.played_word)
            game.set_finished_board(game.played_word)
        window.destroy()
        mainGame(game)
        # return game

    canvas,window = setupWindow()

    bgImage = ImageTk.PhotoImage(Image.open("assets/backgroundMainpage.png")) 
    bg = canvas.create_image(0, 0, image=bgImage, anchor=tk.NW)

    startImage = ImageTk.PhotoImage(Image.open("assets/tombolMulai.png"))
    startButton = canvas.create_image(573+50, 483+100, image=startImage)
    canvas.tag_bind(startButton, "<Button-1>", lambda func: startGame(window))

    window.mainloop()

def mainGame(game,guessResult=(1,""),gameState=(0,"")):

    images=[]
    def create_rectangle(currWin,x,y,a,b,**options):
        win = currWin
        
        if 'alpha' in options:
            # Calculate the alpha transparency for every color(RGB)
            alpha = int(options.pop('alpha') * 255)
            # Use the fill variable to fill the shape with transparent color
            fill = options.pop('fill')
            fill = win.winfo_rgb(fill) + (alpha,)
            image = Image.new('RGBA', (a-x, b-y), fill)
            images.append(ImageTk.PhotoImage(image))
            canvas.create_image(x, y, image=images[-1], anchor='nw')
            canvas.create_rectangle(x, y,a,b, **options)
    
    def endGame(window):
            window.destroy()
            startGame()

    def create_image(size, bgColor, message, font, fontColor):
            W, H = size
            image = Image.new('RGBA', size, bgColor)
            draw = ImageDraw.Draw(image)
            _, _, w, h = draw.textbbox((0, 0), message, font=font)
            draw.text(((W-w)/2, (H-h)/2), message, font=font, fill=fontColor)
            return image

    def tebak(input,window):
        # print(input)
        tempGuessResult = game.get_user_guess(input.lower())
        tempGameState = game.get_eg_status()
        print(game.played_word,game.gameboard,game.gameboard_finished)
        window.destroy()
        mainGame(game,tempGuessResult,tempGameState)

    def okGagalTebak(window):
        window.destroy()
        mainGame(game)

    canvas,window = setupWindow()
    print(game.played_word,game.gameboard,game.gameboard_finished)
    bgImage = ImageTk.PhotoImage(Image.open("assets/background.png")) 
    bg = canvas.create_image(0, 0, image=bgImage, anchor=tk.NW)

    questionImg = ImageTk.PhotoImage(Image.open("assets/kata berisi {} huruf.png".format(str(len(game.played_word))))) 
    questionLabel = canvas.create_image(391, 165, image=questionImg, anchor=tk.NW)

    instructionImg = ImageTk.PhotoImage(Image.open("assets/silahkan tebak 1 huruf.png")) 
    instructionLabel = canvas.create_image(335, 449, image=instructionImg, anchor=tk.NW)

    cekButtonImg = ImageTk.PhotoImage(Image.open("assets/tombolCek.png")) 
    cekButton = canvas.create_image(715, 562-60+30, image=cekButtonImg, anchor=tk.NW)
    canvas.tag_bind(cekButton, "<Button-1>", lambda func: tebak(e1.get(),window))

    fntMain = ImageFont.truetype("assets/LuckiestGuy-Regular.ttf", 29)
    outMain = create_image((194,30),(255,255,255,0),"LANGKAH KE-{}".format(len(game.guess_archieve)),fntMain,'white')
    letterImgMain = ImageTk.PhotoImage(outMain)
    letterLabelMain = canvas.create_image(1013+100, 81, image=letterImgMain)

    # startImage = ImageTk.PhotoImage(Image.open("assets/tombolMulai.png"))
    # startButton = canvas.create_image(573+50, 483+100, image=startImage)
    # canvas.tag_bind(startButton, "<Button-1>", startGame)
    # tes = ImageTk.PhotoImage(Image.open("assets/huruf/Frame.png"))
    # tesImg = ImageTk.PhotoImage(Image.open("assets/huruf/Frame.png"))
    # tesLbl = canvas.create_image(591, 255+50, image=tesImg)
    
    # def drawCurrentWord():
        # canvasX = canvas
        # global canvas
    wordStr = game.gameboard
    # wordStr = "_"*3
    for i in range(len(wordStr)):
        startX = (1230 - (96 * len(wordStr) + 19 * (len(wordStr) - 1))) // 2 + 75
        # print(startX-591)
        startY = 255+50
        mid= len(wordStr) //2
        # currX = startX - (96+19) * (mid-i) if i<=mid else startX + (96+19) * (i-mid)
        currX = startX + (96+19) * (i)
        print(currX)
        # currX += (1230 - (96 * len(wordStr) + 19 * (len(wordStr) - 1))) // 2 + 25
        # print((1230 - (96 * len(wordStr) + 19 * (len(wordStr) - 1))) // 2 + 25)
        # img = ImageTk.PhotoImage(Image.open("assets/huruf/Frame.png"))
        if game.gameboard[i] == '_':
            exec('tesImg{} = ImageTk.PhotoImage(Image.open("assets/huruf/Frame.png"))'.format(str(i)))
            exec('tesLbl = canvas.create_image(currX, startY, image=tesImg{})'.format(str(i), str(i)))
        else:
            ordWord = ord(game.gameboard[i].lower()) - ord("a") + 1
            file="assets/huruf/Frame({}).png".format(ordWord)
            exec('tesImg{} = ImageTk.PhotoImage(Image.open(file))'.format(str(i)))
            exec('tesLbl = canvas.create_image(currX, startY, image=tesImg{})'.format(str(i), str(i)))
        print(currX,startY)



    if (gameState[0]!=0):
        bgImage = ImageTk.PhotoImage(Image.open("assets/background.png")) 
        bg = canvas.create_image(0, 0, image=bgImage, anchor=tk.NW)
        # create_rectangle(window,458, 532, 458+232, 562+85, fill= "white", alpha= .9)
        # create_rectangle(window,0, 0, 1280, 832, fill= "black", alpha= .51)
        # errorImg = ImageTk.PhotoImage(Image.open("assets/errorImage.png")) 
        # errorLabel = canvas.create_image(307, 122, image=errorImg, anchor=tk.NW)

        if(gameState[0]==1):
            cardMenangImage = ImageTk.PhotoImage(Image.open("assets/menang.png")) 
            cardMenang = canvas.create_image(307, 79, image=cardMenangImage, anchor=tk.NW)
            # out = Image.new("RGB", (575, 72), (255, 200, 200))
            
            # d = ImageDraw.Draw(out)
            # d.multiline_text((0, 0), ""+"-".join(game.gameboard_finished), font=fnt, fill=(255, 255, 255), align="center")
            fnt = ImageFont.truetype("assets/LuckiestGuy-Regular.ttf", 63)
            out = create_image((575,72),(255,255,255,0),"-".join(game.gameboard_finished),fnt,'white')
            letterImg = ImageTk.PhotoImage(out)
            letterLabel = canvas.create_image(637, 399+65-50, image=letterImg)


            fnt2 = ImageFont.truetype("assets/LuckiestGuy-Regular.ttf", 35)
            out2 = create_image((575,72),(255,255,255,0),"KATA:",fnt2,'white')
            letterImg2 = ImageTk.PhotoImage(out2)
            letterLabel2 = canvas.create_image(637, 399-50, image=letterImg2)

            fnt3 = ImageFont.truetype("assets/LuckiestGuy-Regular.ttf", 45)
            out3 = create_image((575,72),(255,255,255,0),"DITEBAK DALAM",fnt3,'white')
            letterImg3 = ImageTk.PhotoImage(out3)
            letterLabel3 = canvas.create_image(637, 399+65+85-50-10, image=letterImg3)

            fnt4 = ImageFont.truetype("assets/LuckiestGuy-Regular.ttf", 45)
            out4 = create_image((575,72),(255,255,255,0),"{} LANGKAH".format(len(game.guess_archieve)-1),fnt4,'white')
            letterImg4 = ImageTk.PhotoImage(out4)
            letterLabel4 = canvas.create_image(637, 399+65+85+55-50-10, image=letterImg4)

            okButtonImg = ImageTk.PhotoImage(Image.open("assets/tombolSelesai.png")) 
            okButton = canvas.create_image(544, 511+50+20, image=okButtonImg, anchor=tk.NW)
            canvas.tag_bind(okButton, "<Button-1>", lambda func: endGame(window))

        if(gameState[0]==-1):
            cardKalahImage = ImageTk.PhotoImage(Image.open("assets/kalah.png")) 
            cardKalah = canvas.create_image(307, 79, image=cardKalahImage, anchor=tk.NW)
            fnt = ImageFont.truetype("assets/LuckiestGuy-Regular.ttf", 63)
            out = create_image((519+100,72),(255,255,255,1),"-".join(game.gameboard_finished),fnt,'white')
            letterImg = ImageTk.PhotoImage(out)
            letterLabel = canvas.create_image(377+250, 482+65-50, image=letterImg)
            okButtonImg = ImageTk.PhotoImage(Image.open("assets/tombolSelesai.png")) 
            okButton = canvas.create_image(544, 511+50+20, image=okButtonImg, anchor=tk.NW)
            canvas.tag_bind(okButton, "<Button-1>", lambda func: endGame(window))
        # return

    elif (guessResult[0] == 0):
        # exec('tesImg{} = ImageTk.PhotoImage(Image.open("assets/huruf/Frame.png"))'.format(str(i)))
        # exec('tesLbl = canvas.create_image(currX, startY, image=tesImg{})'.format(str(i), str(i)))
        create_rectangle(window,458, 532, 458+232, 562+85, fill= "white", alpha= .9)
        create_rectangle(window,0, 0, 1280, 832, fill= "black", alpha= .51)
        
        errorImg = ImageTk.PhotoImage(Image.open("assets/errorImage.png")) 
        errorLabel = canvas.create_image(307, 122, image=errorImg, anchor=tk.NW)

        out = Image.new("RGBA", (45, 73), (255, 255, 255,0))
        fnt = ImageFont.truetype("assets/LuckiestGuy-Regular.ttf", 73)
        d = ImageDraw.Draw(out)
        d.multiline_text((0, 0), guessResult[1], font=fnt, fill=(255, 255, 255))
        letterImg = ImageTk.PhotoImage(out)
        letterLabel = canvas.create_image(620+10, 391+35, image=letterImg)

        okButtonImg = ImageTk.PhotoImage(Image.open("assets/tombolOK.png")) 
        okButton = canvas.create_image(544, 511, image=okButtonImg, anchor=tk.NW)
        canvas.tag_bind(okButton, "<Button-1>", lambda func: okGagalTebak(window))

        backButtonImg = ImageTk.PhotoImage(Image.open("assets/backButton.png")) 
        backButton = canvas.create_image(63, 67, image=backButtonImg, anchor=tk.NW)
        canvas.tag_bind(backButtonImg, "<Button-1>", lambda func: endGame(window))

    elif (guessResult[0] == -1):
        create_rectangle(window,458, 532, 458+232, 562+85, fill= "white", alpha= .9)
        create_rectangle(window,0, 0, 1280, 832, fill= "black", alpha= .51)
        errorImg = ImageTk.PhotoImage(Image.open("assets/errorImageOneCharacter.png")) 
        errorLabel = canvas.create_image(307, 122, image=errorImg, anchor=tk.NW)
        okButtonImg = ImageTk.PhotoImage(Image.open("assets/tombolOK.png")) 
        okButton = canvas.create_image(544, 511, image=okButtonImg, anchor=tk.NW)
        canvas.tag_bind(okButton, "<Button-1>", lambda func: okGagalTebak(window))
    elif (guessResult[0] == -2):
        create_rectangle(window,458, 532, 458+232, 562+85, fill= "white", alpha= .9)
        create_rectangle(window,0, 0, 1280, 832, fill= "black", alpha= .51)

        errorImg = ImageTk.PhotoImage(Image.open("assets/errorImageSudahCobaBermain.png")) 
        errorLabel = canvas.create_image(307, 122, image=errorImg, anchor=tk.NW)

        out2 = Image.new("RGBA", (45, 73), (255, 255, 255,0))
        fnt2 = ImageFont.truetype("assets/LuckiestGuy-Regular.ttf", 73)
        d2 = ImageDraw.Draw(out2)
        d2.multiline_text((0, 0), guessResult[1], font=fnt2, fill=(255, 255, 255))
        letterImg2 = ImageTk.PhotoImage(out2)
        letterLabel2 = canvas.create_image(620+10, 391+35, image=letterImg2)

        print(guessResult[1])
        
        okButtonImg = ImageTk.PhotoImage(Image.open("assets/tombolOK.png")) 
        okButton = canvas.create_image(544, 511, image=okButtonImg, anchor=tk.NW)
        canvas.tag_bind(okButton, "<Button-1>", lambda func: okGagalTebak(window))
    elif gameState[0] == 0 :
        e1 = tk.Entry(canvas,width=3,font=('Arial',78),fg='#EAA727')
        canvas.create_window(458+130, 562+30, window = e1)
        
        backButtonImg = ImageTk.PhotoImage(Image.open("assets/backButton.png")) 
        backButton = canvas.create_image(63, 67, image=backButtonImg, anchor=tk.NW)
        canvas.tag_bind(backButton, "<Button-1>", lambda func: endGame(window))
    
    canvas.update()
    # drawCurrentWord()
    canvas.pack()
    window.mainloop()

startGame()

# bgimg= tk.PhotoImage(file = "assets/backgroundMainpage.png")
# limg= tk.Label(window, i=bgimg)
# limg.pack()

# titleImg = tk.PhotoImage(file="assets/judulGame.png")
# titleImgLbl = tk.Label(image=titleImg)
# titleImgLbl.place(x=201,y=193)
# titleImgLbl.pack()



# buttonLoad = Image.open("assets/tombolMulai.png")
# # window.button_img = tk.Button(window, image = buttonImg,width=314,height=92)
# window.buttonImg = ImageTk.PhotoImage(buttonLoad)
# buttonMulai = tk.Button(window, image = window.buttonImg,width=314,height=92)
# # buttonMulai.config(image=window.buttonImg)
# buttonMulai.place(x=483,y=573)


# window.mainloop()


# '''
#    GUI menggunakan Tkinter
# '''
# main_form = Tk()                                                          
# main_form.title("Game Tebak Kata")
# main_form.geometry("600x310")                                              
# main_form.resizable(0,0)                                                   


# alphaList = list(string.ascii_lowercase)                                    
# game.gameboard


# gui_gameboard = tk.Label(main_form, text=game.gameboard ,font = "Verdana 30 bold")
# gui_gameboard.pack(side="top")

# gui_guess_archieve = tk.Label(main_form, text=game.guess_archieve ,font = "Verdana 10 bold")
# gui_guess_archieve.pack()
# gui_guess_archieve.place(bordermode=OUTSIDE, x=200, y=260)

# gui_lives = tk.Label(main_form, text=game.lives ,font = "Verdana 10 bold")
# gui_lives.pack()
# gui_lives.place(bordermode=OUTSIDE, x=200, y=280)

# def btn_Click(self,letter):
#     self.config(state="disabled")
    # game.get_user_guess(game,letter.lower())
#     gui_gameboard['text'] = game.gameboard
#     gui_guess_archieve['text'] = game.guess_archieve
#     gui_lives['text'] = game.lives
#     game.get_eg_status(game)                                                
#     print(letter)    

# def create_button(letter,xpos,ypos,index):
#     letter = tk.Button(main_form, text=(alphaList[index].upper()),command = lambda: btn_Click(letter,alphaList[index].upper()))
#     letter.pack()
#     letter.place(bordermode=OUTSIDE, height=50, width=100,x=xpos,y=ypos)

# def populate_board():                                                       
#     c = 0
#     startpos = 60
#     xpos = 0
#     ypos = startpos
#     while(c < 26):

#         if(c == 6):
#             ypos = startpos + 50
#             xpos = 0
#         elif(c == 12):
#             ypos = startpos + 100
#             xpos = 0
#         elif(c == 18):
#             ypos = startpos + 150
#             xpos = 0
#         elif(c == 24):
#             ypos = startpos + 200
#             xpos = 0

#         create_button(alphaList[c],xpos,ypos,c)
#         xpos = xpos + 100
#         c = c + 1 
# populate_board()
# main_form.mainloop()
# '''
#     Akhir dari GUI
# '''