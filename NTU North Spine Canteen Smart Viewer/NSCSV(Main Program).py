#Author: Song Yu In colaboration with: Tan Wen Kai NTU SCSE Computer Science Yr1 2019
######################################Modules Required###########################################
from tkinter import *
from tkinter import messagebox
import pickle
import datetime
import calendar
######################################Modules Required###########################################

######################################Function Definitions#######################################
#About:....
def popu():
  pass_window = Toplevel()
  pass_window.title("About")

  #positioning
  x_roposition = root.winfo_x()
  y_roposition = root.winfo_y()
  pass_window.geometry("%dx%d+%d+%d" % (400, 240, x_roposition+300, y_roposition+200))
  pass_window.maxsize(400,240)
  pass_window.minsize(400,240)

  #Setting Background:
  psphoto = PhotoImage(file = "time.png")
  psbg_label = Label(pass_window, image = psphoto)
  psbg_label.image = psphoto
  psbg_label.place(x=0, y=0, relwidth=1, relheight=1)

  #Create a label text to display message:
  display_msg = Label(pass_window, text ="\nAuthor: \n\nSong Yu\n\n In colaboration with: \n\nTan Wen Kai\n\nNTU SCSE Computer Science Yr1 \n\n2019", font=('Arial', 13, 'bold'), fg = "Deepskyblue2", bg = "white")
  display_msg.pack()

#Function to display current date and time:
def dtime():
  # get the current date and time from the system running:
  time_now = datetime.datetime.now().strftime('%A  %d / %m / %Y  %H:%M:%S ')
  date_time.config(text=time_now)
  # update every 200 ms:
  date_time.after(200, dtime)

#create a popup window for viewing current menu. Make it a function for the button to trigger
def menuwindow():
    #make use of the menu\operating time dictionary
    global system
    global time_system
    menuwindow = Toplevel()

    #positioning
    x_roposition = root.winfo_x()
    y_roposition = root.winfo_y()
    menuwindow.title("Stalls")  
    menuwindow.geometry("%dx%d+%d+%d" % (550, 600, x_roposition+60, y_roposition+55))
    #menuwindow.tkraise(root)
    menuwindow.maxsize(550,600)
    menuwindow.minsize(550,600)

    #Limit window numbers:
    View_menu_button.config(state = "disable")
    
    def quit_win():
        menuwindow.destroy()
        View_menu_button.config(state='normal')

    #Setting Background:
    mbgphoto = PhotoImage(file = "food3.png")
    mbg_label = Label(menuwindow, image = mbgphoto)
    mbg_label.image = mbgphoto
    mbg_label.place(x=0, y=0, relwidth=1, relheight=1)
       
    #Display welcome message
    welcome = Label(menuwindow, font=('Times', 16, 'bold'), fg = "snow", bg = "black")
    welcome.pack(fill = X)
    if hour < 12:
      welcome.config(text = "Good morning!\nPlease use the drop down menu to choose a stall!")
    elif 12<= hour <16:
      welcome.config(text = "Good afternoon!\nPlease use the drop down menu to choose a stall!")
    elif 16<= hour <24:
      welcome.config(text = "Good evening!\nPlease use the drop down menu to choose a stall!")

    #Create a text box for displaying menu:
    #Create an empty text box first, then insert dish-price pairs line by line since we are using dictionarys
    menu_text = Text(menuwindow, height = 15, width = 70, fg= "snow", background='peachpuff4', font='helvetica 13 bold')
    menu_text.pack() 
    #Setting initial notification:
    menu_text.insert(INSERT, "\n\n\n\t         Welcome to NS smart canteen viewer!\n\tPlease choose from the drop down menu button!")
    menu_text.config(state = 'disabled')

    #The function executed when click the button to view dishes & prices
    def view_dish():
      menu_text.config(state = 'normal')
      menu_text.delete("1.0", END)     
      for stall in system:
        if stall == stall_n.get():         
          dish = list(system[stall].keys())
          price = list(system[stall].values())
                   
          for d,p in zip(dish, price):
            menu_items = "Dish name:   {} \t\t\t\t\t Price: {} SG$\n".format(d,p)
            menu_text.insert(INSERT, menu_items)
          menu_text.config(state = 'disabled')
      else:
          #if no option is chosen, display an error message:
          menu_text.insert(INSERT, "\n\n\n\n\n\n\t \tYou have not chosen a stall yet! \n\t\t\tTo view menus, \n\tplease choose from the drop down menu button!")
          menu_text.config(state = 'disabled')
           
    #create a dropdown list for user to choose a stall
    stall_n = StringVar()
    stall_n.set("Click here to select a stall")
    dropdown = OptionMenu(menuwindow, stall_n, *system)
    dropdown.config(font = ("Arial",16, "bold"), bg = "peachpuff")
    dropdown['menu'].config(font=('times',16, "bold"), fg = "black", bg='snow')
    dropdown.pack(padx = 80, fill = X)

    #create a button to confirm the selection:
    conf = Button(menuwindow, width = 12, text = "Confirm", font=('Arial', 16, 'bold'), bg = "tomato", command = view_dish)
    conf.pack(padx = 80, pady = 20, fill = X)

    #The function executed when click the button to view operating time
    def view_op_hr():      
      menu_text.config(state = 'normal')
      for stall in time_system:
        if stall == stall_n.get():           
          operate_time = time_system[stall]
          time_info = "Stall:    {}  \nOpen {}".format(stall,operate_time)
          messagebox.showinfo("Operating Hours", time_info)
          break
      else:
        #if no option is chosen, display an error message:
        menu_text.delete("1.0", END)  
        menu_text.insert(INSERT, "\n\n\n\n\n\n\t \tYou have not chosen a stall yet! \n\t  \t    To view operating hours, \n\tplease choose from the drop down menu button!")
        menu_text.config(state = 'disabled')

    #create a button to view the operating hours
    op_hour = Button(menuwindow, text = "View Operating Hours", font=('Arial', 16, 'bold'), bg = "deepskyblue2", command = view_op_hr)
    op_hour.pack(padx = 80, fill = X)

    #Close all the stalls
    if hour < 8 or hour > 19:
          menu_text.config(state = 'normal')
          dropdown.configure(state = "disable")
          op_hour.configure(state = "disable")
          conf.configure(state = "disable")
          menu_text.delete("1.0", END)
          menu_text.insert(INSERT, "\n\n\n\n\n\n         Sorry, all stalls are closed now. Please come tomorrow!")
          menu_text.config(state = 'disabled')
    #Bind new protocal for the quit button to limit window numbers:
    menuwindow.protocol("WM_DELETE_WINDOW", quit_win)

#create a popup window for calculating estimated waiting time. Make it a function for the button to trigger
def cal_wait_time():
    #make use of the menu\operating time dictionary
    global system

    wait_time_menu = Toplevel()
    wait_time_menu.title("Wait Time Calculator")

    #positioning
    x_roposition = root.winfo_x()
    y_roposition = root.winfo_y()
    wait_time_menu.geometry("%dx%d+%d+%d" % (550, 380, x_roposition+60, y_roposition+200))

    wait_time_menu.maxsize(550,380)
    wait_time_menu.minsize(550,380)

    #Setting Background:
    wtphoto = PhotoImage(file = "time.png")
    wtbg_label = Label(wait_time_menu, image = wtphoto)
    wtbg_label.image = wtphoto
    wtbg_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Limit window numbers:
    Wait_button.config(state = "disable")
    
    def quit_win():
        wait_time_menu.destroy()
        Wait_button.config(state='normal')

    #Display welcome message
    welcome = Label(wait_time_menu, font=('Arial', 16, 'bold'), fg = "dodgerblue", bg = "white")
    welcome.pack(fill = X, pady = 20)
    if hour < 12:
      welcome.config(text = "Good morning!\nPlease choose a stall ↓ to calculate waiting time!")
    elif 12<= hour <16:
      welcome.config(text = "Good afternoon!\nPlease choose a stall ↓ to calculate waiting time!")
    elif 16<= hour <24:
      welcome.config(text = "Good evening!\nPlease choose a stall ↓ to calculate waiting time!")
  
    #create a dropdown list for user to choose a stall
    stall_n = StringVar()
    stall_n.set("Click here to select a stall")
    dropdown = OptionMenu(wait_time_menu, stall_n, *system)
    dropdown.config(font = ("Arial",16, "bold"), fg = "white", bg = "dodgerblue")
    dropdown['menu'].config(font=('times',16, "bold"), fg = "black", bg='white')
    dropdown.pack(padx = 80, fill = X)

    #Display instruction 1 message
    inst1 = Label(wait_time_menu, text = "Enter the number of people in front:", \
    font=('Arial', 16, 'bold'),width = 30, fg = "dodgerblue", bg = "white")
    inst1.pack()
    #Create a free entry for user to enter the number of people in front
    num_of_people = StringVar()
    time_needed = StringVar()
    num_entry = Entry(wait_time_menu, width = 64, textvariable = num_of_people,bd = 3)
    num_entry.pack(ipady =5)
    num_entry.insert(END, "Please enter a POSITIVE INTEGER here")
    num_entry.focus()
    
    #The function executed when click the button to calculate waiting time
    def calculation():
      #check if the dropdown menu is used:
      input = stall_n.get()
      if input == "Click here to select a stall":
        time_needed.set("You haven't chosen a stall yet.\n Please use the drop down menu above.")
      else:
        for stall in system:
          if stall == stall_n.get():
            if stall in ("McDonald's","Noodle_Stall","Indian_Stall","Chicken_Rice"):         
              try:
                pax = int(num_of_people.get())
                if pax > 30:
                  time_needed.set("Too many people.\n We don't recommend you to wait here.")
                elif pax == 0:
                  time_needed.set("There is currently no people in the queue.")
                elif pax <0:
                  time_needed.set("Invalid input.\n Please enter positive integers!")
                elif 9 <= hour <= 11:
                  wait_time = 3
                  time_needed.set(pax * wait_time)                 
                elif 12 <= hour <= 14:
                  wait_time = 4
                  time_needed.set(pax * wait_time)
                elif 17 <= hour <= 19:
                  wait_time = 3
                  time_needed.set(pax * wait_time)
                else:
                  wait_time = 2
                  time_needed.set(pax * wait_time)
              except:
                time_needed.set("Please key in POSITIVE INTEGERS")
                pass
            elif stall =="KFC":
              try:
                pax = int(num_of_people.get())
                if pax > 30:
                  time_needed.set("Too many people.\n We don't recommend you to wait here.")
                elif pax == 0:
                  time_needed.set("There is currently no people in the queue.")
                elif pax <0:
                  time_needed.set("Invalid input.\n Please enter positive integers!")
                elif 9 <= hour <= 11:
                  wait_time = 5
                  time_needed.set(pax * wait_time)
                elif 12 <= hour <= 14:
                  wait_time = 6
                  time_needed.set(pax * wait_time)                  
                elif 17 <= hour <= 19:
                  wait_time = 6
                  time_needed.set(pax * wait_time)
                else:
                  wait_time = 5
                  time_needed.set(pax * wait_time)
              except:
                time_needed.set("Please key in POSITIVE INTEGERS")
                pass
    #Bind with the "Enter" key on key board:
    num_entry.bind('<Return>', (lambda event: calculation()))  

    #Create a button which can trigger the calculation            
    cal_button = Button(wait_time_menu, text = "Calculate", font=('Arial', 16, 'bold'), bg = "palegreen", command = calculation)
    cal_button.pack(padx = 80, fill = X)
    #Display instruction 2 message
    inst2 = Label(wait_time_menu, text = "The estimated waiting time is:", \
    font=('Arial', 16, 'bold'),width = 30, fg = "dodgerblue", bg = "white")
    inst2.pack()
    #Display the time:
    display_time = Label(wait_time_menu, textvariable = time_needed, font=('Arial', 16, 'bold'), width = 35, fg = "orangered", bg = "white")
    display_time.pack()
    #Display instruction 2 message
    inst3 = Label(wait_time_menu, text = "Minutes", \
    font=('Arial', 16, 'bold'),width = 30, fg = "dodgerblue", bg = "white")
    inst3.pack()

    #Bind new protocal for the quit button to limit window numbers:
    wait_time_menu.protocol("WM_DELETE_WINDOW", quit_win)

#create a popup window for Browsing predefined piclke files. Make it a function for the button to trigger
def browse_file():
    browse_window = Toplevel()
    browse_window.title("Pickle File Browser")

    #positioning
    x_roposition = root.winfo_x()
    y_roposition = root.winfo_y()
    browse_window.geometry("%dx%d+%d+%d" % (450, 300, x_roposition+290, y_roposition+200))
    browse_window.maxsize(450,300)
    browse_window.minsize(450,300)

    #Setting Background:
    bphoto = PhotoImage(file = "time.png")
    bg_label = Label(browse_window, image = bphoto)
    bg_label.image = bphoto
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    #Label text for instruction
    instr1 = Label(browse_window, text = "Step 1: Choose the file type you want to open:",\
    font=('Arial', 13, 'bold'), fg = "dodgerblue", bg = "white")
    instr1.pack(fill = X, pady = 5)

    #create a dropdown list for user to choose the type of file browsing.
    file_type_var = StringVar()
    file_type_var.set("Click to select file type")
    dropdown = OptionMenu(browse_window, file_type_var, "Menu file", "Operating time file")
    dropdown.config(font = ("Arial",13, "bold"), bg = "yellow")
    dropdown['menu'].config(font=('times',12, "bold"), fg = "black", bg='white')
    dropdown.pack(padx = 50, fill = X)

    #Label text for instruction
    instr2 = Label(browse_window, text = "Step 2: Key in the file name you want to open:\n\n Note that you need to add suffix! (e.g. '.pkl')",\
      font=('Arial', 13, 'bold'), fg = "dodgerblue", bg = "white")
    instr2.pack(fill = X, pady = 5)

    #Create a free entry for user to enter the number of people in front
    file_name_var = StringVar()
    message_var = StringVar()
    name_entry = Entry(browse_window, width = 57, textvariable = file_name_var,bd = 2)
    name_entry.pack(ipady = 5)
    name_entry.focus()

    #Function excuted when click the open button or press the "Enter" key:
    def open_file():
      
        if file_type_var.get() == "Click to select file type":
          message_var.set("Please choose file type first!")
        elif file_type_var.get() == "Menu file":
            file_name = file_name_var.get()
            if file_name == "":
              message_var.set("Please enter the file name with suffix first.")
            elif file_name != "General_menu.pkl" and file_name != "Breakfast.pkl":
              message_var.set("File not found, please check your input and suffix.\nNote that you can only open the operating time file. \n i.e. The file name should be either \n'Breakfast.pkl' or 'General_menu.pkl'.")
            else:
              med_file = open(file_name,"rb")
              in_file = pickle.load(med_file)
              if file_name == "General_menu.pkl":
                system = in_file
              elif file_name == "Breakfast.pkl":
                Breakfast = in_file
              messagebox.showinfo("Congratulations!", "File '"+file_name+"' loaded successfully!")
              browse_window.destroy()
                      
        elif file_type_var.get() == "Operating time file":
            file_name = file_name_var.get()
            if file_name == "":
              message_var.set("Please enter the file name with suffix first.")
            elif file_name != "Operate_time.pkl":
              message_var.set("File not found, please check your input and suffix.\nNote that you can only open the operating time file. \n i.e. The file name should be 'Operate_time.pkl'.")
            else:
              med_file = open(file_name,"rb")
              in_file = pickle.load(med_file)
              time_system = in_file
              messagebox.showinfo("Congratulations!", "File '"+file_name+"' loaded successfully!") 
              browse_window.destroy()            

    #Create a button to start browsing the file:
    op_button = Button(browse_window, text = "Open", font=('Arial', 12, 'bold'), fg = "palegreen3", bg = "snow", command = open_file)
    op_button.pack(padx = 50, pady = 8, fill = X)
    
    #Bind with the "Enter" key on key board:
    name_entry.bind('<Return>', (lambda event: open_file()))

    #Create a label text to display message:
    message_var.set("Please kindly follow the instructions above :)")
    display_msg = Label(browse_window, textvariable = message_var, font=('Arial', 13, 'bold'), fg = "orangered", bg = "white")
    display_msg.pack()

#create a popup window for saving dictionaries to file. Make it a function for the button to trigger
def save_2_file():
  save_window = Toplevel()
  save_window.title("Save To Pickle File")

  #positioning
  x_roposition = root.winfo_x()
  y_roposition = root.winfo_y()
  save_window.geometry("%dx%d+%d+%d" % (400, 330, x_roposition+300, y_roposition+200))
  save_window.maxsize(400,330)
  save_window.minsize(400,330)

  #Setting Background:
  sphoto = PhotoImage(file = "time.png")
  sbg_label = Label(save_window, image = sphoto)
  sbg_label.image = sphoto
  sbg_label.place(x=0, y=0, relwidth=1, relheight=1)

  #Display instruction 1 message
  inst1 = Label(save_window, text = "Step 1 - Choose the file type: ", \
  font=('Arial', 16, 'bold'),width = 30, fg = "dodgerblue", bg = "white")
  inst1.pack(pady = 16)

  #create a dropdown list for user to choose the type of file browsing.
  file_type_var = StringVar()
  message_var = StringVar()
  file_type_var.set("Click to select file type")
  dropdown = OptionMenu(save_window, file_type_var, "Menu file", "Operating time file")
  dropdown.config(font = ("Arial",14, "bold"), fg = "dodgerblue", bg = "yellow")
  dropdown['menu'].config(font=('times',12, "bold"), fg = "black", bg='white')
  dropdown.pack(padx = 50, fill = X)

  #Display instruction 2 message
  inst2 = Label(save_window, text = "Step 2 - Enter the file name: \n(without suffix)", \
  font=('Arial', 16, 'bold'),width = 30, fg = "dodgerblue", bg = "white")
  inst2.pack(pady = 16)

  #Create a free entry for user to enter the number of people in front
  file_name_var = StringVar()
  fname_entry = Entry(save_window, width = 50, textvariable = file_name_var, bd = 3)
  fname_entry.pack(ipady =5)
  fname_entry.focus()
  
  def save_execute():
    if file_type_var.get() == "Click to select file type":
          message_var.set("Please choose file type first!")
    elif file_type_var.get() == "Menu file":
      try:
        save_name = file_name_var.get()+"_menu.pkl"
        if file_name_var.get() == "":
          message_var.set("Please enter the file name first.")
        else:
            med_file = open(save_name,"wb")
            pickle.dump(system, med_file)
            med_file.close()
            messagebox.showinfo("Congratulations!", "File '"+save_name+"' saved successfully!")
      except:
        messagebox.showerror("Error", "Invalid file name. Try again")

    elif file_type_var.get() == "Operating time file":
      try:
        save_name = file_name_var.get()+"_OperatingHours.pkl"
        if file_name_var.get() == "":
          message_var.set("Please enter the file name first.")
        else:
            med_file = open(save_name,"wb")
            pickle.dump(time_system, med_file)
            med_file.close()
            messagebox.showinfo("Congratulations!", "File '"+save_name+"' saved successfully!")
      except:
        messagebox.showerror("Error", "Invalid file name. Try again")

  #Create a CONFIRM button:
  conf_button = Button(save_window, text = "CONFIRM", font=('Arial', 16, 'bold'), fg = "red", bg = "snow", command = save_execute)
  conf_button.pack(padx = 48, pady = 10, fill = X)

  #Create a label text to display message:
  message_var.set("Please kindly follow the instructions above :)")
  display_msg = Label(save_window, textvariable = message_var, font=('Arial', 13, 'bold'), fg = "orangered", bg = "white")
  display_msg.pack()

#create a popup window for editing stall menu. Make it a function for the button to trigger
def menu_editor():
  global system

  menu_editor_window = Toplevel()
  menu_editor_window.title("Menu Information Editor")

  #positioning
  x_roposition = root.winfo_x()
  y_roposition = root.winfo_y()
  menu_editor_window.geometry("%dx%d+%d+%d" % (500, 460, x_roposition+270, y_roposition+150))
  menu_editor_window.maxsize(500,460)
  menu_editor_window.minsize(500,460)

  #Setting Background:
  mewphoto = PhotoImage(file = "time.png")
  mewbg_label = Label(menu_editor_window, image = mewphoto)
  mewbg_label.image = mewphoto
  mewbg_label.place(x=0, y=0, relwidth=1, relheight=1)
  
  #prompt a message box for insturction:
  messagebox.showwarning("Note","To add dishes, kindly enter the dish name and price, then click 'ADD/UPDATE'.\n\nTo delete a dish, enter the dish name only and left the price entry unchanged, then click 'DELETE'.")

  #Label text for instruction
  instr1 = Label(menu_editor_window, text = "Choose the stall you want to edit:",\
  font=('Arial', 14, 'bold'), fg = "dodgerblue", bg = "white")
  instr1.pack(fill = X, pady = 20)

  #create a dropdown list for user to choose a stall
  stall_n = StringVar()
  stall_n.set("Click here to select a stall: ↓")
  dropdown = OptionMenu(menu_editor_window, stall_n, *system)
  dropdown.config(font = ("Arial",15), fg = "orangered2", bg = "snow")
  dropdown['menu'].config(font=('times',15, "bold"), fg = "black", bg='white')
  dropdown.pack(padx = 100, fill = X)

  #Label text for instruction
  instr2 = Label(menu_editor_window, text = "Enter the dish name here (Case sensitive!):",\
  font=('Arial', 14, 'bold'), fg = "dodgerblue", bg = "white")
  instr2.pack(fill = X, pady = 10)

  #Create a free entry for user to enter the number of people in front
  dish_name_var = StringVar()
  dish_entry = Entry(menu_editor_window, width = 65, textvariable = dish_name_var,bd = 3)
  dish_entry.pack(ipady = 5)
  dish_entry.insert(END, 'Enter the dish name')
  dish_entry.focus()

  #Label text for instruction
  instr3 = Label(menu_editor_window, text = "Enter the dish price here:",\
  font=('Arial', 14, 'bold'), fg = "dodgerblue", bg = "white")
  instr3.pack(fill = X, pady = 10)

  #Create a free entry for user to enter the number of people in front
  price_var = DoubleVar()
  price_entry = Entry(menu_editor_window, width = 65, textvariable = price_var,bd = 3)
  price_entry.pack(ipady = 5)
  price_entry.insert(END, ' (Enter a float number)')

  #Define a function to add/update dish and price:
  def add_or_update_dish ():
    try:
      if stall_n.get() == "Click here to select a stall: ↓":
        messagebox.showwarning("Warning", "You haven't chosen a stall yet!")
      else:
        dish_name_str = dish_name_var.get()
        price_float = price_var.get()
        price_str = str(price_float)
        if price_float <= 0 or price_float >= 200:
          messagebox.showwarning("Warning", "You set a weried price. Pleace be serious.")
        else:
          for stall in system:
            if stall == stall_n.get():
              system[stall].update({dish_name_str:price_str})
              messagebox.showinfo("Congratulations!","You have added/updated the dish: "+dish_name_str+" with price: "+price_str+" SG$ in the stall: "+stall)             
    except:
      messagebox.showwarning("Warning", "Invalid input. \nPlease check and re-enter the price.")
      pass

  #Create an ADD button:
  add_button = Button(menu_editor_window, text = "ADD/UPDATE", font=('Arial', 16, 'bold'), fg = "palegreen2", bg = "snow", command = add_or_update_dish)
  add_button.pack(padx = 101, pady = 10, fill = X)
  
  #Define a function to delete an existing dish:
  def delete_dish():
      if stall_n.get() == "Click here to select a stall: ↓":
        messagebox.showwarning("Warning", "You haven't chosen a stall yet!")
      else:
        dish_name_str = dish_name_var.get()
        for stall in system:
          if stall == stall_n.get():
            if dish_name_str in system[stall]:
              del system[stall][dish_name_str]
              messagebox.showinfo("Congratulations!","You have deleted the dish: "+dish_name_str+" from the stall: "+stall)            
            else:
              messagebox.showerror("Error", "The dish name you have entered is not in the menu, hence it cannot be deleted. Please check the menu and try again.")

  #Create a DELETE button:
  del_button = Button(menu_editor_window, text = "DELETE", font=('Arial', 16, 'bold'), fg = "red", bg = "snow", command = delete_dish)
  del_button.pack(padx = 101, fill = X)

  #Create a SAVE button:
  save_button = Button(menu_editor_window, text = "SAVE TO PKL FILE", font=('Arial', 16, 'bold'), fg = "dodgerblue2", bg = "snow", command =save_2_file)
  save_button.pack(padx = 101, pady = 10, fill = X)

  #Make the edit info button work again
  def quit_win():
      menu_editor_window.destroy()
      Advance_button.config(state ='normal')
  #Bind new protocal for the quit button to limit window numbers:
  menu_editor_window.protocol("WM_DELETE_WINDOW", quit_win)
  
#create a popup window for editing operating hours. Make it a function for the button to trigger
def optime_editor():
  #Make use of the time_system:
  global time_system

  optime_editor_window = Toplevel()
  optime_editor_window.title("Operating Time Information Editor")

  #positioning
  x_roposition = root.winfo_x()
  y_roposition = root.winfo_y()
  optime_editor_window.geometry("%dx%d+%d+%d" % (400, 420, x_roposition+300, y_roposition+120))
  optime_editor_window.maxsize(400,420)
  optime_editor_window.minsize(400,420)

  #Setting Background:
  oewphoto = PhotoImage(file = "time.png")
  oewbg_label = Label(optime_editor_window, image = oewphoto)
  oewbg_label.image = oewphoto
  oewbg_label.place(x=0, y=0, relwidth=1, relheight=1)
  
  #Label text for instruction
  instr1 = Label(optime_editor_window, text = "Choose the stall you want to edit:",\
  font=('Arial', 14, 'bold'), fg = "dodgerblue", bg = "white")
  instr1.grid(row = 1, padx = 50, pady = 10, columnspan = 3, sticky = (W,E))

  #create a dropdown list for user to choose a stall
  stall_n = StringVar()
  stall_n.set("Click here to select a stall: ↓")
  dropdown = OptionMenu(optime_editor_window, stall_n, *system)
  dropdown.config(font = ("Arial",15), fg = "deepskyblue2", bg = "snow")
  dropdown['menu'].config(font=('times',15, "bold"), fg = "black", bg='white')
  dropdown.grid(row = 2, padx = 50, columnspan = 3, sticky = (W,E))

  #Label text for instruction
  instr2 = Label(optime_editor_window, text = "Choose the starting time here :",\
  font=('Arial', 14, 'bold'), fg = "dodgerblue", bg = "white")
  instr2.grid(row = 3, padx = 50, pady = 10, columnspan = 3, sticky = (W,E))

  #Create a dropdown list for user to choose the starting hour
  start_hour_var = IntVar()
  start_hour_var.set("Hour")
  #Create a list for selecting hours:
  start_hour_list = [h for h in range(0,13)]

  hour_drop = OptionMenu(optime_editor_window, start_hour_var, *start_hour_list)
  hour_drop.config(font = ("Arial",15), fg = "deepskyblue2", bg = "snow")
  hour_drop['menu'].config(font=('Arial',13, ), fg = "black", bg='white')
  hour_drop.configure(width = 6)
  hour_drop.grid(row = 4, column = 0, sticky = E) 
  
  #Create a dropdown list for user to choose the starting minute
  start_min_var = IntVar()
  start_min_var.set("Minute")

  #Create a list for selecting minutes:
  min_list = [m for m in range(0,60)]
  
  min_drop = OptionMenu(optime_editor_window, start_min_var, *min_list)
  min_drop.config(font = ("Arial",15), fg = "deepskyblue2", bg = "snow")
  min_drop['menu'].config(font=('Arial',13, ), fg = "black", bg='white')
  min_drop.configure(width = 6)
  min_drop.grid(row = 4, column = 1, sticky = W)

  #Label text for "A.M."
  tam = Label(optime_editor_window, text = "A.M.",\
  font=('Arial', 14), fg = "dodgerblue", bg = "white")
  tam.grid(row = 4, column = 2, sticky = W)

  #Label text for instruction
  instr3 = Label(optime_editor_window, text = "Choose the ending time here :  ",\
  font=('Arial', 14, 'bold'), fg = "dodgerblue", bg = "white")
  instr3.grid(row = 5, padx = 50, pady = 10, columnspan = 3, sticky = (W,E))

  #Create a dropdown list for user to choose the starting hour
  end_hour_var = IntVar()
  end_hour_var.set("Hour")
  #Create a list for selecting hours:
  end_hour_list = [h for h in range(13,24)]

  e_hour_drop = OptionMenu(optime_editor_window, end_hour_var, *end_hour_list)
  e_hour_drop.config(font = ("Arial",15), fg = "deepskyblue2", bg = "snow")
  e_hour_drop['menu'].config(font=('Arial',13, ), fg = "black", bg='white')
  e_hour_drop.configure(width = 6)
  e_hour_drop.grid(row = 6, column = 0, sticky = E) 
  
  #Create a dropdown list for user to choose the starting minute
  end_min_var = IntVar()
  end_min_var.set("Minute")
    
  e_min_drop = OptionMenu(optime_editor_window, end_min_var, *min_list)
  e_min_drop.config(font = ("Arial",15), fg = "deepskyblue2", bg = "snow")
  e_min_drop['menu'].config(font=('Arial',13, ), fg = "black", bg='white')
  e_min_drop.configure(width = 6)
  e_min_drop.grid(row = 6, column = 1, sticky = W)

  #Label text for "P.M."
  tpm = Label(optime_editor_window, text = "P.M.",\
  font=('Arial', 14), fg = "dodgerblue", bg = "white")
  tpm.grid(row = 6, column = 2, sticky = W)

  #Define a function to update the operating time for a stall for the button to trigger:
  def update_optime():    
      if stall_n.get() == "Click here to select a stall: ↓":
        messagebox.showwarning("Warning", "You haven't chosen a stall yet!")
      else:
        try:
          #Formating:
          if start_hour_var.get() < 10:
            s_hour_str = "0"+str(start_hour_var.get())
          else:
            s_hour_str = str(start_hour_var.get())
          if start_min_var.get() < 10:
            s_minute_str = "0"+str(start_min_var.get())
          else:
            s_minute_str = str(start_min_var.get())
          e_hour_str = str(end_hour_var.get())
          if end_min_var.get() < 10:
            e_minute_str = "0"+str(end_min_var.get())
          else:
            e_minute_str = str(end_min_var.get())
          starting_time_str = s_hour_str + s_minute_str
          ending_time_str = e_hour_str + e_minute_str
          #Final string:
          operating_hours_up = "from " + starting_time_str + " A.M. to " + ending_time_str + " P.M."

          for stall in time_system:
            if stall == stall_n.get():
              time_system[stall] = operating_hours_up
              messagebox.showinfo("Congratulations!","You have updated the operating time of stall: "+stall+"\nThe new operating hour is "+operating_hours_up)             
        except:
          messagebox.showwarning("Warning", "You haven't chosen for the minute or hour. Please check and try again.")
  #Create an UPDATE button:
  update_button = Button(optime_editor_window, text = "UPDATE", font=('Arial', 16, 'bold'), fg = "white", bg = "deepskyblue2", command = update_optime)
  update_button.grid(row = 7, columnspan = 3, ipadx = 105, pady = 10)

  #Create a SAVE button:
  save_button = Button(optime_editor_window, text = "SAVE TO PKL FILE", font=('Arial', 16, 'bold'), fg = "deepskyblue2", bg = "snow", command = save_2_file)
  save_button.grid(row = 9, columnspan = 3, ipadx = 52, pady = 10)

  #Make the edit info button work again
  def quit_win():
      optime_editor_window.destroy()
      Advance_button.config(state ='normal')
  #Bind new protocal for the quit button to limit window numbers:
  optime_editor_window.protocol("WM_DELETE_WINDOW", quit_win)
  
#create a popup window to choose to edit menu or operating hours. Make it a function for the button to trigger
def edit_info():
  edit_window = Toplevel()
  edit_window.title("Stall Information Editor")

  #positioning
  x_roposition = root.winfo_x()
  y_roposition = root.winfo_y()
  edit_window.geometry("%dx%d+%d+%d" % (400, 200, x_roposition+300, y_roposition+260))
  edit_window.maxsize(400,200)
  edit_window.minsize(400,200)

  #Setting Background:
  emphoto = PhotoImage(file = "time.png")
  embg_label = Label(edit_window, image = emphoto)
  embg_label.image = emphoto
  embg_label.place(x=0, y=0, relwidth=1, relheight=1)

  #Limit window numbers:   
  def quit_win():
      edit_window.destroy()
      Advance_button.config(state ='normal')
  
  #Label text for instruction
  instr1 = Label(edit_window, text = "Choose the information you want to edit:",\
  font=('Arial', 14, 'bold'), fg = "dodgerblue", bg = "white")
  instr1.pack(fill = X, pady = 10)

  #Create a button to choose to edit menu:        
  menu_info_sel = Button(edit_window, text = "Menu", font=('Arial', 16,),fg = "White", bg = "tomato", command = lambda:[menu_editor(),edit_window.destroy()])
  menu_info_sel.pack(padx = 50, pady = 8, fill = X)

  #Create a button to choose to edit operating hours:        
  time_info_sel = Button(edit_window, text = "Operating Hours", font=('Arial', 16,), fg = "white", bg = "deepskyblue2", command = lambda:[optime_editor(),edit_window.destroy()])
  time_info_sel.pack(padx = 50, pady = 8, fill = X)

  #Bind new protocal for the quit button to limit window numbers:
  edit_window.protocol("WM_DELETE_WINDOW", quit_win)

#create a popup window that ask the user to key in pass word to edit stall info. 
#Make it a function for the button to trigger
def admin_v():
  pass_window = Toplevel()
  pass_window.title("Permission Required")

  #positioning
  x_roposition = root.winfo_x()
  y_roposition = root.winfo_y()
  pass_window.geometry("%dx%d+%d+%d" % (400, 230, x_roposition+300, y_roposition+200))
  pass_window.maxsize(400,230)
  pass_window.minsize(400,230)

  #Setting Background:
  psphoto = PhotoImage(file = "time.png")
  psbg_label = Label(pass_window, image = psphoto)
  psbg_label.image = psphoto
  psbg_label.place(x=0, y=0, relwidth=1, relheight=1)

  #Limit window numbers:
  Advance_button.config(state = "disable")
    
  def quit_win():
      pass_window.destroy()
      Advance_button.config(state ='normal')

  #Display instruction 1 message
  inst1 = Label(pass_window, text = "Enter the password to continue:", \
  font=('Arial', 16, 'bold'),width = 30, fg = "dodgerblue", bg = "white")
  inst1.pack(pady = 16)

  #Create a free entry for user to enter the number of people in front
  cipher_var = StringVar()
  message_var = StringVar()
  cipher_entry = Entry(pass_window, width = 50, textvariable = cipher_var, bd = 3)
  cipher_entry.pack(ipady =5)
  cipher_entry.focus()

  #define a function to check the ciphertext i.e. password:
  def certi():
    v_cipher = "ed"
    try:
      user_input_password = cipher_var.get()
      if user_input_password != v_cipher:
        message_var.set("Incorret pass word. \nPlease contact with NS canteen administrator.")
      else:
        edit_info()
        pass_window.destroy()
    except:
      message_var.set("Invalid password. An error occured.")
      
  #Bind with the "Enter" key on key board:
  cipher_entry.bind('<Return>', (lambda event: certi()))  
  #Create a CONFIRM button:
  conf_button = Button(pass_window, text = "OK", font=('Arial', 16, 'bold'), fg = "red", bg = "snow", command = certi)
  conf_button.pack(padx = 48, pady = 10, fill = X)

  #Create a label text to display message:
  display_msg = Label(pass_window, textvariable = message_var, font=('Arial', 13, 'bold'), fg = "orangered", bg = "white")
  display_msg.pack()

  #Bind new protocal for the quit button to limit window numbers:
  pass_window.protocol("WM_DELETE_WINDOW", quit_win)

#create a popup window for selecting date. Make it a function for the button to trigger
def user_day_selector():
  sel_date_window = Toplevel()
  sel_date_window.title("Select a specific day")

  #positioning
  x_roposition = root.winfo_x()
  y_roposition = root.winfo_y()
  sel_date_window.geometry("%dx%d+%d+%d" % (500, 540, x_roposition+270, y_roposition+105))
  sel_date_window.maxsize(500,540)
  sel_date_window.minsize(500,540)

  #Setting Background:
  bg_photo = PhotoImage(file = "time.png")
  bg_label = Label(sel_date_window, image = bg_photo)
  bg_label.image = bg_photo
  bg_label.place(x=0, y=0, relwidth=1, relheight=1)
  
  #Limit window numbers:
  Umenu_button.config(state = "disable")
  def quit_win():
      sel_date_window.destroy()
      Umenu_button.config(state='normal')

  #Label text for instruction:
  instr1 = Label(sel_date_window, text = "Choose the date on which you want to view menu:",\
  font=('Arial', 14, 'bold'), fg = "dodgerblue", bg = "white")
  instr1.grid(row = 1, padx = 10, pady = 10, columnspan = 2, sticky = (W,E))
  message_var = StringVar()

  #Label text for instruction
  yinstr = Label(sel_date_window, text = "Year", font=('Arial', 14, 'bold'), fg = "palegreen2", bg = "white")
  yinstr.grid(row = 2, column = 0, columnspan = 2, ipadx = 45, pady = 5)

  #Create a dropdown list for user to choose the year
  year_var = IntVar()
  year_var.set("Year")
  #Create a list for selecting Months:
  year_list = [y for y in range(2017, 2022)]

  year_drop = OptionMenu(sel_date_window, year_var, *year_list)
  year_drop.config(font = ("Arial",15), fg = "deepskyblue2", bg = "snow")
  year_drop['menu'].config(font=('Arial',13, ), fg = "black", bg='white')
  year_drop.configure(width = 28)
  year_drop.grid(row = 3, column = 0, columnspan = 2) 

  #Label text for instruction
  dinstr = Label(sel_date_window, text = "Day", font=('Arial', 14, 'bold'), fg = "palegreen2", bg = "white")
  dinstr.grid(row = 4, column = 0, ipadx = 45, pady = 5, sticky = E)
  
  #Label text for instruction
  minstr = Label(sel_date_window, text = "Month", font=('Arial', 14, 'bold'), fg = "palegreen2", bg = "white")
  minstr.grid(row = 4, column = 1, ipadx = 45, pady = 5, sticky = W)

  #Create a dropdown list for user to choose the Month
  month_var = IntVar()
  month_var.set("Month")
  #Create a list for selecting Months:
  month_list = [m for m in range(1,13)]

  month_drop = OptionMenu(sel_date_window, month_var, *month_list)
  month_drop.config(font = ("Arial",15), fg = "deepskyblue2", bg = "snow")
  month_drop['menu'].config(font=('Arial',13, ), fg = "black", bg='white')
  month_drop.configure(width = 12)
  month_drop.grid(row = 5, column = 1, sticky = W) 

  #Disable the drop down menu of selecting days before the month is selected:
  month_drop.configure(state = "disable")

  def enable_month(a,b,c):
    month_drop.configure(state = "normal")

  #Detect the change in the drop down menu of selecting months and trigger a fucntion to enable selecting days
  year_var.trace("w", enable_month)

  #Create a dropdown list for user to choose the day
  day_var = IntVar()
  day_var.set("Day") 
  #Initialize day_list:
  day_list = [""]    

  #define a function to enable dropdown menu of day with correct days:
  def enable_day(a,b,c):
    day_drop.configure(state = "normal")
    year_drop.configure(state = "disable")
    #for feburary:
    if month_var.get() == 2:
      day_var.set("Day")
      day_drop["menu"].delete(0,"end")
      if year_var.get() == 2020:
        day_list_feb = [str(d) for d in range(1,30)]
      else:
        day_list_feb = [str(d) for d in range(1,29)]
      for days in day_list_feb:
        day_drop['menu'].add_command(label=days, command=lambda value=days: day_var.set(value))
    
    #for months that have 31 days:
    elif month_var.get() in (1,3,5,7,8,10,12):
      day_var.set("Day")
      day_drop["menu"].delete(0,"end")
      day_list_28 = [str(d) for d in range(1,32)]
      for days in day_list_28:
        day_drop['menu'].add_command(label=days, command=lambda value=days: day_var.set(value))
    
    #for months that have 30 days:
    else:
      day_var.set("Day")
      day_drop["menu"].delete(0,"end")
      day_list_28 = [str(d) for d in range(1,31)]
      for days in day_list_28:
        day_drop['menu'].add_command(label=days, command=lambda value=days: day_var.set(value))
  
  day_drop = OptionMenu(sel_date_window, day_var, *day_list)
  day_drop.config(font = ("Arial",15), fg = "deepskyblue2", bg = "snow")
  day_drop['menu'].config(font=('Arial',13, ), fg = "black", bg='white')
  day_drop.configure(width = 12)
  day_drop.grid(row = 5, column = 0, sticky = E)

  #Disable the drop down menu of selecting days before the month is selected:
  day_drop.configure(state = "disable")

  #Detect the change in the drop down menu of selecting months and trigger a fucntion to enable selecting days
  month_var.trace("w", enable_day)

  #Label text for instruction
  instr2 = Label(sel_date_window, text = "Choose the time here :",\
  font=('Arial', 14, 'bold'), fg = "dodgerblue", bg = "white")
  instr2.grid(row = 6, padx = 50, pady = 5, columnspan = 2, sticky = (W,E))

  #Label text for instruction
  instrh = Label(sel_date_window, text = "Hour", font=('Arial', 14, 'bold'), fg = "palegreen2", bg = "white")
  instrh.grid(row = 7, column = 0, ipadx = 45, pady = 5, sticky = E)
  
  #Label text for instruction
  instrm = Label(sel_date_window, text = "Minute", font=('Arial', 14, 'bold'), fg = "palegreen2", bg = "white")
  instrm.grid(row = 7, column = 1, ipadx = 45, pady = 5, sticky = W)
  #Create a dropdown list for user to choose the starting hour
  hour_var = IntVar()
  hour_var.set("Hour")
  #Create a list for selecting hours:
  hour_list = [h for h in range(0,24)]

  hour_drop = OptionMenu(sel_date_window, hour_var, *hour_list)
  hour_drop.config(font = ("Arial",15), fg = "deepskyblue2", bg = "snow")
  hour_drop['menu'].config(font=('Arial',13, ), fg = "black", bg='white')
  hour_drop.configure(width = 12)
  hour_drop.grid(row = 8, column = 0, sticky = E) 
  
  #Create a dropdown list for user to choose the starting minute
  min_var = IntVar()
  min_var.set("Minute")

  #Create a list for selecting minutes:
  min_list = [m for m in range(0,60)]
  
  min_drop = OptionMenu(sel_date_window, min_var, *min_list)
  min_drop.config(font = ("Arial",15), fg = "deepskyblue2", bg = "snow")
  min_drop['menu'].config(font=('Arial',13, ), fg = "black", bg='white')
  min_drop.configure(width = 12)
  min_drop.grid(row = 8, column = 1, sticky = W)

  #define a function to get the weekday from user input:
  def get_week_day():
      year_int = year_var.get()
      day_int = day_var.get()
      month_int = month_var.get()
      return calendar.day_name[datetime.date(year_int, month_int, day_int).weekday()]
  
  

  #create a popup window for viewing menu on specific day. Make it a function for the button to trigger
  def will_time_menu():
      #make use of the menu\operating time dictionary

      #Get input week day detail:
      week_day_str = get_week_day()
      #weekend menu:
      if week_day_str == "Saturday" or week_day_str == "Sunday":
        med_weekend_file = open("weekend_menu.pkl","rb")
        sel_system = pickle.load(med_weekend_file)
      #normal menu:
      elif week_day_str in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
        menu_file = open("General_menu.pkl", "rb")
        sel_system = pickle.load(menu_file)
      #breakfast menu:
      bmenu_file = open("Breakfast.pkl","rb")
      Breakfast = pickle.load(bmenu_file)
      if hour_var.get() < 10:
          del sel_system["McDonald's"]
          del sel_system["KFC"]
          sel_system.update(Breakfast)
      global time_system


      will_menu_window = Toplevel()

      #positioning
      x_roposition = root.winfo_x()
      y_roposition = root.winfo_y()
      will_menu_window.title("Stalls")  
      will_menu_window.geometry("%dx%d+%d+%d" % (550, 600, x_roposition+60, y_roposition+55))
      will_menu_window.maxsize(550,600)
      will_menu_window.minsize(550,600)

      def quit_win():
          will_menu_window.destroy()
          Umenu_button.config(state='normal')

      #Setting Background:
      mbgphoto = PhotoImage(file = "food3.png")
      mbg_label = Label(will_menu_window, image = mbgphoto)
      mbg_label.image = mbgphoto
      mbg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
      #Display welcome message
      welcome = Label(will_menu_window, font=('Times', 16, 'bold'), fg = "snow", bg = "black")
      welcome.pack(fill = X)
      if hour_var.get() < 12:
        welcome.config(text = "The date chosen is:  "+get_week_day()+"   "+str(day_var.get())+" / "+str(month_var.get())+" / "+str(year_var.get())+"    "+ str(hour_var.get())+":"+str(min_var.get())+" \nGood morning!\nPlease use the drop down menu to choose a stall!")
      elif 12<= hour_var.get() <16:
        welcome.config(text = "The date chosen is:  "+get_week_day()+"   "+str(day_var.get())+" / "+str(month_var.get())+" / "+str(year_var.get())+"    "+ str(hour_var.get())+":"+str(min_var.get())+" \nGood afternoon!\nPlease use the drop down menu to choose a stall!")
      elif 16<= hour_var.get() <24:
        welcome.config(text = "The date chosen is:  "+get_week_day()+"   "+str(day_var.get())+" / "+str(month_var.get())+" / "+str(year_var.get())+"    "+ str(hour_var.get())+":"+str(min_var.get())+" \nGood evening!\nPlease use the drop down menu to choose a stall!")

      #Create a text box for displaying menu:
      #Create an empty text box first, then insert dish-price pairs line by line since we are using dictionarys
      menu_text = Text(will_menu_window, height = 15, width = 70, fg= "snow", background='peachpuff4', font='helvetica 13 bold')
      menu_text.pack() 
      #Setting initial notification:
      menu_text.insert(INSERT, "\n\n\n\t         Welcome to NS smart canteen viewer!\n\tPlease choose from the drop down menu button!")
      menu_text.config(state = 'disabled')
      #The function executed when click the button to view dishes & prices
      def view_dish():
        menu_text.config(state = 'normal')
        menu_text.delete("1.0", END)     
        for stall in sel_system:
          if stall == stall_n.get():         
            dish = list(sel_system[stall].keys())
            price = list(sel_system[stall].values())
                    
            for d,p in zip(dish, price):
              menu_items = "Dish name:   {} \t\t\t\t\t Price: {} SG$\n".format(d,p)
              menu_text.insert(INSERT, menu_items)
            menu_text.config(state = 'disabled')
        else:
            #if no option is chosen, display an error message:
            menu_text.insert(INSERT, "\n\n\n\n\n\n\t \tYou have not chosen a stall yet! \n\t\t\tTo view menus, \n\tplease choose from the drop down menu button!")
            menu_text.config(state = 'disabled')

      #create a dropdown list for user to choose a stall
      stall_n = StringVar()
      stall_n.set("Click here to select a stall")
      dropdown = OptionMenu(will_menu_window, stall_n, *sel_system)
      dropdown.config(font = ("Arial",16, "bold"), bg = "peachpuff")
      dropdown['menu'].config(font=('times',16, "bold"), fg = "black", bg='snow')
      dropdown.pack(padx = 80, fill = X)
    
      #create a button to confirm the selection:
      conf = Button(will_menu_window, width = 12, text = "Confirm", font=('Arial', 16, 'bold'), bg = "tomato", command = view_dish)
      conf.pack(padx = 80, pady = 20, fill = X)

      #The function executed when click the button to view operating time
      def view_op_hr():
        menu_text.config(state = 'normal')      
        for stall in time_system:
          if stall == stall_n.get():           
            operate_time = time_system[stall]
            time_info = "Stall:    {}  \nOpen {}".format(stall,operate_time)
            messagebox.showinfo("Operating Hours", time_info)
            break
        else:
            #if no option is chosen, display an error message:
            menu_text.delete("1.0", END)  
            menu_text.insert(INSERT, "\n\n\n\n\n\n\t \tYou have not chosen a stall yet! \n\t  \t    To view operating hours, \n\tplease choose from the drop down menu button!")
            menu_text.config(state = 'disabled')
      #create a button to view the operating hours
      op_hour = Button(will_menu_window, text = "View Operating Hours", font=('Arial', 16, 'bold'), bg = "deepskyblue2", command = view_op_hr)
      op_hour.pack(padx = 80, fill = X)

      if hour_var.get() < 8 or hour_var.get() > 19:
          menu_text.config(state = 'normal')
          dropdown.configure(state = "disable")
          op_hour.configure(state = "disable")
          conf.configure(state = "disable")
          menu_text.delete("1.0", END)
          menu_text.insert(INSERT, "\n\n\n\n\n\n         Sorry, all stalls are closed now. Please come tomorrow!")
          menu_text.config(state = 'disabled')
      #Bind new protocal for the quit button to limit window numbers:
      will_menu_window.protocol("WM_DELETE_WINDOW", quit_win)
 
  #Define a function to proceed:
  def proceed_view():
    #Create a Go to menu viewer button:
    conf_button = Button(sel_date_window, text = "View Menu", font=('Arial', 16, 'bold'), fg = "red", bg = "snow", command = lambda:[will_time_menu(),sel_date_window.destroy()])
    conf_button.grid(row = 11, columnspan = 2, ipadx = 14, pady = 10)

  #Define a function to check the date input:
  def check_date():
    try:
      year_var_int = year_var.get()
      month_var_int = month_var.get()
      day_var_int = day_var.get()
      hour_var_int = hour_var.get()
      min_var_int = min_var.get()
      message_var.set("You have chosen the date:\n"+str(day_var_int)+" / "+str(month_var_int)+" / "+str(year_var_int)+"\nTime: "+ str(hour_var_int)+":"+str(min_var_int)+"h")
      proceed_view()
    except:
      message_var.set("Please make sure you have select \nthe items for all drop down menus")

  #Create a CONFIRM button:
  conf_button = Button(sel_date_window, text = "OK", font=('Arial', 16, 'bold'), fg = "red", bg = "snow", command = check_date)
  conf_button.grid(row = 9, column = 0, ipadx = 62, pady = 15, sticky = E)

  #Define a function to reset the year:
  def choice_reset():
    sel_date_window.destroy()
    user_day_selector()

  #Create a RESET button:
  conf_button = Button(sel_date_window, text = "RESET", font=('Arial', 16, 'bold'), fg = "red", bg = "snow", command = choice_reset)
  conf_button.grid(row = 9, column = 1, ipadx = 43, pady = 15, sticky = W)

  #Create a label text to display message:
  display_msg = Label(sel_date_window, textvariable = message_var, font=('Arial', 13, 'bold'), fg = "orangered", bg = "white")
  display_msg.grid(row = 10, columnspan = 2, padx = 49, pady = 10)

  #Bind new protocal for the quit button to limit window numbers:
  sel_date_window.protocol("WM_DELETE_WINDOW", quit_win)

######################################Function Definitions#######################################

##########################################Main program###########################################
#Version no. Last edit: 13/11/2019:
version = "1.0.5"

root = Tk()
root.title("Nanyang Technological University North Spine Canteen Smart Viewer")

#collect time details
current = datetime.datetime.now()
#24h time will be used. 0-24 as integers 
hour = str(current.time())[0:2]
hour = int(hour)

#Open predefined dictionaries stored in pickle files:
time_file = open("Operate_time.pkl", "rb")
time_system = pickle.load(time_file)
menu_file = open("General_menu.pkl", "rb")
system = pickle.load(menu_file)
bmenu_file = open("Breakfast.pkl","rb")
Breakfast = pickle.load(bmenu_file)

#Get current weekday:
current_day = datetime.date.today()
current_week_day = calendar.day_name[current_day.weekday()]

#weekend menu:
if current_week_day == "Saturday" or current_week_day == "Sunday":
    med_weekend_file = open("weekend_menu.pkl","rb")
    system = pickle.load(med_weekend_file)

#Define an empty menu system
sel_system = {"":{"":""}}

#Loading predefined menu (depends on time) and display in status bar:
if hour < 10:
    del system["McDonald's"]
    del system["KFC"]
    system.update(Breakfast)
    #Status bar at the bottom for debbuging
    status_bar = Label(root, text = "Welcome to NTU North Spine Canteen Smart Viewer. \nCurrent version: "+version, \
      bd = 1, fg = "snow", bg ="black", relief = SUNKEN, anchor = S)
    status_bar.pack(side = BOTTOM, fill = X)
    #messagebox.showinfo("Notification", "Predefined stalls and menu file (Breakfast) loaded successfully!\nPredefined operating hours file loaded successfully!")
else:
    #Status bar at the bottom for debbuging
    status_bar = Label(root, text = "Welcome to NTU North Spine Canteen Smart Viewer. Version "+version, \
      bd = 1, fg = "snow", bg ="black", relief = SUNKEN, anchor = S)
    status_bar.pack(side = BOTTOM, fill = X)
    #messagebox.showinfo("Notification", "Predefined stalls and menu file (General) loaded successfully!\nPredefined operating hours file loaded successfully!")

#Menu bar at the top
top_menu = Menu(root)
root.config(menu = top_menu)
submenu = Menu(top_menu, tearoff = 0)
top_menu.add_cascade(label = "File", menu = submenu)
submenu.add_command(label = "Import Piclke Files...", command = browse_file)
submenu.add_command(label = "About...", command = popu)
submenu.add_separator()
submenu.add_command(label = "Exit...", command = exit)

#Background:
Background_pic = PhotoImage(file = "canteen.png")
Background_can = Canvas(root, width = 1017, height = 667,bd = 0,highlightthickness=0)
Background_can.create_image(508,333, image = Background_pic)
Background_can.pack()

#Show current time and date on the top
date_time = Label(root, font=('Arial', 12, 'bold'), fg = "dodgerblue", bg = "white")
Background_can.create_window(508,10, width =1017, height = 20, window = date_time)
dtime()

#Display welcome message
welcome_main = Label(root, font=('Arial', 12, 'bold'), fg = "dodgerblue", bg = "white")
Background_can.create_window(508, 30, width = 1017, height = 20, window = welcome_main)

if hour <8:
  welcome_main.config(text = "Good morning!  Currently all stalls are closed. Please come tomorrow!")
  messagebox.showwarning("Off service", "Currently all stalls are closed. \nPlease come tomorrow!")
elif 8<=hour < 12:
  welcome_main.config(text = "Good morning!  Please use the button below. Have a nice breakfast!")
elif 12<= hour <16:
  welcome_main.config(text = "Good afternoon!  Please use the button below. Have a nice meal!")
elif 16<= hour <20:
  welcome_main.config(text = "Good evening!  Please use the button below. Have a nice dinner!")
elif 20<= hour <24:
  welcome_main.config(text = "Good evening!  Currently all stalls are closed. Please come tomorrow!")
  messagebox.showwarning("Off service", "Currently all stalls are closed. \nPlease come tomorrow!")

#View menu button
View_menu_button = Button(root, text = "View Current Menu", font = ("Arial", 16), fg = "snow", bg = "steelblue", command = menuwindow)
Background_can.create_window(800, 300, width = 280, height = 50, window = View_menu_button)

#View user-defined day's menu button
Umenu_button = Button(root, text = "View Menu By Other Date", font = ("Arial", 16), fg = "steelblue",bg = "snow", command = user_day_selector)
Background_can.create_window(800, 380, width = 280, height = 50, window = Umenu_button)

#Calculate waiting time button:
Wait_button = Button(root, text = "Calculate Waiting Time", font = ("Arial", 16), fg = "yellow", bg = "rosybrown", command = cal_wait_time)
Background_can.create_window(800, 460, width = 280, height = 50, window = Wait_button)

#Advanced option:
Advance_button = Button(root, text = "Edit Stall Info", font = ("Arial", 16), fg = "snow", bg = "tomato", command = admin_v)
Background_can.create_window(800, 540, width = 280, height = 50, window = Advance_button)

#Close all the stalls
if hour < 8 or hour > 19:
    Wait_button.configure(state = "disable")
      
#Setting the size of the main window:
#root.resizable(width=False, height=False)
root.maxsize(1017,667)
root.minsize(508,433)
root.mainloop()
##########################################Main program###########################################