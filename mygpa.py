#Csv file including information about students and modules with grades achieved are given
#import CSV module to read given file
from dataclasses import dataclass, field    # for procedual programming
import shutil                               # To move a temporary file into stock.csv               
from typing import List                     # For working with shopping lists and shop stock
import csv                                  
import subprocess                           # For clearing the screen
from tempfile import NamedTemporaryFile     # To create a temporary file when writing a CSV




filename = '../CTASample.csv'


# Clear the screen
subprocess.call("cls", shell=True)
print("\t\t GPA Calculator \n++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


@dataclass
class Module:
    grade: int 
    module_name: str = ""

@dataclass
class Student:
    Grade: int
    student_name: str = ""
    Module_List: List[Module]=field(default_factory=list) 

@dataclass
class GPA_Calculator:
    student: List[Student] = field(default_factory=list)
    

# PART 1: Student

# Stock the shop from CSV using the above classes
def create_and_stock_gpa():
    s = GPA_Calculator()
    # Open the stock.csv file
    try:
        with open('../CTASample.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Second row is the first for program
            
            first_row = next(csv_reader)
            print(first_row)
            s.Module_Name = str(first_row[1])
            # Stock up the rest of the csv as product list
            for row in csv_reader:
                p = Student(row[0], str(row[1]))
                ps = Module(p, str(row[2]))
                # Add to the list of items
                s.student.append(ps)
                
        return s
    except FileNotFoundError:
        print(f">>>> ERROR: cannot open {filename}")
