from django import forms
  
class InputForm(forms.Form):
  
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput()) 






    

# # app/models.py

# class MyModel(models.Model):
#     a = CharField()
#     b = CharField()
#     c = IntegerField()




# # app/forms.py

# class MyForm(forms.Form):
#     a1 = CharField()
#     b2 = CharField()
#     c3 = IntegerField()



# # app/views.py
# from .forms import MyForm

# class MyView(View):
    
#     def get(self, request):
#         form = MyForm()
#         context = {
#             "form": form
#         }

#         return render(request, "template.html", context=context)
# s
#     def post(self, request):
#         form = MyForm(date=request.POST)
#         if form.is_valid():
#             data = {
#                 "a": form.a1,
#                 "b": form.a2,
#                 "c": form.a3
#             }
#             obj = MyModel(data)
#             obj.save()
#         return redirect("list")