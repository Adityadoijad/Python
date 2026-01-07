# PowerShell script to commit all tutorial files with proper commit messages
# Navigate to the Python Tutorials directory before running this script

Write-Host "Starting Git repository setup for Python Tutorials..." -ForegroundColor Green

# Initialize git repository if not already initialized
if (-not (Test-Path ".git")) {
    Write-Host "Initializing git repository..." -ForegroundColor Yellow
    git init
    Write-Host "Git repository initialized!" -ForegroundColor Green
}
else {
    Write-Host "Git repository already exists." -ForegroundColor Cyan
}

# Create .gitignore file
Write-Host "Creating .gitignore file..." -ForegroundColor Yellow
@"
# Python
__pycache__/
*.py[cod]
*`$py.class
*.so
.Python
env/
venv/
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Images (if generated)
*.jpg
*.png
"@ | Out-File -FilePath ".gitignore" -Encoding UTF8
git add .gitignore
git commit -m "Add .gitignore"

# Commit README and LICENSE first
Write-Host "`nCommitting documentation files..." -ForegroundColor Yellow
git add README.md LICENSE
git commit -m "Add README and LICENSE"

# Commit index.txt
Write-Host "Committing index file..." -ForegroundColor Yellow
git add index.txt
git commit -m "index"

# Commit each tutorial file individually
Write-Host "`nCommitting tutorial files..." -ForegroundColor Yellow

git add Tutorial1.py; git commit -m "Basics - Hello World & Print Statement"
git add Tutorial2.py; git commit -m "Comments, Escape Sequences, and Print Statement Parameters"
git add Tutorial3.py; git commit -m "Variables and Data Types"
git add Tutorial4.py; git commit -m "Type Casting (Explicit and Implicit)"
git add Tutorial5.py; git commit -m "Taking User Input"
git add Tutorial6.py; git commit -m "Strings"
git add Tutorial7.py; git commit -m "String Slicing"
git add Tutorial8.py; git commit -m"String Methods"
git add Tutorial9.py; git commit -m "If-Else Statements"
git add Tutorial10.py; git commit -m "Match Case Statement"
git add Tutorial11.py; git commit -m "For Loop"
git add Tutorial12.py; git commit -m "While Loop"
git add Tutorial13.py; git commit -m "Break and Continue Statements"
git add Tutorial14.py; git commit -m "Do-While Loop Emulation"
git add Tutorial15.py; git commit -m "Functions"
git add Tutorial16.py; git commit -m "Function Arguments (Default, Keyword, Required, Variable Length)"
git add Tutorial17.py; git commit -m "Lists"
git add Tutorial18.py; git commit -m "List Methods"
git add Tutorial19.py; git commit -m "Tuples"
git add Tutorial20.py; git commit -m "Manipulating Tuples and Tuple Methods"
git add Tutorial21.py; git commit -m "f-Strings (String Formatting)"
git add Tutorial22.py; git commit -m "Docstrings"
git add Tutorial23.py; git commit -m "Recursion"
git add Tutorial24.py; git commit -m "Sets"
git add Tutorial25.py; git commit -m "Set Methods"
git add Tutorial26.py; git commit -m "Dictionaries"
git add Tutorial27.py; git commit -m "Dictionary Methods"
git add Tutorial28.py; git commit -m "Else with For and While Loop"
git add Tutorial29.py; git commit -m "Exception Handling (try-except)"
git add Tutorial30.py; git commit -m "Finally Keyword"
git add Tutorial31.py; git commit -m "Raising Custom Errors"
git add Tutorial32.py; git commit -m "Short Hand If-Else Statement"
git add Tutorial33.py; git commit -m "Enumerate Function"
git add Tutorial34.py; git commit -m "Virtual Environment"
git add Tutorial35_1.py; git commit -m "Import and __name__==__main__"
if (Test-Path "Tutorial35_2.py") { git add Tutorial35_2.py; git commit -m "Import Module Helper File" }
git add Tutorial36.py; git commit -m "OS Module"
git add Tutorial37.py; git commit -m "Local and Global Variables"
git add Tutorial38.py; git commit -m "File I/O (File Handling - Read, Write, Append)"
git add Tutorial39.py; git commit -m "readline() and writelines() Functions"
git add Tutorial40.py; git commit -m "seek(), tell() and truncate() Functions"
git add Tutorial41.py; git commit -m "Lambda Functions"
git add Tutorial42.py; git commit -m "Map, Filter and Reduce Functions"
git add Tutorial43.py; git commit -m "is vs == Operators"
git add Tutorial44.py; git commit -m "OOPS Concept Introduction"
git add Tutorial45.py; git commit -m "Class and Objects"
git add Tutorial46.py; git commit -m "Constructors (__init__)"
git add Tutorial47.py; git commit -m "Decorators"
git add Tutorial48.py; git commit -m "Getters and Setters"
git add Tutorial49.py; git commit -m "Inheritance"
git add Tutorial50.py; git commit -m "Access Specifiers/Modifiers (Public, Private, Protected)"
git add Tutorial51.py; git commit -m "Static Methods"
git add Tutorial52.py; git commit -m "Instance vs Class Variables"
git add Tutorial53.py; git commit -m "Class Methods"
git add Tutorial54.py; git commit -m "Class Methods as Alternative Constructors"
git add Tutorial55.py; git commit -m "dir(), __dict__ and help() Methods"
if (Test-Path "Tutorial56.py") { git add Tutorial56.py; git commit -m "Super Keyword" }
if (Test-Path "TUtorial56.py") { git add TUtorial56.py; git commit -m "Super Keyword" }
if (Test-Path "Tutorial57.py") { git add Tutorial57.py; git commit -m "Magic/Dunder Methods" }
if (Test-Path "TUtorial57emp.py") { git add TUtorial57emp.py; git commit -m "Magic/Dunder Methods - Employee Example" }
git add Tutorial58.py; git commit -m "Method Overriding"
git add Tutorial59.py; git commit -m "Operator Overloading"
git add Tutorial60.py; git commit -m "Single Inheritance"
git add Tutorial61.py; git commit -m "Multiple Inheritance"
if (Test-Path "tutorial62.py") { git add tutorial62.py; git commit -m "Multilevel Inheritance" }
git add Tutorial63.py; git commit -m "Hybrid Inheritance"
git add Tutorial64.py; git commit -m "Hierarchical Inheritance"
git add Tutorial65.py; git commit -m "Time Module"
git add Tutorial66.py; git commit -m "Walrus Operator (:=)"
git add Tutorial67.py; git commit -m "Shutil Module (File and Directory Operations)"
git add Tutorial68.py; git commit -m "Requests Module (HTTP Requests)"
git add Tutorial69.py; git commit -m "Generators"
git add Tutorial70.py; git commit -m "Function Caching"
git add Tutorial71.py; git commit -m "Regular Expressions"
git add Tutorial72.py; git commit -m "AsyncIO"
git add Tutorial73.py; git commit -m "Multithreading"
git add Tutorial74.py; git commit -m "Multiprocessing with ThreadPoolExecutor"

# Commit supporting text files
Write-Host "`nCommitting supporting files..." -ForegroundColor Yellow
if (Test-Path "Tutorial38.txt") {
    git add Tutorial38.txt
    git commit -m "Add Tutorial 38 practice file for File I/O"
    Write-Host "Committed: Tutorial38.txt" -ForegroundColor Green
}

if (Test-Path "Tutorial39.txt") {
    git add Tutorial39.txt Tutorial39one.txt Tutorial39x.txt
    git commit -m "Add Tutorial 39 practice files for readline/writelines"
    Write-Host "Committed: Tutorial39 practice files" -ForegroundColor Green
}

if (Test-Path "Tutorial40.txt") {
    git add Tutorial40.txt
    git commit -m "Add Tutorial 40 practice file for seek/tell/truncate"
    Write-Host "Committed: Tutorial40.txt" -ForegroundColor Green
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Git setup complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "`nNext steps:" -ForegroundColor Yellow
Write-Host "1. Create a repository on GitHub" -ForegroundColor White
Write-Host "2. Add remote: git remote add origin YOUR-REPO-URL" -ForegroundColor White
Write-Host "3. Push to GitHub: git push -u origin main" -ForegroundColor White
Write-Host ""
Write-Host "Total commits created: " -NoNewline -ForegroundColor Cyan
git rev-list --count HEAD
