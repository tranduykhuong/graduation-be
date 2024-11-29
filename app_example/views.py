import datetime
import base64
from io import BytesIO
from firebase_admin import storage

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from django.utils.text import slugify
from app_example.models import Wisher
from app_example.serializer import WisherSerializer
from app_core.exceptions import WisherNotFound


class WisherViewSet(viewsets.ModelViewSet):
    queryset = Wisher.objects.all()
    serializer_class = WisherSerializer

    def get_queryset(self):
        return Wisher.objects.filter(is_active=True).order_by('-pk')


    def create(self, request):
        data = request.data
        name = data["name"]
        relationship = data["relationship"]
        email = data.get("email")
        last3phone = data.get("last3phone")

        slug = slugify(f'{name} {last3phone}')

        wisher = Wisher.objects.filter(key=slug).first()
        if not wisher:
            wisher = Wisher.objects.create(
                name=name,
                email=email,
                relationship=relationship,
                last3phone=last3phone,
                key=slug
            )

        return Response(WisherSerializer(wisher).data)


    def retrieve(self, request, *args, **kwargs):
        try:
            key = kwargs.get('key')
            wisher = self.queryset.get(key=key)
        except Wisher.DoesNotExist:
            raise WisherNotFound

        return Response(WisherSerializer(wisher).data)


    def update(self, request, *args, **kwargs):
        key = kwargs.get('key')

        try:
            wisher = self.queryset.get(key=key)
        except Wisher.DoesNotExist:
            raise WisherNotFound

        data = request.data
        serializer = self.get_serializer(wisher, data=data, partial=True)

        img_base64 = data.get("img_base64")
        if img_base64:
            img_data = base64.b64decode(img_base64)
            img_file = BytesIO(img_data)
            img_file.name = wisher.key + ".jpg"

            filename = img_file.name
            path = "lingobot/" + filename
            bucket = storage.bucket()
            blob = bucket.blob(path)
            blob.upload_from_file(img_file, content_type="image/jpeg")

            avatar_url = (
                "https://firebasestorage.googleapis.com/v0/b/gokag-19eac.appspot.com/o/lingobot%2F"
                + filename
                + "?alt=media"
            )
            data["img_url"] = avatar_url

            print(avatar_url)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
