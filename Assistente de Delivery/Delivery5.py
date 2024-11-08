#Função de Atualização de Status
import json

def lambda_handler(event, context):
    pedido = json.loads(event['body'])
    
    # Lógica para atualizar o status do pedido
    return {
        "statusCode": 200,
        "body": json.dumps({"pedidoId": pedido['pedidoId'], "status": "entregue"})
    }
