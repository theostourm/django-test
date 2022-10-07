# Create your view here.
import csv
import os


from datetime import datetime
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator
from blog.models import Post, Tag


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


def csv_connection(file_path):
    """
    Make the connection with the csv file
    """
    directory = os.getcwd()

    try:
        csv_file = open(directory + file_path, 'r')
        reader = csv.reader(csv_file)
    except FileNotFoundError:
        return 'File not Found'

    return reader


class PostList(APIView):
    """
    Get list of posts, or upload a list of posts from a csv
    """

    def get(self, request):
        """
        return the list of all the posts
        """
        posts = Post.objects.all().order_by('id')
        page_number = self.request.query_params.get('page_number ', 1)
        page_size = self.request.query_params.get('page_size ', 10)
        paginator = Paginator(posts, page_size)
        serializer = PostSerializer(paginator.page(page_number), many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        """
        Connects to the csv file, and upload the entries to the database.
        """
        reader = csv_connection('/data/posts.csv')
        next(reader)

        for id_, row in enumerate(reader):
            (
                slug,
                title,
                description,
                date,
                author_1,
                author_2,
                author_3,
                tags,
                image_url,
                image_description
            ) = row

            # Create the tags objects in the tag table
            tags_list = [tag.strip() for tag in tags.split(',')]
            tag_object_list = []
            for tag in tags_list:
                tag_object, created = Tag.objects.get_or_create(name=tag)
                tag_object_list.append(tag_object)

            # Create the Post object if they do not exist yet
            p, created = Post.objects.get_or_create(
                slug=slug.split('/')[-1],
                title=title,
                description=description,
                date=datetime.strptime(date, "%d %B %Y"),
                author_1=author_1,
                author_2=author_2,
                author_3=author_3,
                image_url=image_url,
                image_description=image_description
            )

            # link the tags with the post
            if created:
                for tag_object in tag_object_list:
                    p.tags.add(tag_object.id)

        return Response("Successfully upload the data")



