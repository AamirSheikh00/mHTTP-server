# Get this from the config file
logPath = './logs/get_log.txt'

# Log format
# Req <> Status Line <> Timestamp


class Logger():
    def __init__(self):
        pass

    def generate(self, req, res):
        logFile = open(logPath, 'a')
        res = res.split('\r\n')
        # req = req.split('\n')
        params = {}
        for i in res[1:]:
            try:
                headerField = i[:i.index(':')]
                params[headerField] = i[i.index(':') + 2:len(i)]
            except:
                pass
        l = len(req)
        log = req[:l-1] +"  "+ res[0] + "  " + params['Date'] + '\n'
        logFile.write(log)
        logFile.close()