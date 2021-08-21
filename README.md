# SimpleKeyLogger
================================================================

A simple key-logger created using python and the pynput library.

This project was created as an initial attempt to create a key
logging application. Further improvments will be made, using
this project as a base. Separate repositories will be created.

# Functions/features:
================================================================

When opening the application the pynput "listener" is used to
read keyboard inputs. 

The data from these inputs are stored in a list, set to store
10 inputs of data, this can be changed by editing line 19 of
the python file.

Once there are 10 inputs stored in the list, it is written to
the text file "rawlog.txt".

The application removes unnecessary text from the data, when 
a key is pressed the listener states "Key.F". "Key" is removed
to make the data in the text file easier to read.

Where the space bar would also be notated as "Key.space", the
application changes it to a blank space " ". To futher make
the text file show an accurate representation of the keyboard 
input.

The application will close when the "ESC" key has been pressed,
any data in the list that has not yet been written to the text
file will be completed before exiting.

# Further Development
================================================================

I currently have plans for 2 major developments within this
application.

Firstly when the backspace key is pressed, the application
currently prints a space " ". I want to fix this issue and find
a way to overwrite the letters being deleted by the user in using
the backspace key.

Secondly this application is to be run from a USB stick. Another
project running in parallel with this, is setting a USB stick to
be hidden by the OS when plugged in, so that the keylogger can
run without the knowledge of the user.

# Included in Repository
================================================================

-KeyLogger.py
Python file that includes all code needed for the running of the
key logger application.

-KeyLogger.pyproj
Python project file created by visual studio, is not needed for
running the application, but may be useful for VS users.

-rawlog.txt
Text file used for storing the data collected during the running
of the KeyLogger application.

-README.md
This file, details regarding the application and the folder it 
sits in.

# Statement regarding intent and usage
================================================================

This project is created for the sole purpose of education and 
will not be used in malicious ways or for the purpose of causing
harm or any person or organisation.
