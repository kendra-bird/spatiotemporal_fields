import csv
from datetime import datetime
    
class Field:
    
    x_loc = 0
    y_loc = 0
    x2_loc = 0
    y2_loc = 0

    def __init__(self, filename):
        try:
            with open(filename, 'rt') as f:
                reader = csv.reader(f)
                next(reader)
                self.track_list = list(reader)
        except:
            print("error reading file")
            exit()

        try:
            self.dtBegin_list = list()
            for line in self.track_list:
                dt = line[6]
                self.dt_field = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S.%f")
                self.dtBegin_list.append(self.dt_field)
        except:
            print("error creating begin date list")
            exit()

        try:
            self.dtEnd_list = list()
            for line in self.track_list:
                dt = line[7]
                self.dt_field = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S.%f")
                self.dtEnd_list.append(self.dt_field)
        except:
            print("error creating end date list")
            exit() 

    def nearestStart(self, sub_date):
            best_match = min(self.dtBegin_list, key=lambda x: abs(x - sub_date))
            results = 0
            for line in self.track_list:
                if best_match == datetime.strptime(line[6], "%Y-%m-%d %H:%M:%S.%f") and results==0:
                    print("The closest matching start time is: " + str(best_match))
                    self.x_loc = str(line[0])
                    self.y_loc = str(line[1])
                    print("The x and y coordinates are " + (self.x_loc) + " " + (self.y_loc))
                    results = results + 1
            return 

    def nearestEnd(self, sub_date):
            best_match = min(self.dtEnd_list, key=lambda x: abs(x - sub_date))
            results = 0
            for line in self.track_list:
                if best_match == datetime.strptime(line[7], "%Y-%m-%d %H:%M:%S.%f") and results==0:
                    print("The closest matching end time is: " + str(best_match))
                    self.x2_loc = str(line[0])
                    self.y2_loc = str(line[1])
                    print("The x and y coordinates are " + (self.x2_loc) + " " + (self.y2_loc))
                    results = results + 1
            return 

    def bestEstimate(self, sub):
        best_x = ((float(self.x_loc) + float(self.x2_loc))/2)
        best_y = ((float(self.y_loc) + float(self.y2_loc))/2)
        print("The best estimation of the farmer's location at " + sub + " is " + str(best_x) + "," + str(best_y) + ".")
        
def ___main___():
    
    sub = input("Enter a date/time combo on June 18th, 2019 between 07:51:28 AM and 12:55:22 PM.  \n\
    Appropriate format is MM/DD/YYYY HH:MM:SS ")

    try:
        sub_date = datetime.strptime(sub, "%m/%d/%Y %H:%M:%S")
    except:
        print("Oops! an error occured.")
        exit();

    traj_data = Field("NewTrajectoryData.csv")

    traj_data.nearestStart(sub_date)
    traj_data.nearestEnd(sub_date)
    
    traj_data.bestEstimate(sub)
    

    

___main___()


