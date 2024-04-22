import json
seed_data = "seed_data/seed_tasks.jsonl"
input_filename = "data/gpt3_comp_generations/finetuning_data/all_generated_instances.jsonl"
finetuning_filename = "LLaMA-Factory/data/all_generated_instances_trans.json"
output_filename = "data/gpt3_comp_generations/finetuning_data/all_generated_instances_trans.json"


formatted_tasks = []

def convert_task_format(input_filename):
    with open(input_filename, 'r') as file:
        tasks = file.readlines()
    
    for task in tasks:
        task_data = json.loads(task)
        # print(task_data)
        new_task = {
            "instruction": task_data['instruction'],
            "input": task_data['input']if 'input' in task_data else '',
            "output": task_data['output'],
            "system": "",
            "history": []
        }
        formatted_tasks.append(new_task)    

def convert_seed_task_format(input_filename):
    with open(input_filename, 'r') as file:
        tasks = file.readlines()
    
    for task in tasks:
        task_data = json.loads(task)
        # print(task_data)
        for i in range(len(task_data['instances'])):
            new_task = {
                "instruction": task_data['instruction'],
                "input": task_data['instances'][i]['input'],
                "output": task_data['instances'][i]['output'],
                "system": "",
                "history": []
            }
        formatted_tasks.append(new_task)

if __name__ == '__main__':
    convert_seed_task_format(seed_data)
    convert_task_format(input_filename)    
    with open(finetuning_filename, 'w') as file:
        json.dump(formatted_tasks, file, indent=4)
    with open(output_filename, 'w') as file:
        json.dump(formatted_tasks, file, indent=4)
    
    print(f"Tasks have been converted and saved")
