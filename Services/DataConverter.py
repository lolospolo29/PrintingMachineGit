from Model.TradingViewData import TradingViewData
import os
import csv
import json

from Services import SecretsManager


class DataConverter:
    def ConvertJsonToClass(self, json_data):
        data = json.loads(json_data)

        if "tradingViewData" in data:
            tradingViewData = data["tradingViewData"]
            tradingViewClass = TradingViewData(
                ticker=tradingViewData['ticker'],
                broker=tradingViewData['Broker'],
                strategy=tradingViewData['strategie'],  # Die Strategie-Daten
                close=tradingViewData['close'],
                open_price=tradingViewData['open'],
                high=tradingViewData['high'],
                low=tradingViewData['low']
            )
            return tradingViewClass

    def JsonToCsvSafeToFolder(self, json_data, secretsmanager):
        data_path = secretsmanager.get_secret('data_path')

        # JSON-Daten in ein Python-Dictionary umwandeln
        data = json.loads(json_data)

        # Zugriff auf den "tradingViewData"-Teil des Dictionaries
        trading_view_data = data['tradingViewData']

        # Extrahiere relevante Informationen
        broker = trading_view_data['Broker']
        strategy_name = trading_view_data['strategie']['name']
        data_records = trading_view_data['strategie']['additional_info']

        # Erstelle den Pfad für die CSV-Datei
        broker_dir = os.path.join(data_path, broker.lower())
        strategy_dir = os.path.join(broker_dir, strategy_name.lower())
        csv_file_path = os.path.join(strategy_dir, 'data.csv')

        # Erstelle die Ordnerstruktur, falls sie nicht existiert
        os.makedirs(strategy_dir, exist_ok=True)

        # Schreibe die Daten in die CSV-Datei
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for record in data_records:
                writer.writerow(record)


#
# data = json.loads(json_data)
#
# # Auf den Namen des Feldes zugreifen
# for person in data:
#     for key in person.keys():
#         print(f"Feldname: {key}")

