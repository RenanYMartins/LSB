def main():
    # Receber um texto
    text = str("Tabela ASCII eh bem legal");

    # Converter em ASCII (decimal)
    decoded = _text_to_ascii(text)

    # Converter em binário
    binary = _ascii_to_binary(decoded)

    print(binary)

def _text_to_ascii(text):
    decode_list = []

    for letter in text:
        decoded = int(ord(letter))
        decode_list.append(decoded)

    return decode_list

def _ascii_to_binary(decoded):
    binary_list = []

    for ascii in decoded:
        binary = format(ascii, "08b")
        binary_list.append(binary)

    # Formar um array de bits
    return ' '.join(binary_list)
        



    # Receber o path da imagem
    # Converter imagem para bits

    # inserir bits do texto nos bits da imagem
    # gerar a imagem e salvar em um diretorio



if __name__ == "__main__":
    main()
