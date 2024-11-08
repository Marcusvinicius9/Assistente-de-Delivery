#Configuração do Workflow da Step Functions

import boto3
import json

# Criação do cliente Step Functions
client_sfn = boto3.client('stepfunctions', region_name='us-east-1')

# Definição do ARN da role com permissões para o Step Functions
role_arn = "arn:aws:iam::123456789012:role/service-role/StepFunctions-DeliveryRole"

# Função para criar a Step Function para o Assistente de Delivery
def criar_step_function():
    definicao_json = {
        "Comment": "Fluxo do Assistente de Delivery",
        "StartAt": "ReceberPedido",
        "States": {
            "ReceberPedido": {
                "Type": "Pass",
                "Next": "ValidarPedido"
            },
            "ValidarPedido": {
                "Type": "Task",
                "Resource": "arn:aws:lambda:us-east-1:123456789012:function:validarPedido",
                "Next": "ProcessarPagamento"
            },
            "ProcessarPagamento": {
                "Type": "Task",
                "Resource": "arn:aws:lambda:us-east-1:123456789012:function:processarPagamento",
                "Next": "AtualizarStatus"
            },
            "AtualizarStatus": {
                "Type": "Task",
                "Resource": "arn:aws:lambda:us-east-1:123456789012:function:atualizarStatus",
                "End": True
            }
        }
    }
    
    response = client_sfn.create_state_machine(
        name="AssistenteDeDelivery",
        definition=json.dumps(definicao_json),
        roleArn=role_arn
    )
    return response

# Cria a Step Function e imprime o ARN
response = criar_step_function()
print("Step Function ARN:", response["stateMachineArn"])
