import requests
import random
import time


#just run this once to generate the email list as a text file.
#10 dot permutations combined with 200 subaddresses should generate 2000 email permuations.
def gen_rand_emails():
    #example dot variations. google ignores dots
    rand_dots = [
        "my.email",
        "m.y.email",
        "mye.ma.i.l",
        "m.y.em.ail",
        "myemai.l",
        "my.e.ma.il",
        "m.y.ema.i.l",
        "mye.m.a.i.l",
        "m.y.e.m.a.i.l",
        "mye.mai.l"
    ]

    rand_subs = [
        "bostonmail",
        "travelingpersonal",
        "team_boston",
        "service_boston",
        "info_daily",
        "account557",
        "notices69",
        "dashboardadmin",
        "alerts_daily",
        "dashboard23",
        "support_overview",
        "alerts55",
        "accountpersonal",
        "project_smith",
        "infoteam",
        "daily92",
        "dailycentral",
        "manageradmin",
        "noticesadmin",
        "daily2024",
        "smithadmin",
        "updatesgroup",
        "smithcentral",
        "dailypersonal",
        "updatesmail",
        "noticesgroup",
        "servicegroup",
        "noticesteam",
        "teamteam",
        "martin92",
        "tasks2024",
        "project_traveling",
        "alertscentral",
        "martinbackup",
        "updates92",
        "tasks_martin",
        "service_smith",
        "team92",
        "updates_johnson",
        "noticescentral",
        "tasks_workspace",
        "info_boston",
        "overviewbackup",
        "project_daily",
        "noticesmail",
        "johnson123",
        "updates_workspace",
        "service_martin",
        "bostonadmin",
        "boston92",
        "johnsongroup",
        "dashboardgroup",
        "tasks_smith",
        "tasksbackup",
        "johnsonmail",
        "team_traveling",
        "supportmail",
        "taskspersonal",
        "updatesbackup",
        "project_workspace",
        "project92",
        "wright2024",
        "info_adams",
        "account_austin",
        "alerts_detroit",
        "info_nashville",
        "alertsteam",
        "account_vegas",
        "denveradmin",
        "scott123",
        "dashboard_adams",
        "nashville2024",
        "tasksadmin",
        "phoenixmail",
        "support_portland",
        "vegasadmin",
        "wright123",
        "support_turner",
        "tasks_young",
        "atlantagroup",
        "detroitmail",
        "team123",
        "infocentral",
        "account_young",
        "servicemail",
        "updates_hall",
        "account_allen",
        "dashboard_young",
        "projectadmin",
        "supportgroup",
        "account_portland",
        "orlandocentral",
        "serviceteam",
        "infogroup",
        "scott2024",
        "turnergroup",
        "tasks_atlanta",
        "denvergroup",
        "info_austin",
        "service_orlando",
        "projectgroup",
        "service_portland",
        "supportteam",
        "support_walker",
        "team_detroit",
        "phoenix123",
        "support_austin",
        "youngmail",
        "teambackup",
        "projectbackup",
        "support_clark",
        "wrightpersonal",
        "alerts_austin",
        "updates_denver",
        "phoenix2024",
        "team_scott",
        "orlando92",
        "teampersonal",
        "tasks92",
        "info_wright",
        "vegas123",
        "tasksgroup",
        "younggroup",
        "team_orlando",
        "denvercentral",
        "service_turner",
        "phoenixcentral",
        "dashboard_nashville",
        "service2024",
        "houstonpersonal",
        "support_vegas",
        "tasks_vegas",
        "dashboard92",
        "info_denver",
        "vegasgroup",
        "dashboard_scott",
        "alerts_phoenix",
        "detroitgroup",
        "service_allen",
        "tasks_scott",
        "projectcentral",
        "orlando123",
        "alerts_nashville",
        "tasksteam",
        "vegaspersonal",
        "alerts_atlanta",
        "clarkteam",
        "info_scott",
        "dashboard2024",
        "clarkmail",
        "portland123",
        "turnerpersonal",
        "info_atlanta",
        "lewisteam",
        "service_young",
        "project_walker",
        "houston2024",
        "team_hall",
        "updates_scott",
        "project_denver",
        "scott92",
        "walkermail",
        "tasks_houston",
        "updates_vegas",
        "adamsmail",
        "houstongroup",
        "atlantapersonal",
        "turneradmin",
        "project_young",
        "service_wright",
        "accountadmin",
        "vegascentral",
        "projectmail",
        "scottpersonal",
        "allen123",
        "info_walker",
        "austinadmin",
        "updates_houston",
        "walkeradmin",
        "accountgroup",
        "updates_austin",
        "scottadmin",
        "supportadmin",
        "austincentral",
        "teamcentral",
        "austinmail",
        "account_lewis",
        "supportcentral",
        "alertspersonal",
        "project_houston",
        "info_phoenix",
        "tasks_walker",
        "dashboard_atlanta",
        "denver92",
        "allen2024",
        "team_denver",
        "alerts2024",
        "account_orlando",
        "atlantacentral",
        "alerts_allen"
    ]

    combinations = []

    for dot in rand_dots:
        for sub in rand_subs:
            combinations.append(f"{dot}+{sub}@gmail.com")

    random.shuffle(combinations)

    with open("random_emails.txt", "w") as file:
        for combination in combinations:
            file.write(combination + "\n")

def rand_agent():
    user_agent = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4; rv:118.0) Gecko/20100101 Firefox/118.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Android 13; Mobile; rv:118.0) Gecko/20100101 Firefox/118.0",
        "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 13; Samsung Galaxy Tab S8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    ]
    return random.choice(user_agent)

def send_request(i, email):
    #put in whatever vars the form requires
    url = ""
    payload = {
        "EMAIL": email,
        "": "",
        "subscribe": "Subscribe"
    }
    headers = {
        "User-Agent": rand_agent(),
        "Referer": "",
        "Origin": ""
    }

    try:
        response = requests.post(url, params={"u": "", "id": ""}, data=payload, headers=headers)

        if response.status_code == 200 and "Your subscription to our list has been confirmed" in response.text:    
            # Success: Append the email to the file
            with open("successful_emails.txt", "a") as file:
                file.write(f"{i}: {email}\n")
            print(f"\nRequest succeeded! Email '{email}' saved to successful_emails.txt.")
        elif response.status_code == 200 and "Too many subscribe attempts" in response.text:
            print(f"Rate Limited: {response.status_code}")
    except requests.exceptions.RequestException as e:
        with open("failed_emails.txt", "a") as file:
            file.write(f"{i}: {email}\n")
        print(f"\nRequest failed for {email}: {e}")


    #print(response.status_code)  # To check if the request was successful
    #print(response.text)  # To print the response content if needed

#loads premade email list
def load_emails():
    try:
        with open("random_emails.txt", "r") as file:
            rand_emails = [line.strip() for line in file.readlines()]
        print(f"Successfully read {len(rand_emails)} emails from random_emails.txt.\n\n")
        return rand_emails
    except FileNotFoundError:
        print(f"Error: random_emails.txt not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

#pauses execution for a random time between 1 and 5 minutes.
def random_sleep():
    sleep_time = random.uniform((1*60), (5*60)) 
    print(f"Sleeping for {sleep_time:.2f} seconds...")
    time.sleep(sleep_time)



#main
rand_emails = load_emails()

i = 11

for email in rand_emails:
    #print(f"Sending submission for {email}")
    #print(f"{i}. {email}")
    send_request(i, email)
    random_sleep()
    i += 1





