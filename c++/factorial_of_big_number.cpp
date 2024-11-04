#include <string>
#include <vector>
#include <sstream>
std::string factorial(int factorial){
    if (factorial < 0){
        return "";
    }
    if (factorial == 0){
        return "1";
    }
    std::vector<int> elements{1};
    for (int i = 2; i <= factorial; i++){
        int carry = 0;
        for (size_t j = 0; j < elements.size(); j++){
            int current = elements[j] * i + carry;
            elements[j] = current % 10;
            carry = current / 10;
        }
        if (carry){
            elements.push_back(carry);
        }
    }
    std::stringstream ss;
    for (auto it = elements.rbegin(); it != elements.rend(); it++){
        ss << *it;
    }
    return ss.str();
}