import json
from dataclasses import dataclass


@dataclass
class Data(object):
    qid: int
    passage: str
    question: str
    choice: list
    prediction: float
    correct_answer: str


class Datas(object):
    """
    data = {
        qid: int,
        passage: str,  // test_mrc_iterative.json -> context
        question: str,  // test_mrc_iterative.json -> question
        process: [
            A: {
                option: str,
                evidence: {  // test_nil_iterative.json -> sentence1, sentence2
                    evd_sentence1: str,
                    evd_sentence2: str
                }
                probably: float,  // test_mc_result.json -> prob[0]
            },
            B: {
                option: str,
                evidence: {  // test_nil_iterative.json -> sentence1, sentence2
                    evd_sentence1: str,
                    evd_sentence2: str
                }
                probably: float,  // test_mc_result.json -> prob[0]
            }...
        ],
        prediction: char,  // test_mc_result.json -> prediction
        correct_answer: char  // test_mc_result.json -> answer
    }
    """

    datas = []

    def __init__(self, data):
        self.datas = [self.grap_data(data)]

    def grap_data(self, data):
        self.data = {
            'qid': data.qid,
            'passage': data.passage,
            'question': data.question,
            'process': {
                'A': {
                    'evidence': {
                        'evd_sentence1': data.choice[0]['evd_sentence1'],
                        'evd_sentence2': data.choice[0]['evd_sentence2']
                    },
                    'probably': data.choice[0]['probably']
                },
                'B': {
                    'evidence': {
                        'evd_sentence1': data.choice[1]['evd_sentence1'],
                        'evd_sentence2': data.choice[1]['evd_sentence2']
                    },
                    'probably': data.choice[1]['probably']
                },
                'C': {
                    'evidence': {
                        'evd_sentence1': data.choice[2]['evd_sentence1'],
                        'evd_sentence2': data.choice[2]['evd_sentence2']
                    },
                    'probably': data.choice[2]['probably']
                },
                'D': {
                    'evidence': {
                        'evd_sentence1': data.choice[3]['evd_sentence1'],
                        'evd_sentence2': data.choice[3]['evd_sentence2']
                    },
                    'probably': data.choice[3]['probably']
                }
            },
            'prediction': data.prediction,
            'correct_answer': data.correct_answer
        }

    def append_data(self, data):
        self.datas.append(self.grap_data(data))


class Collect(object):
    def __init__(self, loading_path):
        self.result, self.text, self.evidence = json.loads(loading_path[0], loading_path[1], loading_path[2])

    def grap_context(self):
        for i in self.text['data']:
            passage = i['context']
            qas = i['qas']  # 每题

            choice = []

            for j in qas:
                option = {}

                choice.append(option)

    def grap_question(self, j):
        qid = j['qid']


if __name__ == '__main__':
    data = Data(
        qid = 1,
        passage = 'str',
        question= 'str',
        choice = [],
        prediction = 0.001,
        correct_answer =  'str'
    )
    print(data.qid)
