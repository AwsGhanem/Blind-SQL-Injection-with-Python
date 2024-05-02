# Blind SQL Injection attack using a Python Script - PortSwigger Lab
## Exploiting SQL injection attack within a vulnerable website (Lab name: Blind SQL injection with conditional responses)

An Automated way for **testing the SQL query** to a specific username, then **finding the password length automatically**, also there is an option to **extract the hash value of the user**.
## 

**This code is a solution to the problem of running N number of Sniper attacks to extract the password. N represents the Password length, assuming that we know the vulnerable SQL query**

**Requriements:**
- Changing the TrackingId
- Changing the SessionId
- Changing the csrf value



# I performed the script on this Lab from PortSwigger
![image](https://github.com/AwsGhanem/Blind-SQL-Injection-with-Python/assets/123994471/132a48a6-58e5-405c-9eae-8c750b95fecf)

# Get the required values from BurpSuite by viewing the login request

![image](https://github.com/AwsGhanem/Blind-SQL-Injection-with-Python/assets/123994471/74249a0f-3e15-49c3-b46c-1a4a910046aa)

![image](https://github.com/AwsGhanem/Blind-SQL-Injection-with-Python/assets/123994471/8f9be079-ee39-4433-b855-2b2ceb6bd997)

**Copy and paste all the required values from the request into the Python script,`Make sure that the values are generated recently or just relaunch the lab and take them`**

  
# Testing the Code
![Screenshot 2024-05-02 184700](https://github.com/AwsGhanem/Blind-SQL-Injection-with-Python/assets/123994471/e62e8897-dd71-4f41-9a9a-1ff91cf95e54)


## About the Script
The code only operates for this lab so far, but the concept can be developed to acomodate on more complex Blind SQL injection attacks
