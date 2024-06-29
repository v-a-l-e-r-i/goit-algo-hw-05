def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 1: #умова виходу з рекурсії
            return n
        if n in cache: #при наявності в каші повертаємо це значення
            return cache[n]

        #запишуємо значення в кеш
        cache[n] = (fibonacci(n - 1) + fibonacci(n - 2))
        return cache[n]

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()


# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
