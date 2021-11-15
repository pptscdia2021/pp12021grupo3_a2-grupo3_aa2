def yfinance(self):
        import yfinance as yf
        df = yf.download( tickers=self.ticker,country= self.pais,
                                        from_date= self.from_date,
                                        to_date= self.to_date)
        
        return df