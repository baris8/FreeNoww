from Ride import Ride

class Filter:
    car1013 = "DATE;LP;BAR;APP\n"
    car398 = "DATE;LP;BAR;APP\n"

    def __init__(self, file):
        self.file = file

    def make_rides(self):
        self.file.readline()
        for line in self.file:
            items = line.split(",")

            ride = self.get_data(items)

            if "398" in ride.lp and ride.bs == "ACCOMPLISHED":
                self.car398 += ride.export_for_csv()
            elif "1013" in ride.lp and ride.bs == "ACCOMPLISHED":
                self.car1013 += ride.export_for_csv()

    def get_data(self, items):
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

    def export_to_file(self, name):
        with open(name + "-398.csv", "w") as file:
            file.write(self.car398)
        with open(name + "-1013.csv", "w") as file:
            file.write(self.car1013)