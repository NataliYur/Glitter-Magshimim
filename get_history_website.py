from web_tools import *
import json


class Attack(Web_tools):


    @classmethod
    def get_history(cls, target_name = "nataliw4") -> None:
        # ---------------------------------------------- #
        # This funcrion gets the user hostory
        # :param target_name: the name of the user
        # :type target_name: str
        # :return: none
        # ---------------------------------------------- #

        try:
            id = super().get_id(target_name)
            ans = super().server_session.session.get(f"{super()._history_url}{id}/")
            text_ans = ans.text
            text_ans = json.loads(text_ans)
            print('-' * 50)
            for user in text_ans:
                print(f"[SEARCH] {user['screen_name']}")
        except Exception as e:
            print(e)

