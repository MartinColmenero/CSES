
def missing_numbers(n, n_list):
    x = sorted(n_list)
    element = 1
    new_list = []
    
    while element < n:
        new_list.append(element)
        element += 1
    
    for x in range(len(new_list)):
        if new_list[x] == x[x]:
            continue
        else:
            return new_list[x]
        

def main():
    num = int(input())
    num_list = input().split()
    
    print(missing_numbers(num, num_list))

if __name__ == "__main__":
    main()