from transformers import AutoTokenizer, pipeline
from enum import Enum
from typing import List, Tuple

class LabelClassification(Enum) :
    NEGATIVE       = "แย่"
    NEUTRAL        = "ปานกลาง"
    POSITIVE       = "ดี"

_classifier = None

def load_classifier() -> pipeline:
    global _classifier

    if _classifier is None:
        # tokenizer = AutoTokenizer.from_pretrained(
        #                             "joeddav/xlm-roberta-large-xnli",
        #                             use_fast=False                
        #                         )
        _classifier = pipeline(
                        "zero-shot-classification",
                        model="joeddav/xlm-roberta-large-xnli",
                        tokenizer="joeddav/xlm-roberta-large-xnli",
                        use_fast=True,
                        trust_remote_code=True
                      )
    return _classifier

def classify(
        desc: str, 
        role: str
    ) -> List[tuple[LabelClassification, float]]:

    classifier = load_classifier()

    input_text = f"บทบาทที่ต้องการ: {role}\Description: \n{desc}"

    labels = [label.value for label in LabelClassification]

    result = classifier(input_text, candidate_labels=labels)

    return [
        ( LabelClassification(label), float(score) )
        for (label, score) in zip(result["labels"], result["scores"])
    ]
