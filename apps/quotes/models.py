from __future__ import unicode_literals
from django.db import models
from ..login.models import User


class QuoteManager(models.Manager):
    def quote_validator(self, postData, id):
        response = {'status': True, 'errors': []}
        if len(postData['author']) < 4:
            response['errors'].append(
                "Quoted by must be more than 3 characters!")
        if len(postData['quote']) < 11:
            response['errors'].append(
                "Message must be more than 10 characters!")
        if len(response['errors']) == 0:
            return response
        else:
            response['status'] = False
        return response

    def addfav(self, id):
        response = {'status': True, 'errors': []}
        if len(Quote.objects.filter(id=id)) == 0:
            response['errors'].append('Cannot find quote!')
        if len(response['errors']) == 0:
            return response
        else:
            response['status'] = False
        return response

    def removefav(self, id):
        response = {'status': True, 'errors': []}
        if len(Quote.objects.filter(id=id)) == 0:
            response['errors'].append('Cannot find quote!')
        if len(response['errors']) == 0:
            return response
        else:
            response['status'] = False
        return response

    def restofquotes(self, id):
        response = []
        quotes = Quote.objects.all().order_by('-id')
        for i in quotes:
            if len(i.favorited_by.filter(id=id)) == 0:
                response.append(i)
        return response


class Quote(models.Model):
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    favorited_by = models.ManyToManyField(User, related_name="favorite_quotes")
    user = models.ForeignKey(User, related_name="quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

    def __repr__(self):
        return "<Quote: {} {} {}>".format(self.user, self.quote, self.author)