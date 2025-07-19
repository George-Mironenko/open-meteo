from etl_process import extract_transform_load
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ETL pipeline for weather data")
    parser.add_argument("--start_date", type=str, required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end_date", type=str, required=True, help="End date (YYYY-MM-DD)")
    args = parser.parse_args()


    extract_transform_load(args.start_date, args.end_date)