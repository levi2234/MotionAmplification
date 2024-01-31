import time
import math
#get width of terminal
import os





#progress bar
class progress():
    
    def __init__(self, iterable, name=None, color="GREEN", capstyle=">", barstyle="█", clear_on_finish=True):
        self.color = color
        self.color = self.setcolor()
        
        if name is None:
            self.name = ""
        else:
            self.name = name + ":"
        self.iterable = iterable
        self.length = len(iterable)
        self.count = 0
        self.barstyle = barstyle
        self.capstyle = capstyle
        self.clear_on_finish = clear_on_finish
        
    def setcolor(self):
        if self.color == "RED":
            return "\033[31m"
        elif self.color == "GREEN":
            return "\033[32m"
        elif self.color == "YELLOW":
            return "\033[33m"
        elif self.color == "BLUE":
            return "\033[34m"
        elif self.color == "MAGENTA":
            return "\033[35m"
        
        
    
    
    def __iter__(self):
        for i in self.iterable:
            width_in_characters = int(int(os.get_terminal_size().columns) /2)
            
            self.count += 1
            
            percentage = math.floor(self.count/self.length * 100)
            
            
            #get length of text before progress bar
            text_length = len(self.name) + len(str(self.length))
            
            #length of progress bar
            progress_bar_length = width_in_characters - text_length
            #number of characters to fill
            fill_length = int(percentage/100 * progress_bar_length)
            #number of characters to empty
            empty_length = progress_bar_length - fill_length
            #print progress bar
            print(f"{self.color}{self.name} {percentage}% [{self.barstyle*fill_length}{self.capstyle}{' '*empty_length}]", end="\r")
            
            #reset color 
            print("\033[0m", end="\r")
            yield i
        
        
            
            
        #clear progress bar
        if self.clear_on_finish:
            print(" "*int(os.get_terminal_size().columns), end="\r")
        else:
            print("\n", end="\r")
        

