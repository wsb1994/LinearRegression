from csv import reader
# read csv file as a list of lists


class data:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            csv_reader = reader(file)
            self.data = list(csv_reader)

        for row in self.data:
            floatrow = [float(item) for item in row]
            row = floatrow

    def cast_to_float(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] = float(self.data[i][j])
