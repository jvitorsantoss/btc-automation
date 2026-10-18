import ssl

import websocket


def ao_abrir(ws):
    print("[+] abriu a conexao...")

def ao_fechar(ws):
    print("[+] fechou a conexao")

def erro(ws, erro):
    print("[+] erro") 
    print(erro) 

def ao_receber_mensagem(ws,message):
    print(message)


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                                on_open=ao_abrir,
                                on_close=ao_fechar,
                                on_message=ao_receber_mensagem,
                                on_error= erro )
    ws.run_forever(sslopt={"cert_reqs":ssl.CERT_NONE})