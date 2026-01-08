import os
import re

def require_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value == "":
        raise RuntimeError(f"Required environment variable '{name}' is not set")
    return value

def updateFile(
    source_path: str,
    old_line: str,
    new_line: str
):
    
    # CASE 1: file does not exist → create it with the new line
    if not os.path.isfile(source_path):
        with open(source_path, "w") as f:
            f.write(new_line + "\n")
        return

    # CASE 2: file exists → update it
    
    # to give permission to read/write/execute
    os.chmod(source_path, 0o755)

    # to read the file
    fin = open(source_path, 'r')

    # to open a temporary output file
    temp_file_source_path = source_path+"1"
    fout = open(temp_file_source_path, 'w')

    # to read the file line by line. Once found, update the line
    for line in fin:
        line=re.sub(old_line, new_line, line)
        fout.write(line)
    
    # to close the opened file
    fin.close()
    fout.close()

    #remove the old file and change the temp output filename
    os.remove(source_path)
    os.rename(temp_file_source_path, source_path)


def main():
    
    # to check if SourcePath and BuildNum env variable exist
    source_path = require_env("SourcePath")
    build_number = require_env("BuildNum")

    source_path = os.path.join(os.environ["SourcePath"],"develop","global","src")
    build_number = os.environ["BuildNum"]

    #to update SContruct file
    updateFile(
        source_path=source_path+"/SConstruct.py",
        old_line="point\=\d+",
        new_line="point="+build_number
    )

    #to update version file
    updateFile(
        source_path=source_path+"/VERSION.py",
        old_line="ADLMSDK_VERSION_POINT=\d+",
        new_line="ADLMSDK_VERSION_POINT="+build_number
    )

main()



