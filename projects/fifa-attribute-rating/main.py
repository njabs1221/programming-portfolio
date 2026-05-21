ATTRIBUTES = {
    "shooting": ["Finishing", "Shot Power", "Long Shots", "Volleys", "Penalties", "Positioning"],
    "passing": ["Vision", "Long Passing", "Short Passing", "Crossing", "Curve", "Free Kick Accuracy"],
    "pace": ["Acceleration", "Sprint Speed"],
    "dribbling": ["Agility", "Balance", "Ball Control", "Composure", "Reactions"],
    "defending": ["Interceptions", "Heading", "Marking", "Standing Tackle", "Sliding Tackle"],
    "physical": ["Jumping", "Stamina", "Strength", "Aggression"],
}


def read_rating(label):
    while True:
        value = int(input(f"{label}: "))
        if 0 <= value <= 100:
            return value
        print("Enter a rating from 0 to 100.")


def average(values):
    return sum(values) / len(values)


def read_player():
    player = {"name": input("Player name: ")}

    for category, labels in ATTRIBUTES.items():
        ratings = [read_rating(label) for label in labels]
        player[category] = round(average(ratings), 2)

    attribute_scores = [player[category] for category in ATTRIBUTES]
    player["overall"] = round(average(attribute_scores), 2)
    return player


def print_leaderboard(players):
    print("\nLeaderboard")
    print("-----------")

    ranked_players = sorted(players, key=lambda player: player["overall"], reverse=True)
    for position, player in enumerate(ranked_players, start=1):
        print(f"{position}. {player['name']} - Overall: {player['overall']}")
        for category in ATTRIBUTES:
            print(f"   {category.title()}: {player[category]}")


def main():
    number_of_players = int(input("Number of players: "))
    players = []

    for _ in range(number_of_players):
        players.append(read_player())

    print_leaderboard(players)


if __name__ == "__main__":
    main()
