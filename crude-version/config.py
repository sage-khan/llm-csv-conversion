command = '''ollama run mistral "Act like an expert in data formatting and structuring. Please read all contents of $(cat {text_file_path}) and structure it into comma separated variable (csv) style table as per example in $(cat {template_path}). Donot make up information. Use information given in $(cat {text_file_path})."'''