import os

# Base directory
base_dir = "/Users/luiscaceres/Library/Mobile Documents/com~apple~CloudDocs/IdeaProjects/Wizard_Battle"

# Define the directory structure
directories = [
    f"{base_dir}/frontend",
    f"{base_dir}/frontend/static",
    f"{base_dir}/frontend/static/css",
    f"{base_dir}/frontend/static/img",
    f"{base_dir}/frontend/static/js",
    f"{base_dir}/frontend/templates",
    f"{base_dir}/backend",
    f"{base_dir}/backend/blockchain",
    f"{base_dir}/backend/contracts"
]

# Create directories
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create necessary files
files = {
    f"{base_dir}/frontend/static/js/logic.js": "",
    f"{base_dir}/frontend/templates/index.html": "",
    f"{base_dir}/frontend/templates/battle.html": "",
    f"{base_dir}/frontend/templates/result.html": "",
    f"{base_dir}/backend/contracts/Game.sol": "",
    f"{base_dir}/backend/wallet.py": "",
    f"{base_dir}/backend/app.py": "",
    # Adding placeholders for images
    f"{base_dir}/frontend/static/img/Legolas.jpeg": "",
    f"{base_dir}/frontend/static/img/Frodo.jpeg": "",
    f"{base_dir}/frontend/static/img/Gandalf.jpeg": "",
    f"{base_dir}/frontend/static/img/Aragorn.jpeg": "",
    f"{base_dir}/frontend/static/img/Saruman.jpeg": "",
    f"{base_dir}/frontend/static/img/Sauron.jpeg": ""
}

for file_path, content in files.items():
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(content)

print("Directory structure and files have been set up in the new specified environment!")
