import string
import datetime
import csv
import os


def parseMonth(list):
    "This function parsers the months to numbers"
    if(list[0]=="jan"):
        list[0]=1
    if(list[0]=="feb"):
        list[0]=2
    if(list[0]=="mar"):
        list[0]=3
    if(list[0]=="apr"):
        list[0]=4
    if(list[0]=="may"):
        list[0]=5
    if(list[0]=="jun"):
        list[0]=6
    if(list[0]=="jul"):
        list[0]=7
    if(list[0]=="aug"):
        list[0]=8
    if(list[0]=="sep"):
        list[0]=9
    if(list[0]=="oct"):
        list[0]=10
    if(list[0]=="nov"):
        list[0]=11
    if(list[0]=="dec"):
        list[0]=12
    return(list)


def parserDate(fromDate):
    "function parser fromHour to a standard format"
    fromDate = string.replace(fromDate,"from-time=","")
    fromDate = string.replace(fromDate,"till-time=","")
    fromDate=fromDate.split("/")
    fromDate = parseMonth(fromDate)
    return fromDate

def parserTime(fromTime):
    "function parser fromTime to standard datetime format"
    fromTime=fromTime.split(":")
    return fromTime

def parserDateTime( data, time):
    "parser DateTime format"
    data=(parserDate(data))
    time=(parserTime(time))
    dateTime=datetime.datetime(int(data[2]), int(data[0]), int(data[1]), int(time[0]), int(time[1]), int(time[2]))
    return dateTime


def getMac(callingStationId):
    "returns the MAC address"
    callingStationId = string.replace(callingStationId,"calling-station-id=","")
    return callingStationId

def getUp(upload):
    "returns the Upload"
    upload = string.replace(upload,"upload=","")
    return upload

def getDown(download):
    "returns the Download"
    download = string.replace(download,"download=","")
    return download

def getUser(user):
    "returns the User"
    user = string.replace(user,"user=","")
    return user

def getCustomer(customer):
    "returns the Customer"
    customer = string.replace(customer,"customer=","")
    return customer

def getNasPort(nasport):
    "returns the NasPort"
    nasport = string.replace(nasport,"nas-port=","")
    return nasport

def getNasPortType(nasporttype):
    "returns the NasPortType"
    nasporttype = string.replace(nasporttype,"nas-port-type=","")
    return nasporttype

def getNasPortId(nasportid):
    "returns the NasPortId"
    nasportid = string.replace(nasportid,"nas-port-id=","")
    return nasportid

def getUserIp(userip):
    "returns the UserIp"
    userip = string.replace(userip,"user-ip=","")
    return userip

def getHostIp(hostip):
    "returns the HostIP"
    hostip = string.replace(hostip,"host-ip=","")
    return hostip

def getStatus(status):
    "returns the Status"
    status = string.replace(status,"status=","")
    return status

def getFromDate(fromdate):
    "returns the fromDate"
    fromdate = string.replace(fromdate,"from-time=","")
    return fromdate

def getTillDate(tilldate):
    "returns the tillTime"
    tilldate = string.replace(tilldate,"till-time=","")
    return tilldate

def getTerminateCause(terminatecause):
    "returns the TerminateCause"
    terminatecause = string.replace(terminatecause,"terminate-cause=","")
    return terminatecause

def getUptime(uptime):
    "returns the Uptime"
    uptime = string.replace(uptime,"uptime=","")
    return uptime

def getAcct(acct):
    "returns AcctSessionId"
    acct=string.replace(acct,"acct-session-id=","")
    return acct

def createCSVNoParser(fileName="02-05-17"):
    "Open the file"
    f = open(fileName+".txt","r")
    lines = f.readlines()
    f.close

    "Create a temp file without the three first lines"
    f = open(fileName+"newFile.txt","wb")
    header = "id customer user nasport nasporttype nasportid callingstationid userip hostip status fromdate fromtime tilldate tilltime terminatecause uptime download upload acct"
    fieldnames = ['id','customer','user','nasport','nasporttype','nasportid', 'callingstationid','userip','hostip','status','fromdate','fromtime','tilldate','tilltime','terminatecause','uptime','download','upload','acct']
    f.write(header+"\n")
    count = 0
    for line in lines:
        if count>2:
            line=" ".join(line.split())
            f.write(line+'\n')
        count = count+1
    f.close()

    "Creates a CSV file with the header no parser yet"
    in_txt = csv.reader(open(fileName+"newFile.txt","rb"),delimiter = " ")
    out_csv = csv.writer(open(fileName+"_newCSV.csv",'wb'))
    out_csv.writerows(in_txt)



def createCSV(fileName,startDate):

    "Receives a Mikrotik UserManager Session and do the parser"

    #Calls the function to create a temp CSV to help the parser procedure"
    createCSVNoParser(fileName)

    ## Fieldnames for the CSV header
    fieldnames = ['id','customer','user','nasport','nasporttype','nasportid', 'callingstationid','userip','hostip','status','fromdate','fromtime','tilldate','tilltime','terminatecause','uptime','download','upload','acct','from','till']


    #Opening the file on the correct CSV format
    fileCSV = open(fileName+"_newCSV.csv")
    input_file = csv.DictReader(fileCSV)
    with open(fileName+"parsedCSV.csv", 'wb') as csvfile:
        counter=0
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        #writer.writeheader()
        for row in input_file:
            counter=counter+1
            #Initializing variables
            id = 0
            customer = 0
            user = 0
            nasport = 0
            nasporttype = 0
            nasportid = 0
            callingstationid = 0
            userip = 0
            hostip = 0
            status = 0
            fromdate = 0
            fromtime = 0
            tilldate = 0
            tilltime = 0
            terminatecause = 0
            uptime = 0
            download = 0
            upload = 0
            acct = 0


            ## There is no Terminate-Cause
            if(row["uptime"]).find("download") > -1:
                id = row["id"]
                customer = getCustomer((row["customer"]))
                user = getUser((row["user"]))
                nasport = getNasPort((row["nasport"]))
                nasporttype = getNasPortType((row["nasporttype"]))
                nasportid = getNasPortId((row["nasportid"]))
                callingstationid = getMac((row["callingstationid"]))
                userip = getUserIp((row["userip"]))
                hostip = getHostIp((row["hostip"]))
                status = getStatus((row["status"]))
                fromdate = (row["fromdate"])
                fromtime = (row["fromtime"])
                tilldate = (row["tilldate"])
                tilltime = (row["tilltime"])
                terminatecause = 0
                uptime = getUptime((row["terminatecause"]))
                download = getDown((row["uptime"]))
                upload = getUp((row["download"]))
                acct = row["acct"]
                fromDateTime = parserDateTime(fromdate,fromtime)
                tillDateTime = parserDateTime(tilldate,tilltime)
                fromdate = getFromDate((row["fromdate"]))
                tilldate = getTillDate((row["tilldate"]))
                ## There is acct-session in the row and no Terminate-Cause
            else:
                if(row["userip"]).find("acct-session-id") != -1 and (row["uptime"]).find("uptime") != -1  :
                    id = row["id"]
                    customer = getCustomer(row["customer"])
                    user = getUser((row["user"]))
                    nasport = getNasPort((row["nasport"]))
                    nasporttype = getNasPortType((row["nasporttype"]))
                    nasportid = getNasPortId((row["nasportid"]))
                    callingstationid = getMac((row["callingstationid"]))
                    userip = getUserIp((row["hostip"]))
                    hostip = getHostIp((row["status"]))
                    status = getStatus((row["fromdate"]))
                    fromdate = (row["fromtime"])
                    fromtime = (row["tilldate"])
                    tilldate = (row["tilltime"])
                    tilltime = (row["terminatecause"])
                    terminatecause = 0
                    uptime = getUptime(row["uptime"])
                    download = getDown(row["download"])
                    upload = getUp(row["upload"])
                    acct = getAcct((row["userip"]))
                    fromDateTime = parserDateTime(fromdate,fromtime)
                    tillDateTime = parserDateTime(tilldate,tilltime)
                    fromdate = getFromDate((row["fromtime"]))
                    tilldate = getTillDate((row["tilldate"]))
                else:
                    if(row["userip"]).find("acct-session-id") != -1:
                            id = row["id"]
                            customer = getCustomer(row["customer"])
                            user = getUser((row["user"]))
                            nasport = getNasPort((row["nasport"]))
                            nasporttype = getNasPortType((row["nasporttype"]))
                            nasportid = getNasPortId((row["nasportid"]))
                            callingstationid = getMac((row["callingstationid"]))
                            userip = getUserIp((row["hostip"]))
                            hostip = getHostIp((row["status"]))
                            status = getStatus((row["fromdate"]))
                            fromdate = (row["fromtime"])
                            fromtime = (row["tilldate"])
                            tilldate = (row["tilltime"])
                            tilltime = (row["terminatecause"])
                            terminatecause = getTerminateCause((row["uptime"]))
                            uptime = getUptime(row["download"])
                            download = getDown(row["upload"])
                            upload = getUp(row["acct"])
                            acct = getAcct((row["userip"]))
                            fromDateTime = parserDateTime(fromdate,fromtime)
                            tillDateTime = parserDateTime(tilldate,tilltime)
                            fromdate = getFromDate((row["fromtime"]))
                            tilldate = getTillDate((row["tilldate"]))
                            ## Default behavior no Parsing needed
                    else:
                            id = row["id"]
                            customer = getCustomer((row["customer"]))
                            user = getUser((row["user"]))
                            nasport = getNasPort((row["nasport"]))
                            nasporttype = getNasPortType((row["nasporttype"]))
                            nasportid = getNasPortId((row["nasportid"]))
                            callingstationid = getMac((row["callingstationid"]))
                            userip = getUserIp((row["userip"]))
                            hostip = getHostIp((row["hostip"]))
                            status = getStatus((row["status"]))
                            fromdate = (row["fromdate"])
                            fromtime = (row["fromtime"])
                            tilldate = (row["tilldate"])
                            tilltime = (row["tilltime"])
                            terminatecause = getTerminateCause((row["terminatecause"]))
                            uptime = getUptime((row["uptime"]))
                            download = getDown((row["download"]))
                            upload = getUp((row["upload"]))
                            acct = (row["acct"])
                            fromDateTime = parserDateTime(fromdate,fromtime)
                            tillDateTime = parserDateTime(tilldate,tilltime)
                            fromdate = getFromDate((row["fromdate"]))
                            tilldate = getTillDate(row["tilldate"])

#            writer.writerow({'id': id,'customer':customer,'user':user,'nasport':nasport,'nasporttype':nasporttype,'nasportid':nasportid,'callingstationid':callingstationid, 'userip':userip,'hostip':hostip, 'status':status, 'fromdate':fromdate,'fromtime':fromtime, 'tilldate':tilldate,'tilltime':tilltime,'terminatecause':terminatecause, 'uptime':uptime,'download':download, 'upload':upload,'acct':acct,'from':fromDateTime,'till':tillDateTime})

            #fromDateTimeComp = datetime.datetime.strptime(fromDateTime, '%Y-%m-%d %H:%M:%S')
            if fromDateTime>=startDate and (fromDateTime <= (startDate+datetime.timedelta(days=7))):
                writer.writerow({'id': id,'customer':customer,'user':user,'nasport':nasport,'nasporttype':nasporttype,'nasportid':nasportid,'callingstationid':callingstationid, 'userip':userip,'hostip':hostip, 'status':status, 'fromdate':fromdate,'fromtime':fromtime, 'tilldate':tilldate,'tilltime':tilltime,'terminatecause':terminatecause, 'uptime':uptime,'download':download, 'upload':upload,'acct':acct,'from':fromDateTime,'till':tillDateTime})
    fileCSV.close()
    os.remove(fileName+"newFile.txt")
    os.remove(fileName+"_newCSV.csv")


textinput = raw_input("UserManager Filename (ex: 7-31-17): ")
startDate = raw_input("Start Date: (ex: 7/23/2017): ")
startDate=parserDate(startDate)
startDate=datetime.datetime(int(startDate[2]), int(startDate[0]), int(startDate[1]), 0, 0, 0)
createCSV(textinput,startDate)
textinput2 = raw_input("UserManager Filename_02 (ex: h2-7-31-17): ")
createCSV(textinput2,startDate)



in_csv1 = csv.reader(open(textinput+"parsedCSV.csv",'rb'))
in_csv2 = csv.reader(open(textinput2+"parsedCSV.csv",'rb'))
out_csv = csv.writer(open(textinput+"_csvConsolidated.csv",'wb'))
header='id','customer','user','nasport','nasporttype','nasportid', 'callingstationid','userip','hostip','status','fromdate','fromtime','tilldate','tilltime','terminatecause','uptime','download','upload','acct','from','till'
out_csv.writerow(header)
out_csv.writerows(in_csv1)
out_csv.writerows(in_csv2)
