from django import forms


class GreetForm(forms.Form):
    dt = forms.CharField(label='日時')
    moyori_cnt = forms.CharField(label='最寄り駅回数')
    moe_cnt = forms.CharField(label='もえ仕事回数')
