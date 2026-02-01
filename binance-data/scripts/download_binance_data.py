#!/usr/bin/env python3
"""
Binance Public Data Downloader

Download historical market data from https://data.binance.vision/

Usage:
    python download_binance_data.py -t spot -s BTCUSDT -i 1h --start-date 2024-01-01 --end-date 2024-01-31
    python download_binance_data.py -t um -s BTCUSDT ETHUSDT --data-type aggTrades --start-date 2024-01-01
    python download_binance_data.py -t um -s BTCUSDT --data-type fundingRate --period monthly --start-date 2024-01-01
    python download_binance_data.py -t um -s BTCUSDT --data-type metrics --start-date 2024-01-01
"""

import os
import json
import urllib.request
import urllib.error
from datetime import datetime, date, timedelta
from pathlib import Path
from argparse import ArgumentParser, RawTextHelpFormatter
from typing import Optional

# Constants
BASE_URL = "https://data.binance.vision/"
INTERVALS = ["1s", "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1mo"]
DAILY_INTERVALS = ["1s", "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d"]
TRADING_TYPES = ["spot", "um", "cm"]
DATA_TYPES = ["klines", "trades", "aggTrades", "fundingRate", "metrics"]
# fundingRate: only monthly data available
# metrics: only daily data available
FUTURES_ONLY_DATA_TYPES = ["fundingRate", "metrics"]


def get_all_symbols(market_type: str) -> list:
    """Fetch all trading symbols from Binance API."""
    urls = {
        "spot": "https://api.binance.com/api/v3/exchangeInfo",
        "um": "https://fapi.binance.com/fapi/v1/exchangeInfo",
        "cm": "https://dapi.binance.com/dapi/v1/exchangeInfo"
    }

    try:
        response = urllib.request.urlopen(urls[market_type])
        data = json.loads(response.read())
        return [s['symbol'] for s in data['symbols']]
    except Exception as e:
        print(f"Error fetching symbols: {e}")
        return []


def build_url(market_type: str, period: str, data_type: str, symbol: str,
              interval: Optional[str] = None, date_str: Optional[str] = None) -> str:
    """Build download URL for Binance data."""

    # Build path
    if market_type == "spot":
        base_path = f"data/spot/{period}/{data_type}/{symbol}"
    else:
        base_path = f"data/futures/{market_type}/{period}/{data_type}/{symbol}"

    if data_type == "klines" and interval:
        base_path = f"{base_path}/{interval}"

    # Build filename
    if data_type == "klines":
        filename = f"{symbol}-{interval}-{date_str}.zip"
    else:
        filename = f"{symbol}-{data_type}-{date_str}.zip"

    return f"{BASE_URL}{base_path}/{filename}"


def download_file(url: str, save_path: str, checksum: bool = False) -> bool:
    """Download a file from URL to save_path."""

    if os.path.exists(save_path):
        print(f"  [SKIP] Already exists: {save_path}")
        return True

    # Create directory
    Path(os.path.dirname(save_path)).mkdir(parents=True, exist_ok=True)

    try:
        print(f"  [DOWN] {os.path.basename(save_path)}", end=" ")
        urllib.request.urlretrieve(url, save_path)
        print("OK")

        # Download checksum if requested
        if checksum:
            checksum_url = url + ".CHECKSUM"
            checksum_path = save_path + ".CHECKSUM"
            try:
                urllib.request.urlretrieve(checksum_url, checksum_path)
            except:
                pass

        return True

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("NOT FOUND")
        else:
            print(f"ERROR: {e}")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False


def generate_dates(start_date: date, end_date: date, period: str) -> list:
    """Generate date strings for the given period."""
    dates = []
    current = start_date

    if period == "monthly":
        while current <= end_date:
            dates.append(current.strftime("%Y-%m"))
            # Move to next month
            if current.month == 12:
                current = date(current.year + 1, 1, 1)
            else:
                current = date(current.year, current.month + 1, 1)
    else:  # daily
        while current <= end_date:
            dates.append(current.strftime("%Y-%m-%d"))
            current += timedelta(days=1)

    return dates


def main():
    parser = ArgumentParser(
        description="Download Binance historical market data",
        formatter_class=RawTextHelpFormatter
    )

    parser.add_argument("-t", "--type", required=True, choices=TRADING_TYPES,
                        help="Market type: spot, um (USD-M), cm (COIN-M)")
    parser.add_argument("-s", "--symbols", nargs="+",
                        help="Symbol(s) to download (e.g., BTCUSDT ETHUSDT)")
    parser.add_argument("-i", "--intervals", nargs="+", default=["1h"],
                        choices=INTERVALS, help="Kline interval(s)")
    parser.add_argument("--data-type", default="klines", choices=DATA_TYPES,
                        help="Data type to download")
    parser.add_argument("--start-date", required=True,
                        help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", default=None,
                        help="End date (YYYY-MM-DD), default: today")
    parser.add_argument("--period", default="daily", choices=["daily", "monthly"],
                        help="Download daily or monthly files")
    parser.add_argument("-o", "--output", default="./binance_data",
                        help="Output directory")
    parser.add_argument("-c", "--checksum", action="store_true",
                        help="Also download checksum files")
    parser.add_argument("--usdt-only", action="store_true",
                        help="Only download USDT pairs (when no symbols specified)")

    args = parser.parse_args()

    # Validate data type for spot market
    if args.type == "spot" and args.data_type in FUTURES_ONLY_DATA_TYPES:
        print(f"Error: {args.data_type} is only available for futures (um/cm), not spot")
        return

    # Auto-adjust period for fundingRate and metrics
    if args.data_type == "fundingRate" and args.period != "monthly":
        print("Note: fundingRate only has monthly data, switching to monthly")
        args.period = "monthly"
    if args.data_type == "metrics" and args.period != "daily":
        print("Note: metrics only has daily data, switching to daily")
        args.period = "daily"

    # Parse dates
    start = datetime.strptime(args.start_date, "%Y-%m-%d").date()
    end = datetime.strptime(args.end_date, "%Y-%m-%d").date() if args.end_date else date.today()

    # Get symbols
    if args.symbols:
        symbols = [s.upper() for s in args.symbols]
    else:
        print(f"Fetching all {args.type} symbols...")
        symbols = get_all_symbols(args.type)
        if args.usdt_only:
            symbols = [s for s in symbols if s.endswith("USDT")]
        print(f"Found {len(symbols)} symbols")

    # Generate dates
    dates = generate_dates(start, end, args.period)

    # Determine intervals
    intervals = args.intervals if args.data_type == "klines" else [None]
    if args.period == "daily" and args.data_type == "klines":
        intervals = [i for i in intervals if i in DAILY_INTERVALS]

    # Download
    count = 0

    print(f"\nDownloading {args.data_type} for {len(symbols)} symbols")
    print(f"Date range: {start} to {end} ({args.period})")
    print(f"Output: {args.output}\n")

    for symbol in symbols:
        print(f"[{symbol}]")
        for interval in intervals:
            for date_str in dates:
                count += 1

                url = build_url(
                    args.type, args.period, args.data_type,
                    symbol, interval, date_str
                )

                # Build save path
                if args.data_type == "klines":
                    filename = f"{symbol}-{interval}-{date_str}.zip"
                    subdir = f"{args.type}/{args.data_type}/{symbol}/{interval}"
                else:
                    filename = f"{symbol}-{args.data_type}-{date_str}.zip"
                    subdir = f"{args.type}/{args.data_type}/{symbol}"

                save_path = os.path.join(args.output, subdir, filename)
                download_file(url, save_path, args.checksum)

    print(f"\nDone! Processed {count} files.")


if __name__ == "__main__":
    main()
