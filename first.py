from transliterate import translit

def make_translit_names_file(source_file: str, target_file: str):
    with open(source_file, encoding='utf-8') as src_file, \
            open(target_file, 'w') as translit_file:
        translit_file.write(translit(src_file.read(), "ru", reversed=True))


make_translit_names_file(source_file="302.txt", target_file="trans.txt")

