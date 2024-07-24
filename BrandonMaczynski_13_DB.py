import sqlite3
import matplotlib.pyplot as plt

# Create a database connection and cursor
conn = sqlite3.connect('population_BM.db')
cursor = conn.cursor()

# Create a table named population
cursor.execute('''CREATE TABLE IF NOT EXISTS population (
                    city TEXT,
                    year INTEGER,
                    population INTEGER
                )''')

# Data for 10 cities in Florida for the year 2023
cities = [
    ('Miami', 2023, 454279),
    ('Orlando', 2023, 309154),
    ('Tampa', 2023, 407599),
    ('Jacksonville', 2023, 949611),
    ('Tallahassee', 2023, 197102),
    ('Fort Lauderdale', 2023, 183109),
    ('St. Petersburg', 2023, 271842),
    ('Hialeah', 2023, 223109),
    ('Gainesville', 2023, 141085),
    ('Sarasota', 2023, 58188)
]

# Insert initial data into the population table
cursor.executemany('INSERT INTO population VALUES (?, ?, ?)', cities)
conn.commit()

# Function to simulate population growth for the next 20 years at a 2% growth rate
def simulate_population_growth():
    for city, year, population in cities:
        for i in range(1, 21):
            new_year = year + i
            new_population = int(population * (1 + 0.02)**i)
            cursor.execute('INSERT INTO population VALUES (?, ?, ?)', (city, new_year, new_population))
    conn.commit()

simulate_population_growth()

# Function to show population growth for a city
def show_population_growth(city):
    cursor.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (city,))
    data = cursor.fetchall()
    if data:
        years = [row[0] for row in data]
        populations = [row[1] for row in data]
        
        plt.figure(figsize=(10, 5))
        plt.plot(years, populations, marker='o')
        plt.title(f'Population Growth for {city}')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.grid(True)
        plt.show()
    else:
        print(f"No data found for city: {city}")

# List of cities
city_names = [city[0] for city in cities]

# Ask user to choose a city
print("Choose a city to display its population growth:")
for i, city in enumerate(city_names, 1):
    print(f"{i}. {city}")

choice = int(input("Enter the number of the city: ")) - 1

if 0 <= choice < len(city_names):
    show_population_growth(city_names[choice])
else:
    print("Invalid choice. Please run the program again and choose a valid option.")

# Close database connection
conn.close()