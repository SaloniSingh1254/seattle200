import requests
import csv
import time

GITHUB_TOKEN = ''
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Step 1: Fetch the list of users from Seattle with over 200 followers using pagination
def fetch_users():
    users = []
    page = 1
    while True:
        url = f'https://api.github.com/search/users?q=location:seattle+followers:>200&per_page=100&page={page}'
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break  # Exit the loop if there is an error

        page_users = response.json().get('items', [])
        if not page_users:
            break  # Exit the loop if there are no more users

        users.extend(page_users)
        page += 1
        time.sleep(1)  # To avoid hitting the API rate limit

    return users

# Step 2: Fetch detailed user information using the user's URL
def fetch_user_details(user_url):
    response = requests.get(user_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {}

# Step 3: Clean company names
def clean_company(company):
    return company.strip('@').strip().upper() if company else ''

# Step 4: Write users to CSV
def write_users_csv(user_data):
    with open('users.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=user_data[0].keys())
        writer.writeheader()
        writer.writerows(user_data)


# Main logic to fetch user data and store in CSV
def main():
    users = fetch_users()
    user_data = []

    # For each user, fetch their detailed information
    for user in users:
        print(f"Fetching details for {user['login']}")
        user_details = fetch_user_details(user['url'])

        if user_details:
            user_info = {
                'login': user_details.get('login', ''),
                'name': user_details.get('name', ''),
                'company': clean_company(user_details.get('company', '')),
                'location': user_details.get('location', ''),
                'email': user_details.get('email', ''),
                'hireable': user_details.get('hireable', ''),
                'bio': user_details.get('bio', ''),
                'public_repos': user_details.get('public_repos', 0),
                'followers': user_details.get('followers', 0),
                'following': user_details.get('following', 0),
                'created_at': user_details.get('created_at', ''),
            }
            user_data.append(user_info)

        # To avoid hitting GitHub rate limits, pause between requests
        time.sleep(1)

    # Write the fetched user data to CSV
    if user_data:
        write_users_csv(user_data)
        print(f"Successfully wrote {len(user_data)} users to users.csv")

# Run the script
if __name__ == '__main__':
    main()
