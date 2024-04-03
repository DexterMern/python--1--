import requests
from bs4 import BeautifulSoup

def detect_website_technologies(url):
    try:
        # Remove "https://" if it exists in the input
        url = url.replace("https://", "")

        # Prepend "https://" to the URL
        full_url = "https://" + url

        # Fetch the website content
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Detect the primary programming language of the website
        meta_tags = soup.find_all('meta')
        programming_language = None
        for tag in meta_tags:
            if 'name' in tag.attrs and tag.attrs['name'].lower() == 'generator':
                programming_language = tag.attrs.get('content')
                break

        # Detect the CMS (Content Management System)
        cms = None
        generator_meta_tag = soup.find('meta', {'name': 'generator'})
        if generator_meta_tag:
            generator_content = generator_meta_tag.get('content', '')
            if 'WordPress' in generator_content:
                cms = 'WordPress'
            elif 'Joomla' in generator_content:
                cms = 'Joomla'
            # You can add more conditions to detect other CMSs.

        return {
            'programming_language': programming_language,
            'cms': cms
        }

    except Exception as e:
        return {'error': str(e)}

if __name__ == "__main__":
    url = input("Please enter the website address (without 'https://'): ")
    result = detect_website_technologies(url)
    
    if 'error' in result:
        print("There was an issue fetching the information.")
    else:
        print("Programming Language: {}".format(result['programming_language']))
        print("CMS (Content Management System): {}".format(result['cms']))
