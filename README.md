# Monitor Wi-Fi 🔍📶

> Script Python para monitorar tentativas de conexão na sua rede Wi-Fi! 🚫🔒

## 📝 Descrição
O Monitor Wi-Fi é um script simples e poderoso para detectar e registrar tentativas de conexão não autorizadas na sua rede Wi-Fi. Ele usa a biblioteca Scapy para capturar e analisar os pacotes de rede, fornecendo informações detalhadas sobre os dispositivos que tentaram se conectar.

## 🤓 Descrição Técnica

<details>
  <summary>
    <strong>Clique para expandir e ver a descrição técnica detalhada</strong>
  </summary>

  Aqui está uma explicação mais detalhada do código e das bibliotecas usadas:

  - **Scapy** 📡: É uma poderosa biblioteca em Python para manipulação e análise de pacotes de rede. Utilizamos o Scapy para capturar e analisar os pacotes de rede da sua rede Wi-Fi.

  - **Dot11** 📶: É uma classe do Scapy que representa o cabeçalho do pacote Wi-Fi. Nós usamos essa classe para filtrar os pacotes que são específicos para a camada Wi-Fi.

  - **Dot11Beacon** 🌐: É uma classe do Scapy que representa os pacotes de beacon, que são enviados periodicamente pelos pontos de acesso para anunciar a presença da rede. Nós utilizamos essa classe para identificar os pontos de acesso na sua rede Wi-Fi.

  - **Dot11ProbeReq** 🔎: É uma classe do Scapy que representa os pacotes de solicitação de probe, que são enviados por dispositivos para procurar redes disponíveis. Nós utilizamos essa classe para identificar os dispositivos que estão tentando se conectar à sua rede.

  - **sniff()** 👃: É uma função do Scapy que permite capturar pacotes de rede. Nós a utilizamos para iniciar a captura de pacotes na interface Wi-Fi especificada.

  - **handle_packet(packet)** 📥: É uma função que definimos para processar cada pacote capturado. Ela recebe um pacote como entrada e realiza as análises necessárias para extrair informações relevantes, como endereços MAC, SSID da rede, tipo de pacote, etc.

  - **monitor_mode(interface)** 🚧: É uma função que definimos para configurar a interface Wi-Fi no modo de monitoramento. Isso permite que a interface capture todos os pacotes de rede, mesmo aqueles que não são direcionados especificamente para ela.

  - **enable_monitor_mode(interface)** 🚀: É uma função que chama o comando de terminal `networksetup` para configurar a interface Wi-Fi no modo de monitoramento usando a ferramenta de linha de comando do macOS.

  - **disable_monitor_mode(interface)** 🔒: É uma função que chama novamente o comando `networksetup` para desativar o modo de monitoramento na interface Wi-Fi, restaurando as configurações originais.

  Essas são as principais explicações técnicas por trás do código e das bibliotecas utilizadas. Essa compreensão mais detalhada ajudará você a entender melhor como o script funciona e como as bibliotecas são empregadas para alcançar o objetivo de monitorar tentativas de conexão na sua rede Wi-Fi.
</details>

## 🚀 Como Usar
1. Certifique-se de ter o Python 3 instalado no seu sistema.
2. Instale as dependências usando o comando: `pip install scapy && pip install datetime`.
4. Abra o terminal e navegue até o diretório do script.
5. Execute o script usando o comando: `python monitor.py` (para rodar o comando em background, podendo fechar o terminal, basta executar o comando `python monitor.py &` que o script funcionará enquanto a máquina estiver ligada).
6. Execute o script usando o comando: `python monitor.py &`.
7. Digite sua senha de administrador/superusuário quando solicitado.
8. Agora, o script está monitorando sua rede Wi-Fi em busca de tentativas de conexão.

## 💡 Dicas
- Certifique-se de que a interface Wi-Fi correta esteja selecionada no script.
- Personalize o código para adicionar funcionalidades extras, como notificações em tempo real ou bloqueio automático de dispositivos suspeitos.

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usar, modificar e distribuir conforme necessário.

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📞 Contato
Se você tiver alguma dúvida ou sugestão, entre em contato comigo pelo e-mail [hugo.shiroma@gmail.com](mailto:hugo.shiroma@gmail.com).

Aproveite o Monitor Wi-Fi e mantenha sua rede protegida! 🛡️🔒
