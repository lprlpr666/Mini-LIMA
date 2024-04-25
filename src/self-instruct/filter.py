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
api_key = "sk-mUmlVDeXLtBFsxZr02DdFf3209Af4a329fE64c39Fb7425Fc"
base_url = "https://lonlie.plus7.plus/v1"
def extract_first_number(s):
    match = re.search(r'\d+', s)  # 使用正则表达式查找连续的数字部分
    if match:
        return match.group()  # 返回找到的第一个连续数字部分
    else:
        return None  # 如果字符串中没有数字，则返回None
nownum=1
number=1

if __name__ == "__main__":
    file_path = 'data/gpt3_comp_generations/finetuning_data/all_generated_instances_trans.json'
    with open(file_path, 'r') as file:
        data = json.load(file)

    for entry in data:
        while (nownum<number):
            nownum+=1
            continue

        print("now process {}".format(nownum))

        prompt="Please evaluate the following output on a scale from 0 to 10, where 0 signifies the worst possible quality and 10 represents the best possible quality. You must only provide a number:\n"
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
        match=extract_first_number(results[0]["response"]["choices"][0]["text"])
        # match = int(results[0]["response"]["choices"][0]["text"])
        print("{} finished".format(nownum))
        nownum +=1 
        if match:
            score = match  # 将匹配的分数转换为整数
            print("提取到的分数为:", score)
            if int(score)>=9:
                with open('filter_data_new.json', 'a') as file:
                    json.dump(entry, file) 
                    file.write('\n')
        else:
            # print("没有找到分数")
            continue
        # if(results.response)
        print ("\n")
        # sleep (1)

