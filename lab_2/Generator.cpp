#include <iostream>
#include <cstdlib>
#include <ctime>
#define SIZE 128


void generator() {
    std::srand(static_cast<unsigned>(std::time(0)));
    for (int i = 0; i < SIZE; ++i) {
        int random_bit = std::rand() % 2;
        std::cout << random_bit;
    }
}


int main() {
    generator();
    return 0;
}