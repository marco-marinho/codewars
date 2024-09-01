#include <vector>
#include <string>

class DirReduction {
public:
    static std::vector<std::string> dirReduc(std::vector<std::string> const &arr);
};

std::vector<std::string> DirReduction::dirReduc(std::vector<std::string> const &arr) {
    std::vector<std::string> stack{"None"};

    for (auto &direction: arr) {
        if ((direction == "EAST" && stack.back() == "WEST")
            || (direction == "WEST" && stack.back() == "EAST")
            || (direction == "NORTH" && stack.back() == "SOUTH")
            || (direction == "SOUTH" && stack.back() == "NORTH")) {
            stack.pop_back();
            } else {
                stack.push_back(direction);
            }
    }
    std::vector<std::string> output{stack.begin() + 1, stack.end()};
    if (arr.size() != output.size()) {
        output = dirReduc(output);
    }
    return output;
}
