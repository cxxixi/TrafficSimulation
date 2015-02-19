import TrafficSimulation
import csv


def main():
    flow = 3
    synchronous = True
    with open("data/Arrival Rates.csv") as inFile:
        reader = csv.reader(inFile)
        arrivalRates = {int(rows[0]): float(rows[1]) for rows in reader}
    with open("data/Travel Matrix.csv") as inFile:
        reader = csv.reader(inFile)
        travelMatrix = {int(rows[0]): rows[1:] for rows in reader}
    for key in travelMatrix:
        for index, item in enumerate(travelMatrix[key]):
            travelMatrix[key][index] = float(travelMatrix[key][index])
    with open("data/Capacity.csv") as inFile:
        reader = csv.reader(inFile)
        capacity = {int(rows[0]): int(rows[1]) for rows in reader}
    with open("data/Signal Timings.csv") as inFile:
        reader = csv.reader(inFile)
        signalTimings = {int(rows[0]): rows[1:] for rows in reader}
    for key in signalTimings:
        for index, item in enumerate(signalTimings[key]):
            signalTimings[key][index] = int(signalTimings[key][index])
    timeLimit = 60 * 60
    for i in range(100):
        print(i)
        simulation = TrafficSimulation.TrafficSimulation(
            arrivalRates, travelMatrix, capacity, flow, signalTimings,
            timeLimit, synchronous)
        simulation.run()
        with open("output/output" + str(i) + ".txt", 'w') as outFile:
            output = simulation.getOutput()
            for elem in output:
                outFile.write("{}\n".format(elem))

if __name__ == "__main__":
    main()
