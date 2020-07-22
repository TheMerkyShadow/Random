import winreg

class Registry():
    def __init__(self,path,user=winreg.HKEY_CURRENT_USER):
        self.User = user
        self.Path = path
        self.Valid = self.Load()
    def Load(self):
        try:
            return winreg.OpenKey(self.User,self.Path,access=winreg.KEY_ALL_ACCESS)
        except FileNotFoundError as e:
            return None
    def Create(self):
        winreg.CreateKey(self.User,self.Path)        
    def __setitem__(self,item,value):
        winreg.SetValueEx(self.Valid,item,0,winreg.REG_SZ,value)
    def __getitem__(self,item=''):
        try:
            return winreg.QueryValueEx(self.Valid,item)[0]
        except FileNotFoundError as e:
            return None
