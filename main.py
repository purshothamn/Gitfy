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
                if commitMsg == None:
                    if os.path.exists('changelog.txt'):
                        self.command("git commit -m 'Refer_changelog.txt'")
                    else:
                        self.command(f"git commit -m 'added {i}'")
                else:
                    commitMsg = commitMsg.replace(' ','_')
                    self.command(f"git commit -m '{commitMsg}'")
            self.gitPush(force=True)
        else:
            ans = input('Do you want to add all the files?? Y/N')
            if ans != 'y' or ans != 'Y' or ans != 'n' or ans != 'N':
                while True:
                    ans = input('Invalid option!! choose Y/N')
                    if ans == 'y' or ans == 'Y' or ans == 'n' or ans == 'N': 
                        break
            if ans == 'y' or ans == 'Y':
                for i in f:
                    self.command(f'git add {i}')
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
                finalRes = input('Do you want to push the changes to repository?? Y/N')
                if finalRes != 'y' or finalRes != 'Y' or finalRes != 'n' or finalRes != 'N':
                    while True:
                        finalRes = input('Invalid response!! choose Y/N')
                        if finalRes == 'y' or finalRes == 'Y' or finalRes == 'n' or finalRes == 'N':
                            break
                if finalRes == 'Y' or finalRes == 'y':
                    self.gitPush()
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
                if req.find(',') and len(req.split(',')) <= len(f):
                    # print(len(req.split(',')))
                    # input('Debug')
                    che = None
                    for i in req.split(','):
                        for l in f:
                            if re.findall(f'{i}.*',l):
                                # print(l)
                                self.command(f'git add {l}')
                                che = True
                            # else:
                            #     print(l+' not a valid file')
                                # input('debug')
                    if che:
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
                        finalRes = input('Do you want to push the changes to repository?? Y/N')
                        if finalRes != 'y' or finalRes != 'Y' or finalRes != 'n' or finalRes != 'N':
                            while True:
                                finalRes = input('Invalid response!! choose Y/N')
                                if finalRes == 'y' or finalRes == 'Y' or finalRes == 'n' or finalRes == 'N':
                                    break
                        if finalRes == 'Y' or finalRes == 'y':
                            self.gitPush()
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
                        # else:
                        #     print('not a valid file')
                    if che == True:
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
                        finalRes = input('Do you want to push the changes to repository?? Y/N')
                        if finalRes != 'y' or finalRes != 'Y' or finalRes != 'n' or finalRes != 'N':
                            while True:
                                finalRes = input('Invalid response!! choose Y/N')
                                if finalRes == 'y' or finalRes == 'Y' or finalRes == 'n' or finalRes == 'N':
                                    break
                        if finalRes == 'Y' or finalRes == 'y':
                            self.gitPush()
                        if finalRes == 'N' or finalRes == 'n':
                            print('Must do a push!! to repository')
                            return
                    else:
                        print('Error occurred!!')
                        return