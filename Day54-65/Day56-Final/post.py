class Post:
    def __init__(self, blog_dict):
        super().__init__()
        self.title = blog_dict['title']
        self.body = blog_dict['body']
        self.subtitle = blog_dict['subtitle']
        self.id = blog_dict['id']