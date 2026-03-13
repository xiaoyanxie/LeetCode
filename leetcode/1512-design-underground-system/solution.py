from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        """
        checkedIn = {
            cardID -> (stationName, time)
            
        }
        stat = {
            (from, to) -> [totalTime, cnt]

            (Leyton, Waterloo) -> [36, 3],
            (Paradise, Cambridge) -> [14, 1]
        }
        
        "checkIn(45,"Leyton",3)",
        "checkIn(32,"Paradise",8)",
        "checkIn(27,"Leyton",10)",
        "checkOut(45,"Waterloo",15)",
        "checkOut(27,"Waterloo",20)",
        "checkOut(32,"Cambridge",22)",
        "getAverageTime("Paradise","Cambridge")",
        "getAverageTime("Leyton","Waterloo")",
        "checkIn(10,"Leyton",24)",
        "getAverageTime("Leyton","Waterloo")",
        "checkOut(10,"Waterloo",38)",
        "getAverageTime("Leyton","Waterloo")"
        """
        self.checkedIn = {}
        self.stat = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        assert id in self.checkedIn
        checkInStation, checkInTime = self.checkedIn[id]
        del self.checkedIn[id]
        self.stat[(checkInStation, stationName)][0] += (t - checkInTime)
        self.stat[(checkInStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.stat:
            return 0.0
        total, cnt = self.stat[(startStation, endStation)]
        assert cnt > 0
        return total / cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
