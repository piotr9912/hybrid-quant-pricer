import numpy as np
from scipy.stats import norm

def black_scholes_european(spot, strike, expiry, r, vol, option_type="call"):
    """Analityczna wycena opcji europejskiej (Black-Scholes) wraz z Deltą."""
    if expiry <= 0:
        price = max(spot - strike, 0) if option_type == "call" else max(strike - spot, 0)
        delta = 1.0 if option_type == "call" and spot > strike else 0.0
        return price, delta

    d1 = (np.log(spot / strike) + (r + 0.5 * vol ** 2) * expiry) / (vol * np.sqrt(expiry))
    d2 = d1 - vol * np.sqrt(expiry)
    
    if option_type.lower() == "call":
        price = spot * norm.cdf(d1) - strike * np.exp(-r * expiry) * norm.cdf(d2)
        delta = norm.cdf(d1)
    else:
        price = strike * np.exp(-r * expiry) * norm.cdf(-d2) - spot * norm.cdf(-d1)
        delta = norm.cdf(d1) - 1.0
        
    return float(price), float(delta)

def monte_carlo_asian_option(spot, strike, expiry, r, vol, option_type="call", steps=50, simulations=50000):
    """Wycena opcji azjatyckiej (zależnej od średniej ceny) przy użyciu Monte Carlo."""
    dt = expiry / steps
    nudt = (r - 0.5 * vol ** 2) * dt
    vtdt = vol * np.sqrt(dt)
    
    # Generowanie losowych przyrostów (wektoryzacja dla szybkości w Pythonie)
    z = np.random.normal(size=(simulations, steps))
    
    # Symulacja ścieżek cenowych
    price_paths = np.zeros((simulations, steps + 1))
    price_paths[:, 0] = spot
    
    for t in range(1, steps + 1):
        price_paths[:, t] = price_paths[:, t - 1] * np.exp(nudt + vtdt * z[:, t - 1])
        
    # Średnia cena arytmetyczna z każdej ścieżki
    path_averages = np.mean(price_paths[:, 1:], axis=1)
    
    if option_type.lower() == "call":
        payoffs = np.maximum(path_averages - strike, 0)
    else:
        payoffs = np.maximum(strike - path_averages, 0)
        
    price = np.exp(-r * expiry) * np.mean(payoffs)
    
    # Wyznaczenie Delty metodą małych zaburzeń (Finite Difference)
    bump = 0.01 * spot
    bumped_averages = path_averages * ((spot + bump) / spot)
    if option_type.lower() == "call":
        bumped_payoffs = np.maximum(bumped_averages - strike, 0)
    else:
        bumped_payoffs = np.maximum(strike - bumped_averages, 0)
    bumped_price = np.exp(-r * expiry) * np.mean(bumped_payoffs)
    
    delta = (bumped_price - price) / bump
    
    return float(price), float(delta)
