CXX = g++ 
CXXFLAGS = -std=c++17 -Wall -Wextra -O2 

TARGET = app 
SOURCES = main.cpp Patient.cpp Clinic.cpp 
OBJECTS = $(SOURCES:.cpp=.o) 

all: $(TARGET) 

$(TARGET): $(OBJECTS) 
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(TARGET) 

main.o: main.cpp Patient.h Clinic.h 
	$(CXX) $(CXXFLAGS) -c main.cpp -o main.o 

Patient.o: Patient.cpp Patient.h 
	$(CXX) $(CXXFLAGS) -c Patient.cpp -o Patient.o 

Clinic.o: Clinic.cpp Clinic.h Patient.h 
	$(CXX) $(CXXFLAGS) -c Clinic.cpp -o Clinic.o 

clean: 
	rm -f $(OBJECTS) $(TARGET)
	 
.PHONY: all clean 