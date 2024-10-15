#include <string>
#include <cstddef>
#include <sstream>

std::string multiply_one(const std::string& a, char b) {
    int carry = 0;
    std::string x(a.rbegin(), a.rend());
    std::stringstream ss;
    for (size_t i = 0; i < x.size(); i++){
        int dx = x[i] - '0';
        int dy = b - '0';
        int current = dx * dy + carry;
        ss << current % 10;
        carry = current / 10;
    }
    if (carry){
        ss << carry;
    }
    std::string result = ss.str();
    return std::string(result.rbegin(), result.rend());
}

std::string add(const std::string& a, const std::string& b) {
    int carry = 0;
    std::string x(a.rbegin(), a.rend());
    std::string y(b.rbegin(), b.rend());
    std::stringstream ss;
    size_t size = std::max(x.size(), y.size());
    for (size_t i = 0; i < size; i++){
        int dx = i < x.size() ? x[i] - '0' : 0;
        int dy = i < y.size() ? y[i] - '0' : 0;
        int current = dx + dy + carry;
        ss << current % 10;
        carry = current / 10;
    }
    if (carry){
        ss << carry;
    }
    std::string result = ss.str();
    return std::string(result.rbegin(), result.rend());
}

std::string multiply(const std::string& a, const std::string& b) {
    int carry = 0;
    std::string x(a.rbegin(), a.rend());
    std::string y(b.rbegin(), b.rend());
    size_t size = std::max(x.size(), y.size());
    std::string current = multiply_one(a, y[0]);
    for (int i = 1; i < y.size(); i++){
        current = add(multiply_one(a, y[i]) + std::string(i,'0'), current);
    }
    current.erase(0, current.find_first_not_of('0'));
    if(current.size() == 0) return "0";
    return current;
}