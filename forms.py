from urllib import request


class CustomerRegisterationForm(forms,ModelForm):
    form = CustomerRegisterationForm()
    return render(request,"wallet/register_customer.html",{"form":form})