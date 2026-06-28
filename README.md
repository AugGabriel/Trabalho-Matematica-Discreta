## Implementação do Trabalho de Matemática Discreta

Essa é a implementação de um organizador de fotos de computador, usando o algoritmo de Busca em profundidade.




* main: conecta o sorter com os caminhos de entrada e saída.

* sort: obtém todos os arquivos do diretório de entrada; filtra eles, mantendo apenas as imagens; cria o caminho para cada uma; e copia cada uma para seu lugar.

* depth_first_search: retorna todos os arquivos dentro do diretório atual.

* is_image: retorna se o arquivo é uma imagem dentre as de formato aceito pelo sistema.

* create_date_path: cria o caminho com aquela data, no formato ano/mês, com o prefixo de onde o diretório do ano deve ficar.

* create_file_path: cria o caminho para a data de criação daquele arquivo.