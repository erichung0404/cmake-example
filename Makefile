CXX = g++
CXXFLAGS = -Wall -Wextra

main: main.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<
