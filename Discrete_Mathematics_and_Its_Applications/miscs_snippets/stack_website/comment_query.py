# https://stackoverflow.com/a/67630599/21294350
# This is not used
# https://meta.stackoverflow.com/a/389198/21294350
from stackapi import StackAPI

comment_ids = [888864, 119492885, 119510415, 888364] # replace this appropriately
semicolon_comments = ';'.join(map(str, comment_ids))
print('Comment ids are', comment_ids)
# the filters are there to ensure only the properties this script needs
# are present in the response. Feel free to change them as you want
# see the API docs for more information:
# https://api.stackexchange.com/docs/filters
api_filters = {
  'comments': '!bB.Oyz3JM2LX3l',
  'questions': '!)riR7Ef(W01pi.05dOb-',
  'questions_answers': '!BLgprJqGKCESh3xPyAtFci6an*MmWe'
}
# dictionary that will contain the comment id and the respective post id
# key => comment id, value => post ids as str array
comments_information = {}
# dictionary that will contain the information about comments and tags
# key => comment id, value => post tags as int array
tags_information = {}

# Uncomment the line below and comment the line after it
# if you already have an API key
# SITE = StackAPI('stackoverflow', key = 'YOUR_KEY_HERE')
SITE = StackAPI('stackoverflow')
comment_info = SITE.fetch('comments/{ids}',
                          ids = semicolon_comments,
                          filter = api_filters['comments'])
print('/comments/{ids} API call done,', len(comment_info['items']), 'returned')
question_ids, answer_ids = [], []
for comment_item in comment_info['items']:
  post_type = comment_item['post_type']
  post_id = comment_item['post_id']
  ids_var = question_ids if post_type == 'question' else answer_ids
  ids_var.append(str(post_id))

  comment_id = comment_item['comment_id']
  try:
    comment_info = comments_information[post_id]
    comment_info.append(comment_id)
  except KeyError:
    comments_information[post_id] = [comment_id]

# ids need to be semicolon-separated, just as above
semicolon_questions = ';'.join(question_ids)
semicolon_answers = ';'.join(answer_ids)

question_info = SITE.fetch('questions/{ids}',
                           ids = semicolon_questions,
                           filter = api_filters['questions'])
print('/questions/{ids} API call done,', len(question_info['items']), 'returned')

for question_item in question_info['items']:
  question_id = question_item['question_id']
  comment_ids = comments_information[question_id]

  # handle multiple comments under the same question
  for comment_id in comment_ids:
    tags_information[comment_id] = question_item['tags']

answer_info = SITE.fetch('answers/{ids}/questions',
                         ids = semicolon_answers,
                         filter = api_filters['questions_answers'])
print('/answers/{ids}/questions API call,', len(question_info['items']), 'returned')
for answer_item in answer_info['items']:
  # find the answer id(s) from the 'answers' field
  q_answer_ids = [answer['answer_id'] for answer in answer_item['answers']]
  answer_ids_set = set(map(int, answer_ids))
  common_list = list(set(q_answer_ids).intersection(answer_ids_set))

  # handle multiple comments under answers in the same question
  for post_id in common_list:
    comment_ids = comments_information[post_id]
    for comment_id in comment_ids:
      tags_information[comment_id] = answer_item['tags']

print('\n', tags_information)
