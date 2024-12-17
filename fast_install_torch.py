import subprocess
import re

## activate conda
import subprocess
import sys

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error: {error.decode('utf-8')}")
        sys.exit(1)
    return output.decode('utf-8')

# # Ask the user if they want to create a new conda environment
# create_env = input("Do you want to create a new conda environment? (y/n): ").lower()

# if create_env == 'y':
#     # Get environment name and Python version
#     env_name = input("Enter the name for the new environment: ")
#     python_version = input("Enter the Python version (e.g., 3.8): ")

#     # Create new environment
#     print(f"Creating new environment '{env_name}' with Python {python_version}...")
#     create_command = f"conda create -n {env_name} python={python_version} -y"
#     run_command(create_command)

#     # Activate the new environment
#     print(f"Activating environment '{env_name}'...")
#     if sys.platform.startswith('win'):
#         activate_command = f"conda activate {env_name}"
#     else:
#         activate_command = f"source activate {env_name}"
    
#     # Run the activation command in a new Python process
#     activate_script = f"""
# import subprocess
# subprocess.run('{activate_command}', shell=True)
# """
#     subprocess.run([sys.executable, '-c', activate_script])

#     print(f"Environment '{env_name}' has been created and activated.")
# else:
#     print("Continuing with the current environment.")

# You can add more operations here, such as installing PyTorch


## Get CUDA Version

try:
    output = subprocess.check_output(['nvcc', '--version']).decode('utf-8')
    cuda_version = output.split('release ')[1].split(',')[0]
    CUDA = 'cu'+ cuda_version.split('.')[0]+ cuda_version.split('.')[1]


    print(f"CUDA version: {cuda_version}")
except:
    print("Can not get CUDA version，you may not install  CUDA")

## Check CUDA Version with torch
CUDA_list = ['cu124', 'cu121', 'cu118', 'cu117', 'cu116', 'cu113', 'cu111','cu110','cu101','cu92']
if CUDA not in CUDA_list:
    print("Availble CUDA Version:")
    print(", ".join(CUDA_list))
    while True:
        user_input = input("\n choose one (such as cu124,recommond you choose higher one): ").lower()
        if user_input in CUDA_list:
            print(f"\n CUDA version is: {user_input}")
            CUDA = user_input
            break
        else:
            print("invalid cuda version \n")
## Match Link
link = {}
with open('torch_link_20241217_update.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        if CUDA in line:
            pattern = r'torch==(\d+\.\d+\.\d+)'
            match = re.search(pattern, line)
            if match:
                link[match.group(1)] = line.strip()

print("Availble torch version:")
for version in link.keys():
    print(version)
while True:
    user_choice = input("\n Choose torch version: ")
    if user_choice in link:
        install_pip = link[user_choice]
        print(f"\n Selected torch is: {user_choice}") 
        break
    else:
        print("invalid torch version \n")

# install torch
print("Executing install_pip command...")
try:
    print('just waiting for few mins...downloading cost few mins (づ｡◕‿‿◕｡)づ \n')
    output = run_command(install_pip)
    print("install_pip command executed successfully.")
    print("Output:")
    print(output)
except Exception as e:
    print(f"An error occurred while executing install_pip: {str(e)}")

print("Install Finished.")