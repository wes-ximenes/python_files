import streamlit as st #Framework de criação de sistemas (Possui site com guia)
from openai import OpenAI  #inteligencia artificial do chat GPT (se quiser consultar o guia no site da openAI)

modelo = OpenAI(api_key="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")
 #api_key, uma chave que a openai disponibiliza, para usar os frames deles é necessario keys pagas, DEPOSITO MIN 5 DOL.

st.write('## ChatBot WesIA')

#session_state = memoria do streamlit
if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = [] #vai iniciar como uma lista vazia e guardar as mensagens do chat.
#dicionario = role + content  {"role": "user", "content": user_msg}  

#exibir o historico de mensagens
for mensagem in st.session_state['lista_mensagens']: #para cada mensagem no dicionario
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

user_msg = st.chat_input('Escreva algo para WesIA: ')
if user_msg: #so vai printar a msg se algo for escrito
    print(user_msg)
    #user -> Ser humano
    #assistant -> IA
    st.chat_message('User').write(user_msg) 
    mensagem = {'role':'user', 'content': user_msg} #sempre que o user enviar uma msg, o user e o conteúdo da msg será guardado no dicionário abaixo
    st.session_state['lista_mensagens'].append(mensagem) #index 7

    #resposta IA
    resposta_modelo = modelo.chat.completions.create(    #tool de interação em conversa
        messages=st.session_state['lista_mensagens'],
        model="gpt-3.5-turbo" #modelo do chat de interação, esse é antigo, mas bem compacto free(acesso limitado)
    ) 
    print(resposta_modelo) #para exibir no terminal a lista de mensagem que ele produziu(não é obrigatorio)
    resp_ia = resposta_modelo.choices[0].message.content #a resposta do assistant vai ser a resposta do modelo IA acima, no elemento 0 da lista 'choices', que é a message content

    #Exibir msg da IA na tela
    st.chat_message('assistant').write(resp_ia)
    mensagem_ia = {'role':'assistant', 'content': resp_ia} #mesmo processo do user, para guardar as respostas da IA no dicionario 'lista_mensagens'
    st.session_state['lista_mensagens'].append(mensagem_ia)

    print(st.session_state['lista_mensagens'])


    #ESSE CHATBOT SÓ VAI RODAR RENOVANDO OS CREDITOS DA APY_KEY (INDEX 4), NO SITE DA OPENAI, ESSA ATUAL JÁ ESTÁ EXPIRADA.