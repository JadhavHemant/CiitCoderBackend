from django.db import models

# Create your models here.
                                              # ------------Master------------------------ 

# ------------------Topic-Model------------------------
class TopicsModel(models.Model):
    topic_name=models.CharField(max_length=100,unique=True, null=True)
    flag=models.IntegerField(default=0)
    class  Meta: 
        ordering =("id",)
        db_table='tbltopics'
    def __str__(self):
        return self.topic_name  
 
 # ---------------Topic-Contents-------------------------
 
class ContentModel(models.Model):
    content_name=models.CharField(max_length=100, null=True)
    topic_id=models.ForeignKey(TopicsModel,related_name='content',on_delete=models.CASCADE)
    flag=models.IntegerField(default=0)
    class  Meta: 
        ordering = ('id',)
        db_table='tbltopiccontents'
    def __str__(self):
        return self.content_name

# --------------------Topic-Post-categories-------------
    
class Postcategories(models.Model):
    category_name=models.CharField(max_length=100,unique=True, null=True)
    flag=models.IntegerField(default=0)
    class  Meta: 
        ordering = ('id',)
        db_table="tblpostcategories"
    def __str__(self):
        return self.category_name

# # # ---------------------------States--------------------

class StatesModel(models.Model):
    state_Name=models.CharField(max_length=100, null=True)
    flag=models.IntegerField(default=0)
    class  Meta: 
        ordering = ('id',)
        db_table = 'tbl_states'
    def __str__(self):
        return self.state_Name

# # -------------------------Cities-----------------------
        
class CitysModel(models.Model):
    city_name=models.CharField(max_length=100, null=True)
    state_id=models.ForeignKey(StatesModel,related_name='cityname',on_delete=models.CASCADE)
    flag=models.IntegerField(default=0)
    class  Meta: 
        ordering =("id",)
        db_table="tblcitys"
    def __str__ (self):
        return self.city_name

# # -------------------------Locations---------------------

class LocationModel(models.Model):
    location_name=models.CharField(max_length=100, null=True)
    city_id=models.ForeignKey(CitysModel,related_name='locations',on_delete=models.CASCADE)
    flag=models.IntegerField(default=0)
    class  Meta: 
        ordering =('id',)
        db_table="tbllocations"
    def __str__ (self):
        return self.location_name
        
# # -------------------------Qualifications-----------------

class QualificationModel(models.Model):
    qualification=models.CharField(max_length=100,unique=True, null=True)
    flag=models.IntegerField(default=0)
    class  Meta: 
        ordering = ('id',)
        db_table = 'tblqualifications'
    def __str__(self):
        return self.qualification_name    

# # -------------------------Specializations----------------

class SpecializationModel(models.Model):
    specialization=models.CharField(max_length=100, unique=True, null=True)
    qualification_id=models.ForeignKey(QualificationModel,related_name='special',on_delete=models.CASCADE)
    flag=models.IntegerField(default=0)
    class  Meta: 
        ordering = ('id',)
        db_table = 'tblspecializations'
    def __self__(self):
        return self.specialization 

# # -------------------------Roles---------------------------

class RoleModel(models.Model):
    role=models.CharField(max_length=100, null=True)
    flag=models.IntegerField(default=0)
    class  Meta: 
        ordering = ('id',)
        db_table = 'tblrole'
    def __self__(self):
        return self.role 

# #-----------------------Genders-----------------------------

class GenderModel(models.Model):
    gender=models.CharField(max_length=100, null=True)
    flag=models.IntegerField(default=0)
    class  Meta: 
        ordering = ('id',)
        db_table = 'tblgenders'
    def __self__(self):
        return self.gender 
   
# #--------------------------Designations------------------ 

class DesignationModel(models.Model):
    designation=models.CharField(max_length=100, null=True)
    flag=models.IntegerField(default=0)
    class  Meta: 
        ordering = ('id',)
        db_table = 'tbldesignations'
    def __self__(self):
        return self.designation 
       
                                   
# #                      #-----------------User--------------------- 

 
# # #----------------------- UserDetails-------------------------------

class UserDetailsModel(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        gender_id=models.ForeignKey(GenderModel,related_name='userdetails',on_delete=models.CASCADE)
        location_id=models.ForeignKey(LocationModel,related_name='userdetails',on_delete=models.CASCADE)
        local_address = models.CharField(max_length=100)
        role_id=models.ForeignKey(RoleModel,related_name='userdetails',on_delete=models.CASCADE) 
        birth_date = models.DateField()
        joining_date = models.DateField()
        user_photo = models.CharField(max_length=100)
        mobile_number= models.CharField(max_length=20)
        emial_address = models.CharField(max_length=100)
        user_name= models.CharField(max_length=100,unique=True)
        is_premium = models.IntegerField(default=0)
        password = models.CharField(max_length=100)
        flag= models.IntegerField(default=0)
        class  Meta: 
            ordering=("id",)
            db_table="tbluser_details"
            
        def __str__(self):
            return self.first_name
            
#     # --------------------------------- UserQualification--------------------------------------

class QualiModel(models.Model):
    user_id=models.ForeignKey(UserDetailsModel,related_name='qualifiaction',on_delete=models.CASCADE)
    specialization_id=models.ForeignKey(SpecializationModel,related_name='qualifiaction',on_delete=models.CASCADE)
    university=models.CharField(max_length=100)
    passing_year=models.ImageField()
    medium=models.CharField(max_length=100)
    percentage=models.FloatField()
    flag=models.IntegerField(default=0)
    class  Meta:  
        ordering=("id",)
        db_table="tbluser_qualifications"

# # # ----------------------------------------tblexperience_details----------------------------------       

class  ExperianceDetailsModel(models.Model): 
    user_id=models.ForeignKey(UserDetailsModel,related_name='ExperianceDetails',on_delete=models.CASCADE)
    designation_id=models.ForeignKey(DesignationModel,related_name='ExperianceDetails',on_delete=models.CASCADE)
    company_name=models.CharField(max_length=255)
    from_year=models.DateField()
    to_year=models.DateField()
    job_descrption=models.CharField(max_length=255)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table="tblexperience_details"       
    def __str__(self):
            return self.company_name
        
        
#----------------------------------------tbluser_professional_expertise----------------------------------       

class UserProfessionalExpertiseModel(models.Model):
    user_id=models.ForeignKey(UserDetailsModel,related_name='userprofession',on_delete=models.CASCADE)
    specilization_id=models.ForeignKey(SpecializationModel,related_name='userprofession',on_delete=models.CASCADE)
    description=models.CharField(max_length=255)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table="tbluser_professional_expertise"       
    def __str__(self):
            return self.description
        


#                                 # ----------------------------Posts ----------------------------
                                    
# #----------------------tbluser_posts-------------------- 

class UserPostModel(models.Model):
    user_id=models.ForeignKey(UserDetailsModel,related_name='userpost',on_delete=models.CASCADE)
    post_date=models.DateField()
    post_title=models.CharField(max_length=100)
    post_description=models.CharField(max_length=255)
    photo=models.CharField(max_length=255)
    is_active=models.IntegerField(default=0)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table="tbluser_posts"       
    def __str__(self):
            return self.post_title

        
#------------------------------tbpost_comments----------------------------
 
class PostCommentsModel(models.Model):
    post_id=models.ForeignKey(UserPostModel,related_name='postcomment',on_delete=models.CASCADE)
    comment_date=models.DateField()
    comment_by_user=models.ForeignKey(UserDetailsModel,related_name='postcomments',on_delete=models.CASCADE)
    comment_message=models.CharField(max_length=255)
    comment_photo=models.CharField(max_length=255)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table="tbpost_comments"       
    def __str__(self):
            return self.comment_date

#-------------------------tbpost_comment_replys---------------------------

class PostCommentReplymodel(models.Model):
    comment_id=models.ForeignKey(PostCommentsModel,related_name='commentreply',on_delete=models.CASCADE)
    reply_date=models.DateField()
    reply_by_user=models.ForeignKey(UserDetailsModel,related_name='commentreply',on_delete=models.CASCADE)
    reply_mesage=models.CharField(max_length=100)
    comment_photo=models.CharField(max_length=100)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table="tbpost_comment_replys"       
    def __str__(self):
            return self. reply_mesage 
            
            
#------------------------tbpost_likes_dislikes-------------------------------
        
class PostLikesDislikesModel(models.Model):
    post_id=models.ForeignKey(UserPostModel,related_name='likedislike', on_delete=models.CASCADE)
    like_dislike_date=models.DateField()
    like_dislike_by_user=models.ForeignKey(UserDetailsModel,related_name='likedislike', on_delete=models.CASCADE)
    is_like=models.IntegerField(default=0)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table="tbl_post_dis_likes"       
    def __str__(self):
            return self.like_dislike_date 
            
#--------------------------------tblpost_likes_shares-------------------------------

class PostLikesSharesModel(models.Model):
    post_id=models.ForeignKey(UserPostModel,related_name='likesshares',on_delete=models.CASCADE)
    share_date=models.DateField()
    share_by_user=models.ForeignKey(UserDetailsModel,related_name='likesshares',on_delete=models.CASCADE)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table='tblpost_likes_shares'      
    def __str__(self):
            return self.share_date

                               #---------------------Admin------------------------
                                    
# #---------------------Admin_Details------------------------

class AdminDetails(models.Model):
    user_name=models.CharField(max_length=100,unique=True, null=True)
    password=models.CharField(max_length=100, null=True)
    class  Meta: 
        ordering = ('id',)
        db_table = 'admin_details_tbl'
    def __self__(self):
        return self.user_name 
    
    
#                                      # ---------------------------------Codes---------------------------
                                
                                
# #------------------------------tblcode_posts----------------------------------- 

class CodePostModel(models.Model):
    user_id=models.ForeignKey(UserDetailsModel,related_name='codepost',on_delete=models.CASCADE)
    date=models.DateField()
    content_id=models.ForeignKey(ContentModel,related_name='codepost',on_delete=models.CASCADE)
    question=models.CharField(max_length=200)
    code=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    is_active=models.IntegerField(default=0)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table="tblcode_post_s"       
    def __str__(self):
            return self.date 

 # -------------------------tbpost_comments------------------------

class PostComment(models.Model):
    post_id=models.ForeignKey(CodePostModel,related_name='commentspost',on_delete=models.CASCADE)
    comment_date=models.DateField()
    comment_by_user=models.ForeignKey(UserDetailsModel,related_name='commentspost',on_delete=models.CASCADE)
    comment_message=models.CharField(max_length=255)
    comment_photo=models.CharField(max_length=255)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table="tbpostcomments"       
    def __str__(self):
            return self.comment_date  


 #------------------------- tbpost_comment_replys------------------------


class PostCommentReplys(models.Model):
    comment_id=models.ForeignKey(PostComment,related_name='commentreplys',on_delete=models.CASCADE)
    reply_date=models.DateField()
    reply_by_user=models.ForeignKey(UserDetailsModel,related_name='commentreplys',on_delete=models.CASCADE)
    reply_mesage=models.CharField(max_length=255)
    comment_photo=models.CharField(max_length=255)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table="tblpost_comment_replys"       
    def __str__(self):
            return self.reply_mesage   


 #------------------------- tbpost_likes_dislikes------------------------

class PostLikesDislikesTBModel(models.Model):
    post_id=models.ForeignKey(CodePostModel,related_name='dislike',on_delete=models.CASCADE)
    like_dislike_date=models.DateField()
    like_dislike_by_user=models.ForeignKey(UserDetailsModel,related_name='dislike',on_delete=models.CASCADE)
    is_like=models.IntegerField(default=0)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table="tbpost_likes_dislikes"       
    def __str__(self):
            return self.like_dislike_date

#--------------------------------------tblpost_likes_shares---------------------
class LikesSharesPostModel(models.Model):
    post_id=models.ForeignKey(CodePostModel,related_name='postshare',on_delete=models.CASCADE)
    share_date=models.DateField()
    share_by_user=models.ForeignKey(UserDetailsModel,related_name='postshare',on_delete=models.CASCADE)
    flag=models.IntegerField(default=0)
    class  Meta:  
            ordering=("id",)
            db_table="post_shares_tbl"       
    def __str__(self):
            return self.share_date 


                           #--------------------------------------Openings-----------------------------------


# ------------------------------------tbljob_openings---------------------------------


class JobOpeningsModel(models.Model):
    opening_date=models.DateField()
    opening_by=models.ForeignKey(UserDetailsModel,related_name='job',on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    experience_required=models.CharField(max_length=255)
    job_description=models.CharField(max_length=255)
    is_active=models.ImageField(default=0)
    flag=models.ImageField(default=0)
    class Meta:
        ordering = ('id',)
        db_table='tbljob_openings'
    def __str__(self):
                return self.opening_date  


# # -----------------------------tbpost_comments----------------------------------------

class CommentPostModel(models.Model):
    opening_id=models.ForeignKey(JobOpeningsModel,related_name='commentpost',on_delete=models.CASCADE)
    comment_date=models.DateField()
    comment_by_user=models.ForeignKey(UserDetailsModel,related_name='commentpost',on_delete=models.CASCADE)
    comment_message=models.CharField(max_length=255)
    comment_photo=models.CharField(max_length=255)
    flag=models.IntegerField(default=0)
    class Meta:
        ordering =('id',)
        db_table='post_comments_tbl'
    def __str__(self):
            return self.comment_date


# # -----------------------------------tbpost_comment_replys------------------------------------------

class CommentPostReplyModel(models.Model):
    comment_id=models.ForeignKey(CommentPostModel,related_name='replypost',on_delete=models.CASCADE)
    reply_date=models.DateField()
    reply_by_user=models.ForeignKey(UserDetailsModel,related_name='replypost',on_delete=models.CASCADE)
    reply_mesage=models.CharField(max_length=255)
    comment_photo=models.CharField(max_length=255)
    flag=models.IntegerField(default=0)
    class Meta:
        ordering =('id',)
        db_table='post_comment_replys_tbl'
    def __str__(self):
            return self.reply_date  
        
        

# # ----------------------------------tbpost_likes_dislikes------------------------------


class PostDislikeModel(models.Model):
    opening_id=models.ForeignKey(JobOpeningsModel,related_name='postdislike',on_delete=models.CASCADE)
    like_dislike_date=models.DateField()
    like_dislike_by_user=models.ForeignKey(UserDetailsModel,related_name='postdislike',on_delete=models.CASCADE)
    is_like=models.IntegerField(default=0)
    flag=models.IntegerField(default=0)
    class Meta:
        ordering =('id',)
        db_table='post_likes_dislikes_tbl'
    def __str__(self):
            return self.like_dislike_date


# # -------------------------------------tblpost_likes_shares--------------------------------------


class PostLikesSharesTableModel(models.Model): 
    opening_id=models.ForeignKey(JobOpeningsModel,related_name='likesharepost',on_delete=models.CASCADE)
    share_date=models.DateField()
    share_by_user=models.ForeignKey(UserDetailsModel,related_name='likesharepost',on_delete=models.CASCADE)
    flag=models.IntegerField(default=0)
    class Meta:
        ordering =('id',)
        db_table='post_likes_shares_tbl'
    def __str__(self):
        return self.share_date



#                         # -------------------------------------Updates--------------------------------------
# # -------------------------------------tblupdates--------------------------------------
class UpdateModel(models.Model):
    update_date=models.DateField()
    update_title=models.CharField(max_length=100)
    update_desription=models.CharField(max_length=255)
    flag=models.IntegerField(default=0)
    class Meta:
        ordering =('id',)
        db_table='tbl_update'
    def __str__(self):
        return self.update_date

