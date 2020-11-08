from Ride import Ride

class Filter:
    car1013 = "DATE;LP;BAR;APP\n"
    car398 = "DATE;LP;BAR;APP\n"

    def __init__(self, file):
        self.file = file
        self.rides = []
        self.create_rides()

    def create_rides(self):
        self.file.readline()
        for line in self.file:
            items = line.split(",")

            ride = self.get_data(items)
            self.rides.append(ride)

    def filter_rides(self, month):
        filtered = []
        for ride in self.rides:
            if ride.date.split(".")[1] == month:
                filtered.append(ride)
        self.rides.clear()
        self.rides = filtered

    def get_data(self, items):
        print(items)
        # Date
        date = items[-12].split(" ")[0]
        # Price
        price = 0
        valueStr = items[-11]
        tipStr = items[-10]
        value = 0
        tip = 0
        if len(valueStr) > 0:
            value = float(items[-11])
        if len(tipStr) > 0:
            tip = float(items[-10])
        price = round(value + tip, 2)
        # Payment Method
        pm = items[-6]
        # Booking State
        bs = items[-5]
        # License Plate
        lp = items[-1].replace("\n", "")

        return Ride(date, price, pm, bs, lp)

    def rides_to_str(self):
        for ride in self.rides:
            if "398" in ride.lp and ride.bs == "ACCOMPLISHED":
                self.car398 += ride.export_for_csv()
            elif "1013" in ride.lp and ride.bs == "ACCOMPLISHED":
                self.car1013 += ride.export_for_csv()

    def export_to_file(self, name):
        self.rides_to_str()
        with open(name + "-398.csv", "w") as file:
            file.write(self.car398)
        with open(name + "-1013.csv", "w") as file:
            file.write(self.car1013)
