# q5.py
# CS253 Assignment
# Question 5
# Name: Rajasa Lingamsetti
# Roll Number: 240596

from abc import ABC, abstractmethod


class PhysicsConstraintError(Exception):
    pass


class RollingStock(ABC):
    def __init__(self, id_str, weight):
        self.id_str = id_str
        self.weight = weight

    @abstractmethod
    def get_weight(self):
        pass


class Locomotive(RollingStock):
    def __init__(self, id_str, weight, pull_capacity, fuel_rate):
        super().__init__(id_str, weight)
        self.pull_capacity = pull_capacity
        self.fuel_rate = fuel_rate

    def get_weight(self):
        return self.weight


class FreightCar(RollingStock):
    def __init__(self, id_str, empty_weight, cargo_weight, destination):
        super().__init__(id_str, empty_weight)
        self.cargo_weight = cargo_weight
        self.destination = destination

    @property
    def total_weight(self):
        return self.weight + self.cargo_weight

    def get_weight(self):
        return self.total_weight


class Train:
    def __init__(self):
        self.stocks = []

    # Add a locomotive or freight car to the train
    def couple(self, stock):
        self.stocks.append(stock)

    # Remove and return a stock by its ID
    def uncouple(self, stock_id):
        for stock in self.stocks:
            if stock.id_str == stock_id:
                self.stocks.remove(stock)
                return stock
        return None

    # Return the total weight of the train
    def get_total_weight(self):
        return sum(stock.get_weight() for stock in self.stocks)

    # Return the total pull capacity of all locomotives
    def get_total_pull(self):
        return sum(
            stock.pull_capacity
            for stock in self.stocks
            if isinstance(stock, Locomotive)
        )

    # Raise an error if train is too heavy
    def validate_physics(self):
        if self.get_total_weight() > self.get_total_pull():
            raise PhysicsConstraintError(
                "Train exceeds locomotive pull capacity"
            )


class RailwayNetwork:
    def __init__(self):
        self.links = {}

    # Add a bidirectional railway link
    def add_link(self, station_a, station_b, distance):
        self.links[(station_a, station_b)] = distance
        self.links[(station_b, station_a)] = distance

    # Return distance between two stations
    def get_distance(self, station_a, station_b):
        if (station_a, station_b) not in self.links:
            raise ValueError(
                f"No route exists between {station_a} and {station_b}"
            )

        return self.links[(station_a, station_b)]


def run_delivery_schedule(train, network, route_list):
    total_fuel = 0.0

    for i in range(len(route_list) - 1):
        current_station = route_list[i]
        next_station = route_list[i + 1]

        # Remove all freight cars that have reached their destination
        cars_to_remove = []

        for stock in train.stocks:
            if (
                isinstance(stock, FreightCar)
                and stock.destination == current_station
            ):
                cars_to_remove.append(stock.id_str)

        for stock_id in cars_to_remove:
            train.uncouple(stock_id)

        # Check train physics before leaving the station
        train.validate_physics()

        locomotives = [
            stock
            for stock in train.stocks
            if isinstance(stock, Locomotive)
        ]

        if len(locomotives) == 0:
            raise PhysicsConstraintError("Train has no locomotive")

        average_fuel_rate = (
            sum(loco.fuel_rate for loco in locomotives)
            / len(locomotives)
        )

        distance = network.get_distance(current_station, next_station)

        fuel_used = (
            train.get_total_weight()
            * distance
            * average_fuel_rate
        )

        total_fuel += fuel_used

    return total_fuel


# Example usage
net = RailwayNetwork()
net.add_link("Delhi", "Kanpur", 400)
net.add_link("Kanpur", "Prayagraj", 200)

train = Train()

train.couple(
    Locomotive(
        "L1",
        weight=100,
        pull_capacity=500,
        fuel_rate=0.01
    )
)

train.couple(
    FreightCar(
        "C1",
        empty_weight=20,
        cargo_weight=80,
        destination="Kanpur"
    )
)

train.couple(
    FreightCar(
        "C2",
        empty_weight=20,
        cargo_weight=180,
        destination="Prayagraj"
    )
)

total_fuel = run_delivery_schedule(
    train,
    net,
    ["Delhi", "Kanpur", "Prayagraj"]
)

print(total_fuel)  # Output: 2200.0