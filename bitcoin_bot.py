import ssl
import json


import websocket
import bitstamp.client

#def client():
    #trading.client = bitstamp.client.Trading(username='', key='', secret='') #user config


#def comprar(quantidade):
    #trading_client = cliente()
    #trading_client.buy_market_order(quantidade)
                                                                #nao vai funcionar pois tem que logar no site e ter saldo para fazer transaçoes

#def vender(quantidade):
    #trading_client = cliente()
    #trading_client.sell_market_order(quantidade)


def ao_abrir(ws):
    print("[+] abriu a conexao...")
    json_subscribe = """
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
} 
"""
    ws.send(json_subscribe)


def ao_fechar(ws):
    print("[+] fechou a conexao")

def erro(ws, erro):
    print("[+] erro", erro)  

def ao_receber_mensagem(ws,message):
    message = json.loads(message)
    if message['event'] == 'trade':
        price = message['data']['price']
        print(price)

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                                on_open=ao_abrir,
                                on_close=ao_fechar,
                                on_message=ao_receber_mensagem,
                                on_error= erro )
    ws.run_forever(sslopt={"cert_reqs":ssl.CERT_NONE})