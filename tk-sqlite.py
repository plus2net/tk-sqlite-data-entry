import tkinter  as tk 
from tkinter import ttk
from tkinter import END
from sqlalchemy import create_engine,text
from sqlalchemy.exc import SQLAlchemyError
from config import my_conn # connection object to Database my_db.db 

my_w = tk.Tk()
my_w.geometry("830x650") # width and height of the window 

def data_insert():
    flag_validation=True # set the flag 
    my_name=name.get() # read name from entry widget
    my_class=class1.get()    # read class from combobox
    
    
    my_gender=gender.get()   # read gender radio button value
    my_address=address.get('1.0',END) # read text data 
    my_hostel=hostel.get() # read checkbox value
    # length of my_name , my_class and my_gender more than 2 
    if(len(my_name) < 2 or len(my_class)<2  or len(my_gender) < 2 ):
            flag_validation=False 
    try:
       my_mark=int(mark.get()) # read mark from entry
    except:
       flag_validation=False 
       msg.config(fg='red',bg='white') # foreground and background colors
       my_str.set("Mark must be integer" )
       msg.after(3000, lambda: my_str.set('Message Here') )
    # add more data validation here   
    if(flag_validation):
       my_str.set("Adding data...")
       try:       
            #my_data=(my_name,my_class,my_mark,my_gender,my_hostel,my_address)
            my_data={'name':my_name,'class':my_class,'mark':my_mark,
                     'gender':my_gender,'hostel':my_hostel,'address':my_address}
            my_query="INSERT INTO student_address (name,class,mark,gender,hostel,address) \
                values (:name,:class,:mark,:gender,:hostel,:address)"
            #print(my_query,my_data)
            r_set=my_conn.execute(text(my_query),my_data)
            my_conn.commit()
            id=r_set.lastrowid

            msg.config(fg='green',bg='white') # foreground and background colors
            my_str.set("Record added,  ID:" + str(id))
            msg.after(3000, lambda: my_str.set('Message Here') )
            show_data() # refresh the data in Treeview
            my_reset() # remove the data inputs from widget 
       except SQLAlchemyError as e:
            error=str(e.__dict__['orig'])
            print(error)
            msg.grid() 
            #return error
            msg.config(fg='red')   # foreground color
            msg.config(bg='yellow') # background color
            print(error)
            my_str.set(error)   
trv = ttk.Treeview(my_w, selectmode ='browse')
trv.grid(row=4,column=1,padx=5,pady=20,columnspan=9)
def show_data():
    global trv
    trv.grid_remove()
    trv = ttk.Treeview(my_w, selectmode ='browse')
    trv.grid(row=4,column=1,padx=5,pady=20,columnspan=9)
    str1="SELECT * FROM student_address  ORDER BY id DESC LIMIT 10"
    r_set=my_conn.execute(text(str1))
    l1=[r for r in r_set.keys()] # List of column headers 
    r_set=[r for r in r_set] # Rows of data
    trv['height']=5 # Number of rows to display, default is 10
    trv['show'] = 'headings' 
    # column identifiers 
    trv["columns"] = l1
    for i in l1:
        trv.column(i, width = 100, anchor ='c')
	# Headings of respective columns
        trv.heading(i, text =i)
    trv.column('address',width=200, anchor='w')
    ## Adding data to treeview 
    for dt in r_set:  
        v=[r for r in dt] # creating a list from each row 
        trv.insert("",'end',iid=v[0],values=v) # adding row
def my_reset():
    for widget in my_w.winfo_children():
        if isinstance(widget, tk.Entry): # If this is an Entry widget class
            widget.delete(0,'end')   # delete all entries 
        if isinstance(widget,ttk.Combobox):
            widget.delete(0,'end') 
        if isinstance(widget,tk.Text):
            widget.delete('1.0','end') # Delete from position 0 till end 
        if isinstance(widget,tk.Checkbutton):
            widget.deselect()

font1=['Arial',18,'normal']
font2=['Arial',10,'normal']
my_w.option_add("*TCombobox*Listbox*Font", font1)

lb1 = tk.Label(my_w,  text='Name', width=5,font=font1 )  
lb1.grid(row=1,column=1,sticky='w',padx=2)
name = tk.Entry(my_w, width=10,bg='lightyellow',font=font1) # added one Entry box
name.grid(row=2,column=1,padx=2)

lb2 = tk.Label(my_w,  text='Class', width=5,font=font1 )  
lb2.grid(row=1,column=2,sticky='w',padx=2)
class_list=['One','Two','Three']
class1 = ttk.Combobox(my_w, values=class_list,width=5,font=font1)
class1.grid(row=2,column=2)

lb3 = tk.Label(my_w,  text='Mark', width=5,font=font1 )  
lb3.grid(row=1,column=3,sticky='w',padx=2)

mark = tk.Entry(my_w, width=3,bg='lightyellow',font=font1) # added one Entry box
mark.grid(row=2,column=3)

lb4 = tk.Label(my_w,  text='Gender', width=7,font=font1 )  
lb4.grid(row=1,column=4,sticky='w',columnspan=3)

gender = tk.StringVar()  # string variable for radio buttons 
gender.set('Female')     # assigned one  value 

r1 = tk.Radiobutton(my_w, text='Male', variable=gender, value='Male')
r1.grid(row=2,column=4) 

r2 = tk.Radiobutton(my_w, text='Female', variable=gender, value='Female')
r2.grid(row=2,column=5) 

r3 = tk.Radiobutton(my_w, text='Others', variable=gender, value='Others')
r3.grid(row=2,column=6) 

lb5 = tk.Label(my_w,  text='Address', width=9,font=font1 )  
lb5.grid(row=1,column=7,sticky='w')

address = tk.Text(my_w, width=20,bg='yellow' , height=3) # Text
address.grid(row=2,column=7,sticky='w')

lb6 = tk.Label(my_w,  text='Hostel', width=7,font=font1 )  
lb6.grid(row=1,column=8)

hostel=tk.BooleanVar(value=False)
c1 = tk.Checkbutton(my_w, font=font1, variable=hostel,
	onvalue=True,offvalue=False,anchor='c')
c1.grid(row=2,column=8)

bt1_add = tk.Button(my_w,   width=4,bg='lightgreen',font=font1,text='Add',command=data_insert) # added one Entry box
bt1_add.grid(row=2,column=9)
my_str=tk.StringVar()
msg=tk.Label(my_w,text='Messages here',font=font1,textvariable=my_str)
msg.grid(row=3,column=1,padx=5,columnspan=9,sticky='w')
# Style for Treeview 
style = ttk.Style(my_w) 
style.theme_use("clam") # set theam to clam
style.configure("Treeview", background="black",rowheight=80,font=font1,
                fieldbackground="black", foreground="white")
style.configure('Treeview.Heading', background="PowderBlue")


def delete_data2():
    global trv
    try:
        p_id = trv.selection()[0] # collect selected row id
        str1="DELETE FROM student_address  WHERE id="+str(p_id)
        r_set=my_conn.execute(text(str1))
        msg.config(fg='green',bg='white') # foreground and background colors
        my_str.set("Record deleted  ")
        msg.after(3000, lambda: my_str.set('Message Here') )
        show_data() # refresh Treeview to reflect the changes
    except:
        msg.config(fg='red',bg='white') # foreground and background colors
        my_str.set("Select a Record first ")
        # foreground and background colors
        msg.after(3000, lambda: my_str.set('Message Here') )
        msg.after(3000,lambda:msg.config(fg='green',bg='white')) 
bt2_delete = tk.Button(my_w,   bg='Red',font=font1,text='Delete row',command=delete_data2) # added one Entry box
bt2_delete.grid(row=5,column=1,columnspan=2)

show_data() # display data in treeview while opening
my_w.mainloop()