from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView


# returns all requests
class BonusRequestList(generics.ListCreateAPIView):
    pass


# returns/update/deletes single request
class BonusRequestSingle(generics.RetrieveUpdateDestroyAPIView):
    pass


# returns all requests of specific worker
class WorkerBonusRequestList(APIView):
    pass


# returns all requests of specific reviewer
class ReviewerBonusRequestList(APIView):
    pass


# returns all bonus_request_history objects
class BonusRequestHistoryList(generics.ListCreateAPIView):
    pass


# returns/update/deletes single bonus_request_history object
class BonusRequestHistorySingle(generics.RetrieveUpdateDestroyAPIView):
    pass


# returns all users
class UserList(generics.ListAPIView):
    pass


# returns/update/deletes info about single user
class UserSingle(generics.RetrieveUpdateDestroyAPIView):
    pass


# returns all reviewers
class ReviewerList(generics.ListAPIView):
    pass


# returns/update/deletes single reviewer
class ReviewerSingle(generics.RetrieveUpdateDestroyAPIView):
    pass


# returns all workers
class WorkerList(generics.ListAPIView):
    pass


# returns/update/deletes single worker
class WorkerSingle(generics.RetrieveUpdateDestroyAPIView):
    pass
