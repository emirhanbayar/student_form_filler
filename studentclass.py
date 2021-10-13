class Student:
    def __init__(self, *args):
        self.student_id = int(args[0][0])
        self.accom = str(args[0][1])
        self.rent = args[0][2]
        self.room = args[0][3]
        if(args[0][4] == "Elektrikli Isıtıcı"):
            self.heat = "Elektrikli ısıtıcı"
        else:
            self.heat = args[0][4]
        self.transp = args[0][5]
        self.work = args[0][6]
        self.outstay = args[0][7]
        self.accident = args[0][8]
        self.oper = args[0][9]
        self.protez = args[0][10]
        self.illpass = args[0][11]
        if args[0][12] == "Sürekli Hastalığı Yok":
            self.illness1 = "Sürekli hastalığı yok"
        else:
            self.illness1 = args[0][12]
        self.drug = args[0][13]
        if (args[0][14] == 0):
            self.broth = 1
        else:
            self.broth = int(args[0][14])
        if args[0][12] == "Sürekli Hastalığı Yok":
            self.illness2 = "Sürekli hastalığı yok"
        else:
            self.illness2 = args[0][15]
        self.kanun = args[0][16]
        self.burs = args[0][17]
        self.family_number = int(args[0][18])
        self.sport = args[0][19]
        self.abroad = args[0][20]

