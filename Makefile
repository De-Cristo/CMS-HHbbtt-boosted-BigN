ROOTCFLAGS = $(shell root-config --cflags)
ROOTLIBS = $(shell root-config --libs)
ROOTGLIBS = $(shell root-config --glibs)

# Compiler options
CC = g++
CFLAGS = -c -Wall -I include/ $(ROOTCFLAGS)

# Linker options
LD = g++
LDFLAGS = $(ROOTLIBS) $(ROOTGLIBS)

# Directories
SRC_DIR = src
OBJ_DIR = obj
LIB_DIR = lib

# Source files and object files
SRC_FILES = $(wildcard $(SRC_DIR)/*.cpp)
OBJ_FILES = $(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$(SRC_FILES))

# Library files
LIBRARIES = $(patsubst $(SRC_DIR)/%.cpp,$(LIB_DIR)/%.so,$(SRC_FILES))

# Targets
all: $(LIBRARIES)

$(LIB_DIR)/%.so: $(OBJ_DIR)/%.o
	$(LD) $(LDFLAGS) -shared $< -o $@

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CC) $(CFLAGS) $< -o $@

# Clean
# clean:
#	rm -f $(OBJ_DIR)/*.o $(LIBRARIES)
