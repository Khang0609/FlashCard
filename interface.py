from DEF import *
from path import *

class Interface(Tk):
    def __init__(self, title, width, height, wordlist):
        super().__init__()
        #size and detail
        self.title = title
        self.width, self.height = width, height
        self.x, self.y = int(self.winfo_screenwidth()/2 - self.width/2), 20

        #asking
        self.word_list = wordlist
        self.dont_remember_list = []
        self.already_asked = []
        self.random_list = []
        self.index = 0
        #config the screen
        self.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.config(bg="#f0f0f0")

        #Everything should be complete except the content
        #question
        self.ask_question = Label(self, font=("Arial 20"),bg="gray")
        self.ask_question.place(x=100,y=50)
        #button for revealing
        self.revealing_button = Button(self, text= "Xem định nghĩa", font=("Arial 15"), command = self.revealDefinition, bg="#5DB996")
        self.revealing_button.place(x=100,y=500)
        #definition
        self.definition = Label(self,font=("Arial 20"),bg="green", fg="white")
        self.definition.place(x=2000, y=500)
        #remember button
        self.remember_button = Button(self, text= "Bạn đã nhớ từ này rồi", font=("Arial 15"), command = self.reset, bg="#5CB338", fg="#FFFFFF")
        self.remember_button.place(x=2000, y=500)
        #not remember button
        self.not_remember_button = Button(self, text= "Bạn chưa nhớ từ này", font=("Arial 15"), command = self.dontRemember, bg="#FB4141", fg="#FFFFFF")
        self.not_remember_button.place(x=2000, y=500)

        self.updateWord()
        self.showQuestion()
        self.mainloop()

    def updateWord(self):
        while len(self.word_list) != len(self.already_asked):
            self.word = random.choice(self.word_list)
            while self.word in self.already_asked:
                self.word = random.choice(self.word_list)
            self.already_asked.append(self.word)
            self.random_list.append(self.word)

    def showQuestion(self):
        self.ask_question.config(text=f"Từ {self.random_list[self.index][0].upper()} có nghĩa là gì?")
        self.definition.config(text=f"Từ dó có nghĩa là {self.random_list[self.index][1].upper()}")

    def nextQuestion(self):
        self.index += 1
        if self.index < len(self.random_list):
            self.showQuestion()
        elif len(self.dont_remember_list) != 0:
            self.everythingHide()
            self.not_yet = Label(self, text="Bạn đã trả bài, những vẫn còn một vài từ bạn chưa nhớ.\nVậy bạn muốn học tiếp không?", bg="gray", font=("Arial 20"))
            self.not_yet.place(x=100, y=100)

            self.yes_button = Button(self, text="Tôi học tiếp",bg="#5CB338", fg="#fff", command=self.keepLearning, font=("Arial 15"))
            self.yes_button.place(x=100,y=400)

            self.no_button = Button(self, text="Tôi nghỉ",bg="#FB4141", fg="#fff", command=quit, font=("Arial 15"))
            self.no_button.place(x=700,y=400)
        else:
            messagebox.showinfo("Tốt lắm!","Bạn đã hoàn thành bài ôn rồi")
            self.destroy()

    def reset(self):
        self.revealing_button.place(x=100, y=500)
        self.remember_button.place(x=2000, y=500)
        self.not_remember_button.place(x=2000, y=500)
        self.definition.place(x=2000, y=500)
        self.nextQuestion()

    def dontRemember(self):
        self.dont_remember_list.append(self.word)
        self.reset()

    def revealDefinition(self):
        self.revealing_button.place(x=2000, y=500)
        self.remember_button.place(x=100, y=500)
        self.not_remember_button.place(x=600, y=500)
        self.definition.place(x=100, y=100)

    def everythingHide(self):
        self.remember_button.place(x=2000, y=500)
        self.not_remember_button.place(x=2000, y=500)
        self.definition.place(x=2000, y=500)
        self.ask_question.place(x=2000,y=500)
        self.revealing_button.place(x=2000, y=500)

    def keepLearning(self):
        self.ask_question.place(x=100,y=50)
        self.revealing_button.place(x=100,y=500)
        self.index = 0
        self.word_list = self.dont_remember_list
        self.already_asked = []
        self.dont_remember_list = []
        self.random_list = []
        self.updateWord()
        self.not_yet.place(x=2000, y=500)
        self.yes_button.place(x=2000, y=500)
        self.no_button.place(x=2000, y=500)




word_list = getVocabList(VOCABULARY)


main_app = Interface("Flash Card", 1000, 600, word_list)