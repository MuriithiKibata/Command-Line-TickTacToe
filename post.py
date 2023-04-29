class Post:
  def __init__(self, post, name):
    self.post = post
    self.name = name

  def post_info(self):
    print(f"Post {self.post} written by {self.name}")
    