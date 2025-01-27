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
        level = Frame(self.w, bg="darkblue", highlightbackground="lightblue", highlightthickness=10, width=width, height=100)   
        level.pack(side=TOP, fill=X)
        
        self.rect_width = 250
        self.rect = Canvas(level,relief='sunken', width=self.rect_width, height=50, bg="blue", highlightbackground="cyan", highlightthickness=10)
        self.rect.pack(side=LEFT, padx=10, pady=10)
        
        def update_rectangle():
            self.rect_width += 250
            self.rect.config(width=self.rect_width)
            
        title = Label(self.w, text="Anxio", font=("Helvetica", 34, "bold", "italic", "underline"), bg="darkblue", fg="white", width=width, height=2)
        title.pack()
        
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
            self.questions = Label(self.w, text=f"{self.level_num}. {self.question[self.level_num-1]}", font=("Times New Roman", 25), bg="white", fg="black")
            self.questions.pack(side=TOP, anchor="center")
        
            self.response_box = Frame(self.w, bg="red", width=width, height=400, highlightbackground="pink", highlightthickness=10)
            self.response_box.pack(anchor="center", fill=X)
            
            for i in range(1, 6):
                score = i
                
                response_button_box = Frame(self.response_box, bg="red", width=width, height=100)
                response_button_box.pack(side=TOP, anchor="center")
                
                res_label = Label(response_button_box, text=f"{i}.", font=("Arial", 20), bg="red", fg="white")
                res_label.pack(side=LEFT, anchor="center", pady=10, padx=10)
                
                response_button = Button(response_button_box, text=f" {responses[i-1]}", font=("Arial", 15), bg="white", fg="black", command=lambda i=score: answer(i), width=75, height=2)
                response_button.pack(side=RIGHT, anchor="center", pady=10, padx=10)
        
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
            
            result = Label(self.w, text=f"Score: {self.score}", font=("Arial", 50), bg="white", fg="black")
            result.pack(anchor="center", pady=30)
            
            if self.score > 145:
                messages = "Repos URGENT !! PRENDS TON WEEK-END"
            elif self.score < 145 and self.score >= 92:
                messages = "Repos d' 1 heure max obligatoire"
            elif self.score < 92 and self.score >= 48:
                messages = "Repos recommandé"
            elif self.score < 48 and self.score >= 24:
                messages = "Repos si besoin"
            else:
                messages = "Tout va bien"
                
            title = Label(self.w, text=f"{messages}", font=("Arial", 75), bg="white", fg="black")
            title.pack()
            
            register = Button(self.w, text="Enregistrer le score", font=("Arial", 75), bg="lightgreen", fg="black", command=lambda score=self.score, past=messages: reg(score, past))
            register.pack()
            
            look = Button(self.w, text="Regarder l'historique des scores", font=("Arial", 75), bg="green", fg="white", command=look_scores)
            look.pack()
        
        def reg(score, past):
            with open("scores.txt", "a") as file:
                file.write(f"(\n Score: {score}\n message: {past}\n)\n")
        
        def look_scores():
            def display_scores():
                
                with open("scores.txt", "r") as file:
                    scores = file.read()
                scores_window = Toplevel(self.w)
                scores_window.title("Scores History")
                scores_window.geometry(f"{width}x{height}")
                scores_window.resizable(False, False)
                scores_window.configure(bg="white")
                
                scores_label = Label(scores_window, text=scores, font=("Arial", 20), bg="white", fg="black", justify=LEFT)
                scores_label.pack(padx=10, pady=10, fill=BOTH, expand=True)
            
            display_scores()
        
        draw(self.responses[self.level_num])
            
        self.w.mainloop()
    
        
# Run the app
if __name__ == "__main__":
    App(width, height)
        
