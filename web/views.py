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
		wolfs		= f.cleaned_data['wolfs']
		mode	 	= f.cleaned_data['mode']
		selectedtheme 	= Theme.objects.filter(Seed__exact=seed)
		# DBにシード値がある
		if selectedtheme:
			# Player IDがメンバ数に収まっている
			if player_id <= member:
				# 狼の数が参加メンバの過半数以下となっている
				if wolfs <= member/2:
					Humantheme 	= selectedtheme[0].HumanTheme
					Wolftheme	= selectedtheme[0].WolfTheme			
					# 正解表示モード
					if mode:
						return render(request, 'form.html', {'form': f, 'seed':seed, 'member':member, 'player_id':player_id, 'mode':mode, 'humantheme':Humantheme, 'wolftheme':Wolftheme, 'wolfs':wolfs} )			
					# 出題モード
					else:
						# id_wolfs(狼ID)の作成
						rseed = 0
						np.random.seed(rseed)
						id_wolfs = np.random.randint(1,member,1)
						while len(id_wolfs) is not wolfs:
							rseed += 1
							np.random.seed(rseed)
							id_add = np.random.randint(1,member,1)
							if id_add not in id_wolfs:
								id_wolfs = np.append(id_wolfs,id_add)
						# playerの狼 or not判定
						print(id_wolfs)
						if player_id in id_wolfs:
							theme = Wolftheme
						else:
							theme = Humantheme				
						return render(request, 'form.html', {'form': f, 'seed':seed, 'member':member, 'player_id':player_id, 'mode':mode, 'theme':theme, 'wolfs':wolfs} )
					# 参加メンバーの半分以上に狼が割り当てられている
				else:
					theme = 'エラー!! 参加メンバーの過半数が狼に指定されています。食い殺される前に狼の数をメンバの半数以下にしてください。'
					return render(request, 'form.html', {'form': f, 'theme':theme} )
			else:
				theme = 'エラー!! プレイヤーIDが参加人数より大きい値となっています。'
				return render(request, 'form.html', {'form': f, 'theme':theme} )
		# DBにシード値がない
		else:
			theme = 'エラー!! シード値が登録範囲にありません。管理者にご一報ください。'
			return render(request, 'form.html', {'form': f, 'theme':theme} )	
	# フォームに値が入力されてなかったら（初回起動時）
	else:
		return render(request, 'form.html', {'form': f} )
