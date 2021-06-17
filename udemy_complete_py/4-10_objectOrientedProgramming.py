# exercise 10: magic methods in python
# dunder / magic methods

class Club:
    def __init__(self, name) -> None:
        self.name = name
        self.players = []
    
    def __len__(self):
        return len(self.players)
    
    def __getitem__(self, i):
        return self.players[i]
    
    def __repr__(self):
        return f"Club {self.name} : {self.players}"

    def __str__(self):
        return f"{self.name} with {len(self)} players"
        
some_club = Club('Arsenal')


some_club.players.append("Rolf")
some_club.players.append("Annie")

print(some_club[0])
print(some_club)