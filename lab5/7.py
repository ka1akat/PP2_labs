def s_to_(snake_str):
    words = snake_str.split('_')
    return words[0] + ''.join(word.title() for word in words[1:])

snake_str="hello_world_example"
camel=s_to_(snake_str)
print(camel)