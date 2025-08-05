Learning Mistakes

- First created a `venv`, build dependencies like `requirement.txt` and `requirement-dev.txt` and put necessary imports and install them, then creating a logging directory like `log`, and create a script called `logger_config.py` in the `app` folder.
- no short flag for requirements.txt, it is jsut `-requirements.txt`
- shortcut way to install instead of one by one `pip install -r requirements.txt -r requirements-dev.txt`
- Need to learn more about logging and the handlers
- Once create logger_config.py need to create a test to see if it works in the `test/` and using the script `test_logger_config.py`
- type casting
- keywords like `assert` and `with`
- Once done with test_logger_config.py, go back to the root and test it `pytest tests/test_logger_config.py` and check. Gave an error! Since this is a package, incorporate `__init__.py` inside `app/` and `tests/`. use command 
`touch app/__init__.py`
`touch tests/__init__.py` and make sure you are in the root directory!!!!
- `main.py` is created once all other .py scripts are done. For now, test each script to see if it works and then a small dataset and then the full dataset. 
- Skipped the ingestion step because the dataset is already clean and well-formatted for prompt construction and self-consistency evaluation. It’s stored in data/clean/marketing_campaign_ready.csv and will be used directly by downstream modules. An ingestion pipeline may be added later if needed.
- Self-consistency doesn’t require your data to be perfectly cleaned in the traditional sense (no missing values, normalized scales, etc.).
- The self-consistency mechanism evaluates whether the LLM produces similar answers for repeated prompts derived from the same input.
- Req: 1) Input rows are interpretable by an LLM 2) Prompt can be generated from each row 3) No corrupted or missing key fields used in prompt 4) Semantic consistency in row content