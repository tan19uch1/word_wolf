from django.shortcuts import render
from django.http.response import HttpResponse
from web.models import Theme
from web.form import InputForm
import numpy as np

def setting(request):
	f = InputForm(request.GET)
	# フォームに値が入力されてたら真
	if f.is_valid():
		seed 		= f.cleaned_data['seed']
		member 	= f.cleaned_data['member']
		player_id 	= f.cleaned_data['player_id']
		mode	 	= f.cleaned_data['mode']
		selectedtheme 	= Theme.objects.filter(Seed__exact=seed)
		# DBにシード値がある
		if selectedtheme:
			Humantheme 	= selectedtheme[0].HumanTheme
			Wolftheme	= selectedtheme[0].WolfTheme			
			# 正解表示モード
			if mode:
				theme = 'your theme'
				return render(request, 'form.html', {'form': f, 'seed':seed, 'member':member, 'player_id':player_id, 'mode':mode, 'humantheme':Humantheme, 'wolftheme':Wolftheme, 'theme':theme} )			
			# 出題モード
			else:
				theme = 'your theme'
				return render(request, 'form.html', {'form': f, 'seed':seed, 'member':member, 'player_id':player_id, 'mode':mode, 'theme':theme} )
		# DBにシード値がない
		else:
			theme = 'None'
			return render(request, 'form.html', {'form': f, 'seed':seed, 'member':member, 'player_id':player_id, 'mode':mode, 'theme':theme} )	# フォームに値が入力されてなかったら（初回起動時）
	else:
		return render(request, 'form.html', {'form': f} )
