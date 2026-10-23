import math, time

def get_ephemeris():
    now = time.time()
    day_num = (now / 86400.0) + 2440587.5 - 2451545.0
    g = math.radians((357.529 + 0.98560028 * day_num) % 360)
    q = (280.459 + 0.98564736 * day_num) % 360
    L = (q + 1.915 * math.sin(g) + 0.020 * math.sin(2 * g)) % 360
    e = math.radians(23.439 - 0.00000036 * day_num)
    
    ra_sun = math.degrees(math.atan2(math.cos(e) * math.sin(math.radians(L)), math.cos(math.radians(L)))) / 15.0
    dec_sun = math.degrees(math.asin(math.sin(e) * math.sin(math.radians(L))))
    
    m_lon = (218.316 + 13.176396 * day_num) % 360
    m_lat = 5.128 * math.sin(math.radians((93.272 + 13.229350 * day_num) % 360))
    m_ra = (math.degrees(math.atan2(math.sin(math.radians(m_lon)) * math.cos(e), math.cos(math.radians(m_lon)))) / 15.0) % 24.0
    
    return ra_sun, dec_sun, m_ra, m_lat

if __name__ == "__main__":
    sun_ra, sun_dec, moon_ra, moon_lat = get_ephemeris()
    print(f"[EPHEMERIS BRIDGED] Sun(RA:{sun_ra:.2f}h, DEC:{sun_dec:+.2f}°) | Moon(RA:{moon_ra:.2f}h, LAT:{moon_lat:+.2f}°)")
