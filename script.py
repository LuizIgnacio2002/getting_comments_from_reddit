import praw
import pandas as pd

def create_reddit_object():
    reddit = praw.Reddit(client_id='1O1QhQbE_gyCtItZp7othw', client_secret='kNd667d1yR_J3cc5-lDGCCWorRkVBw', user_agent='testing_api by u/liqc2002', username='liqc2002', password='werrewaeiouBASE22',)
    return reddit

reddit=create_reddit_object()
urls=[
"https://www.reddit.com/r/devsarg/comments/163wrg7/humo_en_ciencias_de_datos/",
"https://www.reddit.com/r/chileIT/comments/1j608rv/vale_la_pena_un_mag%C3%ADster_en_ciencia_de_datos_o/",
"https://www.reddit.com/r/programacion/comments/1k767iz/como_ven_el_futuro_de_la_ciencia_de_datos/",
"https://www.reddit.com/r/chileIT/comments/1hgrfrv/hay_pega_en_ciencia_de_datos_en_chile/",
"https://www.reddit.com/r/chileIT/comments/15a5mny/valen_la_pena_los_cursos_de_ciencia_de_datos_por/",
"https://www.reddit.com/r/programacion/comments/1bhxteu/qu%C3%A9_tan_dif%C3%ADcil_es_ser_data_scientist_desde_cero/"
]

comments=[]
article_id=[]

for url in urls:
    submission=reddit.submission(url=url)
    id=url.split("/")[6]
    submission.comment_sort = 'best'
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comments.append(comment.body)
        article_id.append(id)

df=pd.DataFrame({"Comments":comments, "Article_ID": article_id})
df.to_csv('reddit_comments.csv')