import sys
from statistics import mean

def display_help():
    print("""
    
    Usage: python main.py <txtfilename>
    
    This program processes F1 lap timing data and displays:
    1. Race name
    2. Fastest driver and time
    3. Driver statistics
    4. Leaderboard in descending order
    """)

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            race_name = file.readline().strip()
            lap_data = []
            for line in file:
                if line.strip():
                    try:
                        driver_code = line[:3].strip()
                        lap_time = float(line[3:].strip())
                        lap_data.append((driver_code, lap_time))
                    except ValueError:
                        print(f"Warning: Invalid lap time format in line: {line.strip()}")
        return race_name, lap_data
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)

def load_driver_details(details_file="f1_drivers.txt"):
    driver_details = {}
    try:
        with open(details_file, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    try:
                        parts = line.strip().split(',')
                        if len(parts) != 4:
                            print(f"Warning: Skipping invalid line in {details_file}: {line.strip()}")
                            continue
                        car_number, driver_code, full_name, team = parts
                        driver_details[driver_code] = {
                            'full_name': full_name,
                            'team': team,
                            'team_code': team[:3].upper(),  # Generate a team code from the team name
                            'car_number': car_number
                        }
                    except Exception as e:
                        print(f"Warning: Could not parse line '{line.strip()}': {e}")
        return driver_details
    except FileNotFoundError:
        print(f"Error: {details_file} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Could not parse {details_file}. Details: {e}")
        sys.exit(1)

def calculate_statistics(lap_data, driver_details):
    driver_stats = {}

    for driver_code, lap_time in lap_data:
        if driver_code not in driver_stats:
            driver_stats[driver_code] = {
                'lap_times': [],
                'details': driver_details.get(driver_code, {
                    'full_name': driver_code,
                    'team': 'Unknown',
                    'team_code': 'UNK',
                    'car_number': '0'
                })
            }
        driver_stats[driver_code]['lap_times'].append(lap_time)

    total_times = []
    for code, stats in driver_stats.items():
        times = stats['lap_times']
        stats['fastest_time'] = min(times)
        stats['average_time'] = mean(times)
        stats['lap_count'] = len(times)
        total_times.extend(times)

    if not total_times:
        print("Error: No valid lap times found.")
        sys.exit(1)

    fastest_driver = min(driver_stats.items(), key=lambda x: x[1]['fastest_time'])
    fastest_driver_code = fastest_driver[0]
    fastest_time = fastest_driver[1]['fastest_time']

    leaderboard = sorted(driver_stats.items(), key=lambda x: x[1]['fastest_time'], reverse=True)

    return fastest_driver_code, fastest_time, driver_stats, mean(total_times), len(total_times), leaderboard

def main():
    if len(sys.argv) != 2 or sys.argv[1] in ('-h', '--help'):
        display_help()
        return

    file_name = sys.argv[1]
    race_name, lap_data = read_file(file_name)
    driver_details = load_driver_details()

    fastest_driver, fastest_time, driver_stats, overall_average, total_laps, leaderboard = calculate_statistics(lap_data, driver_details)

    print(f"\nRace: {race_name}")
    print(f"Fastest Driver: {fastest_driver} with time {fastest_time:.3f}")

    print("\nDriver Statistics:")
    for code, stats in sorted(driver_stats.items()):
        details = stats['details']
        print(f"Driver {details['full_name']} ({details['team']}, Code {details['team_code']}, Car #{details['car_number']}): "
              f"Fastest Lap = {stats['fastest_time']:.3f}, Average Lap = {stats['average_time']:.3f}, Laps = {stats['lap_count']}")

    print("\nLeaderboard (Fastest First in Descending Order):")
    for rank, (code, stats) in enumerate(leaderboard, 1):
        details = stats['details']
        print(f"{rank}. {details['full_name']} ({details['team']}): {stats['fastest_time']:.3f}")

    print(f"\nOverall Average Lap Time: {overall_average:.3f}")
    print(f"Total Laps: {total_laps}")

if __name__ == '__main__':
    main()
