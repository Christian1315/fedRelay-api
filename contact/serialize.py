from rest_framework import serializers
from rest_framework.response import Response


from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("id","nom","prenom","telephone","message","object")

    def custom_query_set(self, *args, **kwargs):
        return Contact.objects.all()
    
    def contact_create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # self.perform_create(serializer)
        data = {'success':True,'data':serializer.data}
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data)
