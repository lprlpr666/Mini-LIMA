import json
input_filename = "data/gpt3_generations/finetuning_data/all_generated_instances.jsonl"
output_filename = "data/gpt3_generations/finetuning_data/all_generated_instances_trans.json"
def convert_task_format(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        tasks = file.readlines()
    formatted_tasks = []
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
    with open(output_filename, 'w') as file:
        json.dump(formatted_tasks, file, indent=4)

if __name__ == '__main__':
    convert_task_format(input_filename, output_filename)
    print(f"Tasks have been converted and saved to {output_filename}")
