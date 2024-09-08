# class StrategyFactory:
#     def returnStrategie(self, strategy_name):
#         # Durchlaufe die Liste der Strategien und weise die Daten der entsprechenden Klasse zu
#         for s in self.strategies:
#             if s['name'] == strategy_name:
#                 if strategy_name == 'RSI':
#                     params = s['parameters']
#                     return StrategyA(
#                         period=params.get('period'),
#                         overbought_level=params.get('overbought_level'),
#                         oversold_level=params.get('oversold_level'),
#                         buy_signal=params.get('buy_signal'),
#                         sell_signal=params.get('sell_signal')
#                     )
#         return None
