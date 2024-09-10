import json
import os
import random
import time
import json

from Model.TradingViewData import TradingViewData


class DataConverter:
    def __init__(self):
        name = "converter"

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

    # for MongoDB
    def ConvertClassToDict(self, obj):
        if isinstance(obj, list):
            return [self.ConvertClassToDict(item) for item in obj]
        elif hasattr(obj, "__dict__"):
            return {key: self.ConvertClassToDict(value) for key, value in obj.__dict__.items()}
        else:
            return obj

    def ConvertClassToJson(self, obj):
        """
        Converts an object to a JSON string.
        """
        return json.dumps(self.ConvertClassToDict(obj), indent=4)

    def JsonToFileToSafeToFolder(self, json_data, secrets_manager):
        """Speichert JSON-Daten direkt in eine Datei, benannt nach dem Ticker mit Zeitstempel."""
        # Lade den Pfad aus der SecretsManager-Instanz
        data_path = secrets_manager.get_secret('data_path')

        # JSON-Daten in ein Python-Dictionary umwandeln
        data = json.loads(json_data)

        # Zugriff auf den "tradingViewData"-Teil des Dictionaries
        trading_view_data = data['tradingViewData']

        # Extrahiere relevante Informationen
        ticker = trading_view_data['ticker']
        broker = trading_view_data['Broker']
        strategy_name = trading_view_data['strategie']['name']

        # Erzeuge den Dateinamen mit dem Tag, der Uhrzeit und einer 6-stelligen eindeutigen ID
        current_time = time.localtime()
        day = current_time.tm_mday
        hour_minute = time.strftime("%H%M")
        unique_id = random.randint(100000, 999999)  # Zufällige 6-stellige ID
        filename_suffix = f"{day}_{hour_minute}_{unique_id}"

        # Erstelle den Pfad für die JSON-Datei
        broker_dir = os.path.join(data_path, broker.lower())
        strategy_dir = os.path.join(broker_dir, strategy_name.lower())
        ticker_dir = os.path.join(strategy_dir, ticker.lower())
        json_file_path = os.path.join(ticker_dir, f'{ticker}_{filename_suffix}.json')

        # Erstelle den Pfad für die JSON-Datei
        broker_dir = os.path.join(data_path, broker.lower())
        strategy_dir = os.path.join(broker_dir, strategy_name.lower())
        ticker_dir = os.path.join(strategy_dir, ticker.lower())
        json_file_path = os.path.join(ticker_dir, f'{ticker}_{filename_suffix}.json')

        # Erstelle die Ordnerstruktur, falls sie nicht existiert
        os.makedirs(ticker_dir, exist_ok=True)

        # Schreibe die JSON-Daten in die Datei
        with open(json_file_path, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)  # Schöne Ausgabe mit Einrückungen

#
# data = json.loads(json_data)
#
# # Auf den Namen des Feldes zugreifen
# for person in data:
#     for key in person.keys():
#         print(f"Feldname: {key}")
