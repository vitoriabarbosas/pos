from flask import Flask, make_response, jsonify, request
from database import Users
from random import randint
from aws import ses

app = Flask('RecargaTop')
app.config['JSON_SORT_KEYS'] = False

@app.route('/users', methods=['GET'])
def get_users():
    return make_response(
        jsonify(Users)
    )

@app.route('/createuser', methods=['POST'])
def createuser():
    createuser = request.json
    id = randint(0,9)
    Users[id] = createuser
    return make_response(
        jsonify(
            {
                "status": 200,
                "message": "Usuário Cadastrado com Sucesso!"
            }
        )
    )
    
@app.route('/profile', methods=['GET']) # http://127.0.0.1:5000/profile?id=1234
def get_tickets():
    args = request.args
    id = int(args.get('id'))
    
    try:
        if id:
            result = Users[id]
    
        return make_response(
            jsonify(result)
        )
        
    except: 
        return make_response(
            jsonify( 
                {
                    "status": 400,
                    "message": "Usuário não encontrado!"
                }
            )
        )
        
@app.route('/profile/buytickets', methods=['POST'])
def buy_ticket():
    args = request.args
    id = int(args.get('id'))
    new_ticket = int(args.get('number'))
    ticket_disponiveis = Users[id]['tickets_disponiveis'] + new_ticket
    saldo_diponivel = Users[id]['saldo_diponivel'] - (new_ticket*3)
    Users[id]['saldo_diponivel'] = saldo_diponivel
    Users[id]['tickets_disponiveis'] = ticket_disponiveis
    ses = ses.build_message(id=id)
    
    return make_response(
            jsonify( 
                {
                    "status": 200,
                    "message": "Obrigado por fazer esta compra!"
                }
            )
        )

app.run() # Local -> 127.0.0.1:5000
#app.run(host="0.0.0.0", port=int("3000"), debug=True) 

