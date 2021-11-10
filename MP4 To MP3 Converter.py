from tkinter import *
from tkinter import filedialog, messagebox
from moviepy import editor as e


root = Tk()
root.title("MP4 To MP3 Converter")
root.geometry("300x200")

root.configure(bg='black')


def file_import():
    global file
    file = filedialog.askopenfilename(initialdir="c:/Users/Welcome/Videos", title='Select The File', filetype=(("MP4", "*.mp4"), ("AVI", "*.avi"), ("MKV", "*.mkv"), ("All Files", "*.*")))
    path.insert(0,str(file))


Label(root, text="MP4 To MP3 Converter", font=("monotype corsiva", 18, "italic", 'bold'), fg='white', bg='black').pack(pady=5)
path= Entry(root, bd=0, width=25, font=('times', 15, 'italic', 'underline'), bg='black', fg='#008FE2')
path.pack(pady=0)
video =Button(root, text='Import Video File', command=file_import, bg='black', fg='gray', activebackground='black', activeforeground="#00FFFF", font=("monotype corsiva", 15, "italic"), bd=0)
video.pack(pady=0)



def export_mp3():
    if len(path.get()) != 0:
        convert = e.VideoFileClip(file)
        converted = filedialog.asksaveasfilename(initialdir="c:/Users/Welcome/Music", title='Name The File', defaultextension='.mp3', filetype=(("MP3", "*.mp3"), ("WAV", "*.wav"), ("All Files", "*.*")))
        convert.audio.write_audiofile(converted)
        messagebox.showinfo("MP4 To MP3 Converter", "MP3 Extracted")
        path.delete(0, END)
    else:
        messagebox.showerror("MP4 To MP3 Converter", "No File Was Imported, \n Please Import A Video File")


def exit():
    d = messagebox.askquestion('Exit Application', "Do You Want Exit The Application?")
    if d =="yes":
        root.destroy()
    else:
        return None



video =Button(root, text='Export Audio', command=export_mp3, bg='black', fg='gray', activebackground='black', activeforeground="#00FF00", font=("monotype corsiva", 15, "italic"), bd=0)
video.pack(pady=0)
close = Button(root, text='Exit', command=exit, bd=0, font=("monotype corsiva", 15, "italic"), bg='black', fg='gray', activebackground='black', activeforeground='#ff0000').pack(pady=0)


root.mainloop()