import requests

def fetch_and_run_code(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        code_content = response.text
        print("Code fetched successfully. Executing the code...")

        exec(code_content, {'__name__': '__main__'})
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching code from URL: {e}")
    except SyntaxError as e:
        print(f"Syntax error in the fetched code: {e}")
    except Exception as e:
        print(f"An error occurred during code execution: {e}")

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/UniDCYT/Advanced-IF/main/Advanced%20IF.py"
    fetch_and_run_code(url)
