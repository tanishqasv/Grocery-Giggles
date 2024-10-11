import tkinter
from tkinter import ttk

#created a main window using tkinter library and named its title 
window = tkinter.Tk()
window.title("Grocery Giggle")
window.geometry("800x600") #increased for better spacement 

#created canvas for vertical scrolling  
canvas = tkinter.Canvas(window)
scroll_y = tkinter.Scrollbar(window, orient="vertical", command=canvas.yview)
scroll_y.pack(side="right", fill="y")

#creating a frame inside window to hold the content together
content_frame = tkinter.Frame(canvas)
canvas.configure(yscrollcommand=scroll_y.set)
canvas.pack(side="left", fill=tkinter.BOTH, expand=True)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

#updating the scrolling when the window is resized
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
content_frame.bind("<Configure>", on_configure)

#function to create labeled input fields
def create_label_entry(parent, label_text, row, col):
    label = tkinter.Label(parent, text=label_text, font=("Times", 15))
    label.grid(row=row, column=col)
    entry = tkinter.Entry(parent, font=("Times", 13))
    entry.grid(row=row + 1, column=col)
    return entry

#making first label with welcome title and first and last names
welcome_giggles = tkinter.LabelFrame(content_frame, text="Welcome to Grocery Giggles", font=("Georgia", 20))
welcome_giggles.grid(row=0, column=0, padx=20, pady=10, columnspan=3, sticky="n")

first_name_entry = create_label_entry(welcome_giggles, "First Name", 0, 0)
last_name_entry = create_label_entry(welcome_giggles, "Last Name", 0, 1)

#using combobox for title 
title_label = tkinter.Label(welcome_giggles, text="Title", font=("Times", 15))
title_label.grid(row=0, column=2)
title_combobox = ttk.Combobox(welcome_giggles, values=["", "Mr.", "Mrs.", "Miss", "Dr.", "Prof."], font=("Times", 13))
title_combobox.grid(row=1, column=2)

#using widgets to get grid spacing in 1st label paneling
for widgets in welcome_giggles.winfo_children():
    widgets.grid_configure(padx=15, pady=15)

#dictionary of all the products along with their prices 
products = {
    "Fresh Fruits": {
        "Banana": 100,
        "Orange": 60,
        "Kiwi": 50,
        "Strawberry": 90,
        "Grapes": 70,
    },
    "Dairy Products": {
        "Milk (1 litre)": 40,
        "Curd/Yogurt (500g)": 30,
        "Butter (100g)": 50,
        "Paneer (200g)": 120,
        "Cheese (200g block or slices)": 150,
    },
    "Green Vegetables": {
        "Spinach (Palak, 250g)": 30,
        "Fenugreek Leaves (Methi, 250g)": 40,
        "Coriander Leaves (Dhaniya 100g)": 20,
        "Lettuce (500g)": 120,
        "Avocado (2 whole)": 150,
    },
    "Underground Vegetables": {
        "Potatoes (1Kg)": 40,
        "Onions (1Kg)": 60,
        "Garlic (250g)": 50,
        "Sweet Potatoes (1Kg)": 120,
        "Beetroot (1Kg)": 150,
    },
    "Meat and Seafood": {
        "Venky's Chicken (1Kg)": 300,
        "Licious's Mutton (1Kg)": 700,
        "Zappfresh's Chicken Legs(500g)": 250,
        "Rohu Fish (1Kg)": 420,
        "Freshwater Prawns (1Kg)": 600,
    },
    "Feminine Hygiene": {
        "Sanitary Napkins (Sofy, Stayfree, Whisper)": 500,
        "Tampons (Playtex, Tampax)": 200,
        "Menstrual Cups (Sirona, Boondh)": 350,
        "pH Balanced Intimate Wash (100-250 ml)": 300,
        "Himalaya Fresh Start Deodorant (100 ml)": 175,
        "Nivea Whitening Deodorant (150 ml)": 250,
    },
    "Bakery and Bread": {
        "White Bread (400g Loaf)": 50,
        "Whole Wheat Bread (400g Loaf)": 40,
        "Buns (pack of 6)": 60,
        "Croissants (pack of 12)": 120,
        "Multigrain Wheat Bread (400g Loaf)": 50,
    },
    "Toiletries": {
        "Colgate Toothpaste Charcoal (250g)": 150,
        "Dove Silk Soap Rosewater (125g)": 60,
        "Pantene Hairstrength Shampoo n' Conditioner (300ml)": 250,
        "Yardley Men's Deodorant (pack of 2)": 120,
        "Yardley Women's Deodorant (pack of 2)": 120,
    },
    "Condiments and Sauces": {
        "Tomato Ketchup (500g)": 150,
        "Soy Sauce (250ml)": 120,
        "Olive Oil (500ml)": 250,
        "Vinegar (500ml)": 80,
        "Mustard Sauce (250g)": 120,
    }
}

#variables to hold all the selections
vars_dict = {}

#function to calculate total price for selected items and update the grand total
def calculate_total():
    total_amount = 0
    selected_items = []
    
    for category, items in products.items():
        for item, price in items.items():
            if vars_dict[item].get() == 1:
                total_amount += price
                selected_items.append((item, price))

    total_selected_label.config(text=f"Total Amount: {total_amount} INR")
    total_selected_count_label.config(text=f"Total Selected Items: {len(selected_items)}")
    return total_amount, selected_items

#function to generate receipt
def generate_receipt():
    total_amount, selected_items = calculate_total()
    gst = total_amount * 0.05  # Example GST calculation at 5%
    tax = total_amount * 0.02   # Example Tax calculation at 2%
    final_amount = total_amount + gst + tax
    
    #getting user details
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    title = title_combobox.get()

    #receipt format given below
    receipt_text = f"           Grocery Giggle Receipt\n"
    receipt_text += f"--------------------------------------------------\n"
    receipt_text += f"Name: {title} {first_name} {last_name}\n\n"
    receipt_text += "Items Purchased:\n"
    for item, price in selected_items:
        receipt_text += f"- {item}: {price} INR\n"
    receipt_text += f"\nTotal Amount: {total_amount} INR\n"
    receipt_text += f"GST (5%): {gst:.2f} INR\n"
    receipt_text += f"Tax (2%): {tax:.2f} INR\n"
    receipt_text += f"Final Amount to Pay: {final_amount:.2f} INR\n"
    receipt_text += "--------------------------------------------------\n"
    receipt_text += "Thank you for shopping with Grocery Giggles!\n"
    
    #making a receipt display box
    receipt_display.delete(1.0, tkinter.END)  # Clear previous text
    receipt_display.insert(tkinter.END, receipt_text)

    #now, using the user information to save the receipt to a text file
    with open("receipt.txt", "w") as f:
        f.write(receipt_text)

#creating sections for each product category in a grid format
row = 1
col = 0
for category, items in products.items():
    label_frame = tkinter.LabelFrame(content_frame, text=category, font=("Georgia", 19), width=120)  
    label_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")  
    content_frame.grid_columnconfigure(col, weight=1)  

    for item_row, (item, price) in enumerate(items.items()):
        vars_dict[item] = tkinter.IntVar()
        checkbox = tkinter.Checkbutton(label_frame, text=f"{item} - {price} INR", variable=vars_dict[item], command=calculate_total)
        checkbox.grid(row=item_row, sticky="w")

    col += 1
    if col >= 3:  #move to the next row after 3 columns
        col = 0
        row += 1

#creating a new frame for the total selection labels
total_frame = tkinter.LabelFrame(content_frame, text="Total Items", font=("Georgia", 20))
total_frame.grid(row=4, column=0, padx=20, pady=10, columnspan=3, sticky="nsew")

#total selection label frame
total_selected_label = tkinter.Label(total_frame, text="Total Amount: 0 INR", font=("Times", 15))
total_selected_label.grid(row=0, column=0, padx=20, pady=5)

total_selected_count_label = tkinter.Label(total_frame, text="Total Selected Items: 0", font=("Times", 15))
total_selected_count_label.grid(row=1, column=0, padx=20, pady=5)

#adding a button to generate the receipt
generate_receipt_button = tkinter.Button(window, text="Generate Receipt", command=generate_receipt, font=("Times", 15))
generate_receipt_button.pack(pady=10)

#creating a frame for the receipt display
receipt_frame = tkinter.LabelFrame(content_frame, text="Receipt", font=("Georgia", 20))
receipt_frame.grid(row=5, column=0, padx=20, pady=10, columnspan=3, sticky="nsew")

#adding a text widget to display the receipt with increased size
receipt_display = tkinter.Text(receipt_frame, width=50, height=20, font=("Courier New", 10), bg="#D3D3D3")  
#using color code for realistic receipt 
receipt_display.pack(padx=10, pady=10)

#and now finally, finishing mainloop
window.mainloop()
