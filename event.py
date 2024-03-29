class event:
    day=0
    month=0
    year=0
    startTime="00:00"
    endTime="0:00"
    def __init__(self, day,month,year,ST,ET):
        self.day=day
        self.month=month
        self.year=year
        self.startTime=ST
        self.endTime=ET
    