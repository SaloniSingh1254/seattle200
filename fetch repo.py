import requests
import csv
import time

GITHUB_TOKEN = ''
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Step 1: Read users from the users.csv
def read_users_csv():
    users = []
    with open('users.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row['login'])
    return users

# Step 2: Fetch repositories for a given user (up to 500 most recently pushed)
def fetch_user_repos(user_login):
    repos = []
    page = 1
    while True:
        url = f'https://api.github.com/users/{user_login}/repos?per_page=100&page={page}&sort=pushed'
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            break  # Exit the loop if there is an error
        
        page_repos = response.json()
        if not page_repos:
            break  # Exit the loop if no more repos
        
        repos.extend(page_repos)
        if len(repos) >= 500:
            break  # Limit to 500 repositories

        page += 1
        time.sleep(1)  # To avoid hitting the API rate limit

    return repos[:500]  # Ensure the limit of 500 repos is respected

# Step 3: Write repositories to CSV
def write_repos_csv(repos_data):
    with open('repositories.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['login', 'full_name', 'created_at', 'stargazers_count', 'watchers_count', 'language', 'has_projects', 'has_wiki', 'license_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(repos_data)

# Main logic to fetch repositories of users in users.csv
def main():
    users = read_users_csv()
    repos_data = []

    # For each user, fetch their repositories
    for user_login in users:
        print(f"Fetching repositories for {user_login}")
        repos = fetch_user_repos(user_login)

        # Process each repository and extract the required fields
        for repo in repos:
            repo_info = {
                'login': user_login,
                'full_name': repo.get('full_name', ''),
                'created_at': repo.get('created_at', ''),
                'stargazers_count': repo.get('stargazers_count', 0),
                'watchers_count': repo.get('watchers_count', 0),
                'language': repo.get('language', ''),
                'has_projects': repo.get('has_projects', False),
                'has_wiki': repo.get('has_wiki', False),
                'license_name': repo.get('license', {}).get('name', '') if repo.get('license') else '',
            }
            repos_data.append(repo_info)

        # To avoid hitting GitHub rate limits, pause between requests
        time.sleep(1)

    # Write the fetched repository data to CSV
    if repos_data:
        write_repos_csv(repos_data)
        print(f"Successfully wrote {len(repos_data)} repositories to repositories.csv")

# Run the script
if __name__ == '__main__':
    main()
