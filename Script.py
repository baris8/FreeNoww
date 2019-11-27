from Ride import Ride

def main():
    file = input("Bitte geben sie den Dateinamen ein:\n")
    f = open(file+".csv", "r")
    f.readline()

    car1013 = "DATE;LP;BAR;APP\n"
    car398 = "DATE;LP;BAR;APP\n"

    for line in f:

        items = line.split(",")

        ride = get_data(items)

        if "398" in ride.lp and ride.bs == "ACCOMPLISHED":
            car398 += ride.export_for_csv()
        elif "1013" in ride.lp and ride.bs == "ACCOMPLISHED":
            car1013 += ride.export_for_csv()

    month = input("Bitte geben sie den Monat ein:\n")

    export_to_file(car1013, "1013-"+ month)
    export_to_file(car398, "398-" + month)

def get_data(items):
    # Date
    date = items[-10].split(" ")[0]
    # Price
    price = 0
    valueStr = items[-8]
    tipStr = items[-7]
    value = 0
    tip = 0
    if len(valueStr) > 0:
        value = float(items[-8])
    if len(tipStr) > 0:
        tip = float(items[-7])
    price = round(value + tip, 2)
    # Payment Method
    pm = items[-5]
    # Booking State
    bs = items[-4]
    # License Plate
    lp = items[-1].replace("\n", "")

    return Ride(date, price, pm, bs, lp)

def export_to_file(output, name):
    with open(name +".csv", "w") as file:
        file.write(output)

if __name__ == "__main__":
    main()