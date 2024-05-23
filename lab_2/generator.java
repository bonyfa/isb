import java.security.SecureRandom;

public class Main {
    
    public static void main(String[] args) {
        // Инициализация генератора случайных чисел
        SecureRandom secureRandom = new SecureRandom();

        // Генерация 128-битной последовательности
        byte[] randomBytes = new byte[16]; // 16 байт для 128 бит
        secureRandom.nextBytes(randomBytes); // Заполнение массива случайными байтами

        // Преобразование массива байтов в двоичную строку
        StringBuilder binaryStringBuilder = new StringBuilder();
        for (byte b : randomBytes) {
            for (int i = 7; i >= 0; i--) {
                binaryStringBuilder.append((b >> i) & 1);
            }
        }

        // Вывод двоичной строки
        System.out.println(binaryStringBuilder.toString());
    }
}