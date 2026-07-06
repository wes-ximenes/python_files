#Código de exemplo de automação usando Selenium no navegador Edge.
#Automação para abrir o navegador e alternar entre abas.

from selenium import webdriver


#O webdriver é uma ferramenta do Selenium que permite controlar um navegador da web para automação de testes ou outras tarefas.
#Nesse caso, estamos usando o webdriver para o Microsoft Edge, mas o Selenium suporta vários navegadores, como Chrome, Firefox, Safari, etc.
driver = webdriver.Edge() #inicializa o driver do Microsoft Edge, permitindo controlar o navegador Edge para automação de testes ou outras tarefas.

#primeira aba
driver.get('https://www.google.com') #navega para a página do Google usando o método get() do driver, que carrega a URL especificada no navegador controlado pelo Selenium.

driver.maximize_window() #maximiza a janela do navegador para garantir que todos os elementos da página sejam visíveis e acessíveis durante a automação.

#find_element() é um método do Selenium usado para localizar um elemento na página da web.
#Ele aceita dois argumentos: o primeiro é o tipo de localizador (neste caso, 'name'), e o segundo é o valor do localizador (neste caso, 'q', que é o nome do campo de pesquisa do Google).
# pesquisa = driver.find_element('name', 'q')

# pesquisa.send_keys('Modiin GR') #envia o texto 'Modiin GR' para o campo de pesquisa localizado anteriormente, simulando a digitação do usuário.

# pesquisa.submit() #submete o formulário de pesquisa, equivalente a pressionar a tecla Enter após digitar a consulta.

#Nova aba
driver.switch_to.new_window('tab') #abre uma nova aba no navegador usando o método switch_to.new_window() do Selenium.

driver.get('https://www.youtube.com') #navega para a página do YouTube usando o método get() do driver, carregando a URL especificada no navegador controlado pelo Selenium.

driver.switch_to.window(driver.window_handles[0]) #retornando para aba de indice 0.

#input() impede que a automação seja encerrada imediatamente após a execução do código. Ele aguardará o pressionamento do enter pelo user.
input('Pressione Enter para fechar o navegador...') 