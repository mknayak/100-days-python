class Post:
    def __init__(self, api_data):
        super().__init__()
        self.id = api_data["id"]
        self.body = api_data["body"]
        self.title = api_data["title"]
        self.subtitle = api_data["subtitle"]
        self.image_url=api_data["image_url"]
