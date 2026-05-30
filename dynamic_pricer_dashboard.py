import sys
import json
import pricer_engine as pe

def main():
    try:
        # sys.argv[0] to nazwa skryptu. Parametry rynkowe zaczynają się od indeksu 1:
        spot = float(sys.argv[1])
        strike = float(sys.argv[2])
        expiry = float(sys.argv[3])
        r = float(sys.argv[4])
        vol = float(sys.argv[5])
        option_type = sys.argv[6]

        # Wywołanie silnika
        price, delta = pe.black_scholes_european(spot, strike, expiry, r, vol, option_type)
        
        # Zapis do pliku wymiany danych
        output = {"price": price, "delta": delta, "status": "OK"}
        with open("C:\\Users\\Piotr\\quant_developer\\output.json", "w") as f:
            json.dump(output, f)
            
    except Exception as e:
        output = {"price": 0, "delta": 0, "status": f"ERROR: {str(e)}"}
        with open("C:\\Users\\Piotr\\quant_developer\\output.json", "w") as f:
            json.dump(output, f)

if __name__ == "__main__":
    main()
