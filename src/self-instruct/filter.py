import json
import tqdm
import os
import random
import openai
from datetime import datetime
import argparse
import time
import re

from openai_api import make_requests
from openai_api import make_chat_requests
api_key = "sk-C6n3jndE0SV8fKVJ4aF2F8A225B54c2b901c966a16765bCb"
base_url = "https://lonlie.plus7.plus/v1"

nownum=1
number=1

if __name__ == "__main__":
    file_path = 'data/gpt3_comp_generations/finetuning_data/all_generated_instances_trans1.json'
    with open(file_path, 'r') as file:
        data = json.load(file)

    for entry in data:
        while (nownum<number):
            nownum+=1
            continue

        print("now process {}".format(number))

        prompt="Please evaluate the following output on a scale from 0 to 5, where 0 signifies the worst possible quality and 5 represents the best possible quality. Provide a score and a brief justification for your evaluation:\n"
        prompt+="instruction: "+entry["instruction"]+"\n"
        if entry["input"]!="":
            prompt+="input: "+entry["input"] +"\n"
        prompt+="output: "+entry["output"]+"\n"
        results = make_requests(
                prompts=prompt,
                max_tokens=1024,
                temperature=0.7,
                top_p=0.5,
                frequency_penalty=0,
                presence_penalty=2,
                stop_sequences=["\n16", "16.", "16 ."],
                logprobs=1,
                n=1,
                best_of=1,
                api_key=api_key,
                base_url=base_url,
        )
        print (results[0]["response"]["choices"][0]["text"])
        score_pattern = r"Score:\s*(\d)"
        match = re.search(score_pattern, results[0]["response"]["choices"][0]["text"])
        print("{} finished".format(number))
        number +=1 
        if match:
            score = int(match.group(1))  # 将匹配的分数转换为整数
            print("提取到的分数为:", score)
            if score>=4:
                with open('filter_data.json', 'a') as file:
                    json.dump(entry, file) 
                    file.write('\n')
        else:
            # print("没有找到分数")
            continue
        # if(results.response)
        print ("\n")
        # sleep (1)

