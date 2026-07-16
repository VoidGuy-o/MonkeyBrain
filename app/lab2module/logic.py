from random import randint, choice
from math import pow
text = "ThisIsMySecretMessageIwantToreturn"
def encode(message, iterations = 1, debug = False):
    message = message.rstrip("\n")
    if iterations == 0:
        return message
    for iter in range(iterations):
        n=0     #Розмірність матриці
        pos = 0 #Позиція в циклі завантаження повідомлення до матриці
        # Пошук розміру матриці
        for i in range(1, 100):
            if len(message) <= i**2:
                n = i
                break
            else:
                continue
        matrix = [[0 for row in range(n)] for column in range(n)] # Матриця, що заповнена нулями
        list_final = [[0 for row in range(n)] for column in range(n)] #Фінальний список (поки заповнений нулями)
        sorting_list = [] # Ліст з рандомним порядком стовпців
        # Заповнення сортінг ліста
        while len(sorting_list) < n: 
            num = randint(0, n-1)
            if num in sorting_list:
                continue
            else:
                sorting_list.append(num)
        # завантаження повідомлення у матрицю
        # Якщо повідомлення закоротке для n^2 розмірності (а воно точно буде меншим), то ми дозаповнюємо матрицю
        for i in range(n):
            matrix[i] = [letter if  letter != None  else 0 for letter in message[pos:pos+n]]
            if len(matrix[i]) < n:
                matrix[i][len(matrix[i]):n] = [choice(message) for i in range(n-len(matrix[i]))]
            pos += n
        #Дебаг перевірка
        if iter == 0 and debug == True:
            for i in range(n):
                print(matrix[i])
            print("===============================")
        #Сама перестановка
        for i in range(0, n):
            for j in range(0, n):
                list_final[i][j] = matrix[j][sorting_list[i]]
        matrix = list_final
        
        res = ''
        for i in range(n):
            res += "".join(list_final[i])
    return res

if __name__ == "__main__":
    # Перевірка всякого лайна
    print(text)
    encoded_message = encode(text, debug=True)
    encoded_message_twotimes = encode(text, 2, debug=True)
    print(encoded_message)
    print("--------------------------------------")
    print(encoded_message_twotimes)

    for i in range(10):
        print(encode("ASUOIfhIhqihgqjg-t0hqg9h", debug=True))
    
