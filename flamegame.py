from tkinter import *  
  
  
def del_same_char(lists01 , lists02):  
    for i in range(len(lists01)) :  
        for j in range(len(lists02)) :  
  
            
            if lists01[i] == lists02[j] :  
                c = lists01[i]  
  
                
                lists01.remove(c)  
                lists02.remove(c)  
  
                
                lists03 = lists01 + ["*"] + lists02  
  
                  
                return [lists03 , True]  
  
    
    lists03 = lists01 + ["*"] + lists02  
    return [lists03 , False]  
  
  

def get_status() :  
      
      
    pl01 = Plyr01_field.get()   
    pl01 = pl01.lower()   
    pl01.replace(" " , "")    
    pl01_list = list(pl01)  
  
     
    pl02 = Plyr02_field.get()  
    pl02 = pl02.lower()  
    pl02.replace(" " , "")  
    pl02_list = list(pl02)  
  
      
    processed = True  
    while processed :    
        rtrn_list = del_same_char(pl01_list , pl02_list)  
        conct_list = rtrn_list[0]   
        processed = rtrn_list[1]  
        a = conct_list.index("*")    
        pl01_list = conct_list[ : a]    
        pl02_list = conct_list[a + 1 : ]  
  
  
    count = len(pl01_list) + len(pl02_list)  
  
    result = ["Friends" , "Love" , "Affection" , "Marriage" , "Enemy" , "Siblings"]  
  
    
    while len(result) > 1 :  
  
         
        a = (count % 
        len(result) - 1)    
          
        if a >= 0 :  
            right = result[a + 1 : ]  
            left = result[ : a]  
  
         
            result = right + left  
  
        else :  
            result = result[ : len(result) - 1]  
          
   
    Value_fields.insert(10 , result[0])  
  
 
def clr_all() :  
    Plyr01_field.delete(0 , END)  
    Plyr02_field.delete(0 , END)  
    Value_fields.delete(0 , END)  
    
    Plyr01_field.focus_set()  
  
# Main code  
if __name__ == "__main__" :  
  
    # Creating a GUI window  
    base = Tk()  
  
    # Setting the bg colour of GUI window  
    base.configure(background = 'light green')  
  
# Setting the configuration of GUI window  
    base.geometry("350x125")  
  
    # setting the name of tkinter GUI window  
    base.title("Flames :)")  
      
    # Creating the Player 1 Name : label  
    lb1 = Label(base , text = " Name1: " ,  
                fg = 'black' , bg = 'pink',height=1, width=7)  
  
    # Creating the Player 2 Name : label  
    lb2 = Label(base , text = "Name2: " ,  
                fg = 'black' , bg = 'pink')  
      
    # Creating a Relation Status : label  
    lb3 = Label(base , text = "Relationship Status: " ,  
                fg = 'black' , bg = 'pink')  
  
      
    lb1.grid(row = 5 , column = 8 , sticky = "E")  
    lb2.grid(row = 6 , column = 8 , sticky = "E" )  
    lb3.grid(row = 8 , column = 8 , sticky = "E")  
  
    
    Plyr01_field = Entry(base)  
    Plyr02_field = Entry(base)  
    Value_fields = Entry(base)  
  
  
    Plyr01_field.grid(row = 5 , column = 9 , ipadx = "50")  
    Plyr02_field.grid(row = 6, column = 9 , ipadx = "50")  
    Value_fields.grid(row = 8 , column = 9 , ipadx = "50")  
  
    
    btn01 = Button(base , text = "Submit" , bg = "red" ,  
                    fg = "black" , command = get_status)  
  
    
    btn02 = Button(base , text = "Clear" , bg = "red" ,  
                    fg = "black" , command = clr_all)  
  
      
    btn01.grid(row = 7, column =9 )  
    btn02.grid(row = 9 , column = 9)  
  
    
    base.mainloop()  