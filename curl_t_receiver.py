import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8786))
    s.listen(1)
    con, cli = s.accept()
    dados = con.recv(200)
    headers, arquivo = dados.split(b'\r\n\r\n')
    headers = headers.decode()
    campos = headers.split('\r\n')
    nome = campos[0].split('PUT /')[1].split(' HTTP')[0]
    tamanho = int(campos[4].split(': ')[1])
    recebidos = len(arquivo)
    with open(nome, 'wb') as f:
        f.write(arquivo)
        print(f'{recebidos}/{tamanho}\t\t', end='\r')
        while recebidos < tamanho:
            arquivo = con.recv(200)
            f.write(arquivo)
            recebidos += len(arquivo)
            print(f'{recebidos}/{tamanho}\t\t', end='\r')
    print()
    con.close()


if __name__ == '__main__':
    main()
