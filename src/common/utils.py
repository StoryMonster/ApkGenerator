import os
import queue

def put_widget_at_center_of_screen(widget):
    screen_width = widget.winfo_screenwidth()
    screen_height = widget.winfo_screenheight()
    client_width = widget.winfo_width()
    client_height = widget.winfo_height()
    client_x_position = int((screen_width - client_width)/2)
    client_y_position = int((screen_height - client_height)/2)
    widget.geometry('{}x{}'.format(client_width, client_height))
    widget.geometry('+{}+{}'.format(client_x_position, client_y_position))


def get_all_java_files(path):
    files = []
    dirs = queue.Queue()
    dirs.put(path)
    while not dirs.empty():
        dir = dirs.get()
        cwd_files = os.listdir(dir)
        for file in cwd_files:
            filepath = os.path.join(dir, file)
            if os.path.isfile(filepath) and file[-5:] == ".java":
                files.append(filepath)
            elif os.path.isdir(filepath):
                dirs.put(filepath)
    return files

def get_R_java_file(path):
    dirs = queue.Queue()
    dirs.put(path)
    while not dirs.empty():
        dir = dirs.get()
        cwd_files = os.listdir(dir)
        for file in cwd_files:
            filepath = os.path.join(dir, file)
            if file == "R.java":
                 return filepath
            elif os.path.isdir(filepath):
                dirs.put(filepath)
    return None

def remove_all_under_folder(folder, depth=0):
    files = os.listdir(folder)
    for file in files:
        filepath = os.path.join(folder, file)
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            remove_all_under_folder(filepath, depth+1)
    if depth != 0:
        os.rmdir(folder)

