from json import dump, load

class Scoreboard:
    def __init__(self, player_name: str, file_name: str = "scoreboard.json") -> None:
        self.player_name = player_name
        self.file_name = file_name
        # self.score = None

    def load_data(self):
        try:
            with open(self.file_name, "r") as file:
                data = load(file)
            return data

        except FileNotFoundError:
            print("ERROR: File not found")
            data: dict = {"guset": 0}
            with open(self.file_name, 'w') as file:
                  dump(data, file)
            print("INFO: File created")
            return data

        except Exception as e:
            print(f"Qualcosa è andato storto :/ --> {e}")

    def get_score(self) -> int:
        data = self.load_data()
        if data:
            if self.player_name in data:
                return int(data[self.player_name])
            return 0
        else:
            return 0

    def update_score(self, new_score: int) -> bool:
        data = self.load_data()

        if data:
            data[self.player_name] = new_score
        else:
            return False

        try:
            with open(self.file_name, "w") as file:
                dump(data, file)
            return True

        except Exception as e:
            print(f"Qualcosa è andato storto :/ --> {e}")
            return False

    def update_record(self, new_score: int) -> None:
        if new_score > self.get_score():
            self.update_score(new_score=new_score)
