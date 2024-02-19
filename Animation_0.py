from tkinter import *
import tkinter.font


class Animation:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root_width, self.root_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        self.canvas = Canvas(self.root, bg="#4381b3", width=self.root_width, height=self.root_height)
        self.canvas.grid(row=0, column=0)

        self.font_binary = tkinter.font.Font(family="Binary CHR BRK", size=100)
        self.font_arial = tkinter.font.Font(family="Arial", size=30)
        self.canvas.create_text(self.root_width / 2, 50, text="CAESAR CIPHER", fill='black', font=self.font_binary)
        self.decrypted_text = "The die is cast"
        self.encrypted_text = ''.join(chr(ord(char) + 3) for char in self.decrypted_text if char.isalpha())
        self.list_of_encrypted_text = []
        self.current_animation = 0
        x1 = (self.root_width - 80 * len(self.decrypted_text)) / 2
        y1 = 300
        x2 = x1 + 70
        y2 = 400
        self.coords = (x1, y1, x2, y2)
        self.display_text_table()
        self.root.bind("<Escape>", lambda event: self.root.attributes("-fullscreen",
                                                                      not self.root.attributes("-fullscreen")))
        self.root.bind("<space>", self.next_animation)

    def next_animation(self, _event):
        if self.current_animation == 0 or self.current_animation == 2:
            self.display_arrows()
        elif self.current_animation == 1 or self.current_animation == 3:
            self.display_text_under()
        elif self.current_animation == 4:
            self.move_chars_animation()

    def display_text_table(self):
        x1 = self.coords[0]
        y1 = self.coords[1]
        x2 = self.coords[2]
        y2 = self.coords[3]
        for char in self.decrypted_text:
            if char.isalpha():
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=3)
                self.canvas.create_text(x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2,
                                        text=char, fill='black', font=self.font_binary)
            x1 += 80
            x2 += 80

    def display_text_under(self):
        x1 = self.coords[0]
        y1 = self.coords[1]
        x2 = self.coords[2]
        y2 = self.coords[3]
        if self.current_animation == 1:
            self.list_of_encrypted_text.append(self.canvas.create_text(x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2 + 100,
                                                                       text=chr(ord(self.decrypted_text[0]) + 3),
                                                                       fill='black', font=self.font_arial))
            self.current_animation += 1
        elif self.current_animation == 3:
            for char in self.decrypted_text[1:]:
                x1 += 80
                x2 += 80
                if char.isalpha():
                    self.list_of_encrypted_text.append(self.canvas.create_text(x1 + (x2 - x1) / 2,
                                                                               y1 + (y2 - y1) / 2 + 100,
                                                                               text=chr(ord(char) + 3),
                                                                               fill='black', font=self.font_arial))
            self.current_animation += 1

    def display_arrows(self):
        x1 = self.coords[0] + 10
        y1 = self.coords[1] - 20
        x2 = self.coords[2] - 10
        y2 = self.coords[3] - 20
        if self.current_animation == 0:
            self.canvas.create_line(x1, y1, x2, y1, fill="black", width=3)
            self.canvas.create_line(x2 + 1, y1 + 1, x2 - 10, y1 - 10, fill="black", width=3)
            self.canvas.create_line(x2 + 1, y1 - 1, x2 - 10, y1 + 10, fill="black", width=3)
            self.canvas.create_text(x1 + (x2 - x1)/2, y1 - 20, text='3', fill='black', font=self.font_arial)
            self.current_animation += 1
        elif self.current_animation == 2:
            for arrow in range(len(self.decrypted_text) - 1):
                if self.decrypted_text[arrow + 1].isalpha():
                    self.canvas.create_line(x1 + (80 * (arrow + 1)), y1, x2 + (80 * (arrow + 1)), y1,
                                            fill="black", width=3)
                    self.canvas.create_line(x2 + 1 + (80 * (arrow + 1)), y1 + 1, x2 - 10 + (80 * (arrow + 1)), y1 - 10,
                                            fill="black", width=3)
                    self.canvas.create_line(x2 + 1 + (80 * (arrow + 1)), y1 - 1, x2 - 10 + (80 * (arrow + 1)), y1 + 10,
                                            fill="black", width=3)
                    self.canvas.create_text(x1 + (x2 - x1) / 2 + (80 * (arrow + 1)), y1 - 20,
                                            text='3', fill='black', font=self.font_arial)
            self.current_animation += 1

    def move_chars_animation(self):
        speed = 5
        reached_bottom = False

        for text_obj in self.list_of_encrypted_text:
            self.canvas.move(text_obj, 0, speed)
            _, y1, _, _ = self.canvas.bbox(text_obj)

            if y1 + 100 >= self.root_height:
                reached_bottom = True

        if not reached_bottom:
            self.root.after(50, self.move_chars_animation)

        else:
            for i, text_obj in enumerate(self.list_of_encrypted_text):
                x1, y1, x2, y2 = self.canvas.bbox(text_obj)
                self.canvas.delete(text_obj)
                x = (x1 + x2) / 2
                y = (y1 + y2) / 2
                self.list_of_encrypted_text[0] = self.canvas.create_text(x, y, text=self.encrypted_text[i], fill="black", font=("Arial", 100))


master = Tk()
app = Animation(master)
master.mainloop()
