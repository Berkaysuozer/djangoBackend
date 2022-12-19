from rest_framework.response import Response
from rest_framework.decorators import api_view
from members.models import Members
from .serializers import MemberSerializer

@api_view(['GET'])
def getData(request):
    Member = Members.objects.all()
    serializer = MemberSerializer(Member, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def addItem(request):
    serializer = MemberSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
 