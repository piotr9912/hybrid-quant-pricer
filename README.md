# Hybrid Quant Pricing Engine with Excel UI

A production-style quantitative developer project demonstrating high-performance option pricing engines integrated directly into an Excel Front-Office UI. This hybrid architecture represents standard investment banking workflows (Desk Quant role) where speed meets user accessibility.

## Features
- **Analytical Engine:** Exact Black-Scholes formulas for European options and analytical Greeks calculation (Delta).
- **Stochastic Engine:** Monte Carlo simulation engine for Asian options (arithmetic average) optimized via vectorized NumPy computations.
- **Robust File-Based IPC:** Seamless and stable data transfer using clean JSON state files, bypassing brittle COM/DLL environment conflicts.
- **Production-Grade Error Handling:** Core exceptions are gracefully caught, formatted as JSON, and sent back to Excel safely without causing application crashes.

## Repository Structure
- `pricer_engine.py`: Pure quantitative core logic (mathematical engines).
- `dynamic_pricer_dashboard.py`: Script accepting CLI arguments and generating the `output.json` state.
- `dynamic_pricer_dashboard.xlsm`: Pre-configured Excel Front-End UI serving as the trader's pricing sheet.
- `requirements.txt`: Project dependencies.

## Production Architecture: File-Based IPC (JSON)
