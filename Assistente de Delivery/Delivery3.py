#Função de Validação de Pedido

import json

def lambda_handler(event, context):
    pedido = event['pedido']
    
    # Lógica de validação de pedido
    if not pedido.get('id') or not pedido.get('itens'):
        return {
            "statusCode": 400,
            "body": json.dumps("Pedido inválido.")
        }
    
    # Se válido, retorna o pedido com status atualizado
    return {
        "statusCode": 200,
        "body": json.dumps({"pedidoId": pedido['id'], "status": "validado"})
    }
