from tkinter import *
from tkinter import ttk
import mysql.connector

def saved_invoices_widgets_to_frame(frame):
    root = frame
    style = ttk.Style()
    style.theme_use('clam')

    frame1 = LabelFrame(root, text="Search Invoice", padx=15, pady=15)
    frame1.grid(row=0, column=0, sticky=W, columnspan=2)

    tree_frame = Frame(root)
    tree_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=6)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.grid(row=0, column=6, sticky='ns')

    tree = ttk.Treeview(tree_frame, columns=("c1", "c2", "c3", "c4", "c5"), show='headings', height=10,
                        yscrollcommand=tree_scroll.set)
    tree.grid(row=0, column=0, columnspan=5, sticky=W)

    tree_scroll.config(command=tree.yview)

    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Product Name")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Colour")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Size")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Quantity")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Rate")

    def show_details():
        bill_id = e_1.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hrjagtap@1",
            database="inventory"
        )

        cursor = mydb.cursor()

        query = "SELECT product_name, colour, size, quantity, rate FROM item WHERE bill_id = %s"
        cursor.execute(query, (bill_id,))

        tree.delete(*tree.get_children())

        rows = cursor.fetchall()

        for row in rows:
            tree.insert("", "end", values=row)

        cursor.close()
        mydb.close()

    bill_no_label = Label(frame1, text="Bill No.:")
    bill_no_label.grid(row=0, column=0)
    e_1 = Entry(frame1, width=40)
    e_1.grid(row=0, column=1, padx=20, pady=10)

    show_details = Button(frame1, text="Show Details", padx=30, pady=2, command=show_details)
    show_details.grid(row=1, column=1)

    frame2 = LabelFrame(root, text="Edit Invoice", padx=15, pady=15)
    frame2.grid(row=3, column=0, sticky=W)
    edit_invoice = Button(frame2, text="Edit", padx=60, pady=10, bd=6, command=lambda: frame3.grid(row=3, column=1, sticky=W))
    edit_invoice.grid(row=0, column=0, columnspan=1)

    frame3 = LabelFrame(root, padx=15, pady=15)
    delete_item = Button(frame3, text="Delete Item", padx=60, pady=10, bd=6)
    delete_item.grid(row=0, column=0, columnspan=1)
    add_item = Button(frame3, text="Add Item", padx=60, pady=10, bd=6)
    add_item.grid(row=1, column=0, columnspan=1)

    frame4 = LabelFrame(root, text="Reprint Bill", padx=15, pady=15)
    frame4.grid(row=3, column=5, sticky=W)
    print_bill = Button(frame4, text="Print Bill", padx=60, pady=10, bd=6)
    print_bill.grid(row=1, column=0, columnspan=1)