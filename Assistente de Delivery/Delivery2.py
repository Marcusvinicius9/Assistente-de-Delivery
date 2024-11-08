#Interação com o Amazon Bedrock

import boto3

# Configuração do cliente para Amazon Bedrock
client_bedrock = boto3.client('bedrock', region_name='us-east-1')

def processar_consulta_cliente(consulta):
    # Configuração do modelo (substitua pelo nome do modelo adequado do Bedrock)
    model_id = "model-id-do-bedrock"

    # Chamada ao modelo de NLP do Bedrock
    response = client_bedrock.invoke_model(
        ModelId=model_id,
        ContentType="text/plain",
        Accept="application/json",
        Body=json.dumps({"text": consulta})
    )

    # Parse da resposta do Bedrock
    resposta = json.loads(response['Body'].read())
    return resposta['generated_text']

# Exemplo de chamada para processar uma consulta do cliente
consulta = "Qual é o status do meu pedido?"
resposta_cliente = processar_consulta_cliente(consulta)
print("Resposta do assistente:", resposta_cliente)
