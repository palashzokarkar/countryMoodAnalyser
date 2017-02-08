from django import forms
from countries import get_countries

class NameForm(forms.Form):

	country_list = get_countries()
	countries_drop_down = forms.ChoiceField(choices = [(country['name'],country['name']) for country in country_list])
	#trending_issues = []