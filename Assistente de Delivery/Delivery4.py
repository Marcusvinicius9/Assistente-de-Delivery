#Função de Processamento de Pagamento

import json

def lambda_handler(event, context):
    pedido = json.loads(event['body'])
    
    # Lógica de processamento de pagamento
    pagamento_aprovado = True  # Exemplo
    
    if pagamento_aprovado:
        return {
            "statusCode": 200,
            "body": json.dumps({"pedidoId": pedido['pedidoId'], "status": "pago"})
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps("Falha no pagamento.")
        }
