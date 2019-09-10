from tkinter import *
import tkinter.messagebox

root=Tk()
root.title("words batch correcter")
root.resizable(0, 0)
root.geometry("+{}+{}".format(600, 400))
mainFrame = Frame(root, width=600, height=400)
mainFrame.pack()
textFrame = Frame(mainFrame, width=100, height=100)
textFrame.pack()
textFrame_1 = Frame(mainFrame, width=100, height=100)
textFrame_1.pack()
textFrame_2 = Frame(mainFrame,width=100, height=100)
textFrame_2.pack()

scrollbar = Scrollbar(textFrame)
scrollbar.pack(side=RIGHT, fill="y")
#textField == sentance
textField = Text(textFrame, width=50, height=10, bd=5, 
 relief="groove")
textField.insert(CURRENT,"enter the text")
textField.pack(side=LEFT, padx=(5, 0), pady=(5, 5))
textField["yscrollcommand"] = scrollbar.set

#textField_2 == wrong word
textField_2= Text(textFrame_1, width=15, height=3, bd=5, 
 relief="groove")
textField_2.insert(CURRENT,"wrong words")
textField_2.pack(side=LEFT, padx=(5,0), pady=(5,5))
#textField_3 == correct word
textField_3= Text(textFrame_1,width=15, height=3, bd=5, 
 relief="groove")
textField_3.insert(CURRENT, "correct words")
textField_3.pack(side=LEFT, padx=(5,0), pady=(5,5))



scrollbar_2 = Scrollbar(textFrame_2)
scrollbar_2.pack(side=RIGHT, fill="y")
textField_4 = Text(textFrame_2, width=50, height=10, bd=5, 
 relief="groove")
textField_4.pack(side=LEFT, padx=(5, 0), pady=(5, 5))
textField_4["yscrollcommand"] = scrollbar_2.set    




def chg():
    sentance = textField.get("1.0",END)
    wrong_word = textField_2.get("1.0",END)
    correct_word = textField_3.get("1.0",END)
    result = str(sentance).replace(wrong_word.strip('\n'), correct_word.strip('\n'))

    textField_4.insert("1.0",result,END)

def res():
    textField_4.delete("1.0",END)
    textField.delete("1.0",END)
def cnt():
    sentance = textField.get("1.0",END)
    wrong_word = textField_2.get("1.0",END)
    correct_word = textField_3.get("1.0",END)
    textField_4.insert("1.0","It was correctted " + str(sentance.count(wrong_word.strip('\n')))+" words\n",END)
    
def msg():
    tkinter.messagebox.showerror("error","there's no words")



def ok():
    sentance = textField.get("1.0",END)
    wrong_word = textField_2.get("1.0",END)
    correct_word = textField_3.get("1.0",END)
    if wrong_word.strip('\n') in str(sentance):
        chg()
        textField_4.insert("1.0","   -------------------------------------------\n",END) 
        cnt()
       
        

    else:
         msg()
    
    

    
okButton = Button(textFrame_1, text="OK", command=ok, height=1, width=4)
okButton.pack(padx=43, pady=(4,5))

resButton = Button(textFrame_1, text="RESET", command=res,height=1,width=4)
resButton.pack() 

root.mainloop()
