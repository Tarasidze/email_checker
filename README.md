# Python Email checker script

## :memo: There are two solutions: 
 

- [Use Hunter API](#rocket-external_api)


## :rocket: Hunter API
    [Contribution guidelines for this script]
    

1. **Create environment:**
   ```
   python -m venv venv
   ```
      and activate it:
   - on windows
        ```shell
        venv\Scripts\activate 
        ```
   - on macOS or Linux:
        ```bash
        source venv/bin/activate 
        ```
     
2. **Install requirements**
   ```
   pip install -r requirements.txt
   ```
3. **Create .env**  
    ```
    rename
    .env_Sample  ->  .env  
   fill your secret api key
   ```
    

## :computer: Script usage

Available methods:
```commandline
    - verify_email
    - add_new_email
    - get_email_data
    - delete_email
    - get_all_emails_list
    - set_api_url

```
Example you can find in example.py