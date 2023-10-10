from tkinter import Tk, Frame


def __set_key(e, root):
    """
    e - event with attribute 'char', the released key
    """
    global key_pressed
    if e.char:
        key_pressed = e.char
        root.destroy()


def get_key(msg="Press any key ...", time_to_sleep=3):
    """
    msg - set to empty string if you don't want to print anything
    time_to_sleep - default 3 seconds
    """
    global key_pressed
    if msg:
        print(msg)
    key_pressed = None
    root = Tk()
    root.overrideredirect(True)
    frame = Frame(root, width=0, height=0)
    frame.bind("<KeyRelease>", lambda f: __set_key(f, root))
    frame.pack()
    root.focus_set()
    frame.focus_set()
    frame.focus_force()  # doesn't work in a while loop without it
    root.after(time_to_sleep * 1000, func=root.destroy)
    root.mainloop()
    root = None  # just in case
    return key_pressed


def __main():
        c = None
        while c != "x":
                c = get_key("", 2)
                if c == "w":
                    print("Robot goes forward")
                if c == "a":
                    print("Robot turns left")
                if c == "d":
                    print("Robot turns right")
                if c == "s":
                    print("Robot goes backward")
                    
        print("You exited out of it.")

if __name__ == "__main__":
    __main()
