from tkinter import *
import ctypes

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

# Create the main window
class App():
    def __init__(self, width, height):
        self.w = Tk()
        self.w.title("Anxio")
        self.w.geometry(f"{width}x{height}")
        self.w.resizable(False, False)
        self.w.configure(bg="white")
        self.w.geometry(f"+0+0")
        
        self.level_num = 1
        level = Frame(self.w, bg="black", width=width, height=100)   
        level.pack(side=TOP, fill=X)
        
        self.rect_width = 250
        self.rect = Canvas(level, width=self.rect_width, height=50, bg="blue", highlightthickness=0)
        self.rect.pack(side=LEFT, padx=10, pady=10)
        
        def update_rectangle():
            self.rect_width += 250
            self.rect.config(width=self.rect_width)
        
        self.score = 0
        
        self.responses = {
                1: ["0", "1", "2", "3", "Plus de 3"],
                2: ["Non, j'ai été de bonne humeur", "Non", "Des maux de têtes", "Oui", "Je me fait mal"],
                3: ["Oui et plus encore", "Oui", "Presque", "Non", "Bloqué depuis des jours"],
                4: ["Non", "Des tremblements", "J'ai souvent mal", "TAIS TOI", "nfjkfdjkvdwfdwjkv"],
                5: ["8", "6", "4", "3", "Non"],
        }
        self.question = [
            "Combien d'éval as-tu cette semaine?",
            "As-tu déjà pensé à te suicider?",
            "As-tu pu terminer tes tâches?",
            "As-tu eu des hallucinations / des voix / des crises cette semaine?",
            "Combien d'heure par nuit dors-tu?",
        ]
        self.past = [
            
        ]
        
        def draw(responses):
            self.questions = Label(self.w, text=f"{self.question[self.level_num-1]}", font=("Arial", 15), bg="white", fg="black")
            self.questions.pack(side=TOP, anchor="nw")
        
            self.response_box = Frame(self.w, bg="red", width=width, height=400)
            self.response_box.pack(side=TOP, fill=X)
            
            for i in range(1, 6):
                score = i
                response_button = Button(self.response_box, text=f"{i}. {responses[i-1]}", font=("Arial", 15), bg="white", fg="black", command=lambda i=score: answer(i))
                response_button.pack(side=TOP, anchor="nw")
        
        def answer(num):
            update_rectangle()
            print(f"Level: {self.level_num}, Answer: {num}")
            
            if self.level_num == 2 and num == 4:
                num = num**2
            if self.level_num == 2 and num == 5:
                num = num**2+5
            if self.level_num == 4:
                num = num*2
            if self.level_num == 4 and num >= 3:
                num = num**2
            
            self.score += num
            self.response_box.destroy()
            self.questions.destroy()
            self.level_num += 1
            if self.level_num in self.responses:
                draw(self.responses[self.level_num])
            else:
                self.response_box.destroy()
                result()
        
        def result():
            self.questions.destroy()
            self.response_box.destroy()
            
            result = Label(self.w, text=f"Score: {self.score}", font=("Arial", 15), bg="black", fg="white")
            result.pack()
            
            if self.score > 145:
                title = Label(self.w, text="Repos URGENT !! PRENDS TON WEEK-END", font=("Arial", 20), bg="black", fg="white")
                title.pack()
            elif self.score < 145 and self.score >= 92:
                title = Label(self.w, text="Repos d' 1 heure max obligatoire", font=("Arial", 20), bg="black", fg="white")
                title.pack()
            elif self.score < 92 and self.score >= 48:
                title = Label(self.w, text="Repos recommandé", font=("Arial", 20), bg="black", fg="white")
                title.pack()
            elif self.score < 48 and self.score >= 24:
                title = Label(self.w, text="Repos si besoin", font=("Arial", 20), bg="black", fg="white")
                title.pack()
            else:
                title = Label(self.w, text="Tout va bien", font=("Arial", 20), bg="black", fg="white")
                title.pack()
            
        
        title = Label(self.w, text="Anxio", font=("Arial", 20), bg="black", fg="white")
        title.pack()
        
        draw(self.responses[self.level_num])
            
        self.w.mainloop()
    
        
# Run the app
if __name__ == "__main__":
    App(width, height)
        
