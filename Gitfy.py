import re, os
from subprocess import *

class Gitfy:
    def __init__(self):
        pass
    def command(self,x):
        return str(Popen(x.split(' '), stdout=PIPE).communicate()[0])

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
    
    def addFiles(self,repoDir=None,force=False,commitMsg=None):
        if repoDir == None:
            repoDir = os.getcwd()
        else:
            repoDir = repoDir
        os.chdir(repoDir)
        f = []
        f.extend(self.getNewFiles())
        print('lists of New files that can be added: '+str(f))
        if force:
            for i in f:
                self.command(f'git add {i}')
                self.command(f"git commit -m 'added{i}'")
            self.command('git push -uf origin master ')
        else:
            ans = input('Do you want to add all the files?? Y/N')
            if ans != 'y' or ans != 'Y' or ans != 'n' or ans != 'N':
                while True:
                    ans = input('Invalid option!! choose Y/N')
                    if ans == 'y' or ans == 'Y' or ans == 'n' or ans == 'N': 
                        break
            if ans == 'y' or ans != 'Y':
                for i in f:
                    self.command(f'git add {i}')
                if commitMsg == None:
                    if os.path.exists('changelog.txt'):
                        self.command("git commit -m 'Refer changelog.txt'")
                    else:
                        res = input('Please type a valid commit message')
                        if len(res) == 0:
                            while True:
                                res = input('Please type a valid commit message cannot be blank')
                                if len(res) > 0:
                                    break
                        self.command(f"git commit -m {res}")
                else:
                    self.command(f"git commit -m {commitMsg}")
                finalRes = input('Do you want to push the changes to repository?? Y/N')
                if finalRes != 'y' or finalRes != 'Y' or finalRes != 'n' or finalRes != 'N':
                    while True:
                        finalRes = input('Invalid response!! choose Y/N')
                        if finalRes == 'y' or finalRes == 'Y' or finalRes == 'n' or finalRes == 'N':
                            break
                if finalRes == 'Y' or finalRes == 'y':
                    self.command('git push -uf origin master')
                if finalRes == 'N' or finalRes == 'n':
                    print('Must do a push!! to repository')
                    return
            
            if ans == 'N' or ans == 'n':
                print(f)
                req = input('Type in the file to add!! to add multiple files use (,) to separate')
                if len(req) == 0:
                    while True:
                        req = input('Must added atleast one file!!')
                        if len(req) > 0:
                            break
                if req.find(',') and len(req.split(',')) == len(f):
                    che = None
                    for i in req.split(','):
                        for l in f:
                            if re.findall(f'{i}.*',l):
                                self.command(f'git add {l}')
                                che = True
                            else:
                                print('not a valid file')
                    if che == True:
                        if commitMsg == None:
                            if os.path.exists('changelog.txt'):
                                self.command("git commit -m 'Refer changelog.txt'")
                            else:
                                res = input('Please type a valid commit message')
                                if len(res) == 0:
                                    while True:
                                        res = input('Please type a valid commit message cannot be blank')
                                        if len(res) > 0:
                                            break
                                self.command(f"git commit -m {res}")
                        else:
                            self.command(f"git commit -m {commitMsg}")
                            finalRes = input('Do you want to push the changes to repository?? Y/N')
                            if finalRes != 'y' or finalRes != 'Y' or finalRes != 'n' or finalRes != 'N':
                                while True:
                                    finalRes = input('Invalid response!! choose Y/N')
                                    if finalRes == 'y' or finalRes == 'Y' or finalRes == 'n' or finalRes == 'N':
                                        break
                            if finalRes == 'Y' or finalRes == 'y':
                                self.command('git push -uf origin master')
                            if finalRes == 'N' or finalRes == 'n':
                                print('Must do a push!! to repository')
                                return
                    else:
                        print('Error occurred!!')
                        return
                else:
                    che = None
                    for e in f:
                        if re.findall(f'{req}.*',e):
                            self.command(f'git add {e}')
                            che = True
                        else:
                            print('not a valid file')
                    if che == True:
                        if commitMsg == None:
                            if os.path.exists('changelog.txt'):
                                self.command("git commit -m 'Refer changelog.txt'")
                            else:
                                res = input('Please type a valid commit message')
                                if len(res) == 0:
                                    while True:
                                        res = input('Please type a valid commit message cannot be blank')
                                        if len(res) > 0:
                                            break
                                self.command(f"git commit -m {res}")
                        else:
                            self.command(f"git commit -m {commitMsg}")
                            finalRes = input('Do you want to push the changes to repository?? Y/N')
                            if finalRes != 'y' or finalRes != 'Y' or finalRes != 'n' or finalRes != 'N':
                                while True:
                                    finalRes = input('Invalid response!! choose Y/N')
                                    if finalRes == 'y' or finalRes == 'Y' or finalRes == 'n' or finalRes == 'N':
                                        break
                            if finalRes == 'Y' or finalRes == 'y':
                                self.command('git push -uf origin master')
                            if finalRes == 'N' or finalRes == 'n':
                                print('Must do a push!! to repository')
                                return
                    else:
                        print('Error occurred!!')
                        return
                    
# print(getNewFiles())
# print(getModified())