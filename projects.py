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


PROJECT_LIST = [
    _Project(
        path = "/mnt/Data_Drive/Codes/Python/useful-modules/git-src/batteryutils"
    ),
    _Project(
        path = "/mnt/Data_Drive/Codes/Python/useful-modules/git-src/Font Size Mapper"
    ),
    _Project(
        path = "/mnt/Data_Drive/Codes/Python/useful-modules/git-src/OpenCV-Magic"
    )
]


PROJECT_COUNT = len(PROJECT_LIST)

print(f"There {'are' if PROJECT_COUNT != 1 else 'is'} {PROJECT_COUNT} project{'s' if PROJECT_COUNT != 1 else ''} registered.")
