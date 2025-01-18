# stats.py

def mean(num):
    
    return sum(num) / len(num) if num else 0

def median(num):

    if not num:
        return 0

    sorted_num = sorted(num)
    n = len(sorted_num)
    middle = n // 2

    if n % 2 == 0:  
        return (sorted_num[middle - 1] + sorted_num[middle]) / 2
    else:  
        return sorted_num[middle]

def mode(num):

    if not num:
        return 0

    from collections import Counter
    frequency = Counter(num)
    max_count = max(frequency.values())

    modes = [key for key, value in frequency.items() if value == max_count]

    if len(modes) == 1:
        return modes[0]  
    else:
        return modes 


if __name__ == "__main__":
    user_input = input("Enter a list of numbers: ")
    num = list(map(float, user_input.split()))

    print("Mean:", mean(num))
    print("Median:", median(num))
    print("Mode:", mode(num))
