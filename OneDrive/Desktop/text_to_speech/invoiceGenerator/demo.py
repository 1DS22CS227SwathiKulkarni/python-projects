from tkinter import *
from fpdf import FPDF
from datetime import date

window = Tk()
window.title("Invoice Generator")

groceries = {
    "Biscuits": 30.00,
    "Shampoo": 200.00,
    "Soap": 100.00,
    "Toothpaste": 50.00,
    "Milk": 20.00,
    "Bread": 50.00,
}
invoice_items = []

def add_grocery():
    selected_grocery = grocery_list_box.get(ANCHOR)
    quantity = int(quantity_entry.get())
    price = groceries[selected_grocery]
    item_total = price * quantity
    invoice_items.append((selected_grocery, quantity, item_total))
    total_amount_entry.delete(0, END) 
    total_amount_entry.insert(END, str(calculate_total()))
    update_invoice_text()

def calculate_total():
    total = 0.0
    for item in invoice_items:
        total += item[2]
    return total

def update_invoice_text():
    invoice_text.delete(1.0, END) #line.column
    for item in invoice_items:
        invoice_text.insert(END, f"Gorcery: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")

def generate_invoice():
    customer_name = customer_entry.get()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 10, text="Invoice", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.cell(0,10,text="Customer: "+customer_name, new_x="LMARGIN", new_y="NEXT", align="L")
    pdf.cell(0, 10, text="Date: "+ str(date.today()), new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0,10,text="", new_x="LMARGIN", new_y="NEXT")

    for item in invoice_items:
        grocery_name, quantity, item_total = item
        pdf.cell(0,10, text=f"Gorcery: {grocery_name}, Quantity:{quantity}, Amount:{item_total}", new_x="LMARGIN", new_y="NEXT")

    pdf.cell(0, 10, "Total Amount:"+ str(calculate_total()), new_x="LMARGIN", new_y="NEXT")
    pdf.output(f"{customer_name}.pdf")

grocery_label = Label(window, text="Grocery: ")
grocery_label.pack()

grocery_list_box = Listbox(window, selectmode=SINGLE)
for grocery in groceries:
    grocery_list_box.insert(END, grocery)
grocery_list_box.pack()

quantity_label = Label(window, text="Quantity")
quantity_label.pack()
quantity_entry = Entry(window)
quantity_entry.pack()

add_button = Button(window, text="Add Grocery", command=add_grocery)
add_button.pack()

total_amount_label = Label(window, text="Total Amount")
total_amount_label.pack()

total_amount_entry = Entry(window)
total_amount_entry.pack()

customer_label = Label(window, text="Customer Name")
customer_label.pack()
customer_entry = Entry(window)
customer_entry.pack()

generate_button = Button(window, text="Generate Invoice", command=generate_invoice)
generate_button.pack()

invoice_text = Text(window, height=10, width=50)
invoice_text.pack()

window.mainloop()
