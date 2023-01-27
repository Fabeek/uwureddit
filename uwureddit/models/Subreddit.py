
class Subreddit:

    def __init__(self, subreddit: str) -> None:
        # general
        self.id: str
        self.display_name: str
        self.title: str
        self.header_img: str
        self.active_user_count: int
        self.icon_img: str
        self.subscribers: int
        self.public_description: str
        self.description_html: str
        self.submit_text: str
        self.key_color: str
        self.created: int
        self.public_description_html: str
        self.banner_img: str
        self.header_title: str
        self.description: str
        self.whitelist_status: str
        self.created_utc: int
        self.lang: str

        # settings
        self.quarantine: bool
        self.allow_videos: bool
        self.allow_images: bool
        self.content_category: str
        self.accept_followers: bool
        self.subreddit_type: str
        self.over18: bool

        # user
        self.user_is_banned: bool
        self.user_is_muted: bool
        self.user_has_favorited: bool
        self.user_is_subscribe: bool
        self.user_is_contributo: bool
        self.user_is_moderator: bool


    def __set_attributs_from_json(self, json: dict):
        json = json["data"]
        
        for attribut in self.__dict__.keys():
            setattr(self, attribut, json[attribut])
