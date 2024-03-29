import requests
import csv
temp_list = []
results = requests.get('https://api.github.com/search/repositories?q=is:public+forks:>200+language:Python').json()
for repo in results['items']:
    if repo['stargazers_count'] >= 2000:
        d_tmp = {'name': repo['name'], 'description': repo['description'], 'html_url': repo['html_url'],
                 'watchers_count': repo['watchers_count'], 'stargazers_count': repo['stargazers_count'],
                 'forks_count': repo['forks_count']}
        temp_list.append(d_tmp)

with open('final_repo.csv', 'w') as file:
    fields = ['name', 'description', 'html_url', 'watchers_count', 'stargazers_count', 'forks_count']
    csv_writer = csv.DictWriter(file, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerows(temp_list)
