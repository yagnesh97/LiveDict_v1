from tkinter import *
import tkinter.messagebox
from PyDictionary import PyDictionary

root=Tk()
root.title("Live Dictionary (Yagnesh Vakharia)")
root.config(bg='light blue')
root.resizable(width=False, height=False)
pyDict=PyDictionary()
radioVar=IntVar()
usrInput=StringVar()


def layout():
    #Menu bar for File cascade and About command... 
    menuBar=Menu(root)
    fileMenu=Menu(menuBar,tearoff=0)
    fileMenu.add_command(label="Save",command=save)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=ex)
    menuBar.add_cascade(label="File", menu=fileMenu)

    #About command
    menuBar.add_command(label="About",command=about)
    
    #radio buttons
    dictRadio=Radiobutton(root,text="Dictionary",variable=radioVar,value=1)
    antoRadio=Radiobutton(root,text="Antonyms",variable=radioVar,value=2)
    synoRadio=Radiobutton(root,text="Synonyms",variable=radioVar,value=3)

    #Search box & bar
    searchBox=Entry(root,width=30,textvariable=usrInput,bg="#f9e0e8")
    searchBar=Button(root,text="Search",width=15,command=search,bg="white")
    
    #results
    scrollbar = Scrollbar(root)
    scrollbar.grid(sticky=N+S+W,column=4,row=3,rowspan=3)

    global results
    results=Text(root,height=7,width=30,wrap=WORD,yscrollcommand=scrollbar.set,bg="#f9e0e8")
    
    #positions
    dictRadio.grid(row=0,column=0,padx=5,pady=5)
    antoRadio.grid(row=0,column=1,padx=5,pady=5)
    synoRadio.grid(row=0,column=2,padx=5,pady=5)
    searchBox.grid(row=1,columnspan=3,ipady=5,pady=10,sticky=S)
    searchBar.grid(row=2,columnspan=3,sticky=N)
    results.grid(row=3,columnspan=3,pady=10,padx=5)
    scrollbar.config(command=results.yview)

    #end
    root.config(menu=menuBar)
    root.mainloop()

#conditional function calling
def search():
    if radioVar.get()==1:
        dictSearch()
    elif radioVar.get()==2:
        antoSearch()
    else:
        synoSearch()

#dictionary search function
def dictSearch():
    if pyDict.meaning(usrInput.get())==None:
        results.delete(1.0,END)
        results.insert(END,"Sorry the word has no such meanings")
    else:
        results.delete(1.0,END)
        for i in pyDict.meaning(usrInput.get()):
            results.insert(END,i)
            results.insert(END,"\n"+pyDict.meaning(usrInput.get())[i][0]+"\n"+"-"*30+"\n")


#antonym search function                
def antoSearch():
    if pyDict.antonym(usrInput.get())==None:
        results.delete(1.0,END)
        results.insert(END,"Sorry the word has no such antonyms")
    else:
        num=1
        results.delete(1.0,END)
        for i in pyDict.antonym(usrInput.get()):
            results.insert(END,"\n"+str(num)+") "+i+"\n")
            num=int(num)+1


#synonym search function
def synoSearch():
    if pyDict.synonym(usrInput.get())==None:
        results.delete(1.0,END)
        results.insert(END,"Sorry the word has no such synonyms")
    else:
        num=1
        results.delete(1.0,END)
        for i in pyDict.synonym(usrInput.get()):
            results.insert(END,"\n"+str(num)+") "+i+"\n")
            num=int(num)+1


#save function
def save():
    try:
        f=open("dict_"+usrInput.get()+".txt","w")
        f.write(results.get(1.0,END))
        f.close()
    except Exception:
        messagebox.showerror("Error","Something went wrong. Please try again!")



        
#about function
def about():
    tk.messagebox.showinfo("About","This program is created by Yagnesh Vakharia.\nContact: yagneshvakharia97@gmail.com")

#destroying the frame
def ex():
    root.destroy()

layout()
