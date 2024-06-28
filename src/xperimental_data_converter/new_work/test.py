import tkinter as tk

def save_value():
    slider_value = scale.get()  # Get the slider value
    print(f"Slider value as integer: {slider_value}")

root = tk.Tk()
root.title("Slider Example")
root.geometry("300x200")

# Create a Scale widget
scale = tk.Scale(root, from_=0, to=100, orient='horizontal')
scale.pack(pady=20)

# Create a Button to save the slider value
save_button = tk.Button(root, text="Save Value", command=save_value)
save_button.pack(pady=20)

root.mainloop()
