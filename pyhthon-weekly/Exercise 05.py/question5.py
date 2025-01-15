import sys

def calculate_statistics(temps):
    temps = list(map(float, temps))
    return max(temps), min(temps), sum(temps) / len(temps)

def main():
    if len(sys.argv) > 1:
        temps = sys.argv[1:]
        max_temp, min_temp, mean_temp = calculate_statistics(temps)
        print(f"Maximum Temperature: {max_temp}")
        print(f"Minimum Temperature: {min_temp}")
        print(f"Mean Temperature: {mean_temp}")
    else:
        print("Please provide temperature readings as command-line arguments.")
main() 