#include <string>
#include <vector>
#include <sstream>
#include <deque>
#include <iostream>

std::string factorial(int factorial)
{
    if (factorial < 0)
    {
        return "";
    }
    if (factorial == 0)
    {
        return "1";
    }
    std::deque<int> elements{1};
    for (int i = 2; i <= factorial; i++)
    {
            int carry = 0;
            for (size_t j = 0; j < elements.size(); j++)
            {
                int current = elements[j] * i + carry;
                elements[j] = current % 10;
                carry = current / 10;
            }
            while (carry)
            {
                elements.push_back(carry % 10);
                carry /= 10;
            }
    }
    std::stringstream ss;
    for (auto it = elements.rbegin(); it != elements.rend(); it++)
    {
        ss << *it;
    }
    return ss.str();
}

int main()
{
    std::cout << factorial(250) << std::endl;
    return 0;
}
