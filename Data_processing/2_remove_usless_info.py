import json

file = '/Users/selenasong/Desktop/COSI_232B_Information_Extraction/Final_Project/data_w_bio/test.json'

treatment_io_list = ['I-Treat_Disorder','I-Drug',  'I-Dosage', 'I-Route','I-Time_elapsed','I-Freq', 'I-Duration', 'I-Treatment.Route', 'I-Treatment.Treat_Disorder', 'I-Treatment.Time_elapsed', 'I-Treatment.Duration', 'I-Treatment.Freq', 'I-Treatment.Drug', 'I-Treatment.Dosage', 'I-Combination.Drug']
treatment_subarg = ['I-Treat_Disorder','I-Drug',  'I-Dosage', 'I-Route','I-Time_elapsed','I-Freq', 'I-Duration']

subject_io_list = ['I-Population', 'I-Sub_Disorder', 'I-Race', 'I-Gender', 'I-Subject.Population', 'I-Subject.Sub_Disorder', 'I-Subject.Gender', 'I-Subject.Race', 'I-Subject.Age']
subject_subarg = ['I-Population', 'I-Sub_Disorder', 'I-Race', 'I-Gender']

new_data = []

with open(file, 'r') as fp:
    for line in fp:
        data = json.loads(line)
        new_io_tags = []
        for bio_tag in data["bio_tags"]:
            if bio_tag in treatment_subarg:
                whole_argument = 'I-Treatment.' + bio_tag.split("-")[1]
            elif bio_tag == 'I-Combination.Drug' or bio_tag == 'I-Treatment.Combination.Drug':
                whole_argument = "I-Treatment.Drug"
            elif bio_tag in subject_subarg:
                whole_argument = "I-Subject." + bio_tag.split("-")[1]
            else:
                whole_argument = bio_tag

            new_io_tags.append(whole_argument)

        data["bio_tags"] = new_io_tags
        data.pop("s_start")
        data.pop("ner")
        data.pop("relation")
        data.pop("event")
        new_data.append(data)


output_file = '/Users/selenasong/Desktop/COSI_232B_Information_Extraction/Final_Project/data_w_bio/deep/test.json'
with open(output_file, 'w') as op:
    for item in new_data:
        json.dump(item,op)
        op.write('\n')
