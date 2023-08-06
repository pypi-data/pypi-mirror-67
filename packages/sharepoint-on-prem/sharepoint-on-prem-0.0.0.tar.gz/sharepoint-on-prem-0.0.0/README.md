# sharepoint-on-prem
A package for basic file handling operations (downloading, uploading, deleting) 
on SharePoint on-premises platforms using ntlm auth method.

## Installation
```
pip install sharepoint-on-prem
```

## Usage
1. Import the handler class  
```
from sp_on_prem import SPFileHandler
```
2. Initiate a connection session  
```
test_session = SPFileHandler(
        site_root_url="https://sharepoint/root/url/",  
        username="your_ntlm_usersname",  
        password="your_ntlm_password",
    )
 ```
 3. Call the methods to do file handle operations
 ```
test_session.download_file(rf="remote/sharepoint/folder/path", lf="local/folder/path", file_name="file name")
 ```
 4. supported file handle operations
- get a list of files in the SharePoint folder
 ```
 test_session.get_file_list(rf="remote/sharepoint/folder/path")
 ```
 - download file
 ```
test_session.download_file(rf="remote/sharepoint/folder/path", lf="local/folder/path", file_name="file name")
```
- upload file
```
test_session.upload_file(rf="remote/sharepoint/folder/path", lf="local/folder/path", file_name="file name")
```
- delete file
```
test_session.delete_file(rf="remote/sharepoint/folder/path", file_name="file name")
 ```