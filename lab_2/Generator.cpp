#include <iostream>
#include <random>

int main() {
    // ������������� ���������� ��������� �����
    std::random_device rd;
    std::mt19937_64 gen(rd());
    std::uniform_int_distribution<uint64_t> dis;

    // ��������� 128-������ ������������������
    for (int i = 0; i < 2; ++i) { // ���������� 2 ����� �� 64 ����
        uint64_t randomNum = dis(gen);
        for (int j = 63; j >= 0; --j) { // ������� ������ ��� �����
            std::cout << ((randomNum >> j) & 1);
        }
    }
    std::cout << std::endl;

    return 0;
}