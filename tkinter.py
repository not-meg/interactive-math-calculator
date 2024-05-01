from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from time import sleep
from time import time

import mathmodule

outputframe = None
entryframe = None


#popup image while starting mathable

def open_img():
    x = 'mathable_welc.gif'
    img = Image.open(x)
    img = img.resize((500,250), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image = img)
    panel.image = img
    panel.grid(row = 2)

#thank you popup when 'quit' pressed

def end_img():
    end = Toplevel()
    end.geometry('500x250')
    y = 'mathable_ty.gif'
    img = Image.open(y)
    img = img.resize((500,250), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    endlbl = Label(end, image = img)
    endlbl.image = img
    endlbl.grid(row = 2)


#all functions


#help button cmd

def entryhelp():
    func_name = fn_dict[selected.get()][subfn1][subfn2]["func"]
    messagebox.showinfo("Help", func_name.__doc__)
    

#go back button (output screen)

def goback():
    global in_entry
    global outputframe
    outputframe.destroy()
    for i in range(len(in_entry)):
        in_entry[i].configure(state = 'normal')
        

#select new operation (output screen)

def select_new():
    global outputframe
    global entryframe
    res = messagebox.askyesno('Go Back?', 'Are you sure you want to go back to the selection menu?')
    if res == True:
        outputframe.destroy()
        entryframe.destroy()
        optioncb['state'] = 'readonly'
        if suboptioncb1 is not None:
            suboptioncb1['state'] = 'readonly'
        if suboptioncb2 is not None:
            suboptioncb2['state'] = 'readonly'


#get input lists

def selection_cb(event):

    global suboptionlabel1
    global suboptioncb1
    global suboptionlabel2
    global suboptioncb2
    global subfn1
    global subfn2

    if suboptionlabel1 is not None:
        suboptionlabel1.destroy()
        suboptionlabel1 = None

    if suboptioncb1 is not None:
        suboptioncb1.destroy()
        suboptioncb1 = None

    if suboptionlabel2 is not None:
        suboptionlabel2.destroy()
        suboptionlabel2 = None

    if suboptioncb2 is not None:
        suboptioncb2.destroy()
        suboptioncb2 = None
        
    if "None" not in fn_dict[selected.get()] :
        sub_fns = list(fn_dict[selected.get()].keys())

        
        suboptionlabel1 = Label(optionframe, text = "Please select a sub operation for "+selected.get(), bg = '#fafac3', font = 'Garamond 13 bold')
        suboptionlabel1.grid(row = 0, column = 1, padx = 20, pady=20)
        suboptioncb1 = ttk.Combobox(optionframe, state = 'readonly', values = sub_fns, textvariable = subselected1, font = 'Garamond 13 bold')
        suboptioncb1.grid(row = 1, column = 1, pady= 20, padx = 20)
        suboptioncb1.bind("<<ComboboxSelected>>", checksubfn1)

    subfn1 = "None"
    subfn2 = "None"

def getinput(in_entry):

    out_list = []
    input_list = fn_dict[selected.get()][subfn1][subfn2]["inputs"]

    for i in range(len(in_entry)):
        if input_list[i][0] == 1:
            out_list.append(int(in_entry[i].get()))
        elif input_list[i][0] == 2:
            out_list.append(float(in_entry[i].get()))
        elif input_list[i][0] == 3:
            l = in_entry[i].get().split(",")
            l = [i for i in l if i != ""]
            out_list.append(list(map(float, l)))
            

    return(out_list)

    
    
#to check if there is subfn1 to be selected

def checksubfn1(event):

    global subfn1
    
    subfn1 = subselected1.get()

    subfn1_vals = list(fn_dict[selected.get()][subselected1.get()])

    global suboptionlabel2
    global suboptioncb2

    if suboptionlabel2 is not None:
        suboptionlabel2.destroy()
        suboptionlabel2 = None
      
    if suboptioncb2 is not None:
        suboptioncb2.destroy()
        suboptioncb2 = None
   

    if "None" not in fn_dict[selected.get()][subselected1.get()]:

        suboptionlabel2 = Label(optionframe, text = "Please select a sub operation for "+subfn1, bg = '#fafac3', font = 'Garamond 13 bold')
        suboptionlabel2.grid(row = 0, column = 2, padx = 20, pady=20)
        
        suboptioncb2 = ttk.Combobox(optionframe, state = 'readonly', values = subfn1_vals, textvariable = subselected2, font = 'Garamond 13 bold')
        suboptioncb2.grid(row = 1, column = 2, padx = 20, pady=20)
        suboptioncb2.bind("<<ComboboxSelected>>", checksubfn2)

#check if there is subfn2 to be selected

def checksubfn2(event):

    global subfn2

    subfn2 = subselected2.get()

def entry_validate_int(inputstr):
    if inputstr == "":
        return True
    return inputstr.isdigit()

def entry_validate_float(inputstr):
    if inputstr == "":
        return True
    try:
        float(inputstr)
        return True
    except:
        return False

def entry_validate_list(inputstr):
    if inputstr == "":
        return True
    l = inputstr.split(',')

    if l[-1] == "":
        l=l[0:-1]


    for i in l:
        try:
            float(i)
        except:
            return False
    return True


def optionclicked():

    global subfn1
    global subfn2

    if optioncb.current() == -1:
        messagebox.showerror('Error', 'You have not selected an operation')

    elif suboptioncb1 is not None and suboptioncb1.current() == -1:
        messagebox.showerror('Error', 'You have not selected a sub operation')

    elif suboptioncb2 is not None and suboptioncb2.current() == -1:
        messagebox.showerror('Error', 'You have not selected a sub operation')

    else:

        input_list = fn_dict[selected.get()][subfn1][subfn2]["inputs"]
        
        optioncb['state'] = 'disabled'
        if suboptioncb1 is not None:
            suboptioncb1['state'] = DISABLED
        if suboptioncb2 is not None:
            suboptioncb2['state'] = DISABLED

        #main frame for accepting inputs
        global entryframe
    
        entryframe=Frame(top, height = 80, width = 400, relief = SUNKEN, borderwidth = 5, bg = '#fafac3')
        entryframe.pack(anchor=NW, fill = X)

        #for labels + entrybox
    
        inputframe = Frame(entryframe, height = 70, width = 400, bg = '#fafac3')
        inputframe.pack(padx = 2, ipadx=10, ipady=20, fill = X)

        lblheader = Label(inputframe, text = "Enter your values here", pady = 20, font = 'Garamond 13 bold', bg = '#fafac3')
        lblheader.grid(row=0, columnspan=3, sticky = "N")

        inputlbl = []
        
        global in_entry
        in_entry = []

        for i in range (0, len(input_list)):

            inputlbl.append(Label(inputframe, text = input_list[i][1], padx = 10, font = 'Garamond 13 bold', bg = '#fafac3'))
            inputlbl[i].grid(row=i+1, column=0)

            if input_list[i][0] == 1:
                validate_func = inputframe.register(entry_validate_int)
            elif input_list[i][0] == 2:
                validate_func = inputframe.register(entry_validate_float)
            elif input_list[i][0] == 3:
                validate_func = inputframe.register(entry_validate_list)

            in_entry.append(Entry(inputframe, font = 'Garamond 13', bg = '#f7f7d7', validate = 'key', validatecommand = (validate_func, '%P')))
            in_entry[i].grid(row=i+1, column=1, padx = 30)


        def entryclicked():

            global in_entry
            global outputframe

            valid = 1

            for i in range(0, len(input_list)):
                if in_entry[i].get() == "":
                    valid = 0

            if valid == 0:

                messagebox.showerror("Error", "Please fill all the required fields!")

            else:

                for i in in_entry:
                    i['state'] = 'disabled'
                
                func_name = fn_dict[selected.get()][subfn1][subfn2]["func"]
            
                outputframe = Frame(top, height = 400, width = 400, relief = SUNKEN, borderwidth = 5, bg = '#fafac3')
                outputframe.pack(anchor=SW, fill = X)

                outputheaderlbl = Label(outputframe, text = "Output", bg = '#fafac3', font = 'Garamond 13 bold')
                outputheaderlbl.grid(row = 0, column = 1, columnspan = 2)

                out_list = getinput(in_entry)

                mathmodule.setoutputframe(outputframe)

                result = func_name(*out_list)

                def resultcheck():

                    
                    s = ""
                    
                    for x in result:
                        if s:
                            s = s +', ' + str(x)
                        else:
                            s = str(x)

                    return s
                        
                o = fn_dict[optioncb.get()][subfn1][subfn2]['output']
                if len(o) > 1:
                    display = o[0].format(*map(eval, o[1:]))
                elif len(o) == 1:
                    display = o[0]
                else:
                    display = ""


                

                if result is not None:

                    if type(result) == list or type(result) == tuple:
                        result = resultcheck()
                        
                    outputlbl = Label(outputframe, text = display+'\n'+str(result), bg = '#fafac3', font = 'Garamond 13 bold') 
                    outputlbl.grid(row = 1, column = 1, columnspan = 2, pady = 30)

                    backbtn = Button(outputframe, text = 'Calculate with Different Inputs', command = goback, bg = '#f5ddbf', activebackground = '#5f4c78', activeforeground = 'white', font = 'Garamond 13 bold')
                    backbtn.grid(padx = 5, pady = 20, row = 3, column = 1)

                    newop = Button(outputframe, text = 'Select New Operation', command = select_new, bg = '#f5ddbf', activebackground = '#5f4c78', activeforeground = 'white', font = 'Garamond 13 bold')
                    newop.grid(padx = 5, pady = 20, row = 3, column = 2)
        
        

        def entryclear():

            res = messagebox.askyesno('Clear input?', 'Are you sure you want to clear all inputs?')
            if res == True:

                for i in range(0, len(input_list)):
                    in_entry[i].delete(0, END)
                    
    
        def entrycancel():

            global outputframe

            res = messagebox.askyesno('Quit Input Menu?', 'Are you sure you want to go back?')
            if res == True:
                entryframe.destroy()
                if outputframe is None:
                    pass
                else:
                    outputframe.destroy()
                    outputframe = None
                optioncb['state'] = 'readonly'
            if suboptioncb1 is not None:
                suboptioncb1['state'] = 'readonly'
            if suboptioncb2 is not None:
                suboptioncb2['state'] = 'readonly'

        clickframe = Frame(entryframe, height = 30, width = 400, bg = '#fafac3')
        clickframe.pack()

        
        #for submit + clear + cancel buttons

        entry_submit = Button(clickframe, text = "Submit", command = entryclicked, bg = '#f5ddbf', activebackground = '#5f4c78', activeforeground = 'white', font = 'Garamond 13 bold')
        entry_submit.grid(row = 4,rowspan=3, column=0, sticky=S, padx=20)
        entry_clear = Button(clickframe, text = "Clear", command = entryclear, bg = '#f5ddbf', activebackground = '#5f4c78', activeforeground = 'white', font = 'Garamond 13 bold')
        entry_clear.grid(row=4,rowspan=3, column=1, sticky=S, padx=20)
        entry_cancel = Button(clickframe, text = "Cancel", command = entrycancel, bg = '#f5ddbf', activebackground = '#5f4c78', activeforeground = 'white', font = 'Garamond 13 bold')
        entry_cancel.grid(row=4,rowspan=3, column=2, sticky=S, padx=20)
        entry_help = Button(clickframe, text = "Help", command = entryhelp, bg = '#f5ddbf', activebackground = '#5f4c78', activeforeground = 'white', font = 'Garamond 13 bold')
        entry_help.grid(row=4, rowspan = 3, column = 3, sticky = S, padx = 20)


def quitwindow():

            res1 = messagebox.askokcancel('Quit', 'Quit Mathable?')
            if res1 == True:
                end_img()
                startTime = time()
                top.after(700, top.destroy)
                

#dictionary that contains all the inputs
#input type 1 = int, input type 2 = float, input type 3 = list of integers

subfn1 = "None"
subfn2 = "None"
in_entry = []


fn_dict = {
            "HCF":
            {"None":
                {"None":
                 {"inputs":
                  [(1, "Enter first number:"),
                   (1, "Enter 2nd number:")],
                  "func":mathmodule.gcd,
                  "output":("The {0} of {1} and {2} is: ", "optioncb.get()", "in_entry[0].get()", "in_entry[1].get()")
                  }}},
            
            "Divisibility":
            {"None":
                {"None":
                 {"inputs":
                  [(1, "Enter a number:")],
                "func":mathmodule.divisibility,
                  "output":("{0} is ", "in_entry[0].get()")
                  }}},
            
            "AP":
            {"None":
                {"None":
                 {"inputs":
                    [(2, "Enter the first term:"),
                    (2, "Enter the common difference:"),
                    (1, "Enter the number of terms:")],
                  "func":mathmodule.ap,
                  "output":("The {0} is: \n", "optioncb.get()")}}},
            
            "GP":
            {"None":
                {"None":
                 {"inputs":
                  [(2, "Enter the first term:"),
                   (2, "Enter the common ratio:"),
                   (1, "Enter the number of terms:")],
                  "func":mathmodule.gp,
                  "output":("The {0} is: \n", "optioncb.get()")}}},
            
            "Roots of Quadratic Equation":
            {"None":
                {"None":
                 {"inputs":
                  [(2, "Enter the coefficient of x^2:"),
                   (2, "Enter the coefficient of x:"),
                   (2, "Enter the constant term:")],
                  "func":mathmodule.qdrtc_eqn,
                  "output":("The roots of the equation are: \n",)}}},
            
                "Area":
                    {"Circle":
                    {"None":
                     {"inputs":
                      [(2, "Enter the radius of the circle:")],
                      "func":mathmodule.circle_area,
                      "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},
                    
                    "Trapezium":
                    {"None":
                     {"inputs":
                      [(2, "Enter the length of the 1st parallel side:"),
                       (2, "Enter the length of the 2nd parallel side:"),
                       (2, "Enter the height of the trapezium:")],
                      "func":mathmodule.trap_area,
                      "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},
                    
                    "Hexagon":
                    {"None":
                     {"inputs":
                      [(2, "Enter the side of the hexagon")],
                      "func":mathmodule.area_hexagon,
                      "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},
                    
                    "Ellipse":
                    {"None":
                     {"inputs":
                      [(2, "Enter the lenth of the semi major axis of the ellipse:"),
                       (2, "Enter the length of the semi minor axis of the ellipse")],
                      "func":mathmodule.area_ell,
                      "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},

                 "Tetrahedron":
                 {"None":
                  {"inputs":
                   [(2, "Enter the length of the side of the tetrahedron:")],
                   "func":mathmodule.area_tetrahedron,
                   "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},

                 "Triangle":
                 {"Right Angled":
                  {"inputs":
                   [(2, "Enter the base of the triangle:"),
                    (2, "Enter the height of the triangle:")],
                   "func":mathmodule.tri_area_right,
                   "output":("The {0} of the {1} {2} is ", "optioncb.get()", "suboptioncb2.get()", "suboptioncb1.get()")},
                  
                  "Scalene":
                  {"inputs":
                   [(2, "Enter the first side:"),
                    (2, "Enter the second side:"),
                    (2, "Enter the third side:")],
                   "func":mathmodule.tri_area_scalene,
                   "output":("The {0} of the {1} {2} is ", "optioncb.get()", "suboptioncb2.get()", "suboptioncb1.get()")},

                  "Isosceles":
                  {"inputs":
                   [(2, "Enter the length of the equal sides:"),
                    (2, "Enter the length of the base:")],
                   "func":mathmodule.tri_area_isosceles,
                   "output":("The {0} of the {1} {2} is ", "optioncb.get()", "suboptioncb2.get()", "suboptioncb1.get()")},

                  "Equilateral":
                  {"inputs":
                   [(2, "Enter the length of the side of the triangle:")],
                   "func":mathmodule.tri_area_equilateral,
                   "output":("The {0} of the {1} {2} is ", "optioncb.get()", "suboptioncb2.get()", "suboptioncb1.get()")}
                  },

                 "Parallelogram":
                 {"Using Diagonals":
                  {"inputs":
                   [(2, "Enter the length of the first diagonal:"),
                    (2, "Enter the length of the second diagonal:"),
                    (2, "Enter the angle (in degrees):")],
                   "func":mathmodule.pllgm_area_diagonals,
                   "output":("The {0} of the {1} {2} is ", "optioncb.get()", "suboptioncb1.get()", "suboptioncb2.get()")},

                  "Using Base and Height":
                  {"inputs":
                   [(2, "Enter the base:"),
                    (2, "Enter the height:")],
                    "func":mathmodule.pllgm_area_bh,
                   "output":("The {0} of the {1} {2} is ", "optioncb.get()", "suboptioncb1.get()", "suboptioncb2.get()")},

                  "Using Trigonometry":
                  {"inputs":
                   [(2, "Enter the length of the first side:"),
                    (2, "Enter the length of the second side:"),
                    (2, "Enter the angle between the two adjacent sides (in degrees):")],
                   "func":mathmodule.pllgm_area_trigo,
                   "output":("The {0} of the {1} {2} is ", "optioncb.get(), suboptioncb1.get()")}
                  }       
                 
                },

            "Number Patterns":
                {"Sum of Cubes of n Numbers":
                {"None":
                 {"inputs":
                  [(1, "Enter the number of terms:")],
                  "func":mathmodule.sum_cubes,
                  "output":("The {0} is: \n", "suboptioncb1.get()")}},

                 "Sum of Squares of n Numbers":
                 {"None":
                  {"inputs":
                   [(1, "Enter the number of terms:")],
                   "func":mathmodule.sum_squares,
                   "output":("The {0} is: \n", "suboptioncb1.get()")}},

                 "Sum of n Numbers":
                 {"None":
                  {"inputs":
                   [(1, "Enter the number of terms:")],
                   "func":mathmodule.sum_num,
                   "output":("The {0} is: \n", "suboptioncb1.get()")}}

                },
                       
            "Profit and Loss":
                {"None":
                 {"None":
                 {"inputs":
                  [(2, "Enter the cost price of the product:"),
                   (2, "Enter the selling price of the product:")],
                  "func":mathmodule.profit_loss,
                  "output":()}}},

            "Statistics":
                {"Mean":
                 {"None":
                  {"inputs":
                   [(3, "Enter the numbers:")],
                   "func":mathmodule.find_mean,
                   "output":("The {0} is: /n", "suboptioncb1.get")}},

                 "Median":
                  {"None":
                   {"inputs":
                    [(3, "Enter the numbers:")],
                    "func":mathmodule.find_median,
                    "output":("The {0} is: /n", "suboptioncb1.get")}},

                  "Mode":
                   {"None":
                    {"inputs":
                     [(3, "Enter the numbers:")],
                     "func":mathmodule.find_mode,
                     "output":("The {0} is: /n", "suboptioncb1.get")}},

                },

            "Volume":
             {"Cylinder":
               {"None":
                {"inputs":
                 [(2, "Enter the radius of the base of the cylinder:"),
                  (2, "Enter the height of the cylinder:")],
                 "func":mathmodule.vol_cyl,
                 "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},

              "Sphere":
              {"None":
               {"inputs":
                [(2, "Enter the radius of the sphere:")],
                "func":mathmodule.sphere_vol,
                "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},

              "Ellipsoid":
              {"None":
               {"inputs":
                [(2, "Enter the radius of the ellipsoid of the 1st axis:"),
                 (2, "Enter the radius of the ellipsoid of the 2nd axis:"),
                 (2, "Enter the radius of the ellipsoid of the 3rd axis:")],
                "func":mathmodule.vol_ellipsoid,
                "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},

              "Cone":
              {"None":
               {"inputs":
                [(2, "Enter the height of the cone:"),
                 (2, "Enter the radius of the base of the cone:")],
                "func":mathmodule.vol_cone,
                "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},
            
              "Rectangular Prism":
              {"None":
               {"inputs":
                [(2, "Enter the length of the prism:"),
                 (2, "Enter the width of the prism:"),
                 (2, "Enter the height of the prism:")],
                "func":mathmodule.vol_prism,
                "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}}

               },
            
            "Surface Area of a Solid":
            {"Cube":
             {"None":
              {"inputs":
               [(2, "Enter the edge of the cube:")],
               "func":mathmodule.sfa_cube,
               "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},

             "Cuboid":
             {"None":
              {"inputs":
               [(2, "Enter the length of the cuboid:"),
                (2, "Enter the breadth of the cuboid:"),
                (2, "Enter the height of the cuboid:")],
               "func":mathmodule.sfa_cuboid,
               "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},

        

             "Sphere":
             {"None":
              {"inputs":
               [(2, "Enter the radius of the sphere:")],
               "func":mathmodule.sfa_sphere,
               "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}},

             "Cylinder":
             {"None":
              {"inputs":
               [(2, "Enter the radius of the base of the cylinder:"),
                (2, "Enter the height of the cylinder:")],
               "func":mathmodule.sfa_cyl,
               "output":("The {0} of the {1} is ", "optioncb.get()", "suboptioncb1.get()")}}

             },

            "Pie Chart":
            {"None":
             {"None":
              {"inputs":
               [(3, "Enter the list of percentages:")],
               "func":mathmodule.pie_chart,
               "outputframe": True}}},

            "Radian-Degree Conversion":
            {"Degrees to Radians":
             {"None":
              {"inputs":
               [(2, "Enter the degree of the angle:")],
               "func":mathmodule.deg_rad,
               "output":"The value in radians is "}},

             "Radians to Degrees":
             {"None":
              {"inputs":
               [(2, "Enter the angle in radians:")],
               "func":mathmodule.rad_deg,
               "output":"The value in degrees is "}},
             }
            
                       
                   
            }



root = Tk()
root.geometry ('500x250')
open_img()

startTime = time()
                
root.after(700, root.destroy)

root.mainloop()

top = Tk()
top.geometry('1020x800')
top.title('Mathable')

#frame for combobox (selection of operation)
optionframe = Frame(top, relief = SUNKEN, borderwidth = 5, bg = '#fafac3')
optionframe.pack(side = TOP, fill = X)



optionlbl = Label(optionframe, text = "Please select an operation from the list below", bg = '#fafac3', font = 'Garamond 13 bold')
optionlbl.grid(row=0, column = 0, pady = 20, padx= 10)

selected = StringVar()


opnvalues = list(fn_dict)

#combobox (selection of operations)
optioncb = ttk.Combobox(optionframe, state = 'readonly', values = opnvalues, textvariable = selected, font = 'Garamond 13 bold')
optioncb.bind("<<ComboboxSelected>>", selection_cb)

optioncb.grid(row=1, column=0, pady = 20, padx = 10)

suboptionlabel1 = None
suboptioncb1 = None
suboptionlabel2 = None
suboptioncb2 = None

subselected1 = StringVar()
subselected2 = StringVar()

#function to perform when the operation SUBMIT button is clicked

optionsubmit = Button(optionframe, text = "Submit", command = optionclicked, bg = '#f5ddbf', activebackground = '#5f4c78', activeforeground = 'white', font = 'Garamond 13 bold')
optionsubmit.grid(row = 2, column = 0, pady = 20)


quit_btn = Button(top, text = "Quit", command = quitwindow, bg = '#ffadad', activebackground = '#5f4c78', activeforeground = 'white', font = 'Garamond 13 bold')
quit_btn.pack(side = BOTTOM)


top.mainloop()
