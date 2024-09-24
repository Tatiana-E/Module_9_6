def all_variants(text):
    my_str = len(text)
    for i in range(1, my_str + 1):
        for j in range(my_str - i + 1):
            yield text[j:j + i]


a = all_variants("abc")
for i in a:
    print(i)