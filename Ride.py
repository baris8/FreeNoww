class Ride:
    def __init__(self, date, price, pm, bs, lp):
        self.date = date.replace("/", ".")
        self.price = price
        self.pm = pm
        self.bs = bs
        self.lp = lp

    def export_for_csv(self):
        if self.pm == "APP":
            return self.date + ";" + self.lp + ";;" + str(self.price).replace('.', ',') + "\n"
        else:
            return self.date + ";" + self.lp + ";" + str(self.price).replace('.', ',') + ";\n"