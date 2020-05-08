from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Theme(models.Model):
	# 管理画面での表示名
	def __str__(self):
		return "Seed:" + str(self.Seed) + ", Human:" + self.HumanTheme + ", Wolf:" + self.WolfTheme

	# モデル
	Seed = models.IntegerField(verbose_name='seed', blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(9999)] )	# 乱数シード値
	HumanTheme = models.CharField(max_length = 128, editable = True)		# 人間側のお題
	WolfTheme = models.CharField(max_length = 128, editable = True)		# 狼側のお題
