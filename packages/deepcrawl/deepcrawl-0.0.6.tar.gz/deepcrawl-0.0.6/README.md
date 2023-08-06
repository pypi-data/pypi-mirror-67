# DeepCrawl API Wrapper

This is a package to simplify use of the DeepCrawl API.

pip install deepcrawl

## Usage


```python
# Specify the local directory where the DeepCrawl package is located
import os
os.chdir('D://dev//deepcrawl_api_wrapper//dc_api_wrapper')

import deepcrawl

```

### Create an API connection


```python
#Specify your API credentials
API_ID = '1798'
API_KEY = 'FqZMhe3JrDsWg4sV8TpB77jRAcYLpJbQxHwTSw24yv86sdXM2kFB1J8lSXKMwm8Lel_tMl9B'

# Create a new connection using API credentials
dc = deepcrawl.ApiConnection(API_ID, API_KEY)
```


```python
dc.token
```




    '0qgVSkpQDh5EcrTDQ1CY9YsL-JJfGtBLWMXHnv18zB5N8te_AA_WYEdE0rqx6hunk5VAzTHSNOTDoCRDfsVcSA'



### Get a list of projects in an account


```python
account_id = 4

projects = dc.get_projects(account_id)
```


```python
print('Found ' + str(len(projects)) + ' projects\n')

if len(projects) > 0:
    for project in range(min(5, len(projects))):
        print(projects[project])
    print('...\n')
```

    Found 4 projects
    
    [4/319084] Google Tag Manager Test
    [4/319073] CSV List upload column header test
    [4/318643] www.deepcrawl.com Continuity Tests
    [4/318814] www.homedepot.com JS test
    ...
    
    

### Get a project


```python
project = projects[0]
```


```python
project.project_settings.__dict__['name']
```




    'Google Tag Manager Test'



### Get a list of crawls


```python
for crawl in project.crawls:
    print(crawl)
```

    [319084/2826526] None
    [319084/2824486] 2020-03-26T05:44:44+00:00
    


```python
# Get a specific project and output the name
project_id = 319084
project = dc.get_project(account_id, project_id)
project
```




    [4/319084] Google Tag Manager Test



### Start a crawl for a project


```python
project.start_crawl()
```




    <Response [201]>



### Get a list of crawls for the project


```python
crawls = dc.get_crawls(account_id, project.id)

print(str(len(crawls)) + ' crawls found')
print('Last Crawl run '+ crawls[0].finished_at)
```

### Get a list of reports for the crawl


```python
# for report in dc.get_reports(dc, account_id, project_id, crawls[0].id):
#     print(report.id)
```
