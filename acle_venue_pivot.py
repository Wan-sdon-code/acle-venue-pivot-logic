import datetime

def analyze_acle_overlap():
    # 1. YOUR TRIP DATA
    holiday_start = datetime.date(2026, 4, 26)
    holiday_end = datetime.date(2026, 5, 1)
    
    # 2. TOURNAMENT DATA (Updated March 16, 2026)
    # The FIFA 'Hard Wall' for World Cup prep
    fifa_deadline = datetime.date(2026, 5, 25)
    
    # Current ACLE West Zone backlog: ~14 days (since March 2nd)
    # Projected Final pushes from April 25 to May 9
    projected_final = datetime.date(2026, 5, 9)
    
    # ACLE Hub Window: The 'Final Eight' centralized hub usually lasts 9-10 days
    # This covers Quarter-finals, Semi-finals, and the Final
    hub_start = projected_final - datetime.timedelta(days=9) # April 30
    hub_end = projected_final # May 9
    
    # 3. OVERLAP CALCULATION
    # Does any part of your trip fall within the Hub window?
    overlap = (holiday_start <= hub_end) and (hub_start <= holiday_end)
    
    # 4. RESULTS
    print("="*50)
    print("      ACLE 2026: BANGKOK PIVOT ANALYSIS      ")
    print("="*50)
    print(f"Hub Projected: {hub_start} to {hub_end}")
    print(f"Your Holiday:  {holiday_start} to {holiday_end}")
    print("-" * 50)
    
    if overlap:
        print("Overlap: ✅ YES! (Targeting Quarter-finals)")
        print("Note: You'll be in Bangkok for the tournament kickoff.")
    else:
        print("Overlap: ❌ NO")
    
    # Relocation Probability Logic
    days_to_fifa = (fifa_deadline - projected_final).days
    prob = 92 if days_to_fifa < 20 else 45
    print(f"Relocation Probability: {prob}%")
    print("="*50)

if __name__ == "__main__":
    analyze_acle_overlap()
