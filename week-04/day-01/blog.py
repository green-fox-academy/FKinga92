# Reuse your BlogPost class
# Create a Blog class
# list of BlogPosts
# add BlogPosts to your list
# delete(int) one item at given index
# update(int, BlogPost) one item at the given index and update it with another BlogPost

from blog_post import BlogPost

class Blog(object):
    def __init__(self):
        self.blogpost = []

    def add(self, BlogPost):
        self.blogpost.append(BlogPost)
    
    def delete(self, int):
        self.blogpost.remove(self.blogpost[int])
    
    def update(self, int, BlogPost):
        self.blogpost.remove(self.blogpost[int])
        self.blogpost.insert(int, BlogPost)

