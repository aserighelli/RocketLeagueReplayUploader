import os
import requests

# Set the folder path where the .replay files are located
folder_path = r'C:\Users\aseri\OneDrive\Documents\My Games\Rocket League\TAGame\Demos'

# Set the API authorization token
auth_token = 'Pd4NJRVMI7845MRloWRqIxqRlZ61r2EaTSF4Hung'

# Set the API endpoint URL for reachability check
api_url = 'https://ballchasing.com/api/'

# Set the API endpoint URL for file upload
upload_url = 'https://ballchasing.com/api/v2/upload'

# Set the parameters for file visibility
params = {'visibility': 'public'}

# Construct the headers with the authorization token
headers = {'Authorization': auth_token}

# Check API reachability
try:
    response = requests.get(api_url, headers=headers)
    print(f'API Reachability Status: {response.status_code}')
    if response.status_code != 200:
        print('API is not reachable. Exiting...')
        exit()
    else:
        print('API is reachable.')
except requests.exceptions.RequestException as e:
    print('Error connecting to the API:', str(e))
    exit()

# List to keep track of successfully uploaded files
uploaded_files = []

# File to store the list of uploaded files
uploaded_files_file = 'uploaded_files.txt'

# Check if the uploaded files file exists
if os.path.exists(uploaded_files_file):
    # Load the list of uploaded files from the file
    with open(uploaded_files_file, 'r') as file:
        uploaded_files = file.read().splitlines()

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.replay'):
        # Check if the file is already uploaded
        if filename in uploaded_files:
            print(f'File already uploaded previously: {filename}')
            continue

        # Construct the full file path
        file_path = os.path.join(folder_path, filename)

        # Create a dictionary of files to upload
        files = {'file': open(file_path, 'rb')}

        # Upload the file
        print(f'Uploading file: {filename}')
        response = requests.post(upload_url, params=params, headers=headers, files=files)

        # Check the response status code
        if response.status_code in [200, 201]:
            print(f'File uploaded successfully: {filename}')
            uploaded_files.append(filename)
        elif response.status_code == 409:
            print(f'File already uploaded previously: {filename}')
            uploaded_files.append(filename)
        else:
            print(f'File upload failed: {filename}')
        print(f'Upload Status Code: {response.status_code}')

# Store the list of uploaded files in the file
with open(uploaded_files_file, 'w') as file:
    file.write('\n'.join(uploaded_files))
