# Projeto de Login e Gerenciamento de Dados com SQL Server e Tkinter

## Requisitos
- Python 3.x
- Biblioteca `pyodbc` para conexão com SQL Server (`pip install pyodbc`)
- SQL Server instalado localmente

## Configuração
1. **Banco de Dados SQL Server**:
   - Certifique-se de que o SQL Server está rodando localmente.
   - Crie um banco de dados chamado `meu_banco` ou altere a configuração no arquivo `ligacao_bd.py` para o nome do seu banco.
   - Altere as credenciais de `UID` e `PWD` no `ligacao_bd.py` conforme necessário.

2. **Arquivo CSV**:
   - O arquivo `clientes.csv` deve estar localizado na pasta `data` do projeto (`meu_projeto/data/clientes.csv`).
   - O caminho é configurado automaticamente para buscar o arquivo no local correto.

## Execução
1. Clone o repositório e entre na pasta:
   ```bash
   git clone https://github.com/seu-usuario/meu-projeto.git
   cd meu-projeto
