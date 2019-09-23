def main():
    f = open("august.csv", "r")
    f.readline()

    car1013 = ""
    car398 = ""

    for line in f:
        items = line.split(";")

        out = get_data(items)
        if out is not None:
            if "D DH 1013" in out:
                car1013 += out
            else:
                car398 += out

    file_1013 = open("1013.csv", "w+")
    file_1013.write(car1013)
    file_1013.close()

def get_data(items):
    # Date
    date = items[-10].split(" ")[0]
    # Price
    price = 0
    valueStr = items[-8]
    tipStr = items[-7]
    if len(valueStr) > 0 and len(tipStr) > 0:
        value = float(items[-8])
        tip = float(items[-7])
        price = round(value + tip, 2)
    # Payment Method
    pm = items[-5]
    # Booking State
    bs = items[-4]
    # License Plate
    lp = items[-1]

    if bs == "CANCELED":
        return None

    if pm == "APP":
        return date + ";" + lp + ";;" + str(price)
    else:
        return date + ";" + lp + ";" + str(price)

if __name__ == "__main__":
    main()