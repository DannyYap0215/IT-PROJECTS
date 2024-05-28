from customtkinter import *
import expenses_piechart
import income_piechart
import usage_barchart

def open_insight_window(expenses_piechart, income_piechart):
    def close_existing_windows():
        # Destroy any existing windows
        for widget in insight_window.winfo_children():
            widget.destroy()
    def on_button_click():
        # Reduce the topmost attribute when a button is clicked
        insight_window.wm_attributes("-topmost", False)
    
    insight_window = CTkToplevel()
    insight_window.title("Insight")
    insight_window.geometry("400x300")
    insight_window.wm_attributes("-topmost",True)

    def open_expenses_piechart():
        expenses_piechart.open_expenses_piechart_window()

    def open_income_piechart():
        income_piechart.open_income_piechart_window()

    def open_usage_barchart():
        usage_barchart.open_usage_barchart_window()

    expenses_button = CTkButton(insight_window, text="Expenses",command=open_expenses_piechart)
    expenses_button.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    income_button = CTkButton(insight_window, text="Income",command=open_income_piechart)
    income_button.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    
    usage_button = CTkButton(insight_window, text="Usage of Budget",command=open_usage_barchart)
    usage_button.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    #check for m1 click on the button if so it goes through the function o_b_c()
    expenses_button.bind("<Button-1>", lambda event: on_button_click())
    income_button.bind("<Button-1>", lambda event: on_button_click())
    usage_button.bind("<Button-1>", lambda event: on_button_click())

    insight_window.mainloop() 