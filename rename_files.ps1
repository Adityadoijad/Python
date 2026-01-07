# PowerShell script to rename Tutorial files to python files
# Uses git mv to preserve history

Write-Host "Renaming Tutorial files to python files..." -ForegroundColor Green

# Rename main tutorial files (Tutorial1.py -> python1.py)
git mv Tutorial1.py python1.py; git commit -m "Basics - Hello World & Print Statement"
git mv Tutorial2.py python2.py; git commit -m "Comments, Escape Sequences, and Print Statement Parameters"
git mv Tutorial3.py python3.py; git commit -m "Variables and Data Types"
git mv Tutorial4.py python4.py; git commit -m "Type Casting (Explicit and Implicit)"
git mv Tutorial5.py python5.py; git commit -m "Taking User Input"
git mv Tutorial6.py python6.py; git commit -m "Strings"
git mv Tutorial7.py python7.py; git commit -m "String Slicing"
git mv Tutorial8.py python8.py; git commit -m "String Methods"
git mv Tutorial9.py python9.py; git commit -m "If-Else Statements"
git mv Tutorial10.py python10.py; git commit -m "Match Case Statement"
git mv Tutorial11.py python11.py; git commit -m "For Loop"
git mv Tutorial12.py python12.py; git commit -m "While Loop"
git mv Tutorial13.py python13.py; git commit -m "Break and Continue Statements"
git mv Tutorial14.py python14.py; git commit -m "Do-While Loop Emulation"
git mv Tutorial15.py python15.py; git commit -m "Functions"
git mv Tutorial16.py python16.py; git commit -m "Function Arguments (Default, Keyword, Required, Variable Length)"
git mv Tutorial17.py python17.py; git commit -m "Lists"
git mv Tutorial18.py python18.py; git commit -m "List Methods"
git mv Tutorial19.py python19.py; git commit -m "Tuples"
git mv Tutorial20.py python20.py; git commit -m "Manipulating Tuples and Tuple Methods"
git mv Tutorial21.py python21.py; git commit -m "f-Strings (String Formatting)"
git mv Tutorial22.py python22.py; git commit -m "Docstrings"
git mv Tutorial23.py python23.py; git commit -m "Recursion"
git mv Tutorial24.py python24.py; git commit -m "Sets"
git mv Tutorial25.py python25.py; git commit -m "Set Methods"
git mv Tutorial26.py python26.py; git commit -m "Dictionaries"
git mv Tutorial27.py python27.py; git commit -m "Dictionary Methods"
git mv Tutorial28.py python28.py; git commit -m "Else with For and While Loop"
git mv Tutorial29.py python29.py; git commit -m "Exception Handling (try-except)"
git mv Tutorial30.py python30.py; git commit -m "Finally Keyword"
git mv Tutorial31.py python31.py; git commit -m "Raising Custom Errors"
git mv Tutorial32.py python32.py; git commit -m "Short Hand If-Else Statement"
git mv Tutorial33.py python33.py; git commit -m "Enumerate Function"
git mv Tutorial34.py python34.py; git commit -m "Virtual Environment"
git mv Tutorial35_1.py python35_1.py; git commit -m "Import and __name__==__main__"
if (Test-Path "Tutorial35_2.py") { git mv Tutorial35_2.py python35_2.py; git commit -m "Import Module Helper File" }
git mv Tutorial36.py python36.py; git commit -m "OS Module"
git mv Tutorial37.py python37.py; git commit -m "Local and Global Variables"
git mv Tutorial38.py python38.py; git commit -m "File I/O (File Handling - Read, Write, Append)"
git mv Tutorial39.py python39.py; git commit -m "readline() and writelines() Functions"
git mv Tutorial40.py python40.py; git commit -m "seek(), tell() and truncate() Functions"
git mv Tutorial41.py python41.py; git commit -m "Lambda Functions"
git mv Tutorial42.py python42.py; git commit -m "Map, Filter and Reduce Functions"
git mv Tutorial43.py python43.py; git commit -m "is vs == Operators"
git mv Tutorial44.py python44.py; git commit -m "OOPS Concept Introduction"
git mv Tutorial45.py python45.py; git commit -m "Class and Objects"
git mv Tutorial46.py python46.py; git commit -m "Constructors (__init__)"
git mv Tutorial47.py python47.py; git commit -m "Decorators"
git mv Tutorial48.py python48.py; git commit -m "Getters and Setters"
git mv Tutorial49.py python49.py; git commit -m "Inheritance"
git mv Tutorial50.py python50.py; git commit -m "Access Specifiers/Modifiers (Public, Private, Protected)"
git mv Tutorial51.py python51.py; git commit -m "Static Methods"
git mv Tutorial52.py python52.py; git commit -m "Instance vs Class Variables"
git mv Tutorial53.py python53.py; git commit -m "Class Methods"
git mv Tutorial54.py python54.py; git commit -m "Class Methods as Alternative Constructors"
git mv Tutorial55.py python55.py; git commit -m "dir(), __dict__ and help() Methods"
if (Test-Path "Tutorial56.py") { git mv Tutorial56.py python56.py; git commit -m "Super Keyword" }
if (Test-Path "TUtorial56.py") { git mv TUtorial56.py python56_alt.py; git commit -m "Super Keyword" }
if (Test-Path "Tutorial57.py") { git mv Tutorial57.py python57.py; git commit -m "Magic/Dunder Methods" }
if (Test-Path "TUtorial57emp.py") { git mv TUtorial57emp.py python57emp.py; git commit -m "Magic/Dunder Methods - Employee Example" }
git mv Tutorial58.py python58.py; git commit -m "Method Overriding"
git mv Tutorial59.py python59.py; git commit -m "Operator Overloading"
git mv Tutorial60.py python60.py; git commit -m "Single Inheritance"
git mv Tutorial61.py python61.py; git commit -m "Multiple Inheritance"
if (Test-Path "tutorial62.py") { git mv tutorial62.py python62.py; git commit -m "Multilevel Inheritance" }
git mv Tutorial63.py python63.py; git commit -m "Hybrid Inheritance"
git mv Tutorial64.py python64.py; git commit -m "Hierarchical Inheritance"
git mv Tutorial65.py python65.py; git commit -m "Time Module"
git mv Tutorial66.py python66.py; git commit -m "Walrus Operator (:=)"
git mv Tutorial67.py python67.py; git commit -m "Shutil Module (File and Directory Operations)"
git mv Tutorial68.py python68.py; git commit -m "Requests Module (HTTP Requests)"
git mv Tutorial69.py python69.py; git commit -m "Generators"
git mv Tutorial70.py python70.py; git commit -m "Function Caching"
git mv Tutorial71.py python71.py; git commit -m "Regular Expressions"
git mv Tutorial72.py python72.py; git commit -m "AsyncIO"
git mv Tutorial73.py python73.py; git commit -m "Multithreading"
git mv Tutorial74.py python74.py; git commit -m "Multiprocessing with ThreadPoolExecutor"

# Rename supporting txt files
Write-Host "`nRenaming supporting txt files..." -ForegroundColor Yellow
if (Test-Path "Tutorial38.txt") {
    git mv Tutorial38.txt python38.txt
    git commit -m "Rename Tutorial38.txt to python38.txt"
}

if (Test-Path "Tutorial39.txt") {
    git mv Tutorial39.txt python39.txt
    git mv Tutorial39one.txt python39one.txt
    git mv Tutorial39x.txt python39x.txt
    git commit -m "Rename Tutorial39 txt files to python39 files"
}

if (Test-Path "Tutorial40.txt") {
    git mv Tutorial40.txt python40.txt
    git commit -m "Rename Tutorial40.txt to python40.txt"
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "File renaming complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "`nNext: Update README.md and index.txt with new filenames" -ForegroundColor Yellow
