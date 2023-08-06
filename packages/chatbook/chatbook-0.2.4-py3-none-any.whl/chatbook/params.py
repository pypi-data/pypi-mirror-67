from inspect import getframeinfo, stack
import json

trace=0

class talk_params:
  def __init__(self,from_dict=None,from_json=None):

    # content extraction related
    self.compounds = True # aggregates compounds
    self.svo_edges = True # includes SVO edges in text graph
    self.subject_centered = True # redirects link from verb with predicate function to ists subject
    self.all_to_sent = False # forces adding links form all lemmas to sentence id
    self.use_to_def = True # forces adding links from sentences to where their important words occur first

    self.prioritize_compounds = 16 # elevates rank of coumpound to favor them as keyphrases

    # summary, and keyphrase set sizes

    self.top_sum = 9 # default number of sentences in summary
    self.top_keys = 10 # # default number of keyphrases

    # maximum values generated when passing sentences to BERT
    self.max_sum = self.top_sum*(self.top_sum-1)/2
    self.max_keys = 1+2*self.top_keys # not used yet

    self.known_ratio=0.8 # ratio of known to unknown words in acceptable sentences

    # query answering related
    self.top_answers = 4 # max number of answers directly shown
    # maximum answer sentences generated when passing them to BERT
    self.max_answers = max(16,self.top_answers*(self.top_answers-1)/2)

    self.cloud_size = 24 # word-cloud size
    self.subgraph_size = 42 # subgraph nodes number upper limit

    self.quiet = True # stops voice synthesis
    self.answers_by_rank = False # returns answers by importance vs. natural order

    self.pers = True # enable personalization of PageRank for QA
    self.expand_query = 2 # depth of query expansion for QA
    self.guess_wh_word_NERs=0 # try to treat wh-word qurieses as special


    # verbosity control

    self.show_rels = 0  # display relations inferreed from text


    if from_json:
      jd = json.loads(from_json)
      self.digest_dict(jd)

    if from_dict :
      self.digest_dict(from_dict)

  def digest_dict(self, pydict):
    d = self.__dict__.copy()
    for k, v in d.items():
      if isinstance(k, str) and k in pydict:
        self.__dict__[k] = pydict[k]

  def __repr__(self):
    return str(self.__dict__)

  def show(self):
    for x,y in self.__dict__.items():
      print(x,'=',y)


def ppp(*args) :
  if trace<0 : return
  caller = getframeinfo(stack()[1][0])

  print('DEBUG:',
        caller.filename.split('/')[-1],
        '->',caller.lineno,end=': ')
  print(*args)
