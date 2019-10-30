from cx_Freeze import setup, Executable

base = None    

executables = [Executable("index.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<Library Management App>",
    options = options,
    version = "<any program version number>",
    description = '<any program description>',
    executables = executables
)