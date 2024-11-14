def conexao():
    import pyodbc

    driver = '{ODBC DRIVER 17 for SQL Server}'#qual vai ser a tecnologia de conexao

    server = "AUD-PORT-020\\SQLEXPRESS" #qual o nome do servidor de BDs

    bdados = "TURMA25" #qual o nome da base de dados

    user = "sa"# qual o user que pode ligar ao servidor

    senha = "z43VGYT@Iu"#qual a senha do user para ligar ao servidor

    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+bdados+';UID='+user+';PWD='+senha)
        print("Conexão bem sucedida")
        return conn

    except:
        return False