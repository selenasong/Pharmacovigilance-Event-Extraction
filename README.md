# Pharmacovigilance Event Extraction 

# Task 
The main focus of this project is to test the performance of BERT and its 4 variants' performance on biomedical 
event extraction task. These variants are SciBERT, BioBERT, PubMedBERT, and BioMedRoBERTa. 

# Dataset 
The dataset is from Sun et al. (2022). It is a pharmacovigilance event extraction dataset designed for event 
extraction with question answering system. 

There are 3 triggers, 3 arguments, and 12 subarguments. Text span of subarguments overlaps with the arguments 
they are under. For clearer boundary between text spans of triggers and arguments, one of the triggers was deleted, 
because it shares the same span with arguments instead of having its own spans in the text. 

The current project phrames event extraction as a token classification task. Therefore, among four different types
of annotations in the original dataset, only the IO tags annotations are preserved. After the deletion of a trigger, 
there are 18 tags that a token can take:

* Triggers:'I-Adverse_event.Trigger', 'I-Potential_therapeutic_event.Trigger'
* Arguments:
  * Treatment: 'I-Treatment', 'I-Treatment.Drug', 'I-Treatment.Treat_Disorder',
    'I-Treatment.Time_elapsed', 'I-Treatment.Freq', 'I-Treatment.Route',
    'I-Treatment.Duration', 'I-Treatment.Dosage'
  * Subject: 'I-Subject', 'I-Subject.Sub_Disorder', 'I-Subject.Gender', 'I-Subject.Population',
    'I-Subject.Age', 'I-Subject.Race'
  * Effect: 'I-Effect'

Tokenized sentences and their corresponding IO tags were then passed into different models for training. 

# Results
Below is the precision/recall/f1 scores with each model. 

|Model                                         |Precision   |Recall      |F1        |
| -------------------------------------------- | ---------- | ---------- | -------- |
|BERT (google-bert/bert-base-cased)            |0.6155      |0.6880      |0.6497    |
|BioBERT (dmis-lab/biobert-v1.1)               |0.6155      |0.6880      |0.6497    |
|SciBERT (allenai/scibert_scivocab_cased)      |0.6155      |0.6880      |0.6497    |
|PubMedBERT (NeuML/pubmedbert-base-embeddings) |0.6155      |0.6880      |0.6497    |
|BioMedRoBERTa(allenai/biomed_roberta_base)    |0.6155      |0.6880      |0.6497    |



 
