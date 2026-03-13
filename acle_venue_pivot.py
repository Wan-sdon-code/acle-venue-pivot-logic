"""
ACLE 2026: Venue & Schedule Predictor
Logic structured with assistance from Gemini 3 Flash.
"""

from datetime import date, timedelta

# 1. My Trip Dates (Booked weeks ago)
my_arrival = date(2026, 4, 26)
my_departure = date(2026, 5, 1)

# 2. Current Market Data
official_final_date = date(2026, 4, 25)
west_zone_status = "POSTPONED" # Confirmed as of March 14

def calculate_forecast(status):
    # Logic: If matches are postponed, the final window must shift
    if status == "POSTPONED":
        # Predicting a 5-to-10 day shift based on logistical backlog
        new_start = official_final_date + timedelta(days=2)
        new_end = official_final_date + timedelta(days=8)
        return new_start, new_end
    return official_final_date, official_final_date

def main():
    start, end = calculate_forecast(west_zone_status)
    
    # Check if the matches happen while I am in Bangkok
    overlap = (start <= my_departure) and (end >= my_arrival)
    
    print("--- ACLE LOGISTICS PREDICTION ---")
    print(f"Projected Match Window: {start} to {end}")
    print(f"Overlap with Holiday: {'YES - LOGIC VALID' if overlap else 'NO'}")
    print("---------------------------------")

if __name__ == "__main__":
    main()
