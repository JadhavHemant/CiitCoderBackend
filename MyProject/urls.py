
# from django.contrib import admin
from django.urls import path
from MyApp.Apis import TopicRestApi,ContentRestApi,PostCategoriesRestApi,StatesRestApi,CitysRestApi,LocationRestApi
from MyApp.Apis import QualificationRestApi,SpecializationRestApi,RoleRestApis,GenderRestApi,DesigRestApi,UserRestApi
from MyApp.Apis import UserQualiRestApi,UseExpRestApi,UserPostRestApi,UserPostComment,UserPostReplyRestApi,UserPostLikeRestApi
from MyApp.Apis import UserPostShareRestApi,UserPostLikeShareRestApi,AdminRestApi,CodePostRestApi,PostCommentReplyRestApi
from MyApp.Apis import CodeCommentRestApi,LikeSharePostRestApi,JobOpenRestApi,CommentPostRestApi,CommentPostReplyReatApi
from MyApp.Apis import PostDislikeRestApi,PostLikesSharesTableRestApi,UpdateRestApi,UserProfeRestApi
urlpatterns = [
                     # Topic Apis

    path('api/topic', TopicRestApi.TopicApis.as_view()),  # GET AND POST data in apis/topic
    path('api/topic/udatedelete/<int:pk>/', TopicRestApi.TopicApiUpdateDeleteApi.as_view()), # update/delete/ data in apis/topic

                     # Content Apis

    path('api/content', ContentRestApi.contentApis.as_view()),  # GET AND POST data in apis/content
    path('api/content/udatedelete/<int:pk>/', ContentRestApi.ContentApiUpdateDeleteApi.as_view()), # update/delete/ data in apis/content

                      # Post Category Api
    path('api/postcateger', PostCategoriesRestApi.PostCateApi.as_view()),
    path('api/postcateger/<int:pk>/', PostCategoriesRestApi.PostCateApi.as_view()), 

                     # State Apis
    path('api/states', StatesRestApi.StateApi.as_view()),
    path('api/states', StatesRestApi.StateUpdateDeleteApi.as_view()), 
                      

                     # City Apis
    path('api/city', CitysRestApi.CityApi.as_view()),
    path('api/city/<int:pk>/', CitysRestApi.CityUpdateDeleteApi.as_view()),  
    
                     #  Locations API  
                     
    path('api/locations', LocationRestApi.LocationApi.as_view()),
    path('api/locations/<int:pk>/', LocationRestApi.LocationUpdateDeleteApi.as_view()),  
                      
                        # Qualification
    path('api/qualification', QualificationRestApi.QualificationApi.as_view()),
    path('api/qualification/<int:pk>/', QualificationRestApi.QualificationUpdateDeleteApi.as_view()),
        
                             # Spelization
    path('api/spelization', SpecializationRestApi.SpeclizeApi.as_view()),
    path('api/spelization/<int:pk>/', SpecializationRestApi.SpeclizeUpdateDeleteApi.as_view()),
                   
                   
                             # Role
    path('api/role', RoleRestApis.RoleApi.as_view()),
    path('api/role/<int:pk>/', RoleRestApis.RoleUpdateDeleteApi.as_view()),
                   
                     
                      # Gender
    path('api/gender', GenderRestApi.GenderApi.as_view()),
    path('api/gender/<int:pk>/', GenderRestApi.GenderUpdateDeleteApi.as_view()),
                   
                    # Designation
    path('api/designation', DesigRestApi.DesigApi.as_view()),
    path('api/designation/<int:pk>/', DesigRestApi.DesigUpdateDeleteApi.as_view()),
                   
                       # User
    path('api/user', UserRestApi.UserApi.as_view()),
    path('api/user/<int:pk>/', UserRestApi.UserUpdateDeleteApi.as_view()),
                   
                   # UserQuali
    path('api/quali/user', UserQualiRestApi.UserQualiApi.as_view()),
    path('api/quali/user/<int:pk>/', UserQualiRestApi.UserQualiUpdateDeleteApi.as_view()),
                   
                    
                   # UserExperience
    path('api/expe/user', UseExpRestApi.UserExpeApi.as_view()),
    path('api/expe/user/<int:pk>/', UseExpRestApi.UserExpeUpdateDeleteApi.as_view()),
    
    path('api/user/posts', UserProfeRestApi.UserProfApi.as_view()),
    path('api/user/posts/<int:pk>/', UserProfeRestApi.UserProfUpdateDeleteApi.as_view()),
                   
                   
                     # UserPost 
    path('api/user/posts', UserPostRestApi.UserPostApi.as_view()),
    path('api/user/posts/<int:pk>/', UserPostRestApi.UserPostUpdateDeleteApi.as_view()),
                   
                    # UserPostComment
    path('api/user/posts/comments', UserPostComment.UserPostCommentApi.as_view()),
    path('api/user/posts/comments/<int:pk>/', UserPostComment.UserPostCommentUpdateDeleteApi.as_view()),
                   
                    # UserPostCommentReplys
    path('api/user/posts/comments/reply', UserPostReplyRestApi.PostCommentReplyApi.as_view()),
    path('api/user/posts/comments/reply/<int:pk>/', UserPostReplyRestApi.PostCommentReplyUpdateDeleteApi.as_view()),
                   
                    # UserDisPostLikeDislike
    path('api/user/posts/dislike', UserPostLikeRestApi.PostlikeApi.as_view()),
    path('api/user/posts/dislike/<int:pk>/', UserPostLikeRestApi.PostlikeUpdateDeleteApi.as_view()),
                   
                    # UserPostShare
    path('api/user/posts/share', UserPostShareRestApi.PostShareApi.as_view()),
    path('api/user/posts/share/<int:pk>/', UserPostShareRestApi.PostShareUpdateDeleteApi.as_view()),
                   
                   # UserPostLikeShare
    path('api/user/posts/like/share', UserPostLikeShareRestApi.PostSharelikeApi.as_view()),
    path('api/user/posts/like/share/<int:pk>/', UserPostLikeShareRestApi.PostSharelikeUpdateDeleteApi.as_view()),
                   
                   # Admin
    path('api/admin', AdminRestApi.AdminApi.as_view()),
    path('api/admin/<int:pk>/', AdminRestApi.AdminUpdateDeleteApi.as_view()),
                   
                   # Code Post
    path('api/codepost', CodePostRestApi.CodePostApis.as_view()),
    path('api/codepost/<int:pk>/', CodePostRestApi.CodePostApiUpdateDeleteApi.as_view()),
                   
                    #   Code Comment Reply
    path('api/code/comment',CodeCommentRestApi.CodeCommentApis.as_view()),
    path('api/code/comment/<int:pk>/', CodeCommentRestApi.CodeCommentApiUpdateDeleteApi.as_view()),
                     
                     
                   # Code Comment Reply
    path('api/codepost/reply', PostCommentReplyRestApi.CodeCommentReplayApis.as_view()),
    path('api/codepost/reply/<int:pk>/', PostCommentReplyRestApi.CodeCommentReplayApiUpdateDeleteApi.as_view()),
                     
                     
                     # Code Share
    path('api/code/share/reply', LikeSharePostRestApi.CodeShareApis.as_view()),
    path('api/code/share/reply/<int:pk>/', LikeSharePostRestApi.CodeShareApiUpdateDeleteApi.as_view()),
                     
                  # Job
    path('api/job', JobOpenRestApi.JobApis.as_view()),
    path('api/job/<int:pk>/', JobOpenRestApi.JobApiUpdateDeleteApi.as_view()),
                     
                   
                      # Code Comment Reply
    path('api/comment/post', CommentPostRestApi.CommentPostApis.as_view()),
    path('api/comment/post/<int:pk>/', CommentPostRestApi.CommentPostApiUpdateDeleteApi.as_view()),
                     
                          # api/comment/post/reply
    path('api/comment/post/reply', CommentPostReplyReatApi.CommentPostReplyApis.as_view()),
    path('api/comment/post/reply/<int:pk>/', CommentPostReplyReatApi.CommentPostReplyApiUpdateDeleteApi.as_view()),
                                    
                    #   api/comment/post/reply
    path('api/comment/post/dislike', PostDislikeRestApi.PostDislikeReplyApis.as_view()),
    path('api/comment/post/dislike/<int:pk>/', PostDislikeRestApi.PostDislikeApiUpdateDeleteApi.as_view()),
                                    
                                    #   api/Code/share
    path('api/code/share/like', PostLikesSharesTableRestApi.PostLikesSharesTableApis.as_view()),
    path('api/code/share/like/<int:pk>/', PostLikesSharesTableRestApi.PostLikesSharesTableApiUpdateDeleteApi.as_view()),
                                  
                                  
                                  
    path('api/update/like', UpdateRestApi.UpdateApis.as_view()),
    path('api/update/<int:pk>/', UpdateRestApi.UpdateUpdateDeleteApi.as_view()),
                                                                      
                     
    # path('api/Image', ImageRestApi.ImageApi.as_view()),
    
        
]
