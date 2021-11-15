def investPy(self):
        import investpy
        import pandas as pd
        df_accion=investpy.get_stock_historical_data(stock = self.ticker,
                                        country= self.pais,
                                        from_date= self.from_date,      
                                        to_date= self.to_date)
        return df_accion