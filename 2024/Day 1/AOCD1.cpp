//AOC 2024 Day 1 in C++

//Plan
//Pair up the smallest number on the left and right, and subtract. Add all the list together.

#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream file("data.txt"); 
    std::string line;

    if(file.is_open()) {
       while (std::getline(file, line)) {
            std::cout << line << std::endl;
        }
        file.close();
    } else {
        std::cerr << "Unable to open file." << std::endl;
    }

    return 0;
}