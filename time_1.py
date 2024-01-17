import ephem
from datetime import datetime, timedelta

def calculate_tithi_ashtottari_dasa(birth_date, birth_time):
    birth_datetime = datetime.combine(birth_date, birth_time)
    birth_date_ephem = ephem.Date(birth_datetime)
    
    observer = ephem.Observer()
    observer.date = birth_date_ephem

    dasa_details = []

    tithis = ['Pratipada', 'Dvitiya', 'Tritiya', 'Chaturthi', 'Panchami',
              'Shashthi', 'Saptami', 'Ashtami', 'Navami', 'Dashami',
              'Ekadashi', 'Dvadashi', 'Trayodashi', 'Chaturdashi', 'Purnima/Amavasya']

    tithi_rulers = ['Venus', 'Sun', 'Moon', 'Mars', 'Mercury', 'Saturn', 'Jupiter', 'Rahu', 'Venus']

    current_date = birth_date_ephem
    for i in range(108):
        moon = ephem.Moon()
        moon.compute(observer)
        birth_moon_phase = moon.phase

        dasa_start_date = current_date
        dasa_end_date = dasa_start_date + birth_moon_phase / 360.0

        dasa_details.append({
            tithi_rulers[i % 9]: {
                'Start': ephem.localtime(dasa_start_date).strftime("%Y-%m-%d %H:%M:%S"),
                'End': ephem.localtime(dasa_end_date).strftime("%Y-%m-%d %H:%M:%S")
            }
        })

        current_date = dasa_end_date

    return dasa_details


birth_date = datetime(2024, 1, 17)
birth_time = datetime.strptime("10:29:13", "%H:%M:%S").time()
tithi_ashtottari_dasa = calculate_tithi_ashtottari_dasa(birth_date, birth_time)


for dasa in tithi_ashtottari_dasa:
    for planet, period in dasa.items():
        print(f"{planet}: {period['Start']} - {period['End']}")
