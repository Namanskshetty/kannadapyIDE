from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title("ಪೈಥಾನ_IDE")#title for the ide
file_path=""

def set_file_path(path):#retins the old file
    global file_path
    file_path=path

def save_as():
    if file_path=="":
        path =asksaveasfilename(filetypes=[("ಪೈಥಾನ ಫೈಲ್","*.py")])#opens the dialog box to save python file
    else:
        path=file_path
    with open(path,"w") as file: #opens path and sends it to file variable
        code=editor.get('1.0',END) #takes all the text from the editor and adds to code
        file.write(code)#writes the above code variable to file
        set_file_path(path)

def open_fie():
    path =askopenfilename(filetypes=[("ಪೈಥಾನ ಫೈಲ್","*.py")])#opens the dialog box to open python file
    with open(path,"r") as file: #opens path and sends it to file variable
        code=file.read()#reads the whole file
        editor.delete('1.0',END) #Deletes from opened file
        editor.insert('1.0',code)#clean formed with replaced with code variable
        set_file_path(path)

def run(): #to run the function
    if file_path=="":#if there is no file it will send this message in order to keep the process from crashing
        save_prompt=Toplevel()#this part gives the prompt
        text=Label(save_prompt,text="ನಿಮ್ಮ ಫಲಿತಾಂಶ ನೋಡುವ ಮುನ್ನ ಫೈಲ ಅನ್ನು ಉಳಿಸಿ್")
        text.pack()
        return
    command=f'python {file_path}'#open file path for the output
    process=subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell= True)#creats the shell
    output, error=process.communicate()
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)

menu_bar=Menu(compiler)
file_menu=Menu(menu_bar,tearoff=8)
file_menu.add_command(label="ತೆರೆ",command=open_fie)
file_menu.add_command(label="ಉಳಿಸು",command=save_as)
file_menu.add_command(label="ಉಳಿಸಿಕೊಳ್ಳವಾ ತರ",command=save_as)
file_menu.add_command(label="ಹೊರಗೆ",command=exit)
menu_bar.add_cascade(label="ಫೈಲ್",menu=file_menu)

run_bar=Menu(menu_bar,tearoff=8)
run_bar.add_command(label="ಓಡು",command=run)
menu_bar.add_cascade(label="ಓಡು",menu=run_bar)

compiler.config(menu=menu_bar)
editor = Text()#give the user permission or the space to write
editor.pack()
code_output=Text(height=8)
code_output.pack()
compiler.mainloop()
