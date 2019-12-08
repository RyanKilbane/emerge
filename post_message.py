import requests
from users import Users
from workspace import SlackWorkspace

def post_message(message, data, users: Users, workspace: SlackWorkspace):
    # Is this a good idea? Should we instead build a dict keyed on email?
    for member in data["members"]:
        # Filter out deleted users
        if (
            member.get("deleted", False) == False
            and member["profile"].get("email", None) != None
            and member["profile"]["email"].lower() in users
        ):

            print(f'{member["id"]}: {member["real_name"]}')

            rdata = {"token": workspace.token, "users": member["id"]}
            response = requests.post("https://slack.com/api/conversations.open", data=rdata)
            data = response.json()
            channel = data["channel"]["id"]

            rdata = {
                "token": workspace.token,
                "as_user": True,
                "channel": channel,
                "text": """Example message""",
            }
            response = requests.post("https://slack.com/api/chat.postMessage", data=rdata)
            status_code = response.status_code
            if status_code != 200:
                print(f"{status_code}: {response.text}")
