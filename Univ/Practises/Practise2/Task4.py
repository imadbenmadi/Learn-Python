prime_sum = 0

for num in range(3, 1000, 2):
    is_prime = True  

    for i in range(2, num):  
        if num % i == 0:  
            is_prime = False
            break  
    
    if is_prime:  
        prime_sum += num  

print(f"The sum of prime numbers between 3 and 999 is {prime_sum}.")
