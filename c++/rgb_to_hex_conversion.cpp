#include <string>
#include <sstream>
#include <algorithm>

std::string rgb_to_hex(int r, int g, int b) {
    static auto digits = "0123456789ABCDEF";
    r = std::clamp(r, 0, 255);
    g = std::clamp(g, 0, 255);
    b = std::clamp(b, 0, 255);
    std::stringstream stream;
    stream << digits[r / 16] << digits[r % 16];
    stream << digits[g / 16] << digits[g % 16];
    stream << digits[b / 16] << digits[b % 16];
    return stream.str();
}
