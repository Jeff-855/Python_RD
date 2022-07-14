from github import Github

github = Github('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')
repository = github.get_user().get_repo('Python_RD_Git')
# path in the repository
filename = 'files/file.json'
content = '{\"name\":\"test\",\"city\":\"Taipei\"}'
# create with commit message
file = repository.get_contents(filename)
print ("size:", file.size)

if file.size > 0:
     content = '{\"name\":\"Jeff\",\"city\":\"Taipei\"}'
     f= repository.update_file(filename, "update_file via PyGithub", content, file.sha)
else :    
     f = repository.create_file(filename, "create_file via PyGithub", content)


