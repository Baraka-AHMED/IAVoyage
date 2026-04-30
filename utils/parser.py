import json

def parse_action(text: str):
    try:
        data = json.loads(text)

        # CAS 1 : déjà liste
        if isinstance(data, list):
            return data

        # CAS 2 : une seule action → on wrap
        if isinstance(data, dict):
            return [data]

        return None

    except:
        return None
