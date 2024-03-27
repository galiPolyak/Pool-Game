CC=clang
CFLAGS=-std=c99 -Wall -pedantic -g

all: a1 _phylib.so

clean:
	rm -f *.o *.so a1 _phylib.so phylib_wrap.c phylib_wrap.o

# Target: libphylib.so
libphylib.so: phylib.o
	$(CC) phylib.o -shared -o libphylib.so -lm

# Target: phylib.o
phylib.o: phylib.c phylib.h
	$(CC) $(CFLAGS) -c phylib.c -fPIC -o phylib.o

# Target: _phylib.so
_phylib.so: phylib_wrap.o libphylib.so
	$(CC) phylib_wrap.o -shared -L. -lphylib -o _phylib.so -lpython3.11 -lm

# Target: phylib_wrap.o
phylib_wrap.o: phylib_wrap.c
	$(CC) $(CFLAGS) -c phylib_wrap.c -I/usr/include/python3.11/ -fPIC -o phylib_wrap.o

# Target: phylib_wrap.c
phylib_wrap.c: phylib.i
	swig -python phylib.i

a1: A1test1.o libphylib.so
	$(CC) A1test1.o -L. -lphylib -o a1 -lm

A1test1.o: A1test1.c phylib.h
	$(CC) $(CFLAGS) -c A1test1.c -o A1test1.o
