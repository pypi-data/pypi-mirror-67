# Scidra Module Utils

[![PyPI version](https://badge.fury.io/py/scidra-module-utils.svg)](https://badge.fury.io/py/scidra-module-utils)

## Version: 0.1.0

## Description

A base class and a set of helper functions to reduce the amount of new code required to create new modules as
well as help enforce expeted variables and functionality of a moodule

## Example Module

```python
from scidra.module_utils import BaseModule, Output, FileRef
from typing import Dict
import json

class TestModule(BaseModule):
    def run_job_logic(self, parameters: dict, files: Dict[str, FileRef]) -> Output:
        assert "message" in parameters

        print(parameters["message"])

        return Output(
            output_json=json.dumps(
                {"out_message": f"{parameters['message']} was printed"}
            )
        )

if __name__ == "__main__":
    TestModule().run()
```
