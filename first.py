from transliterate import translit

print("Hello")
with open('302.txt', encoding='utf-8') as f:
    for name in f:
        translit_name = translit(name, "ru", reversed=True)
        print(translit_name)
