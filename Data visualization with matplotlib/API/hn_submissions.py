from operator import itemgetter
import requests



url = 'https://hacker-news.firebaseio.com/v0/item/9884165.json'
r = requests.get(url)
print("Status code: ", r.status_code)

submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
        str(submission_id) + '.json')
    submision_r = requests.get(url)
    print(submision_r.status_code)
    response_dict = submision_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link':'http://news.ycombinator.com/item?id=' + str(submission_id),
	        'comments': response_dict.get('descendants', 0)
    }

    submission_dicts.append(submission_dict)

