from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from esl import views, adminViews, learnerViews, learnViews, instructorViews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('do_login', views.do_login, name='do_login'),
    path('signup_learner', learnerViews.signup_learner, name='signup_learner'),
    path('signup_instructor', instructorViews.signup_instructor, name='signup_instructor'),
    path('courses', views.courses, name='courses'),
    path('about', views.about, name='about'),
    # Lecture Video

    #  Admin
    path('admin_home', adminViews.admin_home, name="admin_home"),
    path('admin_profile', adminViews.admin_profile, name="admin_profile"),
    path('admin_profile_update', adminViews.admin_profile_update, name="admin_profile_update"),
    path('add_admin', adminViews.add_admin, name='add_admin'),
    path('add_instructor', adminViews.add_instructor, name='add_instructor'),
    path('add_instructor_save', adminViews.add_instructor_save, name='add_instructor_save'),
    path('add_learner', adminViews.add_learner, name='add_learner'),
    path('add_learner_save', adminViews.add_learner_save, name='add_learner_save'),
    path('approve_instructor', adminViews.approve_instructor, name="approve_instructor"),
    path('approve_instructor_detail/<str:id>', adminViews.approve_instructor_detail, name="approve_instructor_detail"),

    path('decline/<str:id>', adminViews.decline, name='decline'),
    path('approve/<str:id>', adminViews.approve, name='approve'),
    # Manage sign language materials
    path('delete_beginner_sign/<str:id>', adminViews.delete_beginner_sign, name='delete_beginner_sign'),
    path('delete_intermediate_sign/<str:id>', adminViews.delete_intermediate_sign, name='delete_intermediate_sign'),
    path('delete_advanced_sign/<str:id>', adminViews.delete_advanced_sign, name='delete_advanced_sign'),
    path('manage_beginner_sign', adminViews.manage_beginner_sign, name='manage_beginner_sign'),
    path('manage_intermediate_sign', adminViews.manage_intermediate_sign, name='manage_intermediate_sign'),
    path('manage_advanced_sign', adminViews.manage_advanced_sign, name='manage_advanced_sign'),
    path('edit_beginner_sign/<id>', adminViews.edit_beginner_sign, name="edit_beginner_sign"),
    path('edit_beginner_sign_save/<id>', adminViews.edit_beginner_sign_save, name="edit_beginner_sign_save"),
    path('edit_intermediate_sign/<id>', adminViews.edit_intermediate_sign, name="edit_intermediate_sign"),
    path('edit_intermediate_sign_save/<id>', adminViews.edit_intermediate_sign_save, name="edit_intermediate_sign_save"),
    path('edit_advanced_sign/<id>', adminViews.edit_advanced_sign, name="edit_advanced_sign"),
    path('edit_advanced_sign_save/<id>', adminViews.edit_advanced_sign_save, name="edit_advanced_sign_save"),
    path('edit_instructor/<str:id>', adminViews.edit_instructor, name="edit_instructor"),
    path('delete_instructor/<id>', adminViews.delete_instructor, name="delete_instructor"),
    path('edit_instructor_save/<str:id>', adminViews.edit_instructor_save, name="edit_instructor_save"),
    path('edit_learner/<str:id>', adminViews.edit_learner, name="edit_learner"),
    path('edit_learner_save/<str:id>', adminViews.edit_learner_save, name="edit_learner_save"),
    path('delete_learner/<str:id>', adminViews.delete_learner, name="delete_learner"),
    path('check_email_exist', adminViews.check_email_exist, name="check_email_exist"),
    path('check_textForSign_exist', adminViews.check_textForSign_exist, name="check_textForSign_exist"),
    path('check_username_exist', adminViews.check_username_exist, name="check_username_exist"),
    path('manage_learner', adminViews.manage_learner, name="manage_learner"),
    path('manage_instructor', adminViews.manage_instructor, name="manage_instructor"),
    path('instructor_feedback_message/', adminViews.instructor_feedback_message, name="instructor_feedback_message"),
    path('instructor_feedback_message_reply/', adminViews.instructor_feedback_message_reply, name="instructor_feedback_message_reply"),
    path('learner_feedback_message/', adminViews.learner_feedback_message, name="learner_feedback_message"),
    path('learner_feedback_message_reply/', adminViews.learner_feedback_message_reply, name="learner_feedback_message_reply"),
    path('delete_instructor_feedback/<id>', adminViews.delete_instructor_feedback, name="delete_instructor_feedback"),
    path('delete_learner_feedback/<id>', adminViews.delete_learner_feedback, name="delete_learner_feedback"),

    
  # Instructor
    # Add aign languages

    path('add_intermediate_sign', instructorViews.add_intermediate_sign, name='add_intermediate_sign'),
    path('add_intermediate_sign_save', instructorViews.add_intermediate_sign_save, name='add_intermediate_sign_save'),
    path('add_beginner_sign', instructorViews.add_beginner_sign, name='add_beginner_sign'),
    path('add_beginner_sign_save', instructorViews.add_beginner_sign_save, name='add_beginner_sign_save'),
    path('add_advanced_sign', instructorViews.add_advanced_sign, name='add_advanced_sign'),
    path('add_advanced_sign_save', instructorViews.add_advanced_sign_save, name='add_advanced_sign_save'),

    # Add Lecture video
    path('add_beginner_lecture_video', instructorViews.add_beginner_lecture_video, name='add_beginner_lecture_video'),
    path('add_beginner_lecture_video_save', instructorViews.add_beginner_lecture_video_save, name='add_beginner_lecture_video_save'),
    path('add_intermediate_lecture_video', instructorViews.add_intermediate_lecture_video, name='add_intermediate_lecture_video'),
    path('add_intermediate_lecture_video_save', instructorViews.add_intermediate_lecture_video_save, name='add_intermediate_lecture_video_save'),
    path('add_advanced_lecture_video', instructorViews.add_advanced_lecture_video, name='add_advanced_lecture_video'),
    path('add_advanced_lecture_video_save', instructorViews.add_advanced_lecture_video_save, name='add_advanced_lecture_video_save'),

    path('account_status', instructorViews.account_status, name="account_status"),
    path('instructor_profile', instructorViews.instructor_profile, name="instructor_profile"),
    path('instructor_home', instructorViews.instructor_home, name="instructor_home"),
    path('instructor_profile_update', instructorViews.instructor_profile_update, name="instructor_profile_update"),
    path('signup_instructor', instructorViews.signup_instructor, name="signup_instructor"),
    path('signup_instructor_save', instructorViews.signup_instructor_save, name="signup_instructor_save"),
    path('instructor_feedback/', instructorViews.instructor_feedback, name="instructor_feedback"),
    path('instructor_feedback_save/', instructorViews.instructor_feedback_save, name="instructor_feedback_save"),

    # Learner URLs
    path('learner_home', learnerViews.learner_home, name="learner_home"),
    path('signup_learner', learnerViews.signup_learner, name='signup_learner'),
    path('signup_learner_save', learnerViews.signup_learner_save, name="signup_learner_save"),
    path('learner_profile', learnerViews.learner_profile, name="learner_profile"),
    path('learner_profile_update', learnerViews.learner_profile_update, name="learner_profile_update"),
    path('learner_feedback/', learnerViews.learner_feedback, name="learner_feedback"),
    path('learner_feedback_save/', learnerViews.learner_feedback_save, name="learner_feedback_save"),

    # Learn urls
    # biginner urls
    path('beginner', learnViews.beginner, name="beginner"),
    path('intermediate', learnViews.intermediate, name="intermediate"),
    path('advanced', learnViews.advanced, name="advanced"),
      # biginner urls
    path('eng_alphabet', learnViews.eng_alphabet, name="eng_alphabet"),
    path('amharic_alphabet', learnViews.amharic_alphabet, name="amharic_alphabet"),
    path('number', learnViews.number, name="number"),
    path('family', learnViews.family, name="family"),
    path('maths', learnViews.maths, name="maths"),
    path('week', learnViews.week, name="week"),
    path('day', learnViews.days, name="days"),
    path('body', learnViews.body, name="body"),
    # Intermidate urls
    path('cloth', learnViews.cloth, name="cloth"),
    path('name', learnViews.names, name="name"),
    path('fruit', learnViews.fruit, name="fruit"),
    path('vegetable', learnViews.vegetable, name="vegetable"),
    path('animal', learnViews.animal, name="animal"),
    path('nature', learnViews.nature, name="nature"),
    path('color', learnViews.color, name="color"),
    path('food', learnViews.food, name="food"),
   # Advanced url
    path('spritual', learnViews.spritual, name="spritual"),
    path('question', learnViews.question, name="question"),



    path('do_login', views.do_login, name='login_form'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('signup_student', views.signup_student, name='signup_student'),
    path('room', views.room),
    path('get_token/', views.getToken),
    path('lobby', views.lobby, name="lobby"),
    path('create_member', views.createMember),
    path('get_member', views.getMember),
    path('delete_member', views.deleteMember),

]

