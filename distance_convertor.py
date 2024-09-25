import tkinter as tk

main_window = tk.Tk()

top_frame = tk.Frame(main_window)
bottom_frame = tk.Frame(main_window)

prompt_label = tk.Label(top_frame, text='Enter a distance in kilometers:')
kilo_entry = tk.Entry(top_frame, width=10)

prompt_label.pack(side='left')
kilo_entry.pack(side='left')

result_label = tk.Label(main_window, text="")
result_label.pack()

def convert():
    kilo = float(kilo_entry.get())
    miles = kilo * 0.6214
    result_label.config(text=f"{kilo} kilometers = {miles:.2f} miles")
    

calc_button = tk.Button(bottom_frame, text='Convert', command=convert)
quit_button = tk.Button(bottom_frame, text='Quit', command=main_window.destroy)

calc_button.pack(side='left')
quit_button.pack(side='left')

top_frame.pack()
bottom_frame.pack()

tk.mainloop()

