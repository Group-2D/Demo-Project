
daysTest = {"MON":900,
            "FRI":1500}

class Test:
    def __init__(self) -> None:
        self.name = "hello"

myTest = Test()

insertedModule = {myTest:daysTest[0]}

print(insertedModule)