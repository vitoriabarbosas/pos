import boto3
from database import Users

def build_message(id):
    try: 
        subject = "Recarga Top: Você tem novos tickets disponíveis!"
        msg =  """
        <br>
        Olá, {} :) <br>
        
        Muito obrigadx por utiliar o RecargaTop!<br>
        
        Você tem {} tickets disponíveis<br>
        e um saldo de R$ {}, que pode ser utilizado<br>
        na compra de novos tickets! 
        
        <br>
    """.format(Users[id]['name'], Users[id]['tickets_disponiveis'], Users[id]['saldo_diponivel'])
        
        message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": msg}}}
        send_mail(message=message)
        
        send_mail(subject, msg)
    
    except Exception as e:
        print(e)
        raise e

def send_mail(message):
    
    try:
        ses = boto3.client("ses")
        
        result = ses.send_email(
                Source= "noreply@recargatop.com", 
                Destination= {"ToAddresses": [Users[id]['email']]}, 
                Message= message
            )
        
        return result
    
    except Exception as e:
        print(e)
        raise e