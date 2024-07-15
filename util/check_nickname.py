def check_validate_nickname(phrases):
    nickname = phrases.split('/')
    if len(nickname) > 2:
        return {"clan_name": nickname[0], "role": nickname[2], "nickname": nickname[1]}
    return None