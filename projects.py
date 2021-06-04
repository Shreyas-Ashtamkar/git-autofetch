import os

class _Project:
    def __init__(self, name=None, url=None, path=None) -> None:
       self.name   = name or path.split('/')[-1]
       self.url    = url
       self._path  = path
       self.path   = self._path
    
    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, val=None):
        try:
            if not val or val.strip() == '':
                raise ValueError("FATAL ERROR : Path not supplied or blank")

            if not os.path.exists(val):
                raise NotADirectoryError(f"{val} is not a directory")
            
            if '.git' not in os.listdir(val):
                raise RuntimeError(f"{self.name} is not a git repository")
                 
        except Exception as e:
            print(e)
            exit(1)
    
    def __str__(self) -> str:
        return self.name
