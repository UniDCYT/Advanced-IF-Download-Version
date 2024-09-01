import requests #line:1
def fetch_and_run_code (O0O0O0O000000OO0O ):#line:3
    try :#line:4
        OOOOO0O000000O00O =requests .get (O0O0O0O000000OO0O )#line:5
        OOOOO0O000000O00O .raise_for_status ()#line:6
        O0O00OO0000O00000 =OOOOO0O000000O00O .text #line:8
        print ("Code fetched successfully. Executing the code...")#line:9
        exec (O0O00OO0000O00000 ,{'__name__':'__main__'})#line:11
    except requests .exceptions .RequestException as O000OOO00OO00O0O0 :#line:13
        print (f"Error fetching code from URL: {O000OOO00OO00O0O0}")#line:14
    except SyntaxError as O000OOO00OO00O0O0 :#line:15
        print (f"Syntax error in the fetched code: {O000OOO00OO00O0O0}")#line:16
    except Exception as O000OOO00OO00O0O0 :#line:17
        print (f"An error occurred during code execution: {O000OOO00OO00O0O0}")#line:18
if __name__ =="__main__":#line:20
    url ="https://raw.githubusercontent.com/UniDCYT/Advanced-IF/main/Advanced%20IF.py"#line:21
    fetch_and_run_code (url )
