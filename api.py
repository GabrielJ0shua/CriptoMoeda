from flask import Flask
from bloco import *
from transancoes import *
from ecdsa import SigningKey, NIST384p

app = Flask(__name__)

@app.route("/")
def hello():
    return "Bem vindo a nossa criptomoeda"

@app.route("/generationKey")
def generationKey():
    arq = open('key.txt','w')
    sk = createSigningKey()
    arq.writelines(str(sk))
    arq.close()
    return "key gerada com sucesso"

@app.route("/coinbase")
def coinbase():
    return COINBASE

@app.route("/validatingTransactionId", methods=['POST'])
def validating(id, transancoes):
    id = request.form['id']
    transancoes = request.form['transancoes']
    if id is type(int) and transancoes is type(Transaction):
        if validatingTransactionId(id, transancoes):
            return "Transação invalida"
        else:
            return "Transação invalida"
    else:
        return "Erro"


if __name__ == "__main__":
    app.run()