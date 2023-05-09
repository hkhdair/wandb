import json

# Monkey patch Prodigy dataset loading for testing
# Would bypass the requirement to maintain local database for storing Prodigy files.


class Database:
    def get_dataset(self, dataset):
        # load sample dataset in JSON format
        file_name = f"{dataset}.json"
        with open(f"prodigy_test_resources/{file_name}") as f:
            return json.load(f)
        return []


class Connect:
    def connect(self):
        return Database()
