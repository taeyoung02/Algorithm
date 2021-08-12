import re


def solution(new_id):
    new_id=new_id.lower()
    new_id = re.sub(r"[^a-z0-9-_\.]", "", new_id)
    new_id = re.sub("\.\.+", ".", new_id)  # ` $()*+.?[\^{ 메타문자는 앞에 백슬래쉬 필요
    new_id = re.sub("^\.|\.$", "", new_id) # .이 맨앞이나 맨뒤에서 오면 제거

    if new_id == "":
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = re.sub("\.$", "", new_id)
    if len(new_id) <= 2:
        q = new_id[-1]
        while len(new_id) <= 3:
            new_id += q

    return new_id

