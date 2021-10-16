# Power Bambu da Cultura (Projeto Avenida Brasil - Way2Labs)
Automação do bambu da cultura da Way2, primeiro bambu open-source do mundo (⌐■_■)
 
 
## Objetivo do projeto
 
Depois do apocalipse da Covid-19, o trabalho remoto virou algo comum para a grande maioria de nós, devs. Mas nem tudo pode ser feito remotamente, por exemplo, cuidar fisicamente do nosso bambu da cultura.
 
Para isso decidimos automatizar algumas tarefas relacionadas a esse cuidado e aprender no caminho. Vamos plugar um sensor capacitivo de umidade no vaso do bambu, para saber quando é necessário regar. Quando a umidade da terra estiver baixa, o próprio bambu vai mandar mensagem pelo Slack pedindo água, substituindo o icônico áudio anterior ("Socorro, bota água, isso vai doer, eu não quero morrer").
 
Faremos a integração dos sensores com um ESP8266/ESP32, visto que essa placa de desenvolvimento já tem conexão com a internet via Wi-Fi. Com o hardware pronto, vamos montar um servidor de Node-RED para fazer a integração dos dados postados com um repositório, que posteriormente será utilizado pelo PowerBI para gerar dashboards em tempo real sobre as condições do bambu. O servidor de Node-RED também será utilizado para a implementação da integração com o Slack.