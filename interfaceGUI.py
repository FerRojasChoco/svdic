import tkinter as tk
from tkinter import filedialog
import customtkinter
from funtionsvd import compress_image
from funtionsvd import value
global image

#opens the files to choose the image and runs the program
def open_file_dialog():
        file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.jfif")])
        if file_path:
            image=file_path
            compress_image(image)

#choose between the grey and rgb scale
def set_scale_choice(scale):
    global scale_choice
    scale_choice=scale
    value(scale_choice)
    if set_scale_choice:
        open_file_dialog()


def run_gui():
    # set appearance mode to "System" (default) or "light" or "dark"
    customtkinter.set_appearance_mode("dark")  

    # set default color theme to "blue" (default) or "dark-blue" or "green"
    customtkinter.set_default_color_theme("dark-blue")  

    # create CTk window
    window = customtkinter.CTk()  
    window.title("Image Compressor")
    window.geometry("500x300")

    #grid
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)
    window.rowconfigure(0, weight= 1)
    window.rowconfigure(1, weight= 2)
    window.rowconfigure(2, weight= 1)
    window.rowconfigure(3, weight= 1)
    window.rowconfigure(4, weight= 20)

    # Labels
    titulo1 = customtkinter.CTkLabel(window, text="SVD", font=("Microsoft JhengHei", 16))  # title: SVD
    titulo1.grid(row=0, column=1, pady=(10, 20))   # Location of title 1


    titulo2 = customtkinter.CTkLabel(window, text="Image Compressor", font=("Microsoft JhengHei", 14))  # title: Image Compressor
    titulo2.grid(row=1, column=1, sticky="n", padx=5, pady=5)   # Location of title 2

    titulo3= customtkinter.CTkLabel(window, text="Select a scale to compress: ", font=("Microsoft JhengHei", 14)) #title: Select Scals
    titulo3.grid(row=2, column=1, sticky="n", padx=5, pady=5)   # Location of title 3
    # Buttons 

    gray_button= customtkinter.CTkButton(window, text="Gray Scale", font=("Microsoft JhengHei", 16), command=lambda: set_scale_choice(1))
    gray_button.grid(row=3, column=0, sticky="ne", padx=(10, 5), pady=(10, 10))

    rgb_button=customtkinter.CTkButton(window, text="RGB Scale", font=("Microsoft JhengHei", 16), command=lambda: set_scale_choice(2))
    rgb_button.grid(row=3, column=3, sticky="nw", padx=(5, 10), pady=(10, 10))

    # Run the application
    window.mainloop()

if __name__ == "__main__":
    run_gui()
