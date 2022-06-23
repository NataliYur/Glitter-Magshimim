import json
import socket
import sys
import atexit


class session:


    _checksum_id  = "110#{gli&&er}"
    _msg_ending = "##"
    _data_start = "{gli&&er}"
    _login_req_id = "100#{gli&&er}"
    _server_ip = "44.224.228.136"
    _server_port = 1336
    _login_error_msg = """Illegal user state{gli&&er}{"type":"Server Failure","header":"Server Error","description":"Illegal user state."""
    _msg_login = {"user_name":"","password":"","enable_push_notifications":True}
    
    
    def checksum_msg(self, checksum: int) -> str:
        # ---------------------------------------------- #
        # This function builds checksum msg
        # :param checksum: checksum to incliude in the msg
        # :type checksum: int
        # :return: the full msg
        # :rtype: str
        # ---------------------------------------------- #

        return  self._checksum_id + str(checksum) + self._msg_ending


    def calculate_checksun(self, data: str) -> int:
        # ---------------------------------------------- #
        # This function calculates checksum
        # :param data: data to get checksum of
        # :type data: str
        # :return: the checksum
        # :type: int
        # ---------------------------------------------- #

        checksum = 0
        for letter in data:
            checksum += ord(letter)
        return checksum


    def build_login_msg(self, data: dict) -> str:
        # ---------------------------------------------- #
        # This function builds the login msg
        # :param data: all the parameters that must appear in the msg (msg data)
        # :type param: dictionary
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        json_data = json.dumps(data)
        return self._login_req_id  + json_data + self._msg_ending


    def connect_to_server(self) -> socket:
        # ---------------------------------------------- #
        # This functio connect to glitter server
        # :return: connection socket
        # :rtype: socket object
        # ---------------------------------------------- #

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self._server_ip, self._server_port)
        sock.connect(server_address)
        return sock


    def authenticate_user(self, user_name: str, password: str, sock: socket) -> tuple:
        # ---------------------------------------------- #
        # This function logs into user account
        # :param user_name: user name to log in 
        # :type user_name: str
        # :param password: the password of the username
        # :type password: str
        # :param sock: socket to the server that we need to log into
        # :type sock: socket
        # :return: password of user and screen name
        # :rtyep: tuple
        # ---------------------------------------------- #

        print("[INFO] logging into app")
        self._msg_login["user_name"] = user_name
        self._msg_login["password"] = password
        client_msg = self.build_login_msg(self._msg_login)
        sock.sendall(client_msg.encode())
        server_msg = sock.recv(2048).decode()
        checksum = self.calculate_checksun(user_name) + self.calculate_checksun(password)
        client_msg = self.checksum_msg(checksum)
        sock.sendall(client_msg.encode())
        server_msg = sock.recv(2048).decode()
        if self._login_error_msg in server_msg:
            print("[ERROR] wrong username/password ):")
            sys.exit()
        data = server_msg[server_msg.find(self._data_start) + len(self._data_start):server_msg.find(self._msg_ending)]
        data = json.loads(data)
        return data["password"], data["screen_name"], data['id']

    
    def __init__(self, user_name: str, password: str) -> None:
        # ---------------------------------------------- #
        # This function starts the "sesion" (opens socket and logs in)
        # :param user_name: user name to log in 
        # :type user_name: str
        # :param password: the password of the username
        # :type password: str
        # :return: tuple with new socket scren name and password
        # :rtype: tuple
        # ---------------------------------------------- #

        self.sock = self.connect_to_server()
        password, user_screen_name, id = self.authenticate_user(user_name, password, self.sock)
        self.password = password
        self.user_screen_name = user_screen_name
        self.username = user_name
        self.id = id
        atexit.register(self.__close)


    def __close(self)-> None:
        # ---------------------------------------------- #
        # This function closess socket
        # return: none
        # ---------------------------------------------- #

        self.sock.close()
        print("[INFO] Closing socket")


class tools:


    _user_name = "natali2"  # Entre your username here
    _password = "natali2"   # Entre your password here 


    server_session = session(_user_name, _password)


    _post_req_id = "550#{gli&&er}"
    _search_req_id = "300#{gli&&er}"
    _like_req_id = "710#{gli&&er}"
    _get_feed_req_id = "500#{gli&&er}"
    _wow_req_id = "750#{gli&&er}"
    _history_req_id = "320#{gli&&er}"
    _comment_msg_id = "650#{gli&&er}"
    _unlike_req_id = "720#{gli&&er}"
    _remove_wow_req_id = "760#{gli&&er}"
    _msg_ending = "##"
    _data_start = "{gli&&er}"
    _login_req_id = "100#{gli&&er}"


    _search_msg = {"search_type":"SIMPLE","search_entry":"natali1"}


    @classmethod
    def build_post_msg(cls, data: dict) -> str:
        # ---------------------------------------------- #
        # This function builds post msg
        # :param data: all the parameters that must appear in the msg (msg data)
        # :type param: dictionary
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        json_data = json.dumps(data)
        return cls._post_req_id + json_data + cls._msg_ending


    @classmethod
    def build_login_msg(cls, data: dict) -> str:
        # ---------------------------------------------- #
        # This function builds the login msg
        # :param data: all the parameters that must appear in the msg (msg data)
        # :type param: dictionary
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        json_data = json.dumps(data)
        return cls._login_req_id  + json_data + cls._msg_ending

    
    @classmethod
    def build_search_msg(cls, data: str) -> str:
        # ---------------------------------------------- #
        # This function builds the search msg
        # :param data: name of user 
        # :type param: str
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        json_data = json.dumps(data)
        return cls._search_req_id  + json_data + cls._msg_ending


    @classmethod
    def find_user_id_by_name(cls, sock: socket, target_name = "natali2") -> int:
        # ---------------------------------------------- #
        # This function finds feed id of by screen name
        # :param sock: the socket to the glitter server
        # :type sock: socket object
        # :target_name: the name of who to search the id
        # :type target_name: str
        # :return: the id
        # :rtype: int
        # ---------------------------------------------- #

        server_msg = ""
        cls._search_msg["search_entry"] = target_name
        msg = cls.build_search_msg(cls._search_msg)
        sock.sendall(msg.encode())
        server_msg = sock.recv(2048).decode()
        server_msg = json.loads(server_msg[server_msg.find(cls._data_start) + len(cls._data_start): server_msg.find(cls._msg_ending)])
        try:
            for i in server_msg:
                if i["screen_name"] == target_name:
                    id = i["id"]
                    return id
        except TypeError:
            print("[ERROR] couldn't find the user")


    @classmethod
    def build_like_msg(cls, data: dict) -> str:
        # ---------------------------------------------- #
        # This function builds the like msg
        # :param data: all the parameters that must appear in the msg (msg data)
        # :type param: dictionary
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        json_data = json.dumps(data)
        return cls._like_req_id  + json_data + cls._msg_ending

    @classmethod
    def build_wow_msg(cls, data: dict) -> str:
        # ---------------------------------------------- #
        # This function builds the wow msg
        # :param data: all the parameters that must appear in the msg (msg data)
        # :type param: dictionary
        # :return: return the ready msg
        #:rtype: str 
        # ---------------------------------------------- #

        json_data = json.dumps(data)
        return cls._wow_req_id  + json_data + cls._msg_ending


    @classmethod
    def build_get_feed_msg(cls, data: dict) -> str:
        # ---------------------------------------------- #
        # This function builds msg that gets feed info
        # :param data: all the parameters that must appear in the msg (msg data)
        # :type param: dictionary
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        json_data = json.dumps(data)
        return cls._get_feed_req_id  + json_data + cls._msg_ending


    @classmethod
    def build_get_history_msg(cls, id: int) -> str:
        # ---------------------------------------------- #
        # This function builds the  msg that get user history
        # :param data: id of user 
        # :type param: int
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        return cls._history_req_id  + str(id) + cls._msg_ending


    @classmethod
    def build_comment_msg(cls, data: dict) -> str:
        # ---------------------------------------------- #
        # This function builds comment msg
        # :param data: all the parameters that must appear in the msg (msg data)
        # :type param: dictionary
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        json_data = json.dumps(data)
        return cls. _comment_msg_id  + json_data + cls._msg_ending


    @classmethod
    def build_unlike_msg(cls, id: int) -> str:
        # ---------------------------------------------- #
        # This function builds the unlike msg
        # :param data: id of user 
        # :type param: int
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        return cls. _unlike_req_id  + str(id) + cls._msg_ending


    @classmethod
    def build_remove_wow_msg(cls, id: int) -> str:
        # ---------------------------------------------- #
        # This function builds the remove wow msg
        # :param data: id of user 
        # :type param: int
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        return cls. _remove_wow_req_id  + str(id) + cls._msg_ending


    @classmethod
    def build_search_wildcard(cls, search_entry = "natali") -> str:
        # ---------------------------------------------- #
        # This function buildswildcard search msg
        # :param search_entry: name to search
        # :type param: str
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        msg = cls._search_msg
        msg["search_type"] = "WILDCARD"
        msg["search_entry"] = search_entry + "%"
        json_msg = json.dumps(msg)
        return cls._search_req_id + json_msg + cls._msg_ending


    @classmethod
    def build_search_id(cls, id = 8096) -> str:
        # ---------------------------------------------- #
        # This function buildswildcard search msg
        # :param id: id to search
        # :type id: int
        # :return: return the ready msg
        # :rtype: str 
        # ---------------------------------------------- #

        msg = cls._search_msg
        msg["search_type"] = "ID"
        msg["search_entry"] = id
        json_msg = json.dumps(msg)
        return cls._search_req_id + json_msg + cls._msg_ending
