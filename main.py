import tkinter as tk
from tkinter import Text, messagebox

# Sample dictionary for spell checking
with open("words.txt", 'r') as file:
    WORDS = [line.strip() for line in file]

class SpellChecker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spell Checker")
        self.geometry("600x500")

        self.text = Text(self, font=("Arial", 14), wrap='word', undo=True)
        self.text.pack(expand=True, fill='both')
        self.text.bind("<KeyRelease>", self.spell_check)
        self.text.tag_configure("mistake", foreground="red")

    def spell_check(self, event=None):
        self.text.tag_remove("mistake", "1.0", tk.END)
        content = self.text.get("1.0", tk.END)
        words = content.split()

        for word in words:
            start_idx = content.find(word)
            end_idx = start_idx + len(word)

            if word.lower() not in WORDS:
                self.text.tag_add("mistake", f"1.0 + {start_idx}c", f"1.0 + {end_idx}c")
                self.text.tag_bind("mistake", "<Enter>", lambda e, w=word: self.show_suggestions(e, w))

    def show_suggestions(self, event, word):
        suggestions = self.get_suggestions(word.lower())
        if suggestions:
            messagebox.showinfo("Suggestions", f"Suggestions for '{word}':\n" + "\n".join(suggestions))

    def get_suggestions(self, word, num_suggestions=3):
        distances = []
        for candidate in WORDS:
            distance = self.levenshtein_distance(word, candidate)
            distances.append((distance, candidate))
        distances.sort()  # Sort by distance (smallest first)
        return [candidate for _, candidate in distances[:num_suggestions]]

    def levenshtein_distance(self, s1, s2):
        # Initialize matrix of zeros
        rows = len(s1) + 1
        cols = len(s2) + 1
        dist = [[0] * cols for _ in range(rows)]

        # Populate matrix of zeros with row and column indices
        for i in range(1, rows):
            dist[i][0] = i
        for j in range(1, cols):
            dist[0][j] = j

        # Iterate over the matrix to compute the cost
        for i in range(1, rows):
            for j in range(1, cols):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                dist[i][j] = min(dist[i - 1][j] + 1,  # deletion
                                 dist[i][j - 1] + 1,  # insertion
                                 dist[i - 1][j - 1] + cost)  # substitution

        return dist[-1][-1]


if __name__ == "__main__":
    app = SpellChecker()
    app.mainloop()
