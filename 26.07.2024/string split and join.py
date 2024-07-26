def split_and_join(line):
    s = line.split(" ")
    result = '-'.join(s)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
