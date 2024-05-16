#include <iostream>
#include <random>

int main() {
    // Инициализация генератора случайных чисел
    std::random_device rd;
    std::mt19937_64 gen(rd());
    std::uniform_int_distribution<uint64_t> dis;

    // Генерация 128-битной последовательности
    for (int i = 0; i < 2; ++i) { // Генерируем 2 числа по 64 бита
        uint64_t randomNum = dis(gen);
        for (int j = 63; j >= 0; --j) { // Выводим каждый бит числа
            std::cout << ((randomNum >> j) & 1);
        }
    }
    std::cout << std::endl;

    return 0;
}