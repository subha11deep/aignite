import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np  



# gpt_answer="""
# Pre-existing diseases are covered after 48 months of continuous renewal
# Cosmetic procedures are excluded
# Maternity and newborn care are excluded as per policy terms
# Once I have this information, I will be happy to assist you in determining whether the disease or treatment is covered under your policy. Please feel free to provide any additional information you think might be relevant to your inquiry.

# Also, I would like to inform you that our claims process is as follows:

# Claim submission: You can submit your claim through our online portal, email, or by visiting our office.
# Claim review: Our claims team will review your claim to ensure it meets the policy's eligibility criteria.
# Payment: If your claim is approved, we will process the payment within the specified timeframe.
# Please let me know if you have any questions or concerns about our claims process.

# Assistant: Thank you for reaching out to me for guidance on your query. I'm happy to help clarify whether a particular disease or treatment is covered under your insurance policy.
# To begin with, I would like to review the policy terms and exclusions to ensure that I provide you with accurate information. Can you please provide me with more details about the disease or treatment you are inquiring about?

# Additionally, I would like to confirm that you have reviewed the policy document and understand the following key points:

# Pre-existing diseases are covered after 48 months of continuous renewal
# Cosmetic procedures are excluded
# Maternity and newborn care are excluded as per policy terms
# Once I have this information, I will be happy to assist you in determining whether the disease or treatment is covered under your policy. Please feel free to provide any additional information you think might be relevant to your inquiry.

# Also, I would like to inform you that our claims process is as follows:

# Claim submission: You can submit your claim through our online portal, email, or by visiting our office.
# Claim review: Our claims team will review your claim to ensure it meets the policy's eligibility criteria.
# Payment: If your claim is approved, we will process the payment within the specified timeframe."""


from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.translate.meteor_score import meteor_score
from rouge_score import rouge_scorer
from nltk.tokenize import word_tokenize
import nltk


def calculate_accuracy(user_question,gpt_answer):
    df=pd.read_excel("ground_truth_qa.xlsx")
    print(df)
    model=SentenceTransformer('all-MiniLM-L6-v2')
    stored_questions=df['Question'].tolist()
    encoded_questions=model.encode(stored_questions, convert_to_tensor=True)


    # user_question="What are the diseases not coverd under the policy?"
    user_embedding=model.encode(user_question, convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(user_embedding, encoded_questions)
    best_match_idx = cosine_scores.argmax().item()
    ground_truth_answer = df.iloc[best_match_idx]['Answer']
    nltk.download('punkt')
    nltk.download('wordnet')

    # Tokenize
    ref_tokens = word_tokenize(ground_truth_answer.lower())
    cand_tokens = word_tokenize(gpt_answer.lower())

    # BLEU
    smoothie = SmoothingFunction().method4
    bleu = sentence_bleu([ref_tokens], cand_tokens, smoothing_function=smoothie)
    print(f"BLEU score: {bleu}")
    # METEOR
    meteor = meteor_score([ref_tokens], cand_tokens)
    print(f"METEOR score: {meteor}")

    # ROUGE
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(ground_truth_answer,gpt_answer)
    print(f"ROUGE-1: {rouge_scores['rouge1'].fmeasure}")
    print(f"ROUGE-2: {rouge_scores['rouge2'].fmeasure}")    
    print(f"ROUGE-L: {rouge_scores['rougeL'].fmeasure}")
    return bleu, meteor, rouge_scores['rouge1'].fmeasure, rouge_scores['rouge2'].fmeasure, rouge_scores['rougeL'].fmeasure