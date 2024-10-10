#include <string>
#include <cstddef>
#include <sstream>

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