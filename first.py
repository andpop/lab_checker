from transliterate import translit

print("Hello")
with open('302.txt', encoding='utf-8') as source_file:
    with open('trans.txt', 'w') as translit_file:
        for name in source_file:
            translit_name = translit(name, "ru", reversed=True)
            print(translit_name)
            translit_file.write(translit_name)
