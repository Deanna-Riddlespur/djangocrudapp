from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Django CRUD Example</h1>
    <a href="/teams_cbv/">Class Based Views</a><br>
    <a href="/teams_fbv/">Function Based Views</a><br>    
    <a href="/teams_fbv_user/">Function Based Views with User Access</a><br>    
    """
    return HttpResponse(html)