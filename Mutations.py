def mutate_string(string, position, character):
    a = list(string)
    a[position] = character
    b = ''.join(a)
    return b

string = input()
position, character = input().split()

f = mutate_string(string, int(position), character)
print(f)