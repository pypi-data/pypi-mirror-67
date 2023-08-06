# EbookMaker


EbookMaker is the tool used for format conversion at Project Gutenberg.
It builds EPUB2 and Kindle files from HTML.
Also it builds HTML4, EPUB2, Kindle, and PDF files from reST sources.


## Prerequisites

* Python2 >= 2.7 or Python3 >= 3.6
* HTMLTidy (http://binaries.html-tidy.org/),
* Kindlegen (https://www.amazon.com/gp/feature.html/?docId=1000765211) or Calibre (https://calibre-ebook.com/)
* TexLive (to build from TeX), and
* groff (not sure when this is needed).

For cover generation

* Cairo https://www.cairographics.org/download/
* Noto Sans and Noto Sans CJK:
    * CentOS or RedHat: `yum install google-noto-sans-cjk-fonts; yum install google-noto-sans-fonts`
    * Ubuntu: `apt-get install fonts-noto-cjk fonts-noto`

Tested with Python 3.6

## Install

(master branch, editable install)
`pipenv install ebookmaker`

Use the ebookmaker.conf file to pass a path to your kindlegen, tex, and groff programs 
if they're not in your PATH. Edit the ebookmaker.conf and copy it to /etc/ebookmaker.conf to 
reset the paths.
Copy ebookmaker.conf to ~/.ebookmaker to override settings in /etc/ebookmaker.conf or to set default 
command line options.

## Sample invocation

(From the directory where you ran `pipenv install`)

`pipenv shell`
`ebookmaker -v -v --make=epub.images --output-dir=/Documents/pg /Documents/library/58669/58669-h/58669-h.htm`

or

`pipenv run ebookmaker -v -v --make=epub.images --output-dir=/Documents/pg /Documents/library/58669/58669-h/58669-h.htm`



## new to pipenv?

Install pipenv  (might be `pip install --user pipenv`, depending on your default python)

`$ pip3 install --user pipenv`

The default install location is `${HOME}/.local/bin`, so add this to your login shell's ${PATH} if needed.

Change directories to where you want to have your ebookmaker environment. Then, to initialize a python 3 virtual environment, do

`$ pipenv --three`

Whenever you want to enter this environment, move to this directory and do:

`$ pipenv shell`
 
Install the gutenberg modules:

`$ pipenv install ebookmaker`

Check your install:

`$ ebookmaker --version`
`EbookMaker 0.9.0`

Since you're in the shell, you can navigate to a book's directory and convert it:

`$ ebookmaker -v -v --make=epub.images --ebook 10001 --title "The Luck of the Kid" --author "Ridgwell Cullum" luck-kid.html`

## Update

`$ cd ebookmaker` to whever you ran `$ pipenv install ebookmaker`

then:

`$ pipenv update ebookmaker`

## Test

Install, as above.

`$ cd ebookmaker` to whever you ran `$ pip install ebookmaker`

then:

`$ git checkout master`

`$ pipenv install -e .`

`$ python setup.py test`

Travis-CI will run tests on branches committed in the gutenbergtools org

## Notes running Ebookmaker on Windows Machine (adapted from @windymilla)

1. Install Python 3.6+ from python.org. Install HTML Tidy - it doesn't come preinstalled on Windows. Add it to the path.
2. Add system environment variable: Right-click "My Computer", then Properties, then Advanced, then Environment variables, then New. Call the variable PYTHON_HOME, and set it to the Python folder.
3. Edit the Path variable and add to the end of it `;%PYTHON_HOME%\;%PYTHON_HOME%\Scripts\`
4. Check by starting a new command window and typing `python`. It should run your version of Python. Quit python with `^Z` & Enter.
5. In command window, type `pip3 install --user pipenv`. Script may warn it has put scripts into a folder such as `C:\Users\myname\AppData\Roaming\Python\Python37\Scripts`, and to add this to the Path environment variable. Do this – don't forget the semicolon before the new folder name! (Possibly might work instead to just copy the newly installed files from where they were installed into your main python scripts folder, i.e. `%PYTHON_HOME%\Scripts` ?)
6. Close old command window and start a new (to get the new path)
7. Create a folder for ebookmaker, e.g. `C:\DP\ebookmaker`
8. In command window, go to the new folder
9. Type `pipenv --three` (note double hyphen) – it will create a "virtual environment", with a new folder, something like `C:\Users\myname\.virtualenvs\ebookmaker-cgaQuYhi`
10. Type `pipenv shell` – prompt will change while in virtual environment
11. Type `pipenv install ebookmaker` – takes a while to install
12. Download GTK+ to get Cairo. Precompiled Win32 binaries are here: http://ftp.gnome.org/pub/gnome/binaries ... _win32.zip
13. Unzip this to a folder, e.g. `C:\DP\gtk` and add `C:\DP\gtk\bin` to the Path environment variable.
14. Exit command window and start a new one to get new path
15. Go to the ebookmaker folder, `C:\DP\ebookmaker`
16. Type `pipenv run python ebookmaker --version` to check ebookmaker version. If this doesn't work (it should, but didn't work for us) try:
    - Look in `C:\Users\myname\.virtualenvs\` and find the name of your virtualev it should be something like `ebookmaker-cgaQuYhi`
    - Type `pipenv run python C:\Users\myname\.virtualenvs\<name of vitualenv>\Scripts\ebookmaker --version` to check ebookmaker version. 
17. If there's error like like no "cairo" or "cairo-2" found, check if your libcairo and libcairo-2 path exist. If they do, edit dlopen in  _init_.py in cairocffi package. Return the path found by ctypes.util.find_library directly instead of calling ffi.dlopen(path).
