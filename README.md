# Pharmacovigilance Event Extraction 

# Task 
The main focus of this project is to test the performance of BERT and its 4 variants' performance on biomedical 
event extraction task. These variants are SciBERT, BioBERT, PubMedBERT, and BioMedRoBERTa. The idea comes from 
Zanella and Toussaint (2023) where the authors compared the performance of these transformer models with POS
tagging embeddings or word stem embeddings with the original BERT model.

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
* Others: 'O'

Tokenized sentences and their corresponding IO tags were then passed into different models for training. 

# Results
Below is the precision/recall/f1 scores with each model. 

|Model                                         |Precision   |Recall      |F1        |
| -------------------------------------------- | ---------- | ---------- | -------- |
|BERT (google-bert/bert-base-cased)            |0.6155      |0.6880      |0.6497    |
|BioBERT (dmis-lab/biobert-v1.1)               |0.6664      |0.7120      |0.6884    |
|SciBERT (allenai/scibert_scivocab_cased)      |0.6717      |0.7110      |0.6908    |
|PubMedBERT (NeuML/pubmedbert-base-embeddings) |0.4738      |0.4800      |0.4769    |
|BioMedRoBERTa(allenai/biomed_roberta_base)    |0.6732      |0.7142      |0.6931    |

The results from above experiments suggest that BioMedRoBERTa and SciBERT have the best
performance on the task, and PubMedBERT performed significantly worse than other models.
This is different from Zanella and Toussaint (2023) where they found BioMedRoBERTa to be
the worst and PubMedBERT to be on the average. A possible reason for the bad results form
PubMedBERT is the specific model (NeuML/pubmedbert-base-embeddings) is not designed for
token classification. The original Microsoft model is not available for training because of
missing file, and this one is specifically designed for QAs and summaries.

# Reference 
Zhaoyue Sun, Jiazheng Li, Gabriele Pergola, Byron Wallace, Bino John, Nigel Greene, Joseph Kim, and Yulan He. 2022. PHEE: A Dataset for Pharmacovigilance Event Extraction from Text. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 5571–5587, Abu Dhabi, United Arab Emirates. Association for Computational Linguistics.

L. Zanella and Y. Toussaint, "Adding Linguistic Information to Transformer Models Improves Biomedical Event Detection?," 2023 18th Conference on Computer Science and Intelligence Systems (FedCSIS), Warsaw, Poland, 2023, pp. 1211-1216, doi: 10.15439/2023F2076. ![image](https://github.com/selenasong/Pharmacovigilance-Event-Extraction/assets/127460254/e02d589c-4e44-4d59-ac66-18ae3cc65aba)


 
