from django import forms


#KYLE
# 
# class myForm(forms.Form):
#     #subclass of forms.form
#     cnt=[
#         ('Strongly agree','Strongly agree'),
#         ('Agree','Agree'),
#         ('Neutral','Neutral'),
#         ('Disagree','Disagree'),
#         ('Strongly disagree','Strongly disagree'),
#     ]
#
#     c_field=forms.ChoiceField(\
#         required=True,\
#         label='Do u think this project is fucking stupid??? ',\
#         label_suffix='  ',\
#         initial='none',\
#         #help_text='choose the country',\
#         error_messages={'required':'Please enter your country', 'invalid choice':'Please select valid resp'},\
#         disabled=False,
#
#         choices=cnt,
#     )
