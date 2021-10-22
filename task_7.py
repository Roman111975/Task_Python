# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return '{}{}{}i'.format(self.real, sign, self.imag)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        return Complex(real, imag)

    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5


print(Complex(1, 2) + Complex(3, 4))
print(Complex(1, 2) * Complex(3, 4))
print(Complex(1, 2) - Complex(3, 4))
print(abs(Complex(3, 4)))
