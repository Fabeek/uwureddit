import requests

class Subreddit:

    def __init__(self, json: str) -> None:
        # general
        self.id: str = None
        self.display_name: str = None
        self.title: str = None
        self.header_img: str = None
        self.active_user_count: int = None
        self.icon_img: str = None
        self.subscribers: int = None
        self.public_description: str = None
        self.description_html: str = None
        self.submit_text: str = None
        self.key_color: str = None
        self.created: int = None
        self.public_description_html: str = None
        self.banner_img: str = None
        self.header_title: str = None
        self.description: str = None
        self.whitelist_status: str = None
        self.created_utc: int = None
        self.lang: str = None

        # settings
        self.quarantine: bool = None
        self.allow_videos: bool = None
        self.allow_images: bool = None
        self.content_category: str = None
        self.accept_followers: bool = None
        self.subreddit_type: str = None
        self.over18: bool = None

        # user
        self.user_is_banned: bool = None
        self.user_is_muted: bool = None
        self.user_has_favorited: bool = None
        self.user_is_subscriber: bool = None
        self.user_is_contributor: bool = None
        self.user_is_moderator: bool = None
    
        self.__set_attributs_from_json(json)


    def __set_attributs_from_json(self, json: dict):
        json = json["data"]

        for attribut in self.__dict__.keys():
            if attribut in json:
                setattr(self, attribut, json[attribut])
