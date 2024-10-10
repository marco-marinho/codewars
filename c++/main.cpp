#include <iostream>
#include <string>
#include "adding_big_numbers.cpp"


int main(){
    std::string a = "10";
    std::string b = "35679";
    std::string c = add(a, b);
    std::cout << c << std::endl;
    return 0;
}