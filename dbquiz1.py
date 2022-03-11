from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 매트릭스 별점
movie = db.movies.find_one({'title': '매트릭스'})
target_star = movie['star']

# 매트릭스와 별점이 같은 영화들 찾기
target_movies = list(db.movies.find({'star': target_star}, {'_id': False}))

for target in target_movies:
    print(target['title'])
