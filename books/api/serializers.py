
from rest_framework import serializers

from Users.models import user

from books.models import(

    Books ,
    Proposed_Book,
    Borrow_book,
    BookRate

)

class CreateBookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Books
        fields = "__all__"
        #     [
        #     'id',
        #     'Title',
        #     'Description',
        #     'BookIMG',
        #     'BookIMG2',
        #     'Categories',
        #     'Publish_date',
        #     'Author',
        #     'ISBN',
        #     'Publisher',
        #     'PDF_Book',
        #     'Audio_Book',
        #
        #
        # ]
        extra_kwargs = {'BookIMG2': {'required': False},
                        'PDF_Book':{'required': False},
                        'Audio_Book' : {'required': False}
                        }


class ViewBooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'



class ProposeBookCreationSerializer(serializers.Serializer):
    Offered_price = serializers.IntegerField()
    Descriptions = serializers.CharField(allow_blank=False, max_length=100)
    books = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)

class BuySerializer(serializers.Serializer):
    OfferID = serializers.IntegerField()

class BorrowBookCreationSerializer(serializers.Serializer):
    Descriptions = serializers.CharField(allow_blank=False, max_length=100)
    books = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)


class BorrowBookStartBorrowSerializer(serializers.Serializer):
    BorrowOfferID = serializers.CharField(allow_blank=False, max_length=20)


class Proposed_BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proposed_Book
        fields = '__all__'

class Borrow_BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrow_book
        fields = '__all__'

class RateSerializer(serializers.Serializer):

    BookID = serializers.IntegerField()
    rate = serializers.IntegerField()

class RateViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookRate
        fields = '__all__'
class Propose_bookView_Serializer(serializers.ModelSerializer):

    Owner = serializers.SlugRelatedField(slug_field="username",queryset=user.objects.all())


    class Meta:
        model = Proposed_Book
        fields = '__all__'




class Book_all_serializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'

class WishSerializer(serializers.Serializer):
    BookID = serializers.CharField()


class FindOBJID(serializers.Serializer):
    Object_ID=serializers.IntegerField()

class rateViewSerializer(serializers.Serializer):
    BookID = serializers.IntegerField()

