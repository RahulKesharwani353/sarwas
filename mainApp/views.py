from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework import status
from utils.ccScore import CC_score_generator
from utils.partition import asin_and_partition_num_generate
from utils.search import search_results

# Create your views here.



# def addData(title, desc, ASIN):
#     import pandas as pd
#     df = pd.read_csv('utils/final-dataset.csv')
#     # df.loc[len(df.index)] = [int(ASIN),title,'0',desc,None] 
#     df.loc[len(df.index)] = [999999,'ASUS laptop','0','npniin jas nkan  km km  ; m;m lmlw',None] 

#     partition = partition_gen(df)
#     print(partition)



class ProductGet(APIView):
        def post(self , request):
            data = request.data
        #     asin = data["asin"]
            title = data["title"]
            description = data["description"]
         
            p,asin =asin_and_partition_num_generate(title=title, desc=description)
            data["partition"] = p
            print("hello: "+str(p))
            #serializer = GetProductDetails(data=data, context= {'request': request})
        #     if serializer.is_valid():
        #         serializer.save()
        #         get_product = serializer.data
        #         return Response({
        #                 'message' : 'files uploaded successfully',
        #                 'data' : serializer.data
        #                 }, status= status.HTTP_200_OK)

            return Response({
                        'message' : 'files uploaded successfully',
                        'data' : data
                        }, status= status.HTTP_200_OK)

class RateProduct(APIView):

        def patch(self , request):
                data = request.data
                asin = data['asin']
                rating = data['rating']
                review = data['review']
                cc = CC_score_generator(asin, review, rating)
                # serializer = CCScoreDetails( temp,data=data, partial=True)
                # if serializer.is_valid():
                #         serializer.save()
                return Response({
                                'message' : 'files uploaded successfully',
                                'data' : cc
                                }, status= status.HTTP_200_OK)

                # return Response({
                #                 'message' : serializer.errors,
                #                 }, status= status.HTTP_400_BAD_REQUEST)                
                


class Search(APIView):
        def get(self, request):
                query = request.query_params['search']
                df = search_results(query=query)
                print(df)
                final_data= []
                for item in range(len(df)):
                        temp = {'asin': df['asin'][item], 'title':df['title'][item], 'ccScore':df['CC_score'][item]}
                        final_data.append(temp)
                return Response({
                        'data': final_data
                        }, status= status.HTTP_200_OK)