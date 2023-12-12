import click

from blog.posts import (
    get_all_posts,
    get_post_by_slug,
    update_post_by_slug,
    new_post,
)


@click.group()
def posts():
    """Manage blog posts"""


@posts.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    """Create a new post"""
    slug = new_post(title, content)
    click.echo(f"Created post with slug: {slug}")


@posts.command("list")
def _list():
    """Lists all posts"""
    for post in get_all_posts():
        click.echo(post)


@posts.command()
@click.argument("slug")
def get(slug):
    """Get post by slug"""
    post = get_post_by_slug(slug)
    click.echo(post or "post not found")


@posts.command()
@click.argument("slug")
@click.option("--content", default=None, type=str)
@click.option("--published", default=None, type=str)
def update(slug, content, published):
    """Update post by slug"""
    data = {}
    if content is not None:
        data["content"] = content
    if published is not None:
        data["published"] = published.lower() == "true"
    update_post_by_slug(slug, data)
    click.echo("Post updated")


def configure(app):
    app.cli.add_command(posts)
