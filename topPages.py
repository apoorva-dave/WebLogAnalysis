import re
import pandas as pd
format_pat= re.compile(
    r"(?P<host>[\d\.]+)\s"
    r"(?P<identity>\S*)\s"
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"
    r"(?P<bytes>\S*)\s"
    r'"(?P<referer>.*?)"\s'
    r'"(?P<user_agent>.*?)"\s*'
)
logPath = "C:\\Users\\Apoorva\\PycharmProjects\\WebLogAnalysis\\sample-access-log.txt"

URLCounts = {}
UserAgents = {}
with open(logPath, "r") as f:
    for line in (l.rstrip() for l in f):
        match= format_pat.match(line)
        if match:
            access = match.groupdict()
            agent = access['user_agent']
            if (not ('bot' in agent or 'spider' in agent or
                             'Bot' in agent or 'Spider' in agent or
                             'W3 Total Cache' in agent or agent == '-')):
                request = access['request']
                fields = request.split()
                if(len(fields)==4):
                    action = fields[0]
                    URL = fields[1]
                    if URL.startswith("/") and "?" in URL:
                        if "/feed" not in URL:
                            if (action == 'GET'):
                                if URL in URLCounts:
                                    URLCounts[URL] = URLCounts[URL] + 1
                                else:
                                    URLCounts[URL] = 1

results = sorted(URLCounts, key=lambda i: int(URLCounts[i]), reverse=True)
#
urlList =[]
for result in results:
    # print(result + ": " + str(URLCounts[result]))
    idx = result.find("?")
    subs = result[:idx]
    urlList.append(subs)

print("Taking top pages visited")
df = pd.DataFrame(urlList)
df = df.head(10)
# print(df)
urlList = df[0].tolist()
urlList = list(set(urlList))
for url in urlList:
    print(url)