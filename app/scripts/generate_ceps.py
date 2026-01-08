import csv
import random


def generate_ceps(quantity=10000):
    ceps = set()
    while len(ceps) < quantity:
        cep = f"{random.randint(10000000, 99999999)}"
        cep = f"{cep[:5]}-{cep[5:]}"
        ceps.add(cep)
    return ceps


def generate_ceps_csv(csv_path):
    ceps = generate_ceps()
    with open(csv_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["cep"])
        for cep in ceps:
            writer.writerow([cep])

if __name__ == "__main__":
    generate_ceps_csv("data/ceps.csv")
