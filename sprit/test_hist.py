from model.hist_db_functions import hist_data

def main():

    hd = hist_data()

    # Beispiel: "get_station"
    station_id = 'b0ad7578-8e3f-cad2-29bc-82380cf58f88'
    station = hd.get_station(station_id)
    print(station)

    # Beispiel "get_prices"
    tag = '2023-12-01'
    prices = hd.get_date_prices(tag)
    print(prices)

if __name__ == "__main__":
    main()