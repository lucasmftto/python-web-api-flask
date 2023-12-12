from datetime import datetime

from blog.database import mongo


def get_all_posts(published: bool = True):
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date")


def get_post_by_slug(slug: str) -> dict:
    post = mongo.db.posts.find_one({"slug": slug})
    return post


def update_post_by_slug(slug: str, data: dict) -> dict:
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})


def new_post(title: str, content: str, published: bool = True) -> str:
    slug = title.lower().replace(" ", "-").replace("_", "-")
    #     TODO: Check if slug exists
    mongo.db.posts.insert_one({
        "title": title,
        "content": content,
        "slug": slug,
        "published": published,
        "date": datetime.now(),
    })

    return slug
