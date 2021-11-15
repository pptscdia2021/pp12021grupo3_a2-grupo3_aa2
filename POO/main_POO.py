from matplotlib.pyplot import plot
import yfinance
import investipy
import pandas as pd
import yfinanc

class Accion:
    def __init__(self,ticker, pais, from_date, to_date):
        self.ticker = ticker
        self.pais = pais
        self.from_date = from_date
        self.to_date = to_date
    def __str__(self):
        return "Ticker: " + self.ticker + " - Pais: " + self.pais + " - fecha desde:  " + self.from_date + " - fecha hasta: " + self.to_date
    
    
    def graficar(self, df_accion):
        
        import matplotlib.pyplot as plt

        plt.xlabel("Fecha")
        plt.xticks(rotation=30, ha='right')
        plt.ylabel("Close", fontsize=15)
        
        plt.gcf().set_size_inches(15, 10)
        plt.show()
        


def main():
  
    opcion=()
        
    while opcion != 4:
        print('*************************************** '),
        print('       MENU CONSULTAS SCRAPING '),
        print('***************************************  \n'),
        print('Selecciona una opción: \n'),
        print('1) Calcular por INVESTIPY.'),
        print('2) Calcular por YFINANCE.'),
        print('3) Calcular por SOAP.'),
        print('4) Finalizar. ')
        opcion = input('Pulsa 1,2,3 o 4 para salir ')
    
        if opcion == '1':
            pais='spain'
            ticker='bbva'
            from_date=str(input("Ingrese la fecha de inicio: "))
            to_date=str(input("Ingrese la fecha de fin: "))
            accion=Accion(ticker, pais, from_date, to_date)

            #ACCEDO A LA FUNCION INVESTIPY DECLARADA EN INVESTIPY.PY
            df_accion=pd.DataFrame(investipy.investPy(accion)) 
            df_accion['Date'] = df_accion.index
            print(df_accion)
            df_accion['Close'].plot(title="BBVA")
            #LLAMO AL METODO GRAFICAR Y LE PASO EL PARAMETRO df_accion 
            accion.graficar(df_accion)
           
            
        elif opcion == '2':
            pais = 'spain'
            ticker='AMZN'
            from_date=str(input("Ingrese la fecha de inicio: "))
            to_date=str(input("Ingrese la fecha de fin: "))
            accio=Accion(ticker,pais, from_date, to_date)
            print(accio)

            #ACCEDO A LA FUNCION INVESTIPY DECLARADA EN INVESTIPY.PY
            df_accio=pd.DataFrame(yfinanc.yfinance(accio)) 
            df_accio['Date'] = df_accio.index
            print(df_accio)
            df_accio['Close'].plot(title="AMZN")
            #LLAMO AL METODO GRAFICAR Y LE PASO EL PARAMETRO df_accion 
            accio.graficar(df_accio)
            
        elif opcion == '3':     
            print("opcion3")
                       
        elif opcion == '4':        
            break;

        
if __name__ == "__main__":
    main()
    
        
        