from strategy.data_cleaner import DataCleaner

if __name__ == "__main__":
    cleaner = DataCleaner()
    dados_com_falhas = [10.0, None, 20.0, 30.0, None]
    
    print("Preenchendo valores nulos:")
    print(cleaner.clean_column(dados_com_falhas))