import requests


def simple_request():
    response = requests.get("http://127.0.0.1:5000")
    return response.json()

def request_quarks():
    response = requests.get("http://127.0.0.1:5000/quarks")
    return response.json()

def request_one_quark():
    response = requests.get("http://127.0.0.1:5000/quarks/up")
    return response.json()


def add_quark():
    response = requests.post("http://127.0.0.1:5000/quarks", json={"name": "bottom", "charge": "+2/3"})
    return response.json()


def update_quark():
    response = requests.put("http://127.0.0.1:5000/quarks/bottom", json={"name": "bottom", "charge": "-2/3"})
    return response


def delete_quark():
    response = requests.delete("http://127.0.0.1:5000/quarks/bottom")
    return response


# test the functions here:
print(request_quarks())
