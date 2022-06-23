import json
import requests
import sys
import atexit
import urllib.parse


class Session():

    _login_url = "http://cyber.glitter.org.il/user/"
    _search_url = "http://cyber.glitter.org.il/history/"

    
    def authenticate_web_user(self, username: str, password: str) -> None:
        # ---------------------------------------------- #
        # This function logs into an account
        # :param username: the username of the account
        # :type username: str
        # :param password: the pasword of the account
        # :type password: str
        # :return: none
        # ---------------------------------------------- #

        login_data = json.dumps([username, password])
        self.session = requests.session()
        self.session.headers.update({'Content-type':"application/json"})
        ans = self.session.post(self._login_url, data = login_data).text
        ans = json.loads(ans)
        print(ans)
        print("[INFO] logging into website")
        try:
            self.sparkle_cookie = ans["sparkle"]
            self.id = ans["user"]["id"]
        except KeyError as e:
            print(e)
            print(f"[ERROR] couldn't login")
            sys.exit()

    def __init__(self, username: str, password: str) -> None:
        # ---------------------------------------------- #
        # This function inits the class parameters (user info)
        # :param username: the username of the account
        # :type username: str
        # :param password: the pasword of the account
        # :type password: str
        # :return: none
        # ---------------------------------------------- #

        self.username = username
        self.password = password
        self.authenticate_web_user(username, password)
        self.session.cookies.set("sparkle", self.sparkle_cookie)
        atexit.register(self.__close)


    def __close(self):
        # ---------------------------------------------- #
        # This function logs out of user account and closes the session
        # :return: none
        # ---------------------------------------------- #

        url = self._login_url + str(self.id) + "/"
        self.session.delete(url)
        self.session.close()
        print("[INFO] closed session with website")



class Web_tools: 


    _username = "nataliw1"  # Entre your username here 
    _password = "nataliw1"  # Entre your password here 
    server_session = Session(_username, _password)

    _post_url = "http://cyber.glitter.org.il/glit"
    _search_url = "http://cyber.glitter.org.il/entities"
    _history_url = "http://cyber.glitter.org.il/history/"
    _password_recovery_code_url = "http://cyber.glitter.org.il/password-recovery-code-request"
    _password_recovery_code_verification = "http://cyber.glitter.org.il/password-recovery-code-verification"
    _search_url = "http://cyber.glitter.org.il/entities"


    _search_data = {"searchType": "", "searchEntry":""}
    
    _simple_search = "SIMPLE"


    @classmethod
    def get_id(cls, name: str) -> int:
        # ---------------------------------------------- #
        # This function gets id of the user
        # :param name: the screen_name of user
        # :type name: str
        # :return: the user id
        # :rtype: int
        # ---------------------------------------------- #

        name =  urllib.parse.quote(name)
        url = f"{cls._search_url}?searchType={cls._simple_search}&searchEntry={name}"
        ans = cls.server_session.session.get(url)
        data = json.loads(ans.text)
        for user in data:
            if user["screen_name"] == name:
                return user["id"]
        raise Exception("[ERORR] the user wasn't found")
