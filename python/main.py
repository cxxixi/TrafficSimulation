import TrafficSimulation


def main():
    flow = 0.5
    rate = [0.5, 0.5, 0.5, 0, 0, 0.5, 0.5, 0, 0,
            0.5, 0.5, 0, 0, 0.5, 0, 0, 0.5, 0.5, 0.5]
    capacity = [10, -1, -1, 10, 10, -1, -1, 10,
                10, -1, -1, 10, 10, -1, 10, 10, -1, -1, -1]
    turnProbs = (0.8, 0.1, 0.1)
    outFile = open("output.csv", "w", newline="")
    simulation = TrafficSimulation.TrafficSimulation(
        rate, capacity, flow, turnProbs, outFile)
    end = 60 * 1
    time = 0
    while time < end:
        print(time)
        time = simulation.nextEvent()
    outFile.close()

if __name__ == "__main__":
    main()
