import sys, os

if sys.version_info.major != 3:
    print("Python version 3 required to run this script")
    exit(1)

service_file = open("projectfetcher.service",'w')

def println(text=""):
    service_file.write(text+'\n')

# Writing Unit part of Unit
println('[Unit]')
println("Description=Github Projects Auto Fetcher")
println("After=multi-user.target")
println()
# Writing the actual Service
println("[Service]")
println("Type=simple")
println(f"ExecStart={sys.executable} {os.path.dirname(__file__)}/projectfetcher.py")
println()
# Writing the actual Install
println("[Install]")
println("WantedBy=multi-user.target")

