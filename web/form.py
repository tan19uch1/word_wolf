from django import forms

class InputForm(forms.Form):
	seed 		= forms.IntegerField()
	member 	= forms.IntegerField()
	player_id 	= forms.IntegerField() 
	mode		= forms.BooleanField(required=False)
