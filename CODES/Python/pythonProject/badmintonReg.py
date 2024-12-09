from pymongo import MongoClient

# Connect to MongoDB server (assuming it's running locally)
client = MongoClient('mongodb://localhost:27017/')

# Create or access the database
db = client['BadmintonTournaments']

# Create or access the collection
collection = db['registrations']

# Insert player registration details
def register_player(player_id, player_name, age, phone_no):
    player = {
        'player-id': player_id,
        'p-name': player_name,
        'age': age,
        'phone no': phone_no
    }
    collection.insert_one(player)
    print(f"Player {player_name} registered successfully!")

# Display all registrations
def display_all_registrations():
    players = collection.find()
    print("All Registered Players:")
    for player in players:
        print(f"Player ID: {player['player-id']}, Name: {player['p-name']}, Age: {player['age']}, Phone No: {player['phone no']}")

# Register some players
register_player(1, "John Doe", 25, "1234567890")
register_player(2, "Jane Smith", 28, "0987654321")

# Display all registered players
display_all_registrations()
