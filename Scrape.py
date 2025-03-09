from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os
# import arrr
from pyscript import document

# Define headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.37',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

def create_unique_filename(base_filename):
    """Create a unique filename by appending numbers if the base filename exists"""
    if not os.path.exists(base_filename):
        return base_filename
    
    base, ext = os.path.splitext(base_filename)
    counter = 1
    while True:
        new_filename = f"{base}_{counter}{ext}"
        if not os.path.exists(new_filename):
            return new_filename
        counter += 1

try:
    # Create request with headers
    # url = "https://www.facebook.com/profile.php?id=100084120669137&sk=about_contact_and_basic_info"
    # url = `https://www.facebook.com/profile.php?id={arrr.translate(UID)}&sk=about_contact_and_basic_info`
    url = f"https://www.facebook.com/profile.php?id={arrr.translate(UID)}&sk=about_contact_and_basic_info"
    req = Request(url=url, headers=headers)
    
    # Open URL with custom headers
    response = urlopen(req)
    content = response.read().decode('utf-8')
    
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    scripts = soup.find_all('script')
    
    # Create a unique filename for the output
    filename = create_unique_filename('scripts.txt')
    
    # Write script contents to file
    with open(filename, 'w', encoding='utf-8') as f:
        for i, script in enumerate(scripts, 1):
            if i == 72:
                if script.string is not None:
                    f.write(f"--- Script {i} ---\n")
                    f.write(script.string.strip())
                    f.write("\n\n")
            elif i == 73:
                 if script.string is not None:
                    f.write(f"--- Script {i} ---\n")
                    f.write(script.string.strip())
                    f.write("\n\n")
            elif i == 79:
                 if script.string is not None:
                    f.write(f"--- Script {i} ---\n")
                    f.write(script.string.strip())
                    f.write("\n\n")
            elif i == 80:
                 if script.string is not None:
                    f.write(f"--- Script {i} ---\n")
                    f.write(script.string.strip())
                    f.write("\n\n")
            else:
                f.write('unexpected condition')
    
    print(f"Scripts have been successfully exported to {filename}")
    
except Exception as e:
    print(f"An error occurred: {str(e)}")