import os

from Services.DataConverter import DataConverter
from Services.SecretsManager import SecretsManager


def main():
    config_file = 'C:\\Users\\Schule\\FIAE_LS5\\src\\PrintingMachineGit\\Config\\config.ini'
    config_dir = os.path.dirname(config_file)
    secrets_path = os.path.join(config_dir, 'secrets.json')

    print(f"Versuche, die Datei zu finden: {secrets_path}")
    print(f"Existiert die Datei? {os.path.exists(secrets_path)}")
    # Erstelle eine SecretsManager-Instanz
    secrets_manager = SecretsManager()

    # Erstelle eine DataConverter-Instanz
    data_converter = DataConverter()

    # Beispiel JSON-Daten
    json_data = '''
    {
        "tradingViewData": {
            "ticker": "AAPL",
            "Broker": "ExampleBroker",
            "strategie": {
                "name": "ExampleStrategy",
                "additional_info": [
                    ["header1", "header2", "header3"],
                    ["value1", "value2", "value3"]
                ]
            },
            "close": 150.0,
            "open": 145.0,
            "high": 155.0,
            "low": 144.0
        }
    }
    '''

    # Konvertiere JSON-Daten in TradingViewData
    trading_view_class = data_converter.ConvertJsonToClass(json_data)
    print(trading_view_class.strategy)


    # Verarbeite die JSON-Daten und schreibe sie in eine CSV-Datei
    data_converter.JsonToCsvSafeToFolder(json_data, secrets_manager)


if __name__ == "__main__":
    main()
