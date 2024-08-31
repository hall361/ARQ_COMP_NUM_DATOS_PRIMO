def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = 25  # ejemplo
if es_primo(num):
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")