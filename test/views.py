from django.shortcuts import render
from django.http import HttpResponseRedirect

def testimage(request):
    return HttpResponseRedirect('https://s3.us-east-2.amazonaws.com/dynamic-image-test/mac.jpg', content_type="image/jpg")

