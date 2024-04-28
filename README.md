**Pool Game with Physics Simulation:**

This project is a pool game that utilizes physics to calculate ball movements and interactions. The core functionality is implemented in a C code file, and a Python file connects it to a server. Additionally, the project utilizes an SQLite3 database to store game information such as player names and ball movements. Finally, the Python server is connected to an HTML file with scripts to display the game to the user and make it interactive.

**Compilation Instructions:**
To compile the C code and create the necessary Python interface, follow these steps:

1. Set the LD_LIBRARY_PATH:
   export LD_LIBRARY_PATH=`pwd`

2. Compile the C code:
   clang -Wall -pedantic -std=c99 -fPIC -c phylib.c -o phylib.o
   clang -shared -o libphylib.so phylib.o -lm

3. Generate Python interface:
   swig -python phylib.i

4. Compile the Python interface:
   clang -Wall -pedantic -std=c99 -c phylib_wrap.c -I/usr/include/python3.11/ -fPIC -o phylib_wrap.o
   clang -Wall -pedantic -std=c99 -shared phylib_wrap.o -L. -L/usr/lib/python3.11 -lpython3.11 -lphylib -o _phylib.so

Ensure to replace /usr/include/python3.11/ and /usr/lib/python3.11 with the correct paths to your Python installation if they are different.

**Usage:**
1. Start the Server:
   python server.py

2. Run the Web Display:
   python3 webDisplay.py <port>
   Replace <port> with the desired port number.
   
3. Open the HTML file in a web browser:
   Open the file in a browser using the following URL format:
   http://localhost:<port>/playerId.html
   Replace <port> with the port number specified when running webDisplay.py.

Dependencies:
C Compiler: Clang (or any C compiler)
Python: Version 3.11 (or compatible)
SWIG: Version 4.0.2 (or compatible)
SQLite3: Version 3.36.0 (or compatible)
Web Browser: Any modern web browser with JavaScript support.
