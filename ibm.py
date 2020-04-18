from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('u1N9ThXmpZUk_-1_F1AaAw-11BbBXFtCbonmmerHbnFI')
assistant = AssistantV1(
    version='2019-02-28',
    authenticator = authenticator
)

assistant.set_service_url('https://gateway-wdc.watsonplatform.net/assistant/api')

response = assistant.message(
    workspace_id='6cfaa408-9ed3-4e80-adcc-fb84f58b435f',
    input={
        'text': 'open c++'
    }
).get_result()


a=response
b=a['intents']
print(b)