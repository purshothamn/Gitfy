from Gitfy import Gitfy

g = Gitfy()
# print(g.getNewFiles())
print(g.addModifiedFiles())
print(g.gitCommit())
print(g.gitPush())