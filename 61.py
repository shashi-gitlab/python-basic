import re
import datetime
def dobCalculate(dob,name):
    # print(dob , name)
    ans = re.split("-" , dob) # [20,2,2000]
    # print(ans,ans[2],ans[-1])
    year = int(ans[-1]) #type casting
    # print(year, type(year))
    ans1 = datetime.date.today()
    ans1 = str(ans1)
    # print(ans1 , type(ans1))
    result1 = re.split("-",ans1)
    # print(result1)
    curyear = int(result1[0])
    # print(curyear, type(curyear))
    age = curyear - year
    print(age)

dobCalculate('20-2-2000' , 'user1')
dobCalculate('20-2-2010' , 'user1')
dobCalculate('20-2-1990' , 'user1')