import post
import like
import feed
import login
import comment
import wow
import history
import search
import get_history_website
import password_web
import sys
import socket
import cookie
import xsrf
import friend


ATTACKS = {
"0": sys.exit,
"1": post.Attack.spoof_date, 
"2": post.Attack.tampering_background_color, 
"3": post.Attack.tampering_font_color, 
"4": post.Attack.spoof_pic, 
"5": post.Attack.tampering_feed,
"6": like.Attack.spam_likes,
"7": feed.Attack.remove_likes_untill_specific_date,
"8": like.Attack.like_private_post,
"9": login.Attack.login_in_someones_account,
"10": wow.Attack.send_wow,
"11": wow.Attack.send_more_than_one_wow,
"12": feed.Attack.remove_wows_untill_specific_date,
"13": wow.Attack.wow_private_post,
"14": history.Attack.get_history,
"15": comment.Attack.spoof_comment_publisher,
"16": comment.Attack.spoof_comment_date,
"17": comment.Attack.post_comment_on_private_post,
"18": feed.Attack.leak_info_about_feed,
"19": search.Attack.wildcard_search,
"20": search.Attack.id_search,
"21": friend.Attack.add_friend,
"22": get_history_website.Attack.get_history,
"23": password_web.Attack.get_password,
"24": cookie.Attack.get_cookie,
"25": xsrf.Attack.xsrf,
"26": xsrf.Attack.post_gif
}


def welcome() -> None:
    # ---------------------------------------------- #
    # This function prints welcome msg
    # :return: none
    # ---------------------------------------------- #

    print("""
-----------------------------
-----------------------------

POC programs for glitter wbsite and app

Website`s URL: http://cyber.glitter.org.il/home

Download app: https://drive.google.com/drive/folders/16C3KHJz8LA-dyhwtNAnRmTwOcBW6cK8w

Made by: Natali
-----------------------------
-----------------------------""")


def menu() -> str:
    # ---------------------------------------------- #
    # This function prints the menu and get the option from the user
    # :return: option that the user choose
    # :rtype: str
    # ---------------------------------------------- #

    opt = input(
"""
-----------------------------
--------- Main Menu ---------
-----------------------------
[0] Exit
-----------------------------

-----------------------------
-------- GLITTER APP --------
-----------------------------

-----------------------------
-------- POST ATTACKS -------

[1] Spoof post date

[2] Tramping background color

[3] Tramping font color

[4] Spoof post avatar

[5] Upload post on another feed (even private)

----------- LIKES -----------

[6] Spam likes to a post

[7] Remove likes from posts untill specific date

[8] Add like to private post

----- LOGIN IN SOMEONES -----

[9] Get password of someones account

------------ WOW ------------

[10] Send wow to a post

[11] Send many wows from the same user

[12] Remove wow from posts untill specific date

[13] Add wow to private post

----- GET SEARCH HISTORY -----

[14] Get search history of someone

---------- COMMENT ----------

[15] Spoof comment publisher

[16] Spoof comment date

[17] Add coment to private post

----------- FEED ------------

[18] Leak info of someones feed public/private

----------- SEARCH ----------

[19] Get wildcard search

[20] Search by user id

----------- FRIEND ----------

[21] Add friend without their permission

-----------------------------
------ GLITTER WEBSITE ------
-----------------------------

----- PRIVACY CHALLENGE -----

[22] Get history

---- PASSWORD CHALLENGE -----

[23] Get password

----- COOKIE CHALLENGE ------

[24] Get cookie

------- XSRF CHALLENGE -------

[25] Make target user post a glit on your feed

[26] Post gif

-----------------------------
Enter the option: """)
    return opt


def main():
    welcome()
    opt = 1
    try:
        while opt != 0:
            opt = menu()
            try:
                ATTACKS[opt]()
            except KeyError:
                print("[ERROR] Wrong option")
            except TimeoutError:
                print("[EROOR] bad internt connection")
                sys.exit()
    except socket.error as e:
        print(f"[ERROR] {e}")
        sys.exit()


if __name__ == "__main__":
    main()
