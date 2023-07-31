from rest_framework import serializers
from MyApp.models import *
from rest_framework.relations import PrimaryKeyRelatedField
# ---------------------------Topics Serializer ------------------------
# API Done crud with filter

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model=TopicsModel
        fields=['id','topic_name','flag']

# ---------------------------Content Serializer ------------------------
# API Done crud 

class ContentSerializer(serializers.ModelSerializer):
    topic_id=PrimaryKeyRelatedField(queryset=TopicsModel.objects.all(),many=False)
    class Meta:
        model=ContentModel
        fields=['id','content_name','topic_id','flag']

# ---------------------------Postcategories Serializer ------------------------
# API Done crud 

class PostcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Postcategories
        fields=['id','category_name','flag']
        
# ---------------------------States Serializer ------------------------
# API Done crud 

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=StatesModel
        fields=['id','state_Name','flag']     

# ---------------------------States Serializer ------------------------
# API Done crud 

class CitysSerializer(serializers.ModelSerializer):
    state_id=PrimaryKeyRelatedField(queryset=StatesModel.objects.all(),many=False)
    class Meta:
        model=CitysModel
        fields=['id','city_name','state_id','flag']   
        
        
        
# ---------------------------Locations Serializer ------------------------
# API Done crud 

class LocationsSerializer(serializers.ModelSerializer):
    city_id=PrimaryKeyRelatedField(queryset=CitysModel.objects.all(),many=False)
    class Meta:
        model=LocationModel
        fields=['id','location_name','city_id','flag']   

# ---------------------------Qualifications Serializer ------------------------
# API Done crud 


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=QualificationModel
        fields=['id','qualification','flag'] 
        
        
 
# ---------------------------Specializations Serializer ------------------------
# API Done crud 

class SpecializationsnSerializer(serializers.ModelSerializer):
    qualification_id=PrimaryKeyRelatedField(queryset=QualificationModel.objects.all(),many=False)
    class Meta:
        model=SpecializationModel
        fields=['id','specialization','qualification_id','flag'] 
  
               
# ---------------------------Roles Serializer ------------------------
# API Done crud 

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoleModel
        fields=['id','role','flag'] 
        
               
# ---------------------------Genders Serializer ------------------------
# API Done crud 

class GendersSerializer(serializers.ModelSerializer):
    class Meta:
        model=GenderModel
        fields=['id','gender','flag'] 
                               
        
# ---------------------------Designations Serializer ------------------------
# API Done crud 

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=DesignationModel
        fields=['id','designation','flag'] 
                               
                 
# ---------------------------UserDetails Serializer ------------------------
# API Done crud 

class UserDetailsSerializer(serializers.ModelSerializer):
    gender_id=PrimaryKeyRelatedField(queryset=GenderModel.objects.all(),many=False)
    location_id=PrimaryKeyRelatedField(queryset=LocationModel.objects.all(),many=False)
    role_id=PrimaryKeyRelatedField(queryset=RoleModel.objects.all(),many=False)
    class Meta:
        model=UserDetailsModel
        fields=['id','first_name','last_name','gender_id','location_id','local_address','role_id','birth_date','joining_date','user_photo','mobile_number','emial_address','user_name','is_premium','password','flag'] 
                               
                  
# ---------------------------UserQualification Serializer ------------------------
# API Done crud 

class QualiSerializer(serializers.ModelSerializer):
    user_id=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    specialization_id=PrimaryKeyRelatedField(queryset=SpecializationModel.objects.all(),many=False)
    class Meta:
        model=QualiModel
        fields=['id','user_id','specialization_id','university','passing_year','medium','percentage','flag'] 
                 
# ---------------------------experience_details Serializer ------------------------
# API Done crud 

class ExperianceDetailsSerializer(serializers.ModelSerializer):
    user_id=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    designation_id=PrimaryKeyRelatedField(queryset=DesignationModel.objects.all(),many=False)
    class Meta:
        model=ExperianceDetailsModel
        fields=['id','user_id','designation_id','company_name','from_year','to_year','job_descrption','flag']         
        
# ---------------------------user_professional_expertise Serializer ------------------------
# API Done crud 

class UserProfessionalExpertiseSerializer(serializers.ModelSerializer):
    user_id=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    specilization_id=PrimaryKeyRelatedField(queryset=SpecializationModel.objects.all(),many=False)
    class Meta:
        model=UserProfessionalExpertiseModel
        fields=['id','user_id','specilization_id','description','flag']       
        
# ---------------------------user_posts Serializer ------------------------
# API Done crud 

class UserPostSerializer(serializers.ModelSerializer):
    user_id=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    class Meta:
        model=UserPostModel
        fields=['id','user_id','post_date','post_title','post_description','photo','is_active','flag']       
        

# ---------------------------post_comments Serializer ------------------------
# API Done crud 

class PostCommentSerializer(serializers.ModelSerializer):
    post_id=PrimaryKeyRelatedField(queryset=UserPostModel.objects.all(),many=False)
    comment_by_user=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)    
    class Meta:
        model=PostCommentsModel
        fields=['id','post_id','comment_date','comment_by_user','comment_message','comment_photo','flag']         
        
        
# ---------------------------post_comment_replys Serializer ------------------------
# API Done crud 
class PostCommentReplysSerializer(serializers.ModelSerializer):
    comment_id=PrimaryKeyRelatedField(queryset=PostCommentsModel.objects.all(),many=False)
    reply_by_user=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    class Meta:
        model=PostCommentReplymodel
        fields=['id','comment_id','reply_date','reply_by_user','reply_mesage','comment_photo','flag'] 
 
 
 # ---------------------------post_likes_dislikes Serializer ------------------------
# API Done crud 

class PostLikesDislikesSerializer(serializers.ModelSerializer):
    post_id=PrimaryKeyRelatedField(queryset=PostCommentsModel.objects.all(),many=False)
    like_dislike_by_user=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    class Meta:
        model=PostLikesDislikesModel
        fields=['id','post_id','like_dislike_date','like_dislike_by_user','is_like','flag']
        
        
# ---------------------------post_likes_shares Serializer ------------------------
# API done Crud
class PostLikesSharesSerializer(serializers.ModelSerializer):
    post_id=PrimaryKeyRelatedField(queryset=PostCommentsModel.objects.all(),many=False)
    share_by_user=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    class Meta:
        model=PostLikesSharesModel
        fields=['id','post_id','share_date','share_by_user','flag']
      
      
        
# ---------------------------Admin_Details Serializer ------------------------
# API done Crud

class AdminDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminDetails
        fields=['id','user_name','password']
        
               
# ---------------------------CodePost Serializer ------------------------
# API done Crud

class CodePostSerializer(serializers.ModelSerializer):
    user_id=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    content_id=PrimaryKeyRelatedField(queryset=ContentModel.objects.all(),many=False)
    class Meta:
        model=CodePostModel
        fields=['id','user_id','date','content_id','question','code','description','is_active','flag']
        
        
# ---------------------------tbpost_comments Serializer ------------------------
# API done Crud

class PostCommentSerializer(serializers.ModelSerializer):
    post_id=PrimaryKeyRelatedField(queryset=CodePostModel.objects.all(),many=False) 
    comment_by_user=PrimaryKeyRelatedField(queryset=ContentModel.objects.all(),many=False)   
    class Meta:
        model=PostComment
        fields=['id','post_id','comment_date','comment_by_user','comment_message','comment_photo','flag']
        
# ---------------------------tbpost_comment_replys Serializer ------------------------
#done Apis
class PostCommReplysSerializer(serializers.ModelSerializer):
    comment_id=PrimaryKeyRelatedField(queryset=PostComment.objects.all(),many=False)
    reply_by_user=PrimaryKeyRelatedField(queryset=ContentModel.objects.all(),many=False)   
    class Meta:
        model=PostCommentReplys
        fields=['id','comment_id','reply_date','reply_by_user','reply_mesage','comment_photo','flag']
                 
# ---------------------------tbpost_likes_dislikes Serializer ------------------------
# API done Crud

class PostLikesDislikesSerializer(serializers.ModelSerializer):
    post_id=PrimaryKeyRelatedField(queryset=CodePostModel.objects.all(),many=False)
    like_dislike_by_user=PrimaryKeyRelatedField(queryset=ContentModel.objects.all(),many=False)   
    class Meta:
        model=PostLikesDislikesTBModel
        fields=['id','post_id','like_dislike_date','like_dislike_by_user','is_like','flag'] 

        
# ---------------------------tblpost_likes_shares Serializer ------------------------
# API done Crud

class LikesSharesPostSerializer(serializers.ModelSerializer):
    post_id=PrimaryKeyRelatedField(queryset=CodePostModel.objects.all(),many=False)
    share_by_user=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)   
    class Meta:
        model=LikesSharesPostModel
        fields=['id','post_id','share_date','share_by_user','flag']
          
                
# ---------------------------JobOpenings Serializer ------------------------
# API done Crud

class JobOpeningslSerializer(serializers.ModelSerializer):
    opening_by=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    class Meta:
        model=JobOpeningsModel
        fields=['id','opening_date','opening_by','company_name','job_title','experience_required','job_description','is_active','flag']
                                
# ---------------------------post_comments Serializer ------------------------
# API done Crud

class CommentPostSerializer(serializers.ModelSerializer):
    opening_id=PrimaryKeyRelatedField(queryset=JobOpeningsModel.objects.all(),many=False)
    comment_by_user=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    class Meta:
        model=CommentPostModel
        fields=['id','opening_id','comment_date','comment_by_user','comment_message','comment_photo','flag']
        

# ---------------------------post_comment_replys Serializer ------------------------
# API done Crud

class CommentPostReplySerializer(serializers.ModelSerializer):
    comment_id=PrimaryKeyRelatedField(queryset=CommentPostModel.objects.all(),many=False)
    reply_by_user=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    class Meta:
        model=CommentPostReplyModel
        fields=['id','comment_id','reply_date','reply_by_user','reply_mesage','comment_photo','flag']


# ---------------------------post_likes_dislikes Serializer ------------------------
# API done Crud

class PostDislikeSerializer(serializers.ModelSerializer):
    opening_id=PrimaryKeyRelatedField(queryset=JobOpeningsModel.objects.all(),many=False)
    like_dislike_by_user=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    class Meta:
        model=PostDislikeModel
        fields=['id','opening_id','like_dislike_date','like_dislike_by_user','is_like','flag']  
       
       
# ---------------------------lpost_likes_shares Serializer ------------------------
# API done Crud

class PostLikesSharesTableSerializer(serializers.ModelSerializer):
    opening_id=PrimaryKeyRelatedField(queryset=JobOpeningsModel.objects.all(),many=False)
    share_by_user=PrimaryKeyRelatedField(queryset=UserDetailsModel.objects.all(),many=False)
    class Meta:
        model=PostLikesSharesTableModel
        fields=['id','opening_id','share_date','share_by_user','flag']       
       
 

# ---------------------------updates Serializer ------------------------
# API done Crud

class UpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=UpdateModel
        fields=['id','update_date','update_title','update_desription','flag']
        
        
        
               
        
        
        
        
        
        
        
        
        
    