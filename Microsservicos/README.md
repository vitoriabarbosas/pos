# RecargaTop

Esse repositório é uma lambda container baseada em flask cujo possui uma integração com AWS SES para envio de emails.

A ideia desse projeto se resume em um API Gateway recebendo requisições e executando a Lambda em questão para execução do backend da aplicação. Quando a rota para compra de tickets for requisitada, um email será enviado ao cliente.

- [Como funciona a API?](#api)
    - [Rotas](#rotas)
    - [Entendendo os Retornos](#entendendo-os-retornos)
        - [Método GET](#método-get)
        - [Método POST](#método-post)
- [Integração com SNS](#integração-com-aws-sns)
- [Documentação de Referência](#documentação-de-referência)

## API

Código python com flask framework. 

Módulos/Bibliotecas requisitadas:
```txt
boto3
logging
flask
random
localstack
```

### Rotas

Esta API possui 4 rotas: 

| **Rota**    | **Método** | **Descrição** |
|-------------|------------|---------------|
| /users      | GET        | Acesso a todos os usuários |
| /profile    | GET        | Acesso a um perfil específico |
| /createuser | POST       | Criação de novos usuários |
| /buytickets | POST       | Compra de novos tickets   |

### Entendendo os Retornos 

#### Método: GET 

**Endpoint: http://127.0.0.1:5000/users**

Neste endpoint você tem um retorno de todos os usuários

```json
{
    "1234": {
        "name": "vitoria",
        "email": "vitoriabarbosas@fiap.com",
        "tickets_disponiveis": 4,
        "tickets_utilizados": 40,
        "saldo_diponivel": 20
    },
    "1235": {
        "name": "matheus",
        "email": "matheuslemes@fiap.com",
        "tickets_disponiveis": 7,
        "tickets_utilizados": 50,
        "saldo_diponivel": 20
    }
}
```

**Endpoint: http://127.0.0.1:5000/profile?id=1234**

Neste endpoint você acessa informações de perfil do usuário com base no seu id

```json
{
    "name": "vitoria",
    "email": "vitoriabarbosas@fiap.com",
    "tickets_disponiveis": 4,
    "tickets_utilizados": 40,
    "saldo_diponivel": 20
}
```

Caso o usuário não exista: 

```json
{
    "status": 400,
    "message": "Usuário não encontrado!"
}
```

#### Método: POST 

**Endpoint: http://127.0.0.1:5000/createuser**

Neste endpoint, é possível realizar a criação de novos usuários

Payload esperado:
```json
{
    "name": "hhuhuhu",
    "email": "hhuhuhu@fiap.com",
    "tickets_disponiveis": 5,
    "tickets_utilizados": 50,
    "saldo_diponivel": 100
}
```

Retorno:
```json
{
    "status": 200,
    "message": "Usuário Cadastrado com Sucesso!"
}
```


**Endpoint: http://127.0.0.1:5000/profile/buytickets?id=1234&number=2**

Com base no query string number, é possível realizar a compra de tickets onde será atualizado o valor total de tickets disponíveis.

Retorno:
```json
{
    "status": 200,
    "message": "Obrigado por fazer esta compra!"
}
```

Neste modo, para visualizar a nova quantidade de tickets e saldo disponíveis na conta, é necessário realizar o **GET** no perfil do usuário. 

Exemplo de retorno **GET** ao realizar a compra de 2 tickets:
```json
{
    "name": "vitoria",
    "email": "vitoriabarbosas@fiap.com",
    "tickets_disponiveis": 6,
    "tickets_utilizados": 40,
    "saldo_diponivel": 14
}
```

### Integração com AWS SNS 

Para o envio de e-mails, foi escolhido o AWS SNS por conta da familiaridade entre os membros do grupo e por já estarmos pensando em um serviço operando na Cloud AWS. Sendo assim, siga os passos para se utilizar a localstack.

Instalar localstack: 
```
pip install localstack
pip install awscli-local
```

Comandos para utilizar a localstack: 
```
$ localstack start
$ awslocal sns create-topic --name sns-recarga-top
$ awslocal sns set-topic-attributes --topic-arn arn:aws:sns:us-east-1:000000000000:sns-recarga-top --attribute-name DisplayName --attribute-value RecargaTopTopico
$ awslocal sns list-topics
$ awslocal sns publish --topic-arn "arn:aws:sns:us-east-1:000000000000:sns-recarga-top" --message "Oi, Vitoria! Muito obrigadx por realizar esta compra!"
$ awslocal sns subscribe --topic-arn arn:aws:sns:us-east-1:000000000000:sns-recarga-top --protocol email --notification-endpoint email@gmail.com
$ awslocal sns set-subscription-attributes --subscription-arn arn:aws:sns:us-east-1:000000000000:sns-recarga-top:eecadcae-30ae-4493-a763-2de9aad3a562 --attribute-name RawMessageDelivery --attribute-value true
```

### Documentação de Referência

- [Lambda Container](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)