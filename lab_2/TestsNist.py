import json
import logging
import os.path
from math import erfc, fabs, sqrt, pow
from mpmath import gammainc

logging.basicConfig(level=logging.INFO)

SETTINGS = os.path.join("sequence.json")
RESULT_PATH = os.path.join("result.txt")
PI_I = {0:0.2148, 1:0.3672, 2:0.2305, 3:0.1875}


def bit_test(sequence: str) -> float:
    try:
        str1 = list(map(float,sequence))
        result_seq = [-1 if x == 0 else x for x in str1]
        result_sum = fabs(sum(result_seq)) / sqrt(len(result_seq))
        p = erfc(result_sum / sqrt(2))
        return p
    except Exception as ex:
        logging.error(f"Invalid sequence : {ex}")


def test_identical_consecutive_bits(sequence: str) -> float:
    try:
        str1 = list(map(float, sequence))

        l = (1/float(len(str1))) * sum(str1)
        if ((fabs(l - 0.5)) >= (2 / sqrt(len(str1)))):
            return 0.0
        Vn = 0
        for i in range (len(str1)-1):
            Vn += 0 if str1[i] == str1[i+1] else 1
        p = erfc((fabs(Vn - 2*len(str1)*l*(1-l)))/(2 * sqrt(2 * len(str1)) * l * (1-l)))
        return p
    except Exception as ex:
        logging.error(f"Wrong str - {ex}")


def test_longest_sequence_of_ones(sequence: str) -> float:
    try:
        str1 = list(map(int, sequence))
        block_size = 8
        blocks = [str1[i:i + block_size] for i in range(0, len(sequence), block_size)]
        v_i = {1: 0, 2: 0, 3: 0, 4: 0}
        for block in blocks:
            once = ""
            while once in ''.join(map(str,block)):
                once += "1"
            once = once[:-1]
            if once.count("1") <= 1:
                v_i[1] += 1
            if once.count("1") == 2:
                v_i[2] += 1
            if once.count("1") == 3:
                v_i[3] += 1
            if once.count("1") >= 4:
                v_i[4] += 1
        x_square = 0
        for i in range(4):
            x_square += pow(v_i[i + 1] - 16 * PI_I[i], 2) / (16 * PI_I[i])
        p = gammainc(3 / 2, x_square / 2)
        return p
    except Exception as ex:
        logging.error(f"Wrong str - {ex}")


if __name__ == "__main__":
    with open(SETTINGS, 'r', encoding='utf-8') as f:
        sequence = json.load(f)

    cpp_seq = sequence['cpp']
    java_seq = sequence['java']

    with open(RESULT_PATH, 'w', encoding='utf-8') as f:
        f.write("Results for C++ sequence\n")
        f.write(str(bit_test(cpp_seq)) + '\n')
        f.write(str(test_identical_consecutive_bits(cpp_seq)) + '\n')
        f.write(str(test_longest_sequence_of_ones(cpp_seq)) + '\n')

        f.write("\nResults for Java sequence\n")
        f.write(str(bit_test(java_seq)) + '\n')
        f.write(str(test_identical_consecutive_bits(java_seq)) + '\n')
        f.write(str(test_longest_sequence_of_ones(java_seq)) + '\n')



