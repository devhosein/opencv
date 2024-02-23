import customtkinter as tk

tk.set_appearance_mode("Dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.geometry("500x350")

def login():
    print("test")

frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


label = tk.CTkLabel(master=frame, text= "login system", font= ("Roboto", 24) )
label.pack(pady= 12, padx=10)



root.mainloop()


