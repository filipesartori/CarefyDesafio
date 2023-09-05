# CarefyDesafio 🚀

Repositório destinado aos códigos feitos e arquivos gerados no desafio da Carefy

# Tutorial do Código

1. É necessário rodar este código com todos os arquivos dentro de um único diretório, pois é necessário que haja o drive para que a biblioteca consiga Selenium rodar.
2. Execute, então, o código loop.py, pois nele está sendo chamada a função "Clica no arquivo DownloadV2", dentro de um loop, para que faça os downloads assim pedidos.
3. Após fazer os downloads, é necessário colocar os arquivos baixados dentro da pasta Planilhas e convertê-los para .XLSX.
4. Então, basta executar o código uniao.py para que sejam unidos todos os arquivos em 3 arquivos com seus anos correspondentes.

# Observações e Dificuldades

Algumas dificuldades foram encontradas no desenvolvimento do código, a principal é que os arquivos exportados do site estão em .XLS, sendo uma extensão antiga no Excel e, com isso, é necessário a conversão destes arquivos em .XLSX. Testei utilizar automações também para este serviço, porém o próprio Excel dificulta esta manipulação por código, por ser uma extensão antiga e vulnerável. Logo, foi necessário fazer a conversão manualmente.

Outra dificuldade é a demora com que os códigos rodam, como são muitos arquivos, com muitos dados cada e o site exportar in loco os dados para uma planilha, há uma grande demora em fazer os downloads dos arquivos no site, e também na parte da união, por conta do grande número de dados. O tamanho dos arquivos é relativamente grande e acaba demorando também para fazer a união e o save destes arquivos.

Com isso, retirando estes impedimentos, o desenvolvimento do código foi tranquilo. Algumas dúvidas surgiram, porém com poucas pesquisas no Google já foi necessário para sanar as dúvidas e continuar o desenvolvimento do código.
