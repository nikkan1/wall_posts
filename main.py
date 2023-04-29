import vk_api
import datetime


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = False
    return key, remember_device


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)
    try:
        vk_session.auth()
    except vk_api.AuthError as err:
        print(err)
        return
    vk = vk_session.get_api()
    resp = vk.wall.get(count=5, offset=0)
    if resp["items"]:
        for item in resp["items"]:
            text = item["text"]
            date = item["date"]
            date_m = datetime.datetime.fromtimestamp(int(date))
            print(text + ";")
            print(f"date: {date_m.date()}, time: {date_m.time()}")


if __name__ == "__main__":
    main()
