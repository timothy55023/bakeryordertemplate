import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

def save_template():
    """ Save the template text from user input. """
    global template_text
    template_text = template_entry.get("1.0", tk.END).strip()
    messagebox.showinfo("Template Saved", "Your template has been saved successfully!")

def generate_message():
    """ Generate the message using the template and the fields. """
    try:
        message = template_text.format(customer_entry.get(), time_entry.get(), details_entry.get())
        output_area.config(state=tk.NORMAL)
        output_area.delete('1.0', tk.END)
        output_area.insert(tk.END, message)
        output_area.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

app = tk.Tk()
app.title("Bakery Order Notification Template")

# Initialize template text
template_text = ""

# UI Elements for template entry
template_label = tk.Label(app, text="Enter your message template (use {} for fields):")
template_label.pack(pady=(10, 0))

template_entry = scrolledtext.ScrolledText(app, height=5, width=50)
template_entry.pack(pady=(5, 10))

save_button = tk.Button(app, text="Save Template", command=save_template)
save_button.pack(pady=(0, 10))

# UI Elements for input fields
field_label = tk.Label(app, text="Enter the details for your message:")
field_label.pack(pady=(10, 2))

customer_entry = tk.Entry(app)
customer_entry.pack(pady=(0, 5))

time_entry = tk.Entry(app)
time_entry.pack(pady=(0, 5))

details_entry = tk.Entry(app)
details_entry.pack(pady=(0, 5))

generate_button = tk.Button(app, text="Generate Message", command=generate_message)
generate_button.pack(pady=(10, 5))

output_area = scrolledtext.ScrolledText(app, state=tk.DISABLED, height=5, width=50)
output_area.pack(pady=(5, 10))

app.mainloop()
