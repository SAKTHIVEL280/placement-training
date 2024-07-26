def count_substring(string, sub_string):
    def count_substring(string, sub_string):
    l1=len(string)
    c=0
    for i in range(0,l1):
        if string[i:i + len(sub_string)] == sub_string:
            c += 1 
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
