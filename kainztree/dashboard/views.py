from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item,Category
from rest_framework import status
from .serializers import ItemSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm

def example_view(request):
    return render(request, 'dashboard/file.html')




class CategoryManagement(generics.ListAPIView,generics.CreateAPIView):

    model=Category
    queryset=model.objects.all()

    def get(self,request):
        return Response(data={'categories_count':self.queryset.count()})
    
    def post(self, request, *args, **kwargs):
        try:
            self.model.objects.create(**request.data)
            return Response({'data':'Category Created ..'},status=status.HTTP_201_CREATED)
            pass
        except Exception as err:
            print(f'exceeption occured in create of category {err}')
            return Response({'error':'Internal Server Error..'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return super().post(request, *args, **kwargs)()


class ItemListView(APIView):
    def get(self, request):
        items = Item.objects.all()
        # print("items are ", items.)
        serializer = ItemSerializer(items, many=True)
        print("Query:", str(items.query))  # Debug statement to print the generated query
        print("Items:", items)  # Debug statement to print retrieved items
        return Response(serializer.data)

@api_view(['GET'])
def get_data(request):
    items = Item.objects.all()
    print(len(items))
    print("item are ", items[0].sku)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_item(request):
    print("request data", request.data)
    serializer = ItemSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    # return render(request,'file.html',{'items_data':})
    return Response(serializer.data,status=status.HTTP_201_CREATED)
    

@api_view(['GET'])
def item_count(self,request):
        return Response(data={'Item_count':self.queryset.count()})


@api_view(['GET'])
def dashboard_view(request):

    try:
        dashboard_data: dict={}
        dashboard_data['categories_count']=Category.objects.count()
        dashboard_data['items_count']=Item.objects.count()
        # counts_data={
        #      'categories_count':Category.objects.count(),
        #      'items_count':Item.objects.count()
        #      }
        items_data=ItemSerializer(Item.objects.all(),many=True).data
        dashboard_data['items_data']=items_data
        # return Response(dashboard_data)
        return render(request,
                      'dashboard.html',
                      {
                          'dashboard_data':dashboard_data
                      })
                    #   {'items_data':items_data,
                    #    'counts_data':counts_data})

    except Exception as err:
            print(f'exceeption occured in create of category {err}')
            return Response({'error':'Internal Server Error..'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# views.py

# views.py



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  # Redirect to wherever you want after signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from .forms import LogInForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the home page after successful login
        else:
            error_msg = "Invalid username or password."
            return render(request, 'login.html', {'form': form, 'error_msg': error_msg})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
