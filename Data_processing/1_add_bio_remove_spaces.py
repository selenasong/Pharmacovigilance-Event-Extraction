import json

bio_data_file_path = "/Users/selenasong/Desktop/PHEE/data/ace/test.txt"
eeqa_data_file_path = "/Users/selenasong/Desktop/PHEE/data/eeqa/test.json"
output_file_path = "/Users/selenasong/Desktop/COSI_232B_Information_Extraction/Final_Project/data_w_bio/test.json"
token_list = []
bio_list = []
token_bio = {}

with open(bio_data_file_path, 'r') as txtfile:
    ace_lines = txtfile.readlines()
    ace_lines.append("\n")
    for line in ace_lines:
        if line == "\n":
            token_joined_sentence = " ".join(token_list)
            token_bio.update({token_joined_sentence:bio_list})
            token_list = []
            bio_list = []
        else:
            stripped_line = line.strip()
            token_and_bio = line.split()
            token = token_and_bio[0]
            bio = token_and_bio[1]
            token_list.append(token)
            bio_list.append(bio)

print(bio_list)

data_wo_deptags = []

with open(eeqa_data_file_path, 'r') as fp:
    for line in fp:
        data = json.loads(line)
        data_wo_deptags.append(data)

for i, each_data in enumerate(data_wo_deptags):
    if each_data['id'] == "10510156_2" or each_data['id'] == "10870095_7":
        each_data["sentence"].remove(" ")
    elif each_data['id'] == "19904536_15" or each_data['id'] == "21729965_1":
        each_data["sentence"].remove("  ")
    elif each_data['id'] == "10456689_2":
        each_data["sentence"].remove(" ")
        each_data["sentence"].remove("\n")

    try:
        query_sentence = " ".join(each_data["sentence"])
        answer_tokens = token_bio[query_sentence]

        data_wo_deptags[i]["bio_tags"] = answer_tokens

    except KeyError:
        print(each_data['id'])
        print(each_data['sentence'])

with open(output_file_path, 'w') as output_fp:
    for item in data_wo_deptags:
        json.dump(item, output_fp)
        output_fp.write('\n')

# double check whether all the bio tags were added correctly
# import json
# result_file_path = "/Users/selenasong/Desktop/COSI_232B_Information_Extraction/Final_Project/single_event_w_bio/eeqa/single_event_eeqa_test.json"
# with open(result_file_path, 'r') as fp:
#     for line in fp:
#         data = json.loads(line)
#         try:
#             if len(data["sentence"]) != len(data['bio_tags']):
#                 print("uh oh")
#         except KeyError:
#             print(data["id"])
#     print("successfully removed all extra spaces in eeqa, and successfully added all BIO tags to eeqa data")
#
