
import requests


class Linkedin:
    
    def linkedin_api(self):
        
        api_key = 'MN8RSazgANvGwb2jUF5DxA' # ? ! from linkedin_api_provider

        headers = {'Authorization': 'Bearer ' + api_key} 

        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin' # ? end point given by provider..

        linkedin_profile_url = 'https://www.linkedin.com/in/amith-kulkarni-1326241b4/' # ? url of the user, [using for loop we can get all users data..]

        response = requests.get(
            api_endpoint,
            params = {'url':linkedin_profile_url, 'skills':'include'}, # ! 'skills': 'include', is if we want any others more details we can add like that..   
            headers = headers    
        )
        return response.json()
    
    

        # ? api_key = 'MN8RSazgANvGwb2jUF5DxA'  # has 9 credit , regenerate if any error about api key..
        # ? this is the the api key from 
        # ? https://github.com/PradipNichite/Youtube-Tutorials/blob/main/Proxycurl_API.ipynb [Proxy Curl website ]