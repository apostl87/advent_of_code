#include <iostream>
#include <deque>
#include <algorithm>
#include <fstream>
#include <string>

int main() {
    std::ifstream file("./17.in");
    std::string inp;
    std::getline(file, inp);
    int skip = std::stoi(inp);

    std::deque<int> buffer = {0};
    for (int i = 1; i <= 2017; ++i) {
        std::rotate(buffer.rbegin(), buffer.rbegin() + (skip % buffer.size()), buffer.rend());
        buffer.push_back(i);
    }

    auto it = std::find(buffer.begin(), buffer.end(), 2017);
    if (it != buffer.end() && ++it != buffer.end()) {
        std::cout << "Part 1: " << *it << std::endl;
    } else {
        std::cout << "Part 1: " << buffer[0] << std::endl;
    }

    buffer = {0};
    int position = 0;
    int afterZero = -1;
    for (int i = 1; i <= 50'000'000; ++i) {
        position = (position + skip) % i + 1;
        if (position == 1) afterZero = i;
    }

    std::cout << "Part 2: " << afterZero << std::endl;

    return 0;
}