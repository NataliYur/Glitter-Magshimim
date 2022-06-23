from tools import *

class Attack(tools):


    @classmethod
    def wildcard_search(cls, name_to_search = "natali") -> None:
        # ---------------------------------------------- #
        # This function search user in waildcard search mode
        # :param name_to_search: user to seacrh in waildcard
        # :type name_to_search: str
        # :return: none
        # ---------------------------------------------- #

        msg = cls.build_search_wildcard(name_to_search)
        super().server_session.sock.sendall(msg.encode())
        server_msg = super().server_session.sock.recv(20048).decode()
        print(f"[SERVER RESPONSE] {server_msg}")


    @classmethod
    def id_search(cls, id = 152) -> None:
        # ---------------------------------------------- #
        # This function search user in id saerch mode
        # :param id: id to search
        # :type id: int
        # :return: none
        # ---------------------------------------------- #
        
        msg = cls.build_search_id(id)
        super().server_session.sock.sendall(msg.encode())
        server_msg = super().server_session.sock.recv(20048).decode()
        print(f"[SERVER RESPONSE] {server_msg}")
