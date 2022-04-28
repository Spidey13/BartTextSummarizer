from transformers import AutoTokenizer, AutoModelForTokenClassification, AutoModelForSequenceClassification, BartTokenizer, BartForConditionalGeneration, TFAutoModelForSequenceClassification
from transformers import pipeline
import tensorflow as tf
from fastai.text.all import *
from transformers import *
from blurr.data.all import *
from blurr.modeling.all import *


# def summarizer(text_to_summarize):
#     model = BartForConditionalGeneration.from_pretrained(
#         "saved_model/my_model_1")
#     tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
#     inputs = tokenizer(text_to_summarize, return_tensors='pt')
#     summary_ids = model.generate(
#         inputs['input_ids'], max_length=500, early_stopping=False)
#     summarized_text = [tokenizer.decode(
#         g, skip_special_tokens=True) for g in summary_ids]
#     return summarized_text[0]

def summarizer(text_to_summarize):
    inf_learn = load_learner(fname='sum_model_export.pkl')
    summarized_text = inf_learn.blurr_generate(text_to_summarize)
    return summarized_text