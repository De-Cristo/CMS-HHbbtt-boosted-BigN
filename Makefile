CXX=g++
CXXFLAGS=-Wall -Wextra -pedantic -std=c++11 -I./include
LDFLAGS=-shared
LIBDIR=./lib
SRCDIR=./src
SCRIPTDIR=./script

all: $(LIBDIR)/mylib.so

$(LIBDIR)/mylib.so: $(SRCDIR)/mylib.cpp | $(LIBDIR)
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

$(LIBDIR):
	mkdir -p $@

install: $(LIBDIR)/mylib.so
	cp $(LIBDIR)/mylib.so $(SCRIPTDIR)

clean:
	rm -rf $(LIBDIR)/mylib.so

.PHONY: all install clean
