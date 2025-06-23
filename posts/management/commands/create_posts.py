from django.core.management.base import BaseCommand, CommandError
from posts.models import Post, Tag, Category


class Command(BaseCommand):
    help = "creates N number of posts"

    def add_arguments(self, parser):
        parser.add_argument("post_number", type=int)

    def handle(self, *args, **options):
        post_number = options.get('post_number', 10)
        title = 'test title'
        content = 'Test content'
        image = 'http://localhost:8000/media/posts/jemali_6YntcYO.webp'
        author_id = 2
        tag = Tag.objects.first()
        category = Category.objects.first()

        for i in range(post_number):
            print(f'creating Post {i}')
            post = Post(title=title,
                        content=content,
                        image=image,
                        author_id=author_id)
            post.save()
            post.tags.add(tag)
            post.categories.add(category)

