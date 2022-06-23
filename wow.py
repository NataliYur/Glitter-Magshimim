from tools import *

class Attack(tools):


    _wow_msg = {"glit_id":0,"user_id":0,"user_screen_name":"0"}
    

    @classmethod
    def send_wow(cls, glit_id = 19550) -> None:
        # ---------------------------------------------- #
        # This function adds wow to a glit
        # :param glit_id: the id of glit to add wow on
        # :type glit_id: int
        # :return: None
        # ---------------------------------------------- #

        cls.get_wow_data(glit_id)
        msg = super().build_wow_msg(cls._wow_msg)
        print("[INFO] sending wow request")
        super().server_session.sock.sendall(msg.encode())
        server_msg = super().server_session.sock.recv(1024).decode()
        print(f"[SERVER RESPONSE] {server_msg}")


    @classmethod
    def send_more_than_one_wow(cls, glit_id = 19548, wow_num = 5) -> None:
        # ---------------------------------------------- #
        # This function adds many wows to a glit
        # :param glit_id: the id of glit to add wow on
        # :typeglit_id: int
        # :param wow_num the number of wow to send
        # :type wow_num: int
        # :return: None
        # ---------------------------------------------- #

        for i in range(wow_num):
            cls.send_wow(glit_id)


    @classmethod
    def wow_private_post(cls, glit_id = 15188) -> None:
        # ---------------------------------------------- #
        # This function adds wow to a private glit
        # :param glit_id: the id of glit to add wow on
        # :type glit_id: int
        # :return: None
        # ---------------------------------------------- #
        
        cls.get_wow_data(glit_id)
        msg = super().build_wow_msg(cls._wow_msg)
        print("[INFO] sending wow request")
        super().server_session.sock.sendall(msg.encode())
        server_msg = super().server_session.sock.recv(1024).decode()
        print(f"[SERVER RESPONSE] {server_msg}")


    @classmethod
    def get_wow_data(cls, glit_id: int) -> None:
        # ---------------------------------------------- #
        # This function creates wow request's data
        # :param glit_id: the id of glit to add wow on
        # :type glit_id: int
        # :return: None
        # ---------------------------------------------- #

        cls._wow_msg["user_id"] = super().server_session.id
        cls._wow_msg["glit_id"] = glit_id
        cls._wow_msg["user_screen_name"] = super().server_session.user_screen_name