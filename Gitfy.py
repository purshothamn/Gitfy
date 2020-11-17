import re, os
from subprocess import *

class Gitfy:
    def __init__(self):
        pass

    def command(self,x):
        return str(Popen(x.split(' '), stdout=PIPE).communicate()[0])

    def gitInit(self):
        status = self.command('git init')
        print(status.replace('\\n','').replace("b'",''))

    def gitConfig(self, remoteName, url, username=None, email=None, global_config=False):
        self.command(f'git remote add {remoteName} {url}')
        if global_config:
            if username == None:
                pass
            else:
                self.command(f'git config --global user.name {username}')
            if email == None:
                pass
            else:
                self.command(f'git config --global user.email {email}')
        else:
            if username == None:
                pass
            else:
                self.command(f'git config user.name {username}')
            if email == None:
                pass
            else:
                self.command(f'git config user.email {email}')

    def gitStatus(self):
        status = self.command('git status')
        status = status.replace('\\t','  ')
        status = status.split('\\n')
        for s in status:
            print(s.replace('\\',' '))

    def getNewFiles(self,repoDir=None):
        if repoDir == None:
            repoDir = os.getcwd()
        else:
            repoDir = repoDir
        os.chdir(repoDir)
        c = self.command('git status')
        if 'Untracked files:' in c.split('\\n'):
            f = c.split('Untracked files:')[1][1:].split("\n")[0].split('\\n')
            lf = []
            checker = None
            for e in f:
                z = e.replace('\\t','#')
                if re.findall('#.*',z):
                    lf.append(z.replace('#',''))
                    checker = True
            if checker:
                return lf
        else:
            return []

    def getModified(self,repoDir=None):
        if repoDir == None:
            repoDir = os.getcwd()
        else:
            repoDir = repoDir
        os.chdir(repoDir)
        c = self.command('git status')
        if 'Changes not staged for commit:' in c.split('\\n'):
            f = c.split('Changes not staged for commit:')[1][1:].split("\\n")
            lf = []
            checker = None
            for e in f:
                z = e.replace('\\t','')
                if re.findall('modified:.*',z):
                    lf.append(e.replace('\\tmodified:   ',''))
                    checker = True
            if checker:
                return lf
        else:
            return []

    def addNewFiles(self,repoDir=None,files=None):
        if repoDir == None:
            repoDir = os.getcwd()
        else:
            repoDir = repoDir
        os.chdir(repoDir)
        gf = self.getNewFiles()
        if len(gf) > 0:
            f = []
            checker = None
            if files == None:
                files = self.getNewFiles()
                f.extend(files)
                checker = True
            else:
                cfile = self.getNewFiles()
                if files.find(','):
                    for i in files.split(','):
                        if i in cfile:
                            f.append(i)
                            checker = True
                        else:
                            print(f'not a valid file {i}')
                elif files.find(' '):
                    for i in files.split(' '):
                        if i in cfile:
                            f.append(i)
                            checker = True
                        else:
                            print(f'Not a valid file {i}')
                elif ',' not in files and ' ' not in files:
                        if files in cfile:
                            f.append(files)
                            checker = True
                        else:
                            print(f'Not a valid file {i}')
            if checker:
                for e in f:
                    self.command(f'git add {e}')
                print('New files added: '+str(f))
        else:
            print('No files to add')    

    def addModifiedFiles(self,repoDir=None,files=None):
        if repoDir == None:
            repoDir = os.getcwd()
        else:
            repoDir = repoDir
        os.chdir(repoDir)
        gm = self.getModified()
        if len(gm) > 0:
            f = []
            checker = None
            if files == None:
                files = self.getModified()
                f.extend(files)
                checker = True
            else:
                cfile = self.getModified()
                if files.find(','):
                    for i in files.split(','):
                        if i in cfile:
                            f.append(i)
                            checker = True
                        else:
                            print(f'not a valid file {i}')
                elif files.find(' '):
                    for i in files.split(' '):
                        if i in cfile:
                            f.append(i)
                            checker = True
                        else:
                            print(f'Not a valid file {i}')
                elif ',' not in files and ' ' not in files:
                        if files in cfile:
                            f.append(files)
                            checker = True
                        else:
                            print(f'Not a valid file {i}')
            if checker:
                for e in f:
                    self.command(f'git add {e}')
                print('New files added: '+str(f))
        else:
            print('No files modified')

    def gitCommit(self,commitMsg=None):
        if commitMsg == None:
            if os.path.exists('changelog.txt'):
                self.command("git commit -m 'Refer_changelog.txt'")
            else:
                res = input('Please type a valid commit message')
                if len(res) == 0:
                    while True:
                        res = input('Please type a valid commit message cannot be blank')
                        if len(res) > 0:
                            break
                res = res.replace(' ','_')
                self.command(f"git commit -m '{res}'")
        else:
            commitMsg = commitMsg.replace(' ','_')
            self.command(f"git commit -m '{commitMsg}'")

    def gitPull(self, remote=None, branch=None):
        if remote == None:
            remote = self.command('git remote').replace("b'",'').replace("\\n'",'')
        else:
            remote = remote
        if branch == None:
            branch = self.command('git branch').replace("b'* ",'').replace("'\\n'",'')
        else:
            branch = branch
        self.command(f'git pull {remote} {branch}')

    def gitPush(self, remote=None, branch=None, force=False):
        if remote == None:
            remote = self.command('git remote').replace("b'",'').replace("\\n'",'')
        else:
            remote = remote
        if branch == None:
            branch = self.command('git branch').replace("b'* ",'').replace("'\\n'",'')
            branch = branch.replace('\\n','')
        else:
            branch = branch
        
        print(branch,remote)
        input('Debug')
        if force:
            self.command(f'git push -uf {remote} {branch}')
        else:
            self.command(f'git push -u {remote} {branch}')