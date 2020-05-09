from django import forms

class InputForm(forms.Form):
	seed 		= forms.IntegerField(label='シード値', min_value=1, max_value=999, initial=0, help_text='※ 0〜999の数字')
	member 	= forms.IntegerField(label='参加メンバー人数', min_value=1, initial=0)
	player_id 	= forms.IntegerField(label='プレイヤーID', min_value=1, initial=0) 
	wolfs 		= forms.IntegerField(label='狼の数', min_value=1, initial=0) 
	mode		= forms.BooleanField(label='正解発表のときはチェック', required=False)
