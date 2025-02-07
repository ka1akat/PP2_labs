def print_permutations(string, perm=""):
    if len(string) == 0:
        print(perm)
    else:
        for i in range(len(string)):
            remaining = string[:i] + string[i+1:]
            print_permutations(remaining, perm + string[i])

string = "abc"
print_permutations(string)
