from typing import Any


class Kurs:
    def __init__(self, departure: str, destination: str, distance: float, courseNumber: int, vehicleMark: str):
        self.departure = departure
        self.destination = destination
        self.distance = distance
        self.courseNumber = courseNumber
        self.vehicleMark = vehicleMark

        @property
        def get_departure(self) -> None:
            return self.departure

        @departure.setter
        def departure(self, value: str) -> FirmaTransportowa:
            self.departure = value

        @property
        def get_destination(self) -> None:
            return self.destination

        @destination.setter
        def destination(self, value: str) -> FirmaSpożywcza:
            self.destination = value

        @property
        def get_distance(self) -> None:
            return self.distance

        @distance.setter
        def distance(self, value: float) -> Odcinek:
            self.distance = value

        @property
        def get_courseNumber(self) -> None:
            return self.courseNumber

        @courseNumber.setter
        def courseNumber(self, value: int) -> FirmaSpożywcza:
            self.courseNumber = value

        @property
        def get_vehicleMark(self) -> None:
            return self.vehicleMark

        @vehicleMark.setter
        def vehicleMark(self, value: str) -> Pojazd:
            self.vehicleMark = value

        def returnVehicleMark() -> None:
            return vehicleMark

        def __str__(self):
            return f'Marka {self.vehicleMark} odjazd z:{self.departure}, jedzie do: {self.destiantion}, dystans: {self.distance}' \
                   f'numer kursu: {self.courseNumber}'


class Pojazd(Kurs):
    def __init__(self, vehicleBrand: str, fuelUsage: float, capacity: float, driverName: str, driverSurname: str):
        super.__init__(self.courseNumber, self.vehicleMark)
        self.vehicleBrand = vehicleBrand
        self.fuelUsage = fuelUsage
        self.capacity = capacity
        self.driverName = driverName
        self.driverSurname = driverSurname

        @vehicleBrand.setter
        def vehicleBrand(self, value):
            self.vehicleBrand = self.vehicleMark

        @fuelUsage.setter
        def fuelUsage(self, value):
            self.fuelUsage = value

        @capacity.setter
        def capacity(self, value):
            self.capacity = value

        @driverName.setter
        def driverName(self, value):
            self.driverName = value

        @driverSurname.setter
        def driverSurname(self, value):
            self.driverSurname = value


class FirmaTransportowa(Kurs):
    def __init__(self, companyName: str, companyCity: str, numberOfVehicles: int, ):
        super.__init__(self.courseNumber, self.departure)
        self.companyName = companyName
        self.departure = companyCity
        self.numberOfVehicles = numberOfVehicles

        @companyName.setter
        def companyName(self, value):
            self.companyName = value

        @companyCity.setter
        def companyCity(self, value):
            self.companyCity = value

        @numberOfVehicles.setter
        def numberOfVehicles(self, value):
            self.numberOfVehicles = value


class Odcinek(Kurs):
    def __init__(self, startPoint: str, endPoint: str, ):
        super.__init__(self.departure, self.destination)
        self.startPoint = startPoint
        self.endPoint = endPoint


class FirmaSpożywcza(Kurs):
    def __init__(self, companyName: str, companyCity: str, ):
        super.__init__(self.destination, self.courseNumber)
        self.companyName = companyName
        self.companyCity = companyCity


k1 = Kurs("Katowice", "Kraków", 100, 2, "DAF")
